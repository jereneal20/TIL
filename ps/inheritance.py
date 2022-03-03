import abc
from typing import *

class Degree(metaclass=abc.ABCMeta):
    degree = None
    @abc.abstractmethod
    def get_degree(self):
        self.degree = "Master"
        return
        # raise NotImplementedError

class Person:
    def __init__(self):
        print("Person")

    def name(self):
        print("Alice")

class Student(Person, Degree):
    # pass
    def __init__(self):
        super().__init__()
        print("student")

    def get_degree(self):
        print("Stu master")
        print(self.degree)

    def tmp(self, li: List[int], tm: int) -> int:
        return li[tm]
        pass

a = Student()
li : List[str] = ["a"]
tm : int = 0
a.tmp(li, tm)
res: List[Person] = [Student(), Person()]
for ppl in res:
    ppl.name()
# a.get_degree()