from abc import ABC, abstractclassmethod
import copy

"""
    Prototype Interface: Defines the clone method that must be implemented by any class that wants to allow cloning.
    Concrete Prototype (EnemyPrototype): Implements the clone method using copy.deepcopy to create a deep copy of the object.
    Client: Uses the prototype to create a clone and then customizes the cloned object as needed.
"""

# Step 1: Define prototype interface
class Prototype(ABC):
    @abstractclassmethod
    def clone():
        pass

# Step 2: Concrete prototype
class EnemyPrototype(Prototype):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Enemy (name={self.name}, health={self.health}, attack power={self.attack_power})"
    
# Step 3: Define client code
def client_code(prototype: EnemyPrototype):
    prototype_clone = prototype.clone()
    print("Before using client code on clone object", prototype_clone)
    prototype_clone.name = "Clone " + prototype_clone.name
    prototype_clone.health += 10
    prototype_clone.attack_power += 5
    print("After using client code on clone object", prototype_clone)

# Creating a prototype for a basic enemy
basic_enemy_prototype = EnemyPrototype("Goblin", 100, 15)
print("Original enemy:", basic_enemy_prototype)

# Using the prototype to create and customize new enemies
client_code(basic_enemy_prototype)

# Check again the original enemy
print("Original enemy:", basic_enemy_prototype)
