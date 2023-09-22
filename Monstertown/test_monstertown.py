import unittest
from monstertown import Town, Mutant, Vampire
import random

class TestMonsterTown(unittest.TestCase):

    def setUp(self):
        # TODO: Create THREE Town objects
        self.muncie = Town("Muncie", 5, 5, 5)
        self.indianapolis = Town("Indianapolis", 5, 5, 5)
        self.carmel = Town("Carmel", 5, 5, 5)
        # TODO: Create TWO Mutant objects
        self.godzilla = Mutant("Godzilla", 40.2, 23000)
        self.raptar = Mutant("Raptar", 20, 10000)
        # TODO: Create TWO Vampire objects
        self.vladimir = Vampire("Vladimir", 2.5, 170)
        self.dracula = Vampire("Dracula", 3, 210)


    def testTownInitializer(self):
        # TODO: Test all three of the Town objects you created in the setUp() method. 
        self.assertEqual(self.muncie.name, 'Muncie')
        self.assertNotEqual(self.muncie.name, 'muncie')
        self.assertNotEqual(self.muncie.name, 'MUNCIE')

        self.assertEqual(self.indianapolis.name, 'Indianapolis')
        self.assertNotEqual(self.indianapolis.name, 'indianapolis')
        self.assertNotEqual(self.indianapolis.name, 'INDIANAPOLIS')

        self.assertEqual(self.carmel.name, 'Carmel')
        self.assertNotEqual(self.carmel.name, 'carmel')
        self.assertNotEqual(self.carmel.name, 'CARMEL')


    def testMutantTerrorizeTown(self):
        # TODO: Write tests that validate that the values for population, buildings, and stoplights will never go below zero no matter how many times the town is terrorized. 
        self.godzilla.terrorize_town(self.muncie)
        self.godzilla.terrorize_town(self.muncie)
        self.godzilla.terrorize_town(self.muncie)
        self.godzilla.terrorize_town(self.muncie)
        self.godzilla.terrorize_town(self.muncie)
        
        self.assertGreaterEqual(self.muncie.population, 0)
        self.assertGreaterEqual(self.muncie.buildings, 0)
        self.assertGreaterEqual(self.muncie.stoplights, 0)


    def testVampireTerrorizeTown(self):
        # TODO: Write tests that validate that the values for population will never go below zero no matter how many times the town is terrorized.
        # TODO: Write tests to ensure that the values for buildings and stoplights never change after terrorizing. 
        self.dracula.terrorize_town(self.muncie)
        self.dracula.terrorize_town(self.muncie)
        self.dracula.terrorize_town(self.muncie)
        self.dracula.terrorize_town(self.muncie)
        self.dracula.terrorize_town(self.muncie)
        self.dracula.terrorize_town(self.muncie)

        self.assertGreaterEqual(self.muncie.population, 0)
        self.assertEqual(self.muncie.buildings, 5)
        self.assertEqual(self.muncie.stoplights, 5)
        

    def testMutantMMI(self):
        # TODO: Write tests that validate the calculated value of a Mutant’s mmi property. 
        # A Mutant with a height of 10 and weight of 6000 should have an mmi of 30.  
        # A Mutant with a height of 2 and weight of 200 should have an mmi of 5.
        # (self.weight/200)/(self.height*.10)
        self.assertEqual(self.godzilla.MutantMMI, 28.60696517412935)
        self.assertEqual(self.raptar.MutantMMI, 25)

    def testVampireMMI(self):
        # TODO: Write tests that validate the calculated value of a Vampire’s mmi property. 
        # A Vampire with a height of 3 and weight of 170 should have an mmi of 25.5. 
        # A Vampire with a height of 1.5 and weight of 90 should have an mmi of 27.
        # ((self.weight/self.height)*.45) 
        self.assertEqual(self.vladimir.VampireMMI, 30.6)
        self.assertEqual(self.dracula.VampireMMI, 31.5)

if __name__ == '__main__':
    unittest.main()