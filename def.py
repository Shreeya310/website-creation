def number_factorial(a):
    if a==1:
        return a
    else:
        return a*number_factorial(a-1)
a=int(input("ENTER THE NUMBER"))
if a<0:
    print("NO,THE FACTORIAL DOES NOT EXISTS.")
elif a==0:
    print("THE FACTORIAL IS 1.")
else:
    print("THE FACTORIAL OF",a,"IS",number_factorial(a))    
