import unittest
from hobbly.core import BookingSystem
class StateMachineTest(unittest.TestCase):
    def setUp(self): self.s=BookingSystem(); self.s.add_listing("L","Test",1000,1)
    def test_idempotency(self):
        self.s.book("B","L","C"); a=self.s.pay("B","K"); b=self.s.pay("B","K"); self.assertFalse(a["idempotent_replay"]); self.assertTrue(b["idempotent_replay"])
    def test_capacity(self):
        self.s.book("B","L","C")
        with self.assertRaises(ValueError): self.s.book("B2","L","C2")
    def test_invalid_transition(self):
        self.s.book("B","L","C"); self.s.pay("B","K")
        with self.assertRaises(ValueError): self.s.pay("B","K2")
    def test_key_cannot_cross_booking_or_outcome(self):
        self.s.book('B','L','C'); self.s.pay('B','K')
        with self.assertRaises(ValueError): self.s.pay('OTHER','K')
        with self.assertRaises(ValueError): self.s.pay('B','K','fail')
    def test_cancel_refund_and_reconcile(self):
        self.s.book('B','L','C'); self.s.pay('B','K'); self.s.cancel('B')
        self.s.book('B2','L','C2')
        self.s.refund('B','R'); self.assertTrue(self.s.refund('B','R')['idempotent_replay'])
        self.assertEqual(self.s.reconcile(),dict(captured_cents=1000,refunded_cents=1000,net_cents=0))
        with self.assertRaises(ValueError): self.s.refund('B','R2')
    def test_failed_payment_no_refund(self):
        self.s.book('B','L','C'); self.s.pay('B','K','fail'); self.s.cancel('B')
        with self.assertRaises(ValueError): self.s.refund('B','R')
        self.assertEqual(self.s.reconcile()['captured_cents'],0)
    def test_invalid_input(self):
        for price,capacity in [(-1,1),(10,0),(10.5,1),(True,1)]:
            with self.assertRaises(ValueError): self.s.add_listing('X','Invalid',price,capacity)
        self.s.book('B','L','C')
        with self.assertRaises(ValueError): self.s.pay('B','K','typo')
