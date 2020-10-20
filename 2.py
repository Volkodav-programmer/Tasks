number1=1
number2=2

while number1+number2<=4000000 or number2+number1<=4000000:
    number1=number1+number2
    number2=number2+number1
    if number1%2==0:
        print(number1)
    if number2%2==0:
        print(number2)

