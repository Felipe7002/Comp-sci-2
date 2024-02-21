
vowels = ["a","A","e","E","i","I","o","O","u","U" ]
name_input = input("Enter name: ")

def check_vowels(name):
    count = 0

    for letter in name:
        if letter in vowels:
            count += 1
    print(count)


def palindrome(name):
    if name.lower() == name[::-1].lower(): return True
    return False


check_vowels(name_input)
print(f"Paildrone: {palindrome(name_input)}")

def first_name(name):
    first_name = ""
    for letter in name:
        if letter != " ":
            first_name += letter
        else:
            break
        return first_name
def get_last_name(name):
    last_name = ""
    for i in range(len(name)-1, -1, -1):
        if name[i] != " ":
            last_name = name[i] + last_name
        else:
            break
    return last_name
def get_middle_names(name):
    middle_names = ""
    first_space = name.index(" ")
    last_space = name.rindex(" ")
    if first_space != last_space:
        middle_names = name[first_space:last_space].strip()
    return middle_names

def

