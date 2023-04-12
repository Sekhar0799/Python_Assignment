class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def fetch(self):
        print(f"{self.name} is fetching the ball!")

    def dig(self):
        print(f"{self.name} is digging a hole!")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def snore(self):
        print(f"{self.name} is snoring loudly!")

    def chew(self):
        print(f"{self.name} is chewing on a bone!")


# Creating objects

dog1 = Dog("Fido", 5, "brown")
dog1.description() 
dog1.get_info() 

terrier = JackRussellTerrier("Jack", 3, "white")
terrier.description() 
terrier.get_info() 
terrier.fetch() 
terrier.dig()

bulldog = Bulldog("Spike", 4, "gray")
bulldog.description() 
bulldog.get_info() 
bulldog.snore() 
bulldog.chew() 
