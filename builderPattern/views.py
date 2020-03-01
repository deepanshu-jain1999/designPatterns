# Basic example of Builder Pattern
# Product to be made: Car
# Components: Engine, Tyres, Speedometer

# Product: Complex object to be made.


class Car:
    '''
    Product: Complex object to be made.
    '''

    def __init__(self):
        self.engine = None
        self.tyres = None
        self.speedometer = None

    def __str__(self):
        return '{} | {} | {}'.format(self.engine, self.tyres, self.speedometer)


class AbstractBuilder:
    '''
    Abstract Builder: provides an interface to create a car object.
    '''

    def __init__(self):
        self.car = None

    def createNewCar(self):
        self.car = Car()


class ConcreteBuilder(AbstractBuilder):
    '''
    Concrete Builder: inherits the Abstract Builder and implements the above interface createNewCar
    of the Abstract Builder class for a car object i.e. to say that
    its object is capable of creating a car by calling createNewCar() of AbstractBuilder;
    provides methods to create components of the product.
    '''

    def addEngine(self, value):
        self.car.engine = value

    def addTyres(self, value):
        self.car.tyres = value

    def addSpeedometer(self, value):
        self.car.speedometer = value


class Director:
    '''
    Director: in charge of building the product using an object of Concrete Builder
    '''

    def __init__(self, builder):
        self._builder = builder

    def constructCar(self):
        self._builder.createNewCar()
        self._builder.addEngine("eng")
        self._builder.addTyres("mrf")
        self._builder.addSpeedometer("speed")

    def getCar(self):
        return self._builder.car


concreteBuilder = ConcreteBuilder()
director = Director(concreteBuilder)
director.constructCar()
carOne = director.getCar()
print("Details of carOne:", carOne)
