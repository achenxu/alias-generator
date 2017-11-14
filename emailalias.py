#!/usr/bin/env python3
'''
EMAIL ALIAS GENERATOR
created with python 3.6.1
'''
import os

def program_start():
  # get user's email address  
  while True:
    # get user email
    email = input("what's your email address? ").lower()
    username = email.split("@")
  # split email and check if valid
    if "@" not in email:
      print("Invalid email")
    elif "." not in username[1]:
      print("Invalid domain")
    elif "+" in email:
      print("Must not be an alias already")
    else: 
      count = input("How many aliases do you want? ")
      break  
  # write user input to file
  f = open("{}.txt".format(username[0]), "w")
  n = 1
  while (n <= int(count)):
    f.write("{}+{}@{}\n".format(username[0],n,username[1]))
    n = n + 1
  f.close()
  print("Done.")
  print("Your file is called {}.txt".format(username[0]))


if __name__ == '__main__':
  program_start()
