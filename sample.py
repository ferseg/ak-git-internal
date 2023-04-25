class Greet: 
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello {self.name}')

# greet('Fernando')
# greet('Joseling')
# greet('Esteban')

greet_fer = Greet('Fernando')
greet_fer.greet()

greet_jos = Greet('Joseling')
greet_jo.greet()

