# Purpose: A program that will allows users to explore and apply different string manipulation techniques in Python.

#Pseudocode
# Print python string methods 
print ("\nPython String Methods:\n"
       "1. capitalized() method\n"
       "2. lstrip() method\n"
       "3. rstrip() method\n"
       "4. strip() method\n"
       "5. lower() method\n"
       "6. upper() method\n"
       "7. title() method\n"
       "8. swapcase() method\n"
       "9. ljust() method\n"
       "10. rjust() method\n"
       "11. center() method\n"
       "12. zfill() method\n"
       "13. find() method\n"
       "14. count() method\n"
       "15. startswith() method\n"
       "16. endswith() method\n"
       "17. isdigit() method\n"
       "18. isnumeric() method\n"
       "19. isdecimal() method\n"
       "20. isalpha() method\n"
       "21. isalnum() method\n"
       "22. islower() method\n"
       "23. isupper() method\n"
       "24. isspace() method\n"
       "25. find() method\n"
       "26. str() method\n"
       "27. len() method\n"
       "28. max() method\n"
       "29. min() method\n"
       "30. split() method\n"
       "31. index() method\n"
       "32. ord() method\n"
       "33. chr() method\n")

# ask a number from the user
choice = int(input("Enter the number of the string method you want to use: "))

# ask a string from the user
string = input("Enter a string to apply the method to: ")

# execute the chosen method 
if choice == 1:
       result = string.capitalize()
elif choice == 2:
       result = string.lstrip()
elif choice == 3:
       result = string.rstrip()
elif choice == 4:
       result = string.strip()
elif choice == 5:
       result = string.lower()
elif choice == 6:
       result = string.upper()
elif choice == 7:
       result = string.title()
elif choice == 8:
       result = string.swapcase()
elif choice == 9:
       width = int(input("Enter the width: "))
       result = string.ljust(width)
elif choice == 10:
       width = int(input("Enter the width: "))
       result = string.rjust(width)
elif choice == 11:
       width = int(input("Enter the width: "))
       result = string.center(width)
elif choice == 12:
       width = int(input("Enter the width: "))
       result = string.zfill(width)
elif choice == 13:
       substring = input("Enter the substring to find: ")
       result = string.find(substring)
elif choice == 14:
       substring = input("Enter the substring to count: ")
       result = string.count(substring)
elif choice == 15:
       substring = input("Enter the substring to check: ")
       result = string.startswith(substring)
elif choice == 16:
       substring = input("Enter the substring to check: ")
       result = string.endswith(substring)
elif choice == 17:
       result = string.isdigit()
elif choice == 18:
       result = string.isnumeric()
elif choice == 19:
       result = string.isdecimal()
elif choice == 20:
       result = string.isalpha()
elif choice == 21:
       result = string.isalnum()
elif choice == 22:
       result = string.islower()
elif choice == 23:
       result = string.isupper()
elif choice == 24:
       result = string.isspace()
elif choice == 25:
       substring = input("Enter the substring to find: ")
       result = string.find(substring)
elif choice == 26:
       result = str(string)
elif choice == 27:
       result = len(string)
elif choice == 28:
       result = max(string)
elif choice == 29:
       result = min(string)
elif choice == 30:
       result = string.split()
elif choice == 31:
       substring = input("Enter the substring to find: ")
       result = string.index(substring)
elif choice == 32:
       result = ord(string)
elif choice == 33:
       result = chr(int(string))
else:
       result = "Invalid choice!"

# print result
# ask if the user wants to try again