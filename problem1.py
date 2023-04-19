phoneDirectory = {}
print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
option = 0
while (option != 5):
  print("1.Add a record")
  print("2.Search a record")
  print("3.Update a record")
  print("4.Delete a record")
  print("5.Quit")
  option = int(input("enter option "))
  if option == 5:
    print("Thank you\n")
  if (option == 1):
    x = input("Enter your name ")
    y = input("Enter new 10-digit phone number ")
    phoneDirectory.update({x: y})
    print("Record added")
    
  elif (option == 3):
    x = input("Enter your name ")
    y = input("Enter new 10-digit phone number:  ")
    phoneDirectory.update({x: y})
    print("Record updated")
  elif (option == 2):
    x = input("Enter name to search:")
    z = 0
    for t in phoneDirectory.keys():
      if t == x:
        print(t, ":", phoneDirectory[t])
        z = 1
      else:
        pass

    if (z == 0):
      print("not found")
      
  elif (option == 4):
    x = input("Enter name")
    del phoneDirectory[x]
    print("Record deleted")
print(phoneDirectory)
  