"""
Author:Felipe Miguens
Date: 2/22/2024
Description: This code manipulates data and does 7 total funtions with a quit feature. 
Bugs: No bugs so far


"""
from matplotlib import pyplot as plt
import time
import os
from pathlib import Path

#This function displays a menu of options and prompts the user to select a function to perform. It then calls the corresponding function based on the user's input.
def main():

    current_dir = Path(__file__).parent
    file_path = current_dir / "gcds_data2.csv"

    '''
    function: This function acts as a menus displaying 
    all the functions available and calls them
    answer: this variables stores the users chosen function
    output: the output is the chosen functions output
    '''
        
    while True:             #loops the options for the program and performs the function until user quits
        file_input = open(file_path)
        
        os.system('cls')
        time.sleep(2)
        os.system('cls')

        print("Menu Enter Choice:")
        print("1) Print All Students in Grade 12")
        print("2) Located Student")
        print("3) View Boys vs Girls")
        print("4) Student Count")
        print("5) Students per Zipcode")
        print("6) Sort Students")
        print("7) Graph Girl Students versus Boy Students")
        print("8) Graph students per grade")
        print("Q) Quit the Program")
        answer = input("Enter a Function:")

        if answer == "1":
            check_seniors(file_input)
        elif answer == "2":
            record_locate(file_input)
        elif answer == "3":
            boys_vs_girls(file_input, "count")
        elif answer == "4":
            student_count(file_input)
        elif answer == "5":
            student_zipcode(file_input)
        elif answer == "6":
            students_sorted(file_input)
        elif answer == "7":
            boys_vs_girls(file_input)
        elif answer == "8":
            count_kids_per_grade(file_input)
        elif answer.upper() == "Q":
            print("Bye")
            break
        else:
            print("Invalid Input. Please Try Again.")
        
    file_input.close()

def check_seniors(file_input):
    """ 
    This function finds all seniors in the school by iterating through the CSV data and checking if a student's grade is 12. It then prints the seniors' names and returns the student's data.
    """
    file_input.seek(1)                              

    for record in file_input:
        kid = record.split(",")
        if kid[3] == "12":
            print(kid[0] + " " + kid[2])
    return kid
#This function prompts the user to enter a student's first and last names and then iterates through the CSV data to find a match. If a match is found, it prints the student's information; otherwise, it prints "No Match Found."
def record_locate(file_input):
    '''
    function: locates a record in the school's database
    last_name: the users chosen record's last name
    first_name: the users chosen record's first name
    output: the record of a student or 'no match found'
    '''
    last_name = input("Enter last name of student")
    first_name = input("Enter first name of student")

    for record in file_input:
        student_data = record.split(",")
        if student_data[2].lower() == last_name.lower() and student_data[0].lower() == first_name.lower():
            print("First Name:", student_data[0],"Middle Name:", student_data[1], "Last Name:", student_data[2], "Grade:", student_data[3], "Advisor", student_data[5], student_data[6], "State:", student_data[8], "City:", student_data[7], "Zipcode:", student_data[9])
            return 
        
    print("No Match Found.")
#This function calculates the number of male and female students in the school by iterating through the CSV data and counting the number of records with a gender value of "M" or "F". If the count parameter is None, it calls the graph_data() function to display a bar chart of the counts; otherwise, it prints the counts to the console.
def boys_vs_girls(file_input, count=None):
    '''
    function: compares the boys vs girl in the school
    output: the amount of boys and girls
    '''
    female_count = 0
    male_count = 0

    for record in file_input:
        kid = record.split(",")
        if kid[4] == "F":
            female_count += 1
        else:
            male_count += 1
    
    if count == None:
        graph_data(file_input, {"Male":male_count, "Female":female_count})

    else:
        print(f"Female: {female_count}")
        print(f"Male: {male_count}")
#This function calculates the total number of students in the school by iterating through the CSV data and counting the number of records.
def student_count(file_input):
    '''
    function: finds the amount of students in the school
    output: the amoutn of students in the school
    '''

    student_count = 0
    for record in file_input:
        student_count += 1

    print(student_count - 1)
  #This function prompts the user to enter a zip code and then iterates through the CSV data to find the number of records that match the zip code. It then prints the number of matches to the console.  
def student_zipcode(file_input):
    '''
    function: finds the amount of students from a certain zipcode
    zipcode: the zipcode chosen by the user
    decision_export: the users responce to exporting data
    output: the amount of students in that zipcode or 'no matches found'
    '''
    zip_count = 0
    zipcode = input("Enter Zipcode").lstrip('0')
    print(zipcode)
    for record in file_input:
        kid = record.split(',')
        if kid[0] != "NameFirst":
            if len(kid) == 10:
                if (kid[9]).replace("\n", '').lstrip('0') == zipcode:
                    zip_count += 1
            else:
                if (kid[8]).replace("\n", '').lstrip('0') == zipcode:
                    zip_count += 1
   
    print(zip_count)
#This function sorts the students in the CSV data by last name and prints their names to the console.
def students_sorted(file_input):
    '''
    function: sorts the students by last name
    output: prints the students in the school by last name
    '''
    for line in file_input:
        record = line.split(",")
        print(record[0], record[2])
    #This function counts the number of students in each grade level by iterating through the CSV data and adding 1 to the corresponding grade level key in a dictionary. It then calls the graph_data() function to display a bar chart of the counts.
def count_kids_per_grade(file_input):
    classes = {"N":0, "PK":0, "K":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0}
    first = True
    for record in file_input:
        if first:
            first = False
            continue
        kid = record.split(",")
        classes[str(kid[3])] += 1
#This function creates a bar chart of the data passed in as a dictionary using the pyplot module from the matplotlib package.
    graph_data(file_input, classes)

def graph_data(file_input, classes):
    fig = plt.figure(figsize = (10, 5))         #creates the figure for the graph
    x = list(classes.keys())
    y = list(classes.values())
    plt.bar(x, y, width = 0.4, color = 'pink')
    plt.xlabel('x - Grades') 
    plt.ylabel('y - Number of Students') 
    plt.title('The Number of Students in Each Grade') 
    plt.show()
        


if __name__ == '__main__':
    main()
