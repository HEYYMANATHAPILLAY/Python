# Constants
MAX_LOGIN_ATTEMPTS = 3
STUDENTS_FILE = "students.txt"
TUTORS_FILE = "tutors.txt"
RECEPTIONISTS_FILE = "receptionists.txt"
CLASSES_FILE = "classes.txt"

# Main menu
def display_main_menu():
    print("Brilliant Tuition Centre Management System")
    print("1. Admin Login")
    print("2. Receptionist Login")
    print("3. Tutor Login")
    print("4. Student Login")
    print("5. Exit")

# Admin login
# Constants
ADMINS_FILE = "admins.txt"

def admin_login():
    attempts = 0
    admin_credentials = read_admin_credentials()

    while attempts < MAX_LOGIN_ATTEMPTS:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Validate admin username and password
        if is_valid_admin_credentials(username, password, admin_credentials):
            print("Admin login successful.")
            admin_menu()
            break
        else:
            print("Invalid username or password. Please try again.")
            attempts += 1

    if attempts == MAX_LOGIN_ATTEMPTS:
        print("Max login attempts exceeded.")

# Function to read admin credentials from the file
def read_admin_credentials():
    admin_credentials = {}
    try:
        with open(ADMINS_FILE, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                admin_credentials[username] = password
    except FileNotFoundError:
        # If the file doesn't exist, return an empty dictionary
        return {}
    return admin_credentials

# Function to validate admin credentials
def is_valid_admin_credentials(username, password, admin_credentials):
    stored_password = admin_credentials.get(username)
    return stored_password == password

# Constants
TUTORS_FILE = "tutors.txt"
RECEPTIONISTS_FILE = "receptionists.txt"
INCOME_FILE = "income.txt"
ADMINS_FILE = "admins.txt"

# Function to register new tutors
def register_tutor():
    print("Registering a new tutor:")
    tutor_name = input("Enter tutor's name: ")
    tutor_password = input("Enter tutor's password: ")
    tutor_subjects = input("Enter tutor's subjects (comma-separated): ")
    tutor_contact = input("Enter tutor's contact number: ")

    # Create a string to represent the tutor's information
    tutor_info = f"{tutor_name},{tutor_password},{tutor_subjects},{tutor_contact}\n"

    # Append the tutor's information to the tutors file
    with open(TUTORS_FILE, "a") as file:
        file.write(tutor_info)

    print("Tutor registered successfully!")

# Function to delete tutors
def delete_tutor():
    print("Deleting a tutor:")
    tutor_name = input("Enter the name of the tutor to delete: ")

    # Read all tutors from the file
    with open(TUTORS_FILE, "r") as file:
        tutors = file.readlines()

    # Find and remove the tutor's information from the list
    updated_tutors = []
    tutor_found = False
    for tutor in tutors:
        if tutor.strip().startswith(tutor_name + ","):
            tutor_found = True
        else:
            updated_tutors.append(tutor)

    # Write the updated tutor list back to the file
    with open(TUTORS_FILE, "w") as file:
        file.writelines(updated_tutors)

    if tutor_found:
        print(f"Tutor '{tutor_name}' has been deleted.")
    else:
        print(f"Tutor '{tutor_name}' not found.")


# Function to register new receptionists
def register_receptionist():
    print("Registering a new receptionist:")
    receptionist_name = input("Enter receptionist's name: ")
    receptionist_username = input("Enter receptionist's username: ")
    receptionist_password = input("Enter receptionist's password: ")

    # Create a string to represent the receptionist's information
    receptionist_info = f"{receptionist_name},{receptionist_username},{receptionist_password}\n"

    # Append the receptionist's information to the receptionists file
    with open(RECEPTIONISTS_FILE, "a") as file:
        file.write(receptionist_info)

    print("Receptionist registered successfully!")

# Function to delete receptionists
def delete_receptionist():
    print("Deleting a receptionist:")
    receptionist_username = input("Enter the username of the receptionist to delete: ")

    # Read all receptionists from the file
    with open(RECEPTIONISTS_FILE, "r") as file:
        receptionists = file.readlines()

    # Find and remove the receptionist's information from the list
    updated_receptionists = []
    receptionist_found = False
    for receptionist in receptionists:
        if receptionist.strip().split(",")[1] == receptionist_username:
            receptionist_found = True
        else:
            updated_receptionists.append(receptionist)

    # Write the updated receptionist list back to the file
    with open(RECEPTIONISTS_FILE, "w") as file:
        file.writelines(updated_receptionists)

    if receptionist_found:
        print(f"Receptionist with username '{receptionist_username}' has been deleted.")
    else:
        print(f"Receptionist with username '{receptionist_username}' not found.")

# Function to view monthly income report
def view_monthly_income_report():
    print("Monthly Income Report:")
    Month = input("Enter the month of income report: ")
    level = input("Enter the level (e.g., Form 1, Form 2, ..., Form 5): ")
    subject = input("Enter the subject: ")

    # Read all income records from the file
    with open(INCOME_FILE, "r") as file:
        income_records = file.readlines()

    total_income = 0
    subject_found = False
    subjects_taken = []

    for record in income_records:
        parts = record.strip().split(",")
        # Skip lines that don't have the correct number of parts
        if len(parts) != 5:
            continue
        record_month, record_level, record_subjects, _, income = parts
        if record_month.lower() == Month.lower() and record_level.lower() == level.lower() and subject.lower() in record_subjects.lower().split(", "):
            total_income += float(income)
            subjects_taken.extend(record_subjects.split(", "))
            subject_found = True

    if subject_found:
        print(f"Total income for {subject} at {level} in {Month}: RM {total_income}")
        print(f"Subjects taken by the student in {Month}: {', '.join(set(subjects_taken))}")
    else:
        print(f"No income records found for {subject} at {level} in {Month}.")


# Function to update admin's own profile
def update_own_profile_admin():
    print("Updating your profile:")
    admin_username = input("Enter your username: ")
    admin_password = input("Enter your current password: ")

    # Read all admins from the file
    with open(ADMINS_FILE, "r") as file:
        admins = file.readlines()

    # Find the admin's information in the list
    admin_info_index = None
    for index, admin in enumerate(admins):
        username, password = admin.strip().split(",")
        if username == admin_username and password == admin_password:
            admin_info_index = index
            break

    if admin_info_index is not None:
        # Update admin's profile
        new_admin_username = input("Enter new username (or leave empty to keep current): ")
        new_admin_password = input("Enter new password (or leave empty to keep current): ")

        if not new_admin_username:
            new_admin_username = admin_username
        if not new_admin_password:
            new_admin_password = admin_password

        # Modify the admin's information in the list
        admins[admin_info_index] = f"{new_admin_username},{new_admin_password}\n"

        # Write the updated admin list back to the file
        with open(ADMINS_FILE, "w") as file:
            file.writelines(admins)

        print("Profile updated successfully!")
    else:
        print("Invalid username or password. Profile update failed.")


# Admin menu
def admin_menu():
    while True:
        print("Admin Menu:")
        print("1. Register/Delete Tutors")
        print("2. Register/Delete Receptionists")
        print("3. View Monthly Income Report")
        print("4. Update Admins own profile")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("1. Register Tutor")
            print("2. Delete Tutor")
            sub_choice = input("Enter your sub-choice: ")

            if sub_choice == "1":
                register_tutor()
            elif sub_choice == "2":
                delete_tutor()
            else:
                print("Invalid sub-choice. Please try again.")

        elif choice == "2":
            print("1. Register Receptionist")
            print("2. Delete Receptionist")
            sub_choice = input("Enter your sub-choice: ")

            if sub_choice == "1":
                register_receptionist()
            elif sub_choice == "2":
                delete_receptionist()
            else:
                print("Invalid sub-choice. Please try again.")

        elif choice == "3":
            view_monthly_income_report()
        elif choice == "4":
            update_own_profile_admin()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")



# Receptionist login
# Constants
MAX_LOGIN_ATTEMPTS = 3
RECEPTIONISTS_FILE = "receptionists.txt"

# Function to read receptionist credentials from the file
def read_receptionist_credentials():
    receptionist_credentials = {}
    try:
        with open(RECEPTIONISTS_FILE, "r") as file:
            for line in file:
                name, username, password = line.strip().split(",")
                receptionist_credentials[username] = password
    except FileNotFoundError:
        return {}
    return receptionist_credentials

# Function to validate receptionist credentials
def is_valid_receptionist_credentials(username, password, receptionist_credentials):
    stored_password = receptionist_credentials.get(username)
    return stored_password == password

# Receptionist login
def receptionist_login():
    attempts = 0
    receptionist_credentials = read_receptionist_credentials()

    while attempts < MAX_LOGIN_ATTEMPTS:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if is_valid_receptionist_credentials(username, password, receptionist_credentials):
            print("Receptionist login successful.")
            receptionist_menu()  # Call the receptionist menu function here
            break
        else:
            print("Invalid username or password. Please try again.")
            attempts += 1

    if attempts == MAX_LOGIN_ATTEMPTS:
        print("Max login attempts exceeded.")


# Receptionist menu
def receptionist_menu():
    while True:
        print("Receptionist Menu:")
        print("1. Register Student and Enroll Subjects")
        print("2. Update Subject Enrollment of a Student")
        print("3. Accept Payment and Generate Receipts")
        print("4. Delete Students Who Have Completed Studies")
        print("5. Update Own Profile")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student_enroll_subjects()
        elif choice == "2":
            update_subject_enrollment()
        elif choice == "3":
            accept_payment_generate_receipts()
        elif choice == "4":
            delete_completed_students()
        elif choice == "5":
            update_own_profile_receptionist()
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to register a student and enroll subjects
# Constants
STUDENTS_FILE = "students.txt"  # Assuming you have a students file

def register_student_enroll_subjects():
    print("Registering a new student and enrolling in subjects:")
    student_name = input("Enter student's name: ")
    student_username = input("Enter student's username: ")
    student_password = input("Enter student's password: ")
    enrolled_subjects = input("Enter subjects to enroll (comma-separated): ")

    # Create a string to represent the student's information
    student_info = f"{student_name},{student_username},{student_password},{enrolled_subjects}\n"

    # Append the student's information to the students file
    with open(STUDENTS_FILE, "a") as file:
        file.write(student_info)

    print("Student registered and enrolled successfully!")

# You can call this function from the receptionist_menu() where the receptionist can perform this action.


# Function to update subject enrollment of a student
# Constants
STUDENTS_FILE = "students.txt"  # Assuming you have a students file

# Function to update subject enrollment of a student
def update_subject_enrollment():
    print("Updating subject enrollment of a student:")
    student_username = input("Enter student's username: ")

    # Read all students from the file
    with open(STUDENTS_FILE, "r") as file:
        students = file.readlines()

    # Find and update the student's information
    student_found = False
    updated_students = []

    for student in students:
        parts = student.strip().split(",")

        if len(parts) >= 2:  # Check if the line has at least 2 values (name, username)
            student_name = parts[0]
            username = parts[1]
            password = parts[2] if len(parts) > 2 else ""  # Default password to empty string if not provided

            if len(parts) > 3:
                enrolled_subjects = parts[3]
            else:
                enrolled_subjects = ""

            if username == student_username:
                new_enrolled_subjects = input("Enter updated subjects (comma-separated): ")
                updated_student_info = f"{student_name},{username},{password},{new_enrolled_subjects}\n"
                updated_students.append(updated_student_info)
                student_found = True
            else:
                updated_students.append(student)
        else:
            # Handle lines with incorrect format (e.g., not enough values)
            print(f"Skipping line with incorrect format: {student}")

    # Write the updated student list back to the file
    with open(STUDENTS_FILE, "w") as file:
        file.writelines(updated_students)

    if student_found:
        print(f"Subject enrollment for student '{student_username}' updated successfully.")
    else:
        print(f"Student with username '{student_username}' not found.")


# You can call this function from the receptionist_menu() where the receptionist can perform this action.



# Function to accept payment and generate receipts
# Constants
STUDENTS_FILE = "students.txt"  # Assuming you have a students file
INCOME_FILE = "income.txt"  # File to store income records

def accept_payment_generate_receipts():
    print("Accepting Payment and Generating Receipts:")

    # Input student's username for payment
    student_username = input("Enter student's username: ")

    # Input month of payment
    payment_month = input("Enter month of payment: ")

    # Input student's form level
    form_level = input("Enter the level (e.g., Form 1, Form 2, ..., Form 5): ")

    # Read all students from the file
    with open(STUDENTS_FILE, "r") as file:
        students = file.readlines()

    # Find the student's information
    student_found = False
    updated_students = []

    for student in students:
        parts = student.strip().split(",")
        if len(parts) >= 4 and parts[1] == student_username:
            student_name, username, password, *enrolled_subjects = parts
            payment_amount = float(input("Enter payment amount: "))
            receipt = generate_receipt(student_name, enrolled_subjects, payment_amount, payment_month, form_level)  # Generate a receipt
            student_found = True
        updated_students.append(student)

    # Write the updated student list back to the file
    with open(STUDENTS_FILE, "w") as file:
        file.writelines(updated_students)

    if student_found:
        print(f"Payment accepted for student '{student_username}'.")
        print("Receipt:")
        print(receipt)
    else:
        print(f"Student with username '{student_username}' not found.")

# Function to generate a receipt
def generate_receipt(student_name, enrolled_subjects, payment_amount, payment_month, form_level):
    # You can customize the receipt format here
    receipt = f"Receipt for: {student_name}\n"
    receipt += f"Enrolled Subjects: {', '.join(enrolled_subjects)}\n"
    receipt += f"Payment Month: {payment_month}\n"
    receipt += f"Form Level: {form_level}\n"
    receipt += f"Payment Amount: {payment_amount} RM\n"
    receipt += "-------------------------\n"

    # Save the receipt to the income file
    with open(INCOME_FILE, "a") as file:
        file.write(receipt)

        # Write a line to the file in a format that can be easily read back
        file.write(f"{payment_month},{form_level},{', '.join(enrolled_subjects)},{payment_amount}\n")

    return receipt


# Function to delete students who have completed studies
def delete_completed_students():
    with open(STUDENTS_FILE, "r") as file:
        lines = file.readlines()

    completed_students = []

    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 3:  # Students with no subjects have 3 parts
            completed_students.append(line)

    if completed_students:
        print("Completed students (students with no subjects enrolled):")
        for student in completed_students:
            print(student.strip())

        confirmation = input("Do you want to delete these completed students? (yes/no): ").lower()
        if confirmation == "yes":
            with open(STUDENTS_FILE, "w") as file:
                for line in lines:
                    if line not in completed_students:
                        file.write(line)
            print("Completed students deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("No completed students found.")



# Function to update receptionist's own profile
def update_own_profile_receptionist():
    print("Updating your profile:")
    receptionist_username = input("Enter your username: ")
    receptionist_password = input("Enter your current password: ")

    # Read all receptionists from the file
    with open(RECEPTIONISTS_FILE, "r") as file:
        receptionists = file.readlines()

    # Find and update the receptionist's information
    receptionist_found = False
    updated_receptionists = []

    for receptionist in receptionists:
        parts = receptionist.strip().split(",")
        if len(parts) == 3 and parts[1] == receptionist_username:
            name, username, _ = parts
            new_password = input("Enter new password (or leave empty to keep current): ")

            # Update the password
            if not new_password:
                new_password = parts[2]

            updated_receptionist_info = f"{name},{username},{new_password}\n"
            updated_receptionists.append(updated_receptionist_info)
            receptionist_found = True
        else:
            updated_receptionists.append(receptionist)

    # Write the updated receptionist list back to the file
    with open(RECEPTIONISTS_FILE, "w") as file:
        file.writelines(updated_receptionists)

    if receptionist_found:
        print("Profile updated successfully!")
    else:
        print("Invalid username or password. Profile update failed.")


# Constants
MAX_LOGIN_ATTEMPTS = 3
TUTORS_FILE = "tutors.txt"
classes = []

def load_tutors_from_file(file_path):
    tutors = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 4:
                    name = parts[0].strip()
                    password = parts[1].strip()
                    subjects = parts[2].strip()
                    contact = parts[3].strip()
                    tutor = {
                        "name": name,
                        "password": password,
                        "subjects": subjects,
                        "contact": contact
                    }
                    tutors.append(tutor)
    except FileNotFoundError:
        return []

    return tutors


# Function to read tutor credentials from the file
def read_tutor_credentials():
    tutor_credentials = {}
    try:
        with open(TUTORS_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 2:
                    username = parts[0].strip()
                    password = parts[1].strip()
                    tutor_credentials[username] = password
    except FileNotFoundError:
        pass
    return tutor_credentials

# Function to validate tutor credentials
def is_valid_tutor_credentials(username, password, tutor_credentials):
    stored_password = tutor_credentials.get(username)
    return stored_password == password

# Tutor login
# Tutor login
# Tutor login
def tutor_login(tutors):  # Add the tutors parameter
    attempts = 0
    tutor_credentials = read_tutor_credentials()

    while attempts < MAX_LOGIN_ATTEMPTS:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if is_valid_tutor_credentials(username, password, tutor_credentials):
            print("Tutor login successful.")
            tutor_menu(tutors)  # Pass the tutors list to the tutor menu function
            break
        else:
            print("Invalid username or password. Please try again.")
            attempts += 1

    if attempts == MAX_LOGIN_ATTEMPTS:
        print("Max login attempts exceeded.")



# Function to add class information
def add_class_information():
    class_id = input("Enter class id: ")  # Prompt for class id
    tutor_name = input("Enter tutor name: ")
    subject_name = input("Enter subject name: ")
    charges = float(input("Enter charges for the class: "))
    class_schedule = input("Enter class schedule: ")

    new_class = {
        "class_id": class_id,  # Add class id to the class information
        "tutor_name": tutor_name,
        "subject_name": subject_name,
        "charges": charges,
        "class_schedule": class_schedule
    }

    classes.append(new_class)
    print("Class information added successfully!")

    # Save the updated class information to a file (e.g., classes.txt)
    save_classes_to_file()

def save_classes_to_file():
    with open(CLASSES_FILE, "w") as file:
        for class_info in classes:
            line = f"{class_info['tutor_name']},{class_info['subject_name']},{class_info['charges']},{class_info['class_schedule']}\n"
            file.write(line)
    print("Class information saved to file.")

# Function to update and delete class information
def update_delete_class_information():
    print("Update and Delete Class Information:")
    print("1. Update Class Information")
    print("2. Delete Class Information")
    sub_choice = input("Enter your sub-choice: ")

    if sub_choice == "1":
        update_class_information()
    elif sub_choice == "2":
        delete_class_information()
    else:
        print("Invalid sub-choice. Please try again.")

def update_class_information():
    print("Updating Class Information:")
    class_id = input("Enter class id for the class to update: ")  # Update class by class id

    # Search for the class by class id
    class_to_update = None
    for class_info in classes:
        if class_info["class_id"] == class_id:  # Use class id to find the class
            class_to_update = class_info
            break

    if class_to_update:
        # Update class information
        print("Current Class Information:")
        print(f"Tutor: {class_to_update['tutor_name']}")
        print(f"Subject: {class_to_update['subject_name']}")
        print(f"Charges: {class_to_update['charges']}")
        print(f"Class Schedule: {class_to_update['class_schedule']}")

        # Prompt for new information
        new_charges = float(input("Enter new charges for the class: "))
        new_class_schedule = input("Enter new class schedule: ")

        # Update the class information
        class_to_update["charges"] = new_charges
        class_to_update["class_schedule"] = new_class_schedule

        # Save the updated class information to a file
        save_classes_to_file()
        print("Class information updated successfully!")
    else:
        print("Class not found.")

def delete_class_information():
    print("Deleting Class Information:")
    class_id = input("Enter class id for the class to delete: ")  # Delete class by class id

    # Search for the class by class id
    class_to_delete = None
    for class_info in classes:
        if class_info["class_id"] == class_id:  # Use class id to find the class
            class_to_delete = class_info
            break

    if class_to_delete:
        # Remove the class from the list
        classes.remove(class_to_delete)

        # Save the updated class information to a file
        save_classes_to_file()
        print("Class information deleted successfully!")
    else:
        print("Class not found.")




# Function to view list of students enrolled
def view_enrolled_students():
    print("Viewing Enrolled Students:")

    tutor_name = input("Enter tutor name: ")
    subject_name = input("Enter subject name: ")

    # Search for the class with the given tutor and subject
    class_found = False
    for class_info in classes:
        if class_info["tutor_name"] == tutor_name and class_info["subject_name"] == subject_name:
            class_found = True
            print(f"Enrolled students for {subject_name} class by {tutor_name}:")
            # In a real implementation, you would fetch the enrolled students' data
            # and display it here. For this example, we'll just display a placeholder message.
            print("Student 1")
            print("Student 2")
            print("Student 3")
            break

    if not class_found:
        print("Class not found.")


def update_own_profile_tutor(tutors):
    print("Updating your profile:")
    tutor_username = input("Enter your username: ")
    tutor_password = input("Enter your current password: ")

    # Read all tutor information from the file
    tutor_credentials = read_tutor_credentials()

    # Find the tutor's information in the list
    tutor_info_index = None
    for index, (username, password) in enumerate(tutor_credentials.items()):
        if username == tutor_username and password == tutor_password:
            tutor_info_index = index
            break

    if tutor_info_index is not None:
        print("Enter new details:")
        new_tutor_name = input("Enter new name: ")
        new_tutor_password = input("Enter new password: ")
        new_tutor_subjects = input("Enter new subjects (comma-separated): ")
        new_tutor_contact = input("Enter new contact number: ")

        # Update tutor's information
        tutor_credentials[new_tutor_name] = new_tutor_password

        # Save the updated tutor credentials back to the file
        with open(TUTORS_FILE, "w") as file:
            for username, password in tutor_credentials.items():
                tutor_info = f"{username},{password}\n"
                file.write(tutor_info)

        # Update tutor's details in the tutors list
        for tutor in tutors:
            if tutor['name'] == tutor_username:  # Update based on tutor's name
                tutor['name'] = new_tutor_name
                tutor['password'] = new_tutor_password
                tutor['subjects'] = new_tutor_subjects.split(',')
                tutor['contact'] = new_tutor_contact
                break

        # Save the updated tutors list to file (using the same function as classes)
        save_tutors_to_file(tutors)

        print("Profile updated successfully!")
    else:
        print("Invalid username or password. Profile update failed.")

def save_tutors_to_file(tutors):
    with open(TUTORS_FILE, "w") as file:
        for tutor in tutors:
            tutor_info = f"{tutor['name']},{tutor['password']},{tutor['subjects']},{tutor['contact']}\n"
            file.write(tutor_info)
    print("Tutor information saved to file.")

def load_tutors_from_file(file_path):
    tutors = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 4:  # Assuming at least 4 parts for tutor info
                    name = parts[0].strip()
                    password = parts[1].strip()
                    subjects = parts[2].strip()
                    contact = parts[3].strip()
                    tutor = {
                        "name": name,
                        "password": password,
                        "subjects": subjects,
                        "contact": contact
                    }
                    tutors.append(tutor)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []

    return tutors

# Main function
def tutor_menu(tutors):
        while True:
            print("Tutor Menu:")
            print("1. Add Class Information")
            print("2. Update and Delete Class Information")
            print("3. View List of Students Enrolled")
            print("4. Update Own Profile")
            print("5. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_class_information()
            elif choice == "2":
                update_delete_class_information()
            elif choice == "3":
                view_enrolled_students()
            elif choice == "4":
                    update_own_profile_tutor(tutors)  # Pass the tutors list to the function
                    pass
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")



# Define the path to the student data file
STUDENTS_FILE = "student_data.txt"

# Function to load student data from a file
def load_student_data():
    try:
        student_data = []
        with open(STUDENTS_FILE, "r") as file:
            for line in file:
                # Split the line into individual pieces of student information
                student_info = line.strip().split(',')
                student = {
                    'username': student_info[0],
                    'password': student_info[1],
                    # Add more fields as needed
                }
                student_data.append(student)
        return student_data
    except FileNotFoundError:
        print(f"Student data file '{STUDENTS_FILE}' not found.")
        return []

# Function to validate student login credentials
def validate_login(username, password):
    student_data = load_student_data()
    for student in student_data:
        if student['username'] == username and student['password'] == password:
            return True
    return False
#Student login
# Constants
STUDENTS_FILE = "students.txt"

def student_login():
    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if validate_login(username, password):
            print("Login successful!")

            # return username, password
            student_menu(username)

        print("Invalid username or password. Please try again.")
        attempts += 1

    print("Too many login attempts. Please contact the support team.")

# Student menu
def student_menu(username):
    while True:
        print("Student Menu:")
        print("1. View Schedule of Classes")
        print("2. Send Request to Change Subject Enrollment")
        print("3. Delete Pending Change Subject Request")
        print("4. View Payment Status and Balance")
        print("5. Update Own Profile")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_class_schedule(username)
        elif choice == "2":
            new_subject_name = input("Enter new subject name: ")
            send_request_change_subject_enrollment(username, subject_name, new_subject_name)
        elif choice == "3":
            request_index = int(input("Enter the index of the request to delete: ")) - 1
            delete_change_request(username, request_index)
        elif choice == "4":
            view_payment_status(username)
        elif choice == "5":
            update_own_profile(username)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to view schedule of classes
def view_class_schedule(username):
    print("Viewing class schedule for:", username)
    student_data = load_student_data()
    print("Loaded student data:", student_data)

    for student in student_data:
        print("Checking student:", student['username'])
        if student['username'] == username:
            print("Student found:", student['username'])
            print("Class Schedule:")
            for subject in student['subjects']:
                print(f"Subject: {subject['name']}, Time: {subject['time']}")
            return
    print("Student not found.")

# Function to send request to change subject enrollment
def send_request_change_subject_enrollment(username, subject_name, new_subject_name):
    student_data = load_student_data()
    for student in student_data:
        if student['username'] == username:
            print("Before change request:", student['change_requests'])
            request = {
                'subject_name': subject_name,
                'new_subject_name': new_subject_name
            }
            student['change_requests'].append(request)
            print("After change request:", student['change_requests'])
            save_student_data(student_data)
            print("Change request sent successfully.")
            return
    print("Student not found.")

# Function to delete pending change subject request
def delete_change_request(username, request_index):
    student_data = load_student_data()
    for student in student_data:
        if student['username'] == username:
            request_index = int(input("Enter the index of the request to delete: ")) - 1
            if 0 <= request_index < len(student['change_requests']):
                del student['change_requests'][request_index]
                save_student_data(student_data)
                print("Change request deleted successfully.")
            else:
                print("Invalid request index.")

# Function to view payment status
def view_payment_status(username):
    student_data = load_student_data()
    for student in student_data:
        if student['username'] == username:
            print(f"Payment Status: {student['payment_status']}")
            print(f"Total Balance: {student['total_balance']}")
            return
    print("Student not found.")


    # Function to update student's own profile
    def update_own_profile(username):
        student_data = load_student_data()
        for student in student_data:
            if student['username'] == username:
                print("Enter current profile information:")
                student['name'] = input("Name: ")
                student['contact'] = input("Contact: ")
                student['address'] = input("Address: ")

            print("Enter new profile information:")
            student['name'] = input("Name: ")
            student['contact'] = input("Contact: ")
            student['address'] = input("Address: ")

            # Save changes to student data after profile update
            save_student_data(student_data)
            print("Profile updated successfully.")
            return
        print("Student not found.")

        # Function to save student data
        def save_student_data(student_data):
            try:
                with open(STUDENTS_FILE, "w") as file:
                    for student in student_data:
                        # Convert the student's information into a comma-separated string
                        student_info = [
                            student['username'],
                            student['password'],
                            ','.join([f"{subject['name']}:{subject['time']}" for subject in student['subjects']]),
                            ','.join([f"{request['subject_name']}:{request['new_subject_name']}" for request in
                                      student['change_requests']]),
                            student['payment_status'],
                            str(student['total_balance']),
                            student['name'],
                            student['contact'],
                            student['address']
                        ]
                        student_info_str = ','.join(student_info)
                        file.write(student_info_str + "\n")
                print("Student data saved successfully.")
            except Exception as e:
                print("Error while saving student data:", e)

# Main program
def main():
    # Load tutors from file into the tutors list
    tutors = load_tutors_from_file(TUTORS_FILE)

    while True:
        display_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_login()
        elif choice == "2":
            receptionist_login()
        elif choice == "3":
            tutor_login(tutors)  # Pass the tutors list to the tutor_login function
        elif choice == "4":
            student_login()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
