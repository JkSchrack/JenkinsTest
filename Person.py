import datetime

class Person:
    def __init__(self, name, location, age):
        self.name = name
        self.location = location
        self.age = age

    def dob(self):
        print("%s is %d and was born in %d... maybe." % (self.name, self.age, datetime.datetime.now().year-self.age))
