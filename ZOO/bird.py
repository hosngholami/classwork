from .animal import Animal

class Bird(Animal):
    def __repr__(self):
        return self.type

    def fly(self):
        if self.type == 'parandeh':
            return f"{self.name} can't fly"
        return f"{self.name} can fly"
    
