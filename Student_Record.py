import os

doc_path = os.path.expanduser("~\Documents")
if not os.path.exists(doc_path):
    os.makedirs(doc_path)

while True:
    print("==== Student Records Menu ====\n" +
          "1. Register Student\n" +
          "2. Open Student Record\n" +
          "3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n==== Student Registration ====")
        studentNo = int(input("Student No.: "))
        lastName = input("Last Name: ")
        firstName = input("First Name: ")
        middleInitial = input("Middle Initial: ")
        program = input("Program: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        birthday = input("Birthday: ")
        contactNo = int(input("Contact No.: "))

        data = [
            f"Student No.: {studentNo}",
            f"Full Name: {lastName.capitalize()}, {firstName.capitalize()} {middleInitial.capitalize()}.",
            f"Program: {program.upper()}",
            f"Age: {age}",
            f"Gender: {gender.capitalize()}",
            f"Birthday: {birthday}",
            f"Contact No.: {contactNo}"
        ]

        file_path = os.path.join(doc_path, f"{studentNo}.txt")
        with open(file_path, "w") as f:
            for line in data:
                f.write(line + "\n")

    elif choice == 2:
        print("==== Open Student Record ====")
        studentNo = int(input("Enter Student No.: "))
        file_path = os.path.join(doc_path, f"{studentNo}.txt")
        try:
            with open(file_path, "r") as f:
                print("\n==== Student Record ====")
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("Error: Student record not found.")

    elif choice == 3:
        print("Goodbye!!!")
        break

    else:
        print("Invalid input. Please enter a valid number.")
