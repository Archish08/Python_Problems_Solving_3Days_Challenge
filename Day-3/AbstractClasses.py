from abc import ABC

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Vehicle is car000")
    
c=Car()
c.start()