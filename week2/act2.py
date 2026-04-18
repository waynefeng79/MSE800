class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def show_info(self):
        print(f"name: {self.name} age: {self.age} id: {self.id}")

def main():
    a = Student("A", 35, 1234)
    b = Student("B", 20, 345)
    c = Student("C", 26, 567)

    students = [a, b, c]
    while True:
        order = input("Sort by(name/age/id): ")
        match order:
            case "name":
                students.sort(key=lambda x: x.name)
                break
            case "age":
                students.sort(key=lambda x: x.age)
                break
            case "id":
                students.sort(key=lambda x: x.id)
                break
            case _:
                print("Error sort type, input again!")

    for student in students:
        student.show_info()

if __name__ == "__main__":
    main()
    
