class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tiredness = 50
        self.hapiness = 50
    def sleep(self):
        self.tiredness += 0
    def lay(self):
        self.tiredness += 20
    def eat(self):
        self.hapiness += 75
    def play(self):
        self.hapiness += 100
        self.tiredness += 75