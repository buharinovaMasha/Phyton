import json

# Человек
class Person :
    def __init__(self, name = "", age = 0, well = "", citizenship = ""):
        self.name = name
        self.age = age
        self.well = well
        self.citizenship = citizenship
        
    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self)-> str:
        return self.__str__()


     
if __name__ == "__main__":
    a = Person(1, 2, 3, 4)
    print(a.__dict__)






