#Author: Felipe Miguens
#Date:3/14/2024 
#Discription: this code will siplify your name down to the last letter
#bugs: no bugs

#This function displays a menu of options and prompts the user to select a function to perform. It then calls the corresponding function based on the user's input.
def main():
    name_input = input("Enter name: ")
    while True:#loops the options for the program and performs the function until user quits
        print("1) Print check vowels")
        print("2) Palindrome")
        print("3) What's your first name")
        print("4) What's your middle name")
        print("5) What's your last name")
        print("6) Find consonant frequency")
        print("7) Check for title")
        print("8) Find if name contains hyphen")
        print("9) Convert letter to upper case")
        print("10) Convert letter to lower case")
        print("11) Find your initials")

        answer = input("Enter Name Function:")

        if answer == "1":
            check_vowels(name_input)
        elif answer == "2":
            print(palindrome(name_input))
        elif answer == "3":
            print(get_first_name(name_input))
        elif answer == "4":
            print(get_middle_name(name_input))
        elif answer == "5":
            print(get_last_name(name_input))
        elif answer == "6":
            count = consonant_frequency(name_input)
            print("Total Frequency:" + str(count))
        elif answer == "7":
            print(check_titles(name_input))
        elif answer == "8":
            print(boolean_hyphen(name_input))
        elif answer == "9":
            print(convert_upper(name_input))
        elif answer == "10":
            print(convert_lower(name_input))
        elif answer == "11":
            print(initials(name_input))

            if answer == "Q":
                print("bye")
        else:
            print("invalid responce")
#input: checks to see how many vowels there are in your name
#output: tell you how many vowels there are
def check_vowels(name):
    count = 0

    for letter in name:
        if letter in ["a","A","e","E","i","I","o","O","u","U" ]:
            count += 1
    print(count)
#checks to see if your name is a palindrome
def palindrome(name):
    if name.lower() == name[::-1].lower(): return True
    return False
#input: checks to see if your typed in a first name
#output: returns your first name
def get_first_name(name):
    first_name = ""
    for letter in name:
        if letter != " ":
            first_name += letter
        else:
            break
    
    return first_name
#input: check if you typed in your last name
#output: returns last name
def get_last_name(name):
    last_name = ""
    for i in range(len(name)-1, -1, -1):
        if name[i] != " ":
            last_name = name[i] + last_name
        else:
            break
    return last_name
#input: check if you typed in your middle name
#output: returns middle name
def get_middle_name(name):
    middle_names = ""
    first_space = name.index(" ")
    last_space = name.rindex(" ")
    if first_space != last_space:
        middle_names = name[first_space:last_space].strip()
    return middle_names
#input: checks to see if your name has any consonants
#output: returns the amount of consonants in your name
def consonant_frequency(name):
    name = convert_lower(name)
    hold_number = 0
    for letter in name:
        num = ord(letter)
        if num>97 and num<122:
            if num == 97 or num == 101 or  num == 105 or  num == 111 or num == 117:
                continue
            else: 
                 hold_number = hold_number +1
    return hold_number
#input:checks if your name has any titels
#output: returns a titel if your name has one
def check_titles(name):
    titles = ["Dr.", "Sir", "Esq", "Ph.d"] 
    for title in titles:
        if title in name:
            return True
    return False
#input: checks if your name contains a hyphen
#output: returns true if your name contains one
def boolean_hyphen(name):
    for char in name:
        if char == "-":
            return True
    return False
#converts all letters in your name to lower case
def convert_lower(name):
    output = ""
    for letter in name:
        num = ord(letter)
        if num>=65 and num<=97:
            num = num + 32
            letter = chr(num)
            output = output + letter
        else:
            output = output + letter
    return output
#converst all lettres in your name to upper case
def convert_upper(name):
    output = ""
    for letter in name:
        num = ord(letter)
        if 122 >= num >= 97:
            num = num - 32
            letter = chr(num)
            output = output + letter
        else:
            output = output + letter
    return output
#returns the initials in your name
def initials(name):
    first_name = get_first_name(name)
    last_name = get_last_name(name)


    return first_name[0] + last_name[0]

main()
    




