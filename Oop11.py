# Class Method @classmethod (decorator)
class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Anver Ali")
print(p1.name)
print(Person.name)