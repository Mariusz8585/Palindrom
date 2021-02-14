word = input("enter a word or phrase: ")

def is_palindrome(word):
    letters = list(word.replace(" ", ""))
    is_palindrome = True
    for letter in letters:
        if letter == letters[-1]:
            letters.pop()
        else:
            is_palindrome = False
            break
    return is_palindrome

if is_palindrome(word) == True:
    print("You enter a palindrome")
else:
    print("You didnt enter a palindrome")