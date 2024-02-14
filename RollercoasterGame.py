print("Welcome to the ")
print("Please book the tickets!")
bill = 0
height = int(input("What is your height in cm?"))
if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("How old you are?"))
  if age < 12:
    bill = 5
    print("Children ticket")
  if age <= 18:
    bill = 7
    print("Youth ticket")
  else:
    bill = 12
    print("Adults ticket")
  wants_photo = input("Do you want a photo taken ? Y or N\n")
  if wants_photo == "Y" or "y":
    bill = bill + 3
  print(f"Your final bill is {bill}$.")
  
else:
  print("Sorry , grow taller !! Cannot ride the rollercoaster!!")
print("Thank You !!")  