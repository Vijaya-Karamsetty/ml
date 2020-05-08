import json


class Student:
    def __init__(self, sid, name, email, age, other_names, friends):
        self.id = sid
        self.name = name
        self.age = age
        self.email = email
        self.other_names = other_names
        self.friends = friends


def convertToJson(obj):
    return json.dumps(obj.__dict__)


def convertToObject(json_file):
    with open(json_file, 'r') as file:
        return Student(**json.load(file))


# convert Json to Python object

studentObj = convertToObject('Student.json')
for attr in dir(studentObj):
    print("Student.%s = %r" % (attr, getattr(studentObj, attr)))

# convert Object to Json
print(studentObj.__dict__)
