#multiplication table of any integer

n = int(input("Enter the number: "))

for i in range(1,11):
  print(str(n) +  " * ", i ," = ", n*i)
