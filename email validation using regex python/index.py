# email validation using regex python
--Minimum length 6, uppercase not, first letter alphabetic, @ at onec time, dot postion end 3rd or 4th position , not space includeed
--`? Matches the expression`
--
import re
email_condition = "^[a-z 0-9]?[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}"
user_email= input("Enter your Email: ")
if re.search(email_condition,user_email):
    print("Email address is right")
else:
    print("wrong email address")
