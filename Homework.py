class Kindergarten:

    target_group = 'children'

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self._hobby = hobby

    def get_name(self):
        return f"This is {self.name}."

    def get_age(self):
        return f"He/she is {self.age}."

    def get_hobby(self):
        return f"He/she likes {self._hobby}."

    def set_new_hobby(self, new_hobby):
        self._hobby = new_hobby


child_1 = Kindergarten("Anna", 5, 'painting')
print(child_1.get_name())
print(child_1.get_age())
print(child_1.get_hobby())
print(child_1.target_group)

child_2 = Kindergarten("Mark", 4, 'reading')
print(child_2.get_name())
print(child_2.get_age())
print(child_2.get_hobby())
print(child_2.target_group)


class Group(Kindergarten):

    def __init__(self, name, age, hobby, parents):
        super().__init__(name, age, hobby)
        self.parents = parents

    def under_five(self):
        if self.age < 5:
            return "He/she is under 5 years ols"
        else:
            return "He/she is over 5 years old"

    def full_family(self):
        if self.parents >= 2:
            return "He/she has full family "
        else:
            return "He/she has no full family"


child_3 = Group("Tina", 6, "jumping", 2)

print(child_3.get_name())
print(child_3.get_age())
print(child_3.get_hobby())
print(child_3.under_five())
print(child_3.full_family())

child_1.set_new_hobby('eating ice cream')
print(child_1.get_hobby())










