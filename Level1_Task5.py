#Write a Python function that checks whethera given string is a palindrome. A palindromeis a word, phrase, or sequence that reads the same backward as forward (e.g.,"madam" or"racecar").

def palindrome(a):
    a = a.lower().replace(" ","")
    if a==a[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
    
    return a

a = input("Enter a String")
palindrome(a)







