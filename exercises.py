# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel ('a', 'e', 'i', 'o', u')', print: "The letter x is a vowel."
# - If the letter is a consonan't', print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    vowel = ['A', 'E', 'I', 'O', 'U']
    user_letter = input('Enter a letter A-Z and determine its type: ').upper()
    
    while len(user_letter) != 1 or user_letter.isdigit():
        user_letter = input('Enter a letter A-Z and determine its type: ').upper()
        print('Please try again, input must be one letter')
    
    else:
        for _ in vowel:
            if _ == user_letter:
                print(
                    f'The letter {user_letter} is a vowel'
            )
                break
            else: 
                print(
            f'The letter {user_letter} is a consonant'
         )
                break

# Call the function
check_letter()
