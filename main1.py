num=int(input("enter the number to check="))
if num>31:
    print("number is greater than 31")
    if num%2==0:
     print("it is even as well")
    else:
     print("it is odd")
else: 
  print("it is smaller than 31")