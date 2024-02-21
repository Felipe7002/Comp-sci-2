
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

