contacts={}
while True:
      print("\n1. Add contacts")
      print("2.Search contacts")
      print("3.Update contacts")
      print("4.Delete contact")
      print("5.List all contacts") 
      print("6.Exit")
      choice=input("enter a number:")
      if choice=="1":
          name=input("enter name:")
          phone=input("enter number:")
          contacts[name]=phone
          print(f"{name} added successfully ")
      elif choice=="2":
           name=input("enter name to search")
           phone=contacts.get(name)
           if phone:
                print(f"{name} phone number is{phone}")
           else:
                print(f"{name} not found")
      elif choice==3:
           name=input("enter name to update")
           if name in contacts:
                phone=input("enter new phone number:")
                print(f"{name} is updated")
           else:
                print(f"{name} is not found")
      elif choice=="4":
           if name in contacts:
                del contacts[name]
                print(f"{name} is deleted")
           else:
                print(f"{name} is not found")
      elif choice=="5":
           print("\ncontacts:")
           for name in sorted(contacts):
                print(f"{name}:{contacts[name]}")
      elif choice=="6" or choice.lower()=="exit":
           print("existing contacts book")
           break
      else:
           print("invalid choice.try again.")
           
           

            

           
