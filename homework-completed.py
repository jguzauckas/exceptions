# Create a class to represent a person.
# The class should have the following variables:
# - name - str
# - age - int
# - occupation - str
# - hobbies - list[str]
# The class should have the following methods:
# - __init__() - takes in one hobby to start a list
# - __str__()
# - hello() - prints a greeting to that person
# - add_hobby() - adds a provided string to the hobbies list
# - specific_hobby() - user gives an index, function returns hobby
#   at that index. Check for IndexError
# - getter and setter methods for name, age, and occupation. Make sure
#   to check for values that are acceptable. Raise a ValueError if they try
#   to set age to a negative number


class Person:
    def __init__(self, n: str, a: int, o: str, h: str) -> None:
        self._name = n
        self._age = a
        self._occupation = o
        self._hobbies = list()
        self._hobbies.append(h)

    def __str__(self) -> str:
        return f"{self._name} works in {self._occupation} and is {self._age} years old."

    def hello(self) -> None:
        print(f"Hello {self._name}!")

    def add_hobby(self, h: str) -> None:
        self._hobbies.append(h)

    def specific_hobby(self, i: int) -> str:
        try:
            ans = self._hobbies[i]
        except IndexError as ie:
            print(ie)
        else:
            return ans

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, n: str) -> None:
        self._name = n

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, a: int) -> None:
        if a < 0:
            raise ValueError("Can't have a negative age")
        self._age = a

    @property
    def occupation(self) -> str:
        return self._occupation

    @occupation.setter
    def occupation(self, o: str) -> None:
        self._occupation = o


# Test each of your methods with an instance of a Person
p1 = Person("Mr. G", 24, "Teacher", "Gamer")
print(p1)
p1.hello()
p1.add_hobby("Programmer")
p1.specific_hobby(3)
p1.specific_hobby(1)
p1.name = "Mr. Guzauckas"
print(p1.name)
p1.occupation = "Math and Computer Science Teacher"
print(p1.occupation)
print(p1.age)
p1.age = -5
