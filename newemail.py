'''
EMAIL ALIAS GENERATOR
by John Nutter
Nov. 11, 2017
created with python 3.6.1
'''
import os

def program_start():
  # get user's email address
  email = input("what's your email address? ").lower()
  
  # split email and check if valid
  if "@" in email:
    username = email.split("@")
    if not "." in username[1]:
      print("Invalid domain")
      program_start()
    
  else: 
    print("Invalid email")
    program_start()

  # get user's desired number of aliases  
  count = input("How many aliases do you want? ")

  # write user input to file
  f = open("{}.txt".format(username[0]), "w")
  n = 1
  while (n <= int(count)):
    f.write("{}+{}@{}\n".format(username[0],n,username[1]))
    n = n + 1
  f.close()
    
  print("Done.")

program_start()
