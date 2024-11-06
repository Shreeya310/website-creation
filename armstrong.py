
num = int(input("Enter a number:"))
sum = 0
var= num
while var> 0:
   digit = var % 10
   sum += digit ** 3
   var//= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
