import random
import math
import string

class Town():

    def __init__(self, name: str, population: int, buildings: int, stoplights: int):
        """Create a new instance of Town"""
        self.name = string.capwords(name)
        self.population = population
        self.buildings = buildings
        self.stoplights = stoplights

    def describe_town(self) -> str:
        return f'{self.name} has a population of {self.population}, {self.buildings} buildings, and {self.stoplights}.'

class Monster():

    def __init__(self, name: str, height: float, weight: int):
        """Initialize a new object of the Monster class. Height is in meters. Weight is in pounds."""
        self.name = name
        self.height = height
        self.weight = weight
        self.location = None # Instance of the Town class

    def say_hello(self) -> str:
        return f'Hi, my name is {self.name}'
    
    def describe_activity(self) -> str:
        if self.location == None:
            return f'{self.name} is totally bored.'
        else:
            return f'{self.name} is terrorizing {self.location.name}'
        
    def terrorize_town(self, target: Town) -> Town:
        """Monster attacks modify the population, buildings, and stoplights."""
        self.location = target

        print(f'A monster is attacking! {self.describe_activity()}')

        if target.population > 0:
            target.population = target.population - 50
        else:
            target.population = 0

        if target.buildings > 0:
            target.buildings = target.buildings - 10
        else:
            target.buildings = 0


        if target.stoplights > 0:
            target.stoplights = target.stoplights - 5
        else:
            target.stoplights = 0


        return target

    @property
    def MonsterMMI(self) -> float:
        pass

        
    
class Vampire(Monster):

    def __init__(self, name: str, height: float, weight: int):
        """Initialize a new instance of the Vampire class. Height is meters. Weight is pounds."""
        super().__init__(name, height, weight)

    def terrorize_town(self, target: Town) -> Town:
        self.location = target

        # print(f'A vampire is attacking! {self.describe_activity}')

        if target.population > 0:
            target.population = target.population - 1
        else:
            target.population = 0


        return target
    
    @property
    def VampireMMI(self) -> float:
        return ((self.weight/self.height)*.45)
    
class Mutant(Monster):
    def __init__(self, name: str, height: float, weight: int):
        """Initialize a new instance of the Mutant class. Height is meters. Weight is pounds."""
        super().__init__(name, height, weight)

        
    def terrorize_town(self, target: Town) -> Town:
        """Mutant attacks modify the population, buildings, and stoplights."""
        self.location = target

        print(f'A mutant is attacking! {self.describe_activity()}')

        # Mutants kill between 1 person to up to 10% of the population in an attack
        
        if target.population > 0:
            target.population = target.population - random.randint(0, math.floor(target.population*.1))        
        else:
            target.population = 0
       
        if target.buildings > 0:
            target.buildings = target.buildings - random.randint(0, math.floor(target.buildings*.15))
        else:
            target.buildings = 0

        if target.stoplights > 0:
            target.stoplights = target.stoplights - random.randint(0, math.floor(target.stoplights*.12))
        else:
            target.stoplights = 0
        
    def rampage(self, indiana: [Town]) -> list:
        
        self.location = indiana

        terrorized_towns = []

        for town in indiana:
            self.terrorize_town(town)
            print(town.describe_town())


        return terrorized_towns
    
    @property
    def MutantMMI(self) -> float:
        return (self.weight/200)/(self.height*.10)
