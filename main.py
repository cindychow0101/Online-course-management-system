import sqlite3
import csv

# Create tables
def create_table():
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS student_info (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    PhoneNumber TEXT,
    Email VARCHAR(100)
)
''')
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS instructor_info (
    InstructorID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    PhoneNumber TEXT,
    Email VARCHAR(100)
)
''')
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS course_info (
    CourseID VARCHAR(20) PRIMARY KEY NOT NULL,
    Name VARCHAR(100) NOT NULL,
    InstructorID INT NOT NULL,
    FOREIGN KEY (InstructorID) REFERENCES instructor_info(InstructorID)
)
''')
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS course_material_info (
    MaterialID INTEGER PRIMARY KEY AUTOINCREMENT,
    CourseID VARCHAR(20) NOT NULL,
    MaterialType VARCHAR(100) NOT NULL,
    MaterialLink VARCHAR(200),
    FOREIGN KEY (CourseID) REFERENCES course_info(CourseID)
)
''')
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS enrollment_info (
    EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INT NOT NULL,
    CourseID VARCHAR(20) NOT NULL,
    Grade VARCHAR(2),
    EnrollmentDate TEXT NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES student_info(StudentID),
    FOREIGN KEY (CourseID) REFERENCES course_info(CourseID)
)
''')
    
    conn.commit()
    conn.close()

# Add data into tables
def add_student(Name, Age, PhoneNumber, Email):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO student_info (Name, Age, PhoneNumber, Email) VALUES (?, ?, ?, ?)', (Name, Age, PhoneNumber, Email))
    conn.commit()
    conn.close()
    print(f"Student {Name} added successfully.")
def add_instructor(Name, Age, PhoneNumber, Email):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO instructor_info (Name, Age, PhoneNumber, Email) VALUES (?, ?, ?, ?)', (Name, Age, PhoneNumber, Email))
    conn.commit()
    conn.close()
    print(f"Instructor {Name} added successfully.")
def add_course(CourseID, Name, InstructorID):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO course_info (CourseID, Name, InstructorID) VALUES (?, ?, ?)', (CourseID, Name, InstructorID))
    conn.commit()
    conn.close()
    print(f"Added course {CourseID} successfully.")
def add_course_material(CourseID, MaterialType, MaterialLink):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO course_material_info (CourseID, MaterialType, MaterialLink) VALUES (?, ?, ?)', (CourseID, MaterialType, MaterialLink))
    conn.commit()
    conn.close()
    print(f"Added course material for {CourseID} successfully.")
def add_enrollment(StudentID, CourseID, Grade, EnrollmentDate):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO enrollment_info (StudentID, CourseID, Grade, EnrollmentDate) VALUES (?, ?, ?, ?)', (StudentID, CourseID, Grade, EnrollmentDate))
    conn.commit()
    conn.close()
    print(f"Added enrollment for StudentID {StudentID} successfully.")

# Update data into tables
def update_student(StudentID, Name=None, Age=None, PhoneNumber=None, Email=None):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    if Name:
        cursor.execute('UPDATE student_info SET Name = ? WHERE StudentID = ?', (Name, StudentID))
    if Age:
        cursor.execute('UPDATE student_info SET Age = ? WHERE StudentID = ?', (Age, StudentID))
    if PhoneNumber:
        cursor.execute('UPDATE student_info SET PhoneNumber = ? WHERE StudentID = ?', (PhoneNumber, StudentID))
    if Email:
        cursor.execute('UPDATE student_info SET Email = ? WHERE StudentID = ?', (Email, StudentID))
    conn.commit()
    conn.close()
    print(f"Updated student {StudentID} successfully.")
def update_instructor(InstructorID, Name=None, Age=None, PhoneNumber=None, Email=None):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    if Name:
        cursor.execute('UPDATE instructor_info SET Name = ? WHERE InstructorID = ?', (Name, InstructorID))
    if Age:
        cursor.execute('UPDATE instructor_info SET Age = ? WHERE InstructorID = ?', (Age, InstructorID))
    if PhoneNumber:
        cursor.execute('UPDATE instructor_info SET PhoneNumber = ? WHERE InstructorID = ?', (PhoneNumber, InstructorID))
    if Email:
        cursor.execute('UPDATE instructor_info SET Email = ? WHERE InstructorID = ?', (Email, InstructorID))
    conn.commit()
    conn.close()
    print(f"Updated instructor {InstructorID} successfully.")
def update_course(CourseID, Name=None, InstructorID=None):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    if Name:
        cursor.execute('UPDATE course_info SET Name = ? WHERE CourseID = ?', (Name, CourseID))
    if InstructorID:
        cursor.execute('UPDATE course_info SET InstructorID = ? WHERE CourseID = ?', (InstructorID, CourseID))
    conn.commit()
    conn.close()
    print(f"Updated course {CourseID} successfully.")
def update_course_material(MaterialID, CourseID=None, MaterialType=None, MaterialLink=None):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    if CourseID:
        cursor.execute('UPDATE course_material_info SET CourseID = ? WHERE MaterialID = ?', (CourseID, MaterialID))
    if MaterialType:
        cursor.execute('UPDATE course_material_info SET MaterialType = ? WHERE MaterialID = ?', (MaterialType, MaterialID))
    if MaterialLink:
        cursor.execute('UPDATE course_material_info SET MaterialLink = ? WHERE MaterialID = ?', (MaterialLink, MaterialID))
    conn.commit()
    conn.close()
    print(f"Updated course material {MaterialID} successfully.")
def update_grade(EnrollmentID, Grade):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE enrollment_info SET Grade = ? WHERE EnrollmentID = ?', (Grade, EnrollmentID))
    conn.commit()
    conn.close()
    print(f"Updated grade for EnrollmentID {EnrollmentID} successfully.")

# View or search data from tables
def view_course_materials(CourseID):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM course_material_info WHERE CourseID = ?', (CourseID,))
    rows = cursor.fetchall()
    conn.close()
 
    if rows:
        for row in rows:
            print(f"MaterialID: {row[0]}, CourseID: {row[1]}, MaterialType: {row[2]}, MaterialLink: {row[3]}")
    else:
        print(f"No course materials found for CourseID {CourseID}.")
def view_enrollment():
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM enrollment_info')
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"EnrollmentID: {row[0]}, StudentID: {row[1]}, CourseID: {row[2]}, Grade: {row[3]}")
    else:
        print("No enrollment history found.")
def search_records(table_name, column, value):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE {column} LIKE ?", ('%' + value + '%',))
    rows = cursor.fetchall()
    conn.close()
 
    if rows:
        for row in rows:
            print(row)
    else:
        print(f"No records found matching the search criteria.")

# Delete data from tables
def delete_course_material(MaterialID):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM course_material_info WHERE MaterialID = ?", (MaterialID,))
    conn.commit()
    conn.close()
    print(f"Deleted course material with ID {MaterialID} successfully.")
def delete_enrollment(EnrollmentID):
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM enrollment_info WHERE EnrollmentID = ?', (EnrollmentID,))
    conn.commit()
    conn.close()
    print(f"Deleted enrollment with ID {EnrollmentID} successfully.")

#Export to csv file
def export_to_csv():
    conn = sqlite3.connect('course.db')
    cursor = conn.cursor()
 
    cursor.execute("SELECT * FROM student_info")
    student_data = cursor.fetchall()
 
    cursor.execute("SELECT * FROM instructor_info")
    instructor_data = cursor.fetchall()
 
    cursor.execute("SELECT * FROM course_info")
    course_data = cursor.fetchall()
 
    cursor.execute("SELECT * FROM course_material_info")
    material_data = cursor.fetchall()
 
    cursor.execute("SELECT * FROM enrollment_info")
    enrollment_data = cursor.fetchall()
 
    with open('course_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
 
        writer.writerow(['Table', 'Data'])
        writer.writerow(['student_info', student_data])
        writer.writerow(['instructor_info', instructor_data])
        writer.writerow(['course_info', course_data])
        writer.writerow(['course_material_info', material_data])
        writer.writerow(['enrollment_info', enrollment_data])
 
    print("Data exported to course_data.csv successfully.")
    conn.close()

# Operations (Add, update, view and search, delete)
def add_operations():
    print("\nAdd Operations:")
    print("1. Add Student")
    print("2. Add Instructor")
    print("3. Add Course")
    print("4. Add Course Material")
    print("5. Add Enrollment")

    choice = input("Choose an option: ")

    if choice == '1':
        Name = input("Enter Name: ")
        Age = input("Enter Age: ")
        PhoneNumber = input("Enter Phone Number (if any): ")
        Email = input("Enter Email (if any): ")
        add_student(Name, Age, PhoneNumber, Email)

    elif choice == '2':
        Name = input("Enter Name: ")
        Age = input("Enter Age: ")
        PhoneNumber = input("Enter Phone Number (if any): ")
        Email = input("Enter Email (if any): ")
        add_instructor(Name, Age, PhoneNumber, Email)

    elif choice == '3':
        CourseID = input("Enter Course ID: ")
        Name = input("Enter Name: ")
        InstructorID = input("Enter InstructorID: ")
        add_course(CourseID, Name, InstructorID)

    elif choice == '4':
        CourseID = input("Enter Course ID: ")
        MaterialType = input("Enter Material Type: ")
        MaterialLink = input("Enter Material Link (if any): ")
        add_course_material(CourseID, MaterialType, MaterialLink)

    elif choice == '5':
        StudentID = input("Enter Student ID: ")
        CourseID = input("Enter Course ID: ")
        Grade = input("Enter Grade: ")
        EnrollmentDate = input("Enter Enrollment Date (YYYY-MM-DD): ")
        add_enrollment(StudentID, CourseID, Grade, EnrollmentDate)

    else:
        print("Invalid option.")
def update_operations():
    print("\nUpdate Operations:")
    print("1. Update Student")
    print("2. Update Instructor")
    print("3. Update Course")
    print("4. Update Course Material")
    print("5. Update Grade")

    choice = input("Choose an option: ")

    if choice == '1':
        StudentID = input("Enter Student ID: ")
        Name = input("Enter new Name (or leave blank): ")
        Age = input("Enter new Age (or leave blank): ")
        PhoneNumber = input("Enter new Phone Number (or leave blank): ")
        Email = input("Enter new Email (or leave blank): ")
        update_student(StudentID, Name or None, Age or None, PhoneNumber or None, Email or None)

    elif choice == '2':
        InstructorID = input("Enter Instructor ID: ")
        Name = input("Enter new Name (or leave blank): ")
        Age = input("Enter new Age (or leave blank): ")
        PhoneNumber = input("Enter new Phone Number (or leave blank): ")
        Email = input("Enter new Email (or leave blank): ")
        update_instructor(InstructorID, Name or None, Age or None, PhoneNumber or None, Email or None)

    elif choice == '3':
        CourseID = input("Enter Course ID: ")
        Name = input("Enter new Name (or leave blank): ")
        InstructorID = input("Enter new Instructor ID (or leave blank): ")
        update_course(CourseID, Name or None, InstructorID or None)

    elif choice == '4':
        MaterialID = input("Enter Material ID: ")
        CourseID = input("Enter new Course ID (or leave blank): ")
        MaterialType = input("Enter new Material Type (or leave blank): ")
        MaterialLink = input("Enter new Material Link (or leave blank): ")
        update_course_material(MaterialID, CourseID or None, MaterialType or None, MaterialLink or None)

    elif choice == '5':
        EnrollmentID = input("Enter Enrollment ID: ")
        Grade = input("Enter new Grade: ")
        update_grade(EnrollmentID, Grade)

    else:
        print("Invalid option.")
def view_operations():
    print("\nView Operations:")
    print("1. View Enrollment History")
    print("2. View Course Material")
    print("3. Search Records")

    choice = input("Choose an option: ")

    if choice == '1':
        view_enrollment()
        
    elif choice == '2':
        CourseID = input("Enter Course ID:")
        view_course_materials(CourseID)

    elif choice == '3':
        table_name = input("Enter table name: ")
        column = input("Enter column name: ")
        value = input("Enter search value: ")
        search_records(table_name, column, value)

    else:
        print("Invalid option.")
def delete_operations():
    print("\nView Operations:")
    print("1. Delete Course Material")
    print("2. Delete Enrollment")

    choice = input("Choose an option: ")

    if choice == '1':
        MaterialID = input("Enter Material ID:")
        delete_course_material(MaterialID)
        
    elif choice == '2':
        EnrollmentID = input("Enter Enrollment ID:")
        delete_enrollment(EnrollmentID)

    else:
        print("Invalid option.")

# Main function
def main():
    create_table()
    while True:
        print("\nMain Menu:")
        print("1. Add")
        print("2. Update")
        print("3. View or search")
        print("4. Delete")
        print("5. Export to csv file")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_operations()
        elif choice == '2':
            update_operations()
        elif choice == '3':
            view_operations()
        elif choice == '4':
            delete_operations()
        elif choice == '5':
            export_to_csv()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()