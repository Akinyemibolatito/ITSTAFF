f_name = input ('what is your first name? ')
first_name = f_name[0:2]
l_name =input('what is your last name? ')
last_name = l_name [-3:-1]
email = input ('what is your email? ')
import random
import string
def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
password = first_name+last_name+randomString(5)
print (password)
is_satisifed = True
if is_satisifed:
   print ('password is good')
   print ('password successfully set')
   list = [first_name , last_name , email, password ]
   print (list)
else:
    print('not satisfied?')
    print ("enter your own password")
    password= input("make sure it is 7 characters or more, thanks.enter_password?  ")
    password = string.ascii_letters
    if (len(password)> 7):
        print ('password successfully set')
    else:
        print (" last attempt,make sure it is 7 or more characters,enter password again? ")








