class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    #Inherit from the Super Class (Animal)
    def __init__(self):
        super().__init__()
    #Modify the existing breathe method
    def breathe(self):
        super().breathe()
        print("Underwater")

    def swim(self):
        print("Swimming along.")

nemo = Fish()
nemo.swim()
nemo.breathe()