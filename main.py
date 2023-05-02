import tkinter as tk
import mysql.connector as mysql

# Create the main window
root = tk.Tk()
root.title("Student Database")

# Connect to the MySQL database
conn = mysql.connect(
    host="localhost",
    user="root",
    password="12345",
    database="student_database"
)

# Create the search function
def search():
    # Clear any previous search results
    result_area.delete("1.0", tk.END)
    
    # Get the course name entered by the user
    course_name = course_name_entry.get()
    
    # Prepare an SQL statement to search for students in the given course
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM StudentMst WHERE Course = %s", (course_name,))
    result = cursor.fetchall()
    
    # Display the search results in the result area
    if len(result) > 0:
        for student in result:
            result_area.insert(tk.END, f"SID: {student[0]}\nName: {student[1]}\nCourse: {student[2]}\nEducation: {student[3]}\nPersonal: {student[4]}\nFees: {student[5]}\n\n")
    else:
        result_area.insert(tk.END, "No students found in that course.")
    
    # Close the cursor
    cursor.close()

# Create the function to add data to the database
def add_data():
    # Get the values entered by the user
    sid = sid_entry.get()
    name = name_entry.get()
    course = course_entry.get()
    education = education_entry.get()
    personal = personal_entry.get()
    fees = fees_entry.get()
    
    # Prepare an SQL statement to insert the data into the database
    cursor = conn.cursor()
    sql = "INSERT INTO StudentMst (SID, Name, Course, Education, Personal, Fees) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (sid, name, course, education, personal, fees)
    cursor.execute(sql, values)
    conn.commit()
    
    # Clear the input fields
    sid_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    education_entry.delete(0, tk.END)
    personal_entry.delete(0, tk.END)
    fees_entry.delete(0, tk.END)
    
    # Close the cursor
    cursor.close()

# Create the GUI elements for the search function
course_name_label = tk.Label(root, text="Enter course name:")
course_name_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search)
result_area = tk.Text(root)

# Add the GUI elements for the search function to the main window
course_name_label.pack()
course_name_entry.pack()
search_button.pack()
result_area.pack()

# Create the GUI elements for the add data function
sid_label = tk.Label(root, text="SID:")
sid_entry = tk.Entry(root)
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)
course_label = tk.Label(root, text="Course:")
course_entry = tk.Entry(root)
education_label = tk.Label(root, text="Education:")
education_entry = tk.Entry(root)
personal_label = tk.Label(root, text="Personal:")
personal_entry = tk.Entry(root)
fees_label = tk.Label(root, text="Fees:")
fees_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Data", command=add_data) 
sid_label.pack()
sid_entry.pack()
name_label.pack()
name_entry.pack()
course_label.pack()
course_entry.pack()
education_label.pack()
education_entry.pack()
personal_label.pack()
personal_entry.pack()
fees_label.pack()
fees_entry.pack()
add_button.pack()

# Start the main loop 
root.mainloop()
