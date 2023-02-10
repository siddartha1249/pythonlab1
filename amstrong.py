num=int(input("enter the number"))
order =len(str(num))
sum =0
temp =num
while (temp >= 1):
    digit = temp % 10
    sum += pow(digit,order)
    temp = int(temp/10)
    
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")