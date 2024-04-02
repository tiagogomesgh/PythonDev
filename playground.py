# Tiago Gomes
# Playground.py
# The purpose of this file is to become more familiar with python in a free environment.
# While also testing out Pythons LSP Capabilities.


def main () :
  userInput = str(input("Would you like to add a contact? (y/n) "))

  contacts = open("Contact.txt","w")

  while userInput != 'n':

    firstName = str(input("Enter the first name of this contact: "))
    contacts.write(firstName + '\n')
    lastName = str(input("Enter the last name of this contact: "))
    contacts.write(lastName + '\n')
    phoneNumber = str(input("Enter the phone number of this contact: "))
    contacts.write(phoneNumber + '\n' + '\n')

    userInput = str(input("Would you like to add another contact? (y/n) "))

  print("Contact has been added!")
  contacts.close()
main ()
