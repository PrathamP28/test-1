# 🍃🍀  
import json

class JsonFile:
    def add():
        pass
    def remove():
        pass
    def read():
        with open("data.json", "r") as file:
            data = json.load(file)

        john_age = next(person["age"] for person in data["data"] if person["name"] == "Jane")
        print(john_age)
    def list_projects():
        pass
    def edit():
        pass    



# written by Pratham 🍂🍁
