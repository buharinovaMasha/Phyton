"""
Современные парадигмы программирования на Python
Лабораторная работа 2. ООП
Реализовать иерархию классов некоторой 
предметной области.
Реализовать сериализацию/десериализацию
состояния в json (xml, html...)
"""

from pprint import pprint
import json

from Person import Person
from Room import Room
from Hostel import Hostel, HostelSerialize, HostelDeserialize


oldHostel = Hostel("1", "2", 
                [Room("3", [
                    Person("4", "5", "6", "7"), 
                    Person("8", "9", "10", "11"), 
                    Person("12", "13", "14", "15")]), 
                Room("16", [
                    Person("17", "18", "19", "20"), 
                    Person("21", "22", "23", "24"), 
                    Person("25", "26", "27", "28")])])


HostelSerialize(oldHostel, "1.json")
newHostel = HostelDeserialize("1.json")
pprint(newHostel.__dict__)


