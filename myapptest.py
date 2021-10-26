import unittest
def get_check_cost(cost):
    if cost < 30000:
        bike_name= 'heroHonda'
    elif cost < 100000:
        bike_name = 'Apache'
    else:
        bike_name = 'Bullet'
    return bike_name
class NearestExitTests(unittest.TestCase):
    def test_row_1(self):
        self.assertEqual(get_check_cost(20000), 'heroHonda','The Nearest cost to row is in the Herohonda!')
def test_row_20(self):
    self.assertEqual(get_check_cost(50000), 'Apache', 'The Nearest cost to row 20 is in the Apache!')
def test_row_40(self):
    self.assertEqual(get_check_cost(150000), 'Bullet', 'The Nearest cost to row 40 is in thebullet!')
unittest.main()
# git push https://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@github.com/PavanKumarKunnathu/ docker_practice.git