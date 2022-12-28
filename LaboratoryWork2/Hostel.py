import json
from Person import Person
from Room import Room

# Общага
class Hostel :
    def __init__(self, number = 0, address = "", rooms = []):
        self.number = number
        self.address = address
        self.rooms = rooms
        self.__dict__["rooms"] = [i.__dict__ for i in self.rooms]
    
    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self)-> str:
        return self.__str__()


# Функция сериализации общаги
def HostelSerialize(hostel, path):
    with open(path, 'w') as outfile:
        json.dump(hostel.__dict__, outfile, indent=4)
        

# Функция десериализации общаги
def HostelDeserialize(pas):
    def Decode(obj):
        if "rooms" in obj:
            return Hostel(obj["number"], obj["address"], [Decode(i) for i in obj["rooms"]])
        elif "persons" in obj:
            return Room(obj["number"], [Decode(i) for i in obj["persons"]])
        else:
            return Person(obj["name"], obj["age"], obj["well"], obj["citizenship"])
    with open(pas) as json_file:
        data = json.load(json_file)
    return Decode(data)
     
     
if __name__ == "__main__":    
    a = Hostel(1, "2", [Room(1, [Person(1, 2, 3, 4), Person(1, 2, 3, 4)]), Room(1, [Person(1, 2, 3, 4), Person(1, 2, 3, 4)])])
    print(a.__dict__)






