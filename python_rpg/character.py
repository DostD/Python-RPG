""" character.py
The base class for the player and any NPCs in the game. Will have attributes
and behavior common to all characters
"""

class Character:
    """Any playing and non-playing characters share these traits
    
    Attributes:
        name: a string
        class_name: string name of character class
        strength: int physical power and carrying capacity
        dexterity: int agility, balance, coordintion
        constitution: int endurance, stamina, health
        intelligence: int reasoning, knowledge, memory
        ...and so on (you chose which of these you want)"""
    
    def __init__(self, name: str, class_name="") -> None:
        self.name = name
        self.class_name = class_name

        # initialize all remanining stats (we'll create a function to set them)
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0

    def get_stats(self) -> str:
        """ return a formatted string of stats """   
        stats = f"Name: {self.name}\nClass: {self.class_name}\n"
        stats += f"Strength: {self.strength}\nDexterity: {self.dexterity}"
        stats += f"\nConstitution: {self.constitution}"
        stats += f"\nIntelligence: {self.intelligence}"
        return stats
    
# global scope
if __name__ == "__main__":
    player = Character("Riven", "Grave-Walker")
    print(player.get_stats())