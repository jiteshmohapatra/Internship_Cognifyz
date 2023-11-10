#Develop a Python function that validates whether a given string is a valid emailaddress. Implement checks for the format,including the presence of an "@" symbol and a domain name

def check_email(res1):
    if "@" in res1 and "." in res1:
        return True
    else:
        return False
print(check_email("jitesh@gmail.com"))  # it will return True
print(check_email("myemail")) # it will return false
    