class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting with moderate hunger
        self.energy = 5  # Starting with moderate energy
        self.happiness = 5  # Starting with moderate happiness
        self.tricks = []  # List to store learned tricks

    def eat(self):
        """Reduces hunger by 3 points (but not below 0) and increases happiness by 1 (but not above 10)"""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        """Increases energy by 5 points (but not above 10)"""
        self.energy = min(10, self.energy + 5)

    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1"""
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        """Prints the current state of the pet"""
        print(f"\n----------- {self.name}'s Status --------------")
        print(f"Hunger:    {self.hunger}/10")
        print(f"Energy:    {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print("--------------------------------------------------")

    def train(self, trick):
        """Teaches the pet a new trick and stores it in the tricks list"""
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        """Prints all learned tricks"""
        if self.tricks:
            print(f"\n{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"--- {trick} ---")
        else:
            print(f"\n{self.name} hasn't learned any tricks yet.")
