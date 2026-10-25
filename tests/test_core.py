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
