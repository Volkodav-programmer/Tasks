hundr=100
hundr1=101
palidrom1=0
palidrom2=0
palidrom3=0
max_pal=None
while hundr<1000 and hundr1<1000:
    eq1=hundr*hundr1
    str1=str(eq1)

    if str1[0]==str1[4]:
        palidrom1=int(str1)

    eq2=hundr*hundr
    str2=str(eq2)

    if str2[0]==str2[4]:
        palidrom2=int(str2)

    eq3=hundr1*hundr1
    str3=str(eq3)

    if str3[0]==str3[4]:
        palidrom3=int(str3)

    if len(str1)==6 and len(str2)==6 and len(str3)==6:
        eq1=hundr*hundr1
        str1=str(eq1)

        if str1[0]==str1[5]:
            palidrom1=int(str1)

        eq2=hundr*hundr
        str2=str(eq2)

        if str2[0]==str2[5]:
            palidrom2=int(str2)

        eq3=hundr1*hundr1
        str3=str(eq3)

        if str3[0]==str3[5]:
            palidrom3=int(str3)


    if palidrom1>palidrom2>palidrom3 or palidrom1>palidrom3>palidrom2:
        max_pal=palidrom1

    elif palidrom2>palidrom1>palidrom3 or palidrom2>palidrom3>palidrom1:
        max_pal=palidrom2

    elif palidrom3>palidrom1>palidrom2 or palidrom3>palidrom1>palidrom2:
        max_pal=palidrom3

    hundr+=1
    hundr1+=1
print(max_pal)


    
