import json


class A:
    def __init__(self, name, id):
        self.name = name
        self.id = id


a = A("Pionpill", "12345")
print(a.__dict__)
a.address = "214000"
print(a.__dict__)
