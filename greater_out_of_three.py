#greatest out of three

a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
c = float(input("Enter your third number: "))

if a > b and a > c:
  print(a ," is greater than ", b ," and ", c)

elif b > a and b > c:
  print(b ," is greater than ", a ," and ", c)

elif c > a and c > b:
  print(c ," is greater than ", a ," and ", b)

else:
  print("Two or more numbers are equal!")
