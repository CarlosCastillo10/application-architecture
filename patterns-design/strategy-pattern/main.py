from operator import attrgetter
from person import Person

if __name__ == '__main__':
    persons = [
        Person("Israel", 21),
        Person("Pablo", 22),
        Person("Carlos", 22),
        Person("Jucaritas", 21)
    ]

print("Sorted by age")
print(sorted(persons, key=attrgetter('age')))


print("\nSorted by name")
print(sorted(persons, key=attrgetter('name')))


print("\nSorted by age and name")
print(sorted(persons, key=attrgetter('age', 'name')))