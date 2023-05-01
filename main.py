import tkinter as tk
import mysql.connector as mysql

# Create the main window
root = tk.Tk()
root.title("Student Database")

# Create the search function
def search():
    # Clear any previous search results
    result_area.delete("1.0", tk.END)
    
    # Get the course name entered by the user
    course_name = course_name_entry.get()
    
    # Connect to the MySQL database
    conn = mysql.connect(
        host="localhost",
        user="root",
        password="12345",
        database="student_database"
    )
    
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
    
    # Close the database connection and cursor
    cursor.close()
    conn.close()

# Create the GUI elements
course_name_label = tk.Label(root, text="Enter course name:")
course_name_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search)
result_area = tk.Text(root)

# Add the GUI elements to the main window
course_name_label.pack()
course_name_entry.pack()
search_button.pack()
result_area.pack()

# Start the main event loop
root.mainloop()
