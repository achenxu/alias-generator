#!/usr/bin/env python3
'''
EMAIL ALIAS GENERATOR
created with python 3.6.1
'''
import os

def main():
  # get user's email address
  while True:
    # get user email
    email = (input("what's your email address? "))
    username = email.lower().split("@")

    # handling malformed email addresses
    if "@" not in email:
      print("Invalid email")
    elif "." not in username[1]:
      print("Invalid domain")
    elif "+" in email:
      print("Must not be an alias already")
    else:
      try: # handling non-valid numbers
        count = int(input("How many aliases do you want? "))
        break
      except (ValueError):
        print("Not a valid number! Try again.")

  # write user input to file
  filename = (f'{username[0]}.txt')
  file = open(filename, "w")
  n = 1
  while (n <= count):
    file.write(f"{username[0]}+{n}@{username[1]}\n")
    n += 1
  file.close()
  print("Done.")
  print(f"Your file is called {filename}")


if __name__ == '__main__':
  main()
