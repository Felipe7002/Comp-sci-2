#Name:
#Description
#Sources:
#Bugs:
#Bonuses:
#Log: 11/13/2023 - starting new function

import csv

def main():
   
    """ doc """
    file_input = open("C:/Users/FMiguens26/Desktop/student_data_2023.csv", "a+")

    file_input.readline()                       #skip first line of header info
    answer = "Y"
    go = True

    print("Menu: Enter Choice or 'Q' to (Q)uit:")
    print("1) Print All Student in Grade 12")
    print("2) Print students by zip code")
    print("3) Get student by last name")
    print("4) add new data entry")
  


   
    while go is True:

        if answer == "1":
            check_seniors(file_input)
        elif answer == "2":
            zipcode = input("Enter Zipcode:")
            get_students_by_zip(file_input, zipcode)
        elif answer == "3":
            name = input("Enter last name:")
            look_up_student(file_input, name)
        elif answer == "4":
           
            add_person(file_input,)

            file_input = open("C:/Users/FMiguens26/Desktop/student_data_2023.csv", "r")
        elif answer.lower() == "Q":
            go = False
            print("bye")
            file_input.close()
           
        answer = input("Enter Choice or 'Q' to quit")


def check_seniors(file_in):
    """ doc 
    Description: find && print all seniors from data
    file_in - pointer to open file for processing
    returns - void
    
    """

    file_in.seek(1)                                     #move pointer to line 1

    for record in file_in:
        kid = record.split(",")
        if kid[3] == "Grade 12":
            print(kid[0] + " " + kid[2])

def get_students_by_zip(file_in, zip):
    file_in.seek(1)

    for record in file_in:
        kid = record.split(",")
        if str(kid[7][:4]) == zip:
            print(kid[1] + " " + kid[2] + " " + kid[3])
def look_up_student(file_in, name):
    file_in.seek(1)


    for record in file_in:
        kid = record.split(",")
        if kid[2].lower() == name.lower():
            print(kid)




   
def add_person(file_in):

    first_name = input("Enter first name")
    middle_name = input("Enter middle name")
    last_name = input("Enter last name")
    grade = input("Enter grade")
    advisor = input("Enter advisor's name")
    town = input("Enter town name")
    state = input("Enter state name")
    zip_code = input("Enter zipcode")

    
    file_in.write(first_name + "," + middle_name + "," + last_name + "," + grade + "," + advisor + "," + town + "," + state + "," + zip_code + ",")
    file_in.close()

if __name__ == '__main__':
    main()
