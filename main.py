class House:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType


    def __eq__(self, other):
        if isinstance(other, House):
           return self.numberOfFloors == other.numberOfFloors




h1 = House(18, 'ЖК Горский')
h2 = House(18, 'Домик в деревне')
print(h1 == h2)
