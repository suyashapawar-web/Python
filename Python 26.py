class Robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
Tom = Robot("Tom", 10)
Jerry = Robot("Jerry", 15)
print("{} is {} years old".format(Tom.name, Tom.age))
print("{} is {} years old".format(Jerry.name, Jerry.age))