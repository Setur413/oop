class Power:
    def __init__(self, name, description, power_level):
        self.name = name
        self.description = description
        self.power_level = power_level

class Superhero:
    def __init__(self, name, secret_identity, powers=None):
        self.name = name
        self._secret_identity = secret_identity  # Encapsulated attribute
        self.powers = powers if powers else []
        self.health = 100
        self.experience = 0
    
    def add_power(self, power):
        """Add a new power to the hero's abilities."""
        self.powers.append(power)
        print(f"{self.name} learned {power.name}!")
    
    def reveal_identity(self, password):
        """Demonstrate encapsulation by protecting the secret identity."""
        if password == "HEROES_UNITE":
            return self._secret_identity
        return "Nice try, villain!"
    
    def train(self):
        """Increase experience through training."""
        self.experience += 10
        print(f"{self.name} trained hard! Experience: {self.experience}")
    
    def total_power_level(self):
        """Calculate hero's total power level."""
        return sum(power.power_level for power in self.powers)

class Sidekick(Superhero):
    def __init__(self, name, secret_identity, mentor):
        super().__init__(name, secret_identity)
        self.mentor = mentor
        self.training_level = 1
    
    def train_with_mentor(self):
        """Override train method to include mentor bonus."""
        self.experience += 15  # Extra experience due to mentor guidance
        self.training_level += 1
        print(f"{self.name} trained with {self.mentor}!")
        print(f"Training Level: {self.training_level}")
    
    def assist_hero(self, mission_difficulty):
        """Special method for sidekicks."""
        success_chance = self.training_level * 10
        print(f"Assist chance: {success_chance}% on difficulty {mission_difficulty}")

# Example usage:
if __name__ == "__main__":
    # Create some powers
    super_strength = Power("Super Strength", "Ability to lift incredible weights", 80)
    flight = Power("Flight", "Ability to soar through the skies", 70)
    
    # Create a main hero
    superman = Superhero("Superman", "Clark Kent")
    superman.add_power(super_strength)
    superman.add_power(flight)
    
    # Create a sidekick
    robin = Sidekick("Robin", "Dick Grayson", "Batman")
    robin.train_with_mentor()
    
    # Demonstrate functionality
    print(f"Superman's total power level: {superman.total_power_level()}")
    print(f"Superman's identity: {superman.reveal_identity('WRONG_PASSWORD')}")
    print(f"Superman's identity: {superman.reveal_identity('HEROES_UNITE')}")
    
    robin.assist_hero(5)