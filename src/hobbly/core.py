from __future__ import annotations
import hashlib, json, sqlite3
from pathlib import Path

PROJECT_ID="PRJ-HOBBLY-PROTOTYPE"
class BookingSystem:
    def __init__(self, path=":memory:"):
        self.db=sqlite3.connect(path); self.db.row_factory=sqlite3.Row
        self.db.executescript("""CREATE TABLE IF NOT EXISTS listings(id TEXT PRIMARY KEY,title TEXT,price_cents INT,capacity INT); CREATE TABLE IF NOT EXISTS bookings(id TEXT PRIMARY KEY,listing_id TEXT,status TEXT,customer TEXT); CREATE TABLE IF NOT EXISTS payments(idempotency_key TEXT PRIMARY KEY,booking_id TEXT,status TEXT,amount_cents INT);""")
        self.db.execute('CREATE TABLE IF NOT EXISTS refunds(idempotency_key TEXT PRIMARY KEY,booking_id TEXT UNIQUE,amount_cents INT)')
    def add_listing(self,id,title,price_cents,capacity):
        if type(price_cents) is not int or price_cents<0 or type(capacity) is not int or capacity<1: raise ValueError('invalid_listing')
        self.db.execute("INSERT INTO listings VALUES(?,?,?,?)",(id,title,price_cents,capacity)); self.db.commit()
    def book(self,bid,lid,customer):
        listing=self.db.execute("SELECT * FROM listings WHERE id=?",(lid,)).fetchone();
        if not listing: raise ValueError("listing_not_found")
        used=self.db.execute("SELECT count(*) FROM bookings WHERE listing_id=? AND status!='cancelled'",(lid,)).fetchone()[0]
        if used>=listing["capacity"]: raise ValueError("slot_full")
        self.db.execute("INSERT INTO bookings VALUES(?,?,?,?)",(bid,lid,"pending_payment",customer)); self.db.commit(); return "pending_payment"
    def pay(self,bid,key,outcome="capture"):
        prior=self.db.execute("SELECT * FROM payments WHERE idempotency_key=?",(key,)).fetchone()
        if outcome not in ('capture','fail'): raise ValueError('invalid_payment_outcome')
        if prior:
            expected='captured' if outcome=='capture' else 'failed'
            if prior['booking_id']!=bid or prior['status']!=expected: raise ValueError('idempotency_conflict')
            return dict(prior)|{"idempotent_replay":True}
        booking=self.db.execute("SELECT * FROM bookings WHERE id=?",(bid,)).fetchone()
        if not booking or booking["status"]!="pending_payment": raise ValueError("invalid_booking_state")
        amount=self.db.execute("SELECT price_cents FROM listings WHERE id=?",(booking["listing_id"],)).fetchone()[0]
        status="captured" if outcome=="capture" else "failed"
        self.db.execute("INSERT INTO payments VALUES(?,?,?,?)",(key,bid,status,amount)); self.db.execute("UPDATE bookings SET status=? WHERE id=?",("confirmed" if status=="captured" else "payment_failed",bid)); self.db.commit()
        return {"idempotency_key":key,"booking_id":bid,"status":status,"amount_cents":amount,"idempotent_replay":False}
    def booking(self,bid): return dict(self.db.execute("SELECT * FROM bookings WHERE id=?",(bid,)).fetchone())
    def cancel(self,bid):
        row=self.db.execute('SELECT * FROM bookings WHERE id=?',(bid,)).fetchone()
        if not row: raise ValueError('booking_not_found')
        if row['status']=='cancelled': return 'cancelled'
        if row['status'] not in ('pending_payment','payment_failed','confirmed'): raise ValueError('invalid_booking_state')
        self.db.execute('UPDATE bookings SET status=? WHERE id=?',('cancelled',bid)); self.db.commit()
        return 'cancelled'
    def refund(self,bid,key):
        prior=self.db.execute('SELECT * FROM refunds WHERE idempotency_key=?',(key,)).fetchone()
        if prior:
            if prior['booking_id']!=bid: raise ValueError('idempotency_conflict')
            return dict(prior)|{'idempotent_replay':True}
        booking=self.db.execute('SELECT * FROM bookings WHERE id=?',(bid,)).fetchone()
        capture=self.db.execute("SELECT * FROM payments WHERE booking_id=? AND status='captured'",(bid,)).fetchone()
        if not booking or booking['status']!='cancelled' or not capture: raise ValueError('refund_not_allowed')
        if self.db.execute('SELECT 1 FROM refunds WHERE booking_id=?',(bid,)).fetchone(): raise ValueError('already_refunded')
        self.db.execute('INSERT INTO refunds VALUES(?,?,?)',(key,bid,capture['amount_cents'])); self.db.commit()
        return dict(idempotency_key=key,booking_id=bid,amount_cents=capture['amount_cents'],idempotent_replay=False)
    def reconcile(self):
        captured=self.db.execute("SELECT COALESCE(SUM(amount_cents),0) FROM payments WHERE status='captured'").fetchone()[0]
        refunded=self.db.execute('SELECT COALESCE(SUM(amount_cents),0) FROM refunds').fetchone()[0]
        return dict(captured_cents=captured,refunded_cents=refunded,net_cents=captured-refunded)
def run(root: Path):
    (root/"artifacts").mkdir(parents=True,exist_ok=True)
    dbpath=root/"artifacts/demo.sqlite"; dbpath.unlink(missing_ok=True); s=BookingSystem(dbpath)
    s.add_listing("L1","Synthetic workshop",10000,2); s.book("B1","L1","synthetic-customer-1"); first=s.pay("B1","KEY-001"); replay=s.pay("B1","KEY-001")
    s.book("B2","L1","synthetic-customer-2"); failure=s.pay("B2","KEY-002","fail")
    invalid_rejected=False
    try: s.pay("B1","KEY-003")
    except ValueError: invalid_rejected=True
    fee_rate=.04; fixed_fee=100; variable_cost=5500
    economics={"gross_value_cents":first["amount_cents"],"platform_revenue_cents":round(first["amount_cents"]*fee_rate+fixed_fee),"modeled_contribution_cents":round(first["amount_cents"]*fee_rate+fixed_fee-variable_cost),"assumption":"synthetic unit economics"}
    result={"project_id":PROJECT_ID,"claim_scope":"synthetic transaction-state demonstration","happy_path":first,"idempotent_replay":replay,"failure_path":failure,"failure_booking_state":s.booking("B2")["status"],"invalid_transition_rejected":invalid_rejected,"economics":economics,"prediction_passed":replay["idempotent_replay"] and invalid_rejected and s.booking("B1")["status"]=="confirmed"}
    (root/"artifacts/results.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    (root/"artifacts/transaction-log.json").write_text(json.dumps([first,replay,failure],indent=2),encoding="utf-8")
    arts=[]
    for rel in ["artifacts/results.json","artifacts/transaction-log.json","artifacts/demo.sqlite"]:
        p=root/rel; arts.append({"artifact_id":"ART-"+hashlib.sha256(rel.encode()).hexdigest()[:12].upper(),"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"validation_status":"tested","reproduce_command":"make reproduce"})
    (root/"artifacts/evidence-manifest.json").write_text(json.dumps({"project_id":PROJECT_ID,"generated":"2026-10-25","data_class":"synthetic","artifacts":arts},indent=2),encoding="utf-8")
    return result
