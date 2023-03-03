class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"


class Age:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Age: {self.age}"


class ChangeInfo:
    def change_info(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class SuperClass(ChangeInfo):
    pass


class FinalClass(Person, Age, SuperClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def some_method(self):
        pass

    def some_other_method(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

person = Person("John")
print(person)  

age = Age(25)
print(age)  

change_info = ChangeInfo()
change_info.change_info("Sarah", 30)
print(change_info)  

final_class = FinalClass("Mark", 40)
print(final_class)  
