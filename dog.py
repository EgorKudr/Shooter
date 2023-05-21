class Dog:
    def __init__(self, age, color, name=None):
        self.age = age
        self.color = color
        self.name = name
    def bark(self):
        print("собака ", self.name, "сделала гаф")