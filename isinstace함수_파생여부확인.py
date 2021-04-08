class Person:
    pass
class Bird:
    pass
class Student(Person):
    pass

p, s = Person(), Student()
print("p is instance of Person: ", isinstance(p, Person))    #isinstance 는 true false 구문임
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))