import hashlib,json
from pathlib import Path
from hobbly.core import BookingSystem
ROOT=Path(__file__).resolve().parents[1]

def main():
    s=BookingSystem(); s.add_listing('L','Synthetic service',5000,1); s.book('B','L','synthetic')
    capture=s.pay('B','K'); replay=s.pay('B','K')
    conflict=False
    try: s.pay('OTHER','K')
    except ValueError: conflict=True
    s.cancel('B'); refund=s.refund('B','R'); repeat=s.refund('B','R')
    s.book('B2','L','another-synthetic'); balance=s.reconcile()
    source=ROOT.parents[1]/'00. ARCHIVE SYSTEM/portfolio/MANAGEMENT-VALIDATION-CASES.yaml'
    case=next(x for x in json.loads(source.read_text())['cases'] if x['project']=='Hobbly'); p=case['inputs']
    revenue=p['booking_value']*p['take_rate']; support_limit=revenue-p['payment_cost']-p['expected_loss']
    base=support_limit-p['support_cost']; negative=support_limit-case['negative_change']['support_cost']
    assert conflict and replay['idempotent_replay'] and repeat['idempotent_replay'] and balance['net_cents']==0
    assert base==case['expected_base'] and negative==case['expected_negative']
    result=dict(id='HOBBLY-MANAGEMENT-REVIEW-001',scope='synthetic sequential states and contribution arithmetic',
                capture=capture,refund=refund,reconciliation=balance,key_conflict_rejected=conflict,
                base_contribution=base,negative_contribution=negative,support_break_even=support_limit,unit='EUR/completed booking',
                source_hashes={'src/hobbly/core.py':hashlib.sha256((ROOT/'src/hobbly/core.py').read_bytes()).hexdigest(),
                               str(source.relative_to(ROOT.parents[1])):hashlib.sha256(source.read_bytes()).hexdigest()},
                limits=['No live PSP','No concurrent-safety claim','No measured support cost','No regulatory compliance claim'])
    (ROOT/'artifacts/management-review.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'docs/MODEL-VALIDATION-MEMO.md').write_text(f'''# Hobbly — validation and decision memo

Private synthetic study. Eight repository tests cover capacity, key replay/conflict, valid states, cancellation, refund, amount reconciliation and invalid inputs.

## Result

One capture of 5000 cents and one full refund of 5000 cents reconcile to zero net payment flow. Replay produces no second financial event. Cross-booking key reuse is rejected. Cancellation releases the local slot. This is a sequential local reference, not provider settlement.

At the separately declared economic scenario, platform contribution is EUR {base:.2f} per completed booking and EUR {negative:.2f} when support cost rises. The break-even support cost is EUR {support_limit:.2f}, before fixed costs and tax. Gross booking value is not platform revenue. The pre-recorded cost forecast matches the arithmetic.

## Decision

Continue documenting the service and compare a manual/existing-product baseline. Do not deploy a payment service from this reference. Confirm cancellation terms, support workload, refund fees, settlement rules and access responsibilities before implementation. A favorable unit contribution does not establish total profitability.

## Post-mortem

The earlier implementation replayed a key without checking the booking identity and treated any unknown outcome as failure. Both now reject ambiguous input. Full-refund reconciliation was absent and is now demonstrated. Authorization/capture, concurrency, partial refunds and chargebacks remain explicit gaps; no claim of production safety is made.

Source and handoff: DELIVERY-SPECIFICATION.md, MODEL-CARD.md, the local reference tests and artifacts/management-review.json. The historical technical demo uses a different synthetic pricing scenario; do not combine its numbers with this management scenario.
''')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
