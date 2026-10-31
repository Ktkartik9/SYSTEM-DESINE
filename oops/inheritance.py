class Animal:
    def __init__(self, name: str, age: int):
        print("Animal INIT")
        self.name = name
        self.age = age

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

    def move(self):
        print("I am moving")


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print("I am barking")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Breed: {self.breed}")


dog = Dog("Cheery", 5, "Indie")

dog.display()
dog.eat()
dog.sleep()
dog.move()
dog.bark()