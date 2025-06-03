import unittest
from oar.core.cyborg import Cyborg


class TestCyborg(unittest.TestCase):

    def setUp(self):
        self.cyborg = Cyborg()

    def test_get_manager_ids(self):
        self.assertEqual(self.cyborg.get_manager_ids("tdavid"), {"gjospin"})

    def test_get_team_lead_ids(self):
        self.assertEqual(self.cyborg.get_team_lead_ids("tdavid"), {"rioliu"})
