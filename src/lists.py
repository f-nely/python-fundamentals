from user import User

cont = 1
userList = []

while cont != 0:
  firstName = input("Enter your first name: ")
  lastName = input("Enter your last name: ")
  age = int(input("Enter your age: "))

  user = User(firstName, lastName, age)
  userList.append(user)

  if user.age == 99:
    break

  if user.age == 98:
    continue

  print(f"Hi, {user.firstName} {user.lastName}, your age is {user.age}!")

  if user.age <= 17:
    print(f"{user.firstName} is teenager!")
  elif user.age >= 18 and user.age <= 50:
    print(f"{user.firstName} is adult!")
  else:
    print(f"{user.firstName} is elderly!")

  cont = int(input("Do you want to continue registering? 0 - Exit, 1 - Continue "))

else:
  print("List of registered users: ")
  for i in userList:
    print(f"Full name: {i.firstName} {i.lastName}, age {i.age}!")
  print("The loop entered the else!")