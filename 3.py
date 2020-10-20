number=int(input('Введите число: '))
b=2
delitel=None
while b!=number:
    if b>7:
        #Проверка простоты делителя большего чем 7
        if b%2!=0 and b%3!=0 and b%5!=0 and b%7!=0:
            #Проверка деления числа на простой делитель больший чем 7
            if number%b==0 and b!=number:
                delitel=b
    elif delitel==None and b%6!=0 and b%4!=0:
        if number%b==0: #2
            delitel=b
    b+=1
print(delitel)
    
#6008 5147 5143
#Ну вообщем оно работает
#Число слишком большое


