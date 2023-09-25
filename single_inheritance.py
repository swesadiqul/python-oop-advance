class Pet:
    def __init__(self, name):
        self.name = name

    def feed(self):
        pass

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        
    def feed(self):
        return f"{self.name} is eating dog food."

class Cat(Pet):
    def feed(self):
        return f"{self.name} is eating cat food."

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.feed())  # Output: Buddy is eating dog food.
print(cat.feed())  # Output: Whiskers is eating cat food.



