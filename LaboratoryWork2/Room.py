import json
from Person import Person

# Комната
class Room :
    def __init__(self, number = 0, persons = []):
        self.number = number
        self.persons = persons
        self.__dict__["persons"] = [i.__dict__ for i in self.persons]
         
    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self)-> str:
        return self.__str__()

     
if __name__ == "__main__":
    a = Room(1, [Person(1, 2, 3, 4), Person(1, 2, 3, 4)])
    print(a.__dict__)





