from Student import Student

def main():
    student = Student()
    student2 = Student()

    student.setName('Alex')
    student.setRollNumber(123)
    print(student.getName())
    print(student.getRollNumber())

    student2.setName('Igor')
    print(student.getName())
    print(student2.getName())

main()