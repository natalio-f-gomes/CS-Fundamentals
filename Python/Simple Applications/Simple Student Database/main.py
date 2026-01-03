"""
Date 11/10/2022
Camille
Project 5
"""
# This dictionary stores al the student data
student_dictionary_list = []

#file is a variable, we open the Student_data.txt in read mode
file = open("Student_data.txt","r")

#for each line in file
for i in file:
    # we want to separate the elements by using the keyword "split" which splits the rows based on the paremeter ipued
    # which in this case is "|"
    # name variable stores the first index of the file
    #Important to remember that index always starts at zero
    name = i.split("|")[0]
    # id variable stores the second index of the file
    id = i.split("|")[1]
    # id variable stores the third index of the file
    credits = i.split("|")[2]
    # id variable stores the fourth index of the file
    gpa = i.split("|")[3]

    #Create a student dictionary that assigns the vairables name,id,credits, and gpa into the keys: name, id,credits, gpa
    #Important to remember that in a dictionary we have a key and a value
    student_dictionary  = {
    "name": name,
    "id": id,
    "credits": int(credits),
    "gpa": float(gpa)}
    # Insert the dictionary into the list at index 0
    student_dictionary_list.insert(0,student_dictionary)


# this function takes the input parameter and if perform actions with it based on if statements.
def perform_command(user_input):
    # If the paramenter equals 1
    if user_input =="1":
        #Ask the user for student name, id,etc
        new_name = input("Enter the name of the new student: ")
        new_id = input("Enter the ID  of the new student: ")
        new_credits = input("Enter the number of credits: ")
        new_gpa = input("Enter the GPA: ")
        # Add all this new information into a new dictionary
        add_to_dict = {
            "name": new_name,
            "id": new_id,
            #Important to convert credits and gpa to numbers
            "credits": int(new_credits),
            "gpa": float(new_gpa)}
        #We want to append this to the dictionary list, not insert it.
        student_dictionary_list.append(add_to_dict)
    #If user inputs 2
    if user_input =="2":
        #iterate trough the list and in each row, if the key "credist" is less the 25 print the student info
        for student in student_dictionary_list:
            if student["credits"]<25:
                print(student)
    if user_input =="3":
        # iterate trough the list and in each row, if the key "gpa" is less the 2.0 print the student info
        for student in student_dictionary_list:
            if student["gpa"] < 2.0:
                print(student)
    if user_input =="4":
        # iterate trough the list and in each row, if the key "gpa" is greater then 3. print the student info
        for student in student_dictionary_list:
            if student["gpa"] > 3.0:
                print(student)
    #if user inputs 5 we want to exit out of the program, we use quit() instead of  break, because
    # it is not inside of while loop
    if user_input =="5":
        exit()
# This fucntion puts everything toguther
def load_data():
    #This is an infinite loop that only stops when is called the quit() function
    while True:
        #Keep aking the user to input thei options forever until they want to stop the program
        user_input = input("""
        1) Add a student
        2) Find Master students(those with less than 25 credits)
        3) Find students on probation(those with gpa less than 2)
        4) Find honor students (those with gpa greater than 2)
        5) Exit the program
        A: """)
        #call the perform_command function and pass user_input as a parameter
        perform_command(user_input)

if __name__ == '__main__':
    #finally we call load data
    load_data()
