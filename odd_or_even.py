#either the number is odd or even

inp = int(input("Enter your Number: "))

if inp > 0 and inp%2 == 0:
  print("Number is Even")
elif inp >0 and inp%2 == 1:
  print("Number is Odd")
else:
  print("Enter Valid Number")
