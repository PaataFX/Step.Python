import unittest
from employee import Employee


def setUpModule():
    print("\nRunning SetUpModule")

def tearDownModule():
    print("\nTearing Down SetUpModule")


#Fixtures

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nSetting Up Class")

    @classmethod
    def tearDownClass(cls):
        print("\nTearing Down Class")

    def setUp(self):
        print("\nSetting Up")
        self.employee1 = Employee("George", "Lagvilava", 5000)
        self.employee2 = Employee("Elene", "Fagava", 17000)

    def tearDown(self):
        print("\nTearing Down")

    def test_email(self):
        print("\nTesting Email")


        self.assertEqual(self.employee1.email, "g.lagvilava@gmail.com")
        self.assertEqual(self.employee2.email, "e.fagava@gmail.com")


        self.employee1.firstname = "Levan"
        self.employee2.firstname = "Mariam"

        self.assertEqual(self.employee1.email, "l.lagvilava@gmail.com")
        self.assertEqual(self.employee2.email, "m.fagava@gmail.com")

    def test_full_name(self):
        print("\nTesting Fullname")

        self.assertEqual(self.employee1.full_name, "George Lagvilava")
        self.assertEqual(self.employee2.full_name, "Elene Fagava")

        self.employee1.firstname = "Levan"
        self.employee2.firstname = "Mariam"

        self.assertEqual(self.employee1.full_name, "Levan Lagvilava")
        self.assertEqual(self.employee2.full_name, "Mariam Fagava")




if __name__ == "__main__":
    unittest.main()