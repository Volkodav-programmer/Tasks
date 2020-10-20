number=1000
sum=0
while number!=0:
    if number%5==0 or number%3==0:
        sum+=number
    number-=1
print(sum)

        