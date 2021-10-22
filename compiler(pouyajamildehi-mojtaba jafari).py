alphabet={"a","b","c","d","e","f","g",'h',"i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
symbol={"+","-","*","/","^"}
number={"0","1","2","3","4","5","6","7","8","9"}
ok=[1,2,3,5,8,9,12,13,15,16]

a="1)letter(letter/digit)*: a65cf;"
b="2)identifier: x=;"
c="3)letter=letter/digit: x=5; , x=y;"
d="4)letter=letter/digit (+,-,*,/,^) letter/digit: x=x+y;"
e="5)use if , while : if:; , while:;"
f="6)letter ++,letter--,letter-=letter/digit,letter+=;etter/degeit: x++; ,x-=y;"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
flag=0;
while flag==0:
    s=0
    j=0
    m=0
    i=0
    x=input("matne mored nazar khodra vared konid va dar enteha semicolon(;) bzanid :")
    matn=x
    print(matn)
    for n in range (0,len(matn)):
        if matn[n]==";":
            j=n

    while i!=j:
        if s==0 and i==m:
            if matn[i] in alphabet:
                s=1
                m=m+1
            else:
                s=20    
        if s==1 and i==m:
            if matn[i] in alphabet or matn[i] in number:    
                s=1
                m=m+1    
            else :
                if matn[i]=="=":
                    s=2
                    m=m+1
                else:
                    if matn[i]=="-":
                        s=6
                        m=m+1
                    else:
                        if matn[i]=="+":
                            s=7
                            m=m+1
                        else:
                            if matn[i]==":":
                                s=14
                                m=m+1
                            else :
                                s=20    
                               
        if s==2 and i==m:
            if matn[i] in alphabet or matn[i] in number:
                s=3
                m=m+1
            else:
                s=20

        if s==3 and i==m:
            if matn[i] in alphabet or matn[i] in number:
                s=3
                m=m+1
            else:
                if matn[i] in symbol:
                    s=4
                    m=m+1
                else :
                    s=20

        if s==4 and i==m:
            if matn[i] in alphabet or matn[i] in number:
                s=5
                m=m+1
            else:
                s=20

        if s==5 and i==m:
            if matn[i] in alphabet or matn[i] in number:
                s=5
                m=m+1
            else:
                if matn[i] in symbol:
                    s=4
                    m=m+1
                else:
                    s=20

        if s==6 and i==m:
            if matn[i]=="-":
                s=8
                m=m+1
            else:
                if matn[i]=="=":
                    s=10
                    m=m+1
                else:
                    s=20

        if  s==7 and i==m:
            if matn[i]=="+":
                s=9
                m=m+1
            else:
                if matn[i]=="=":
                    s=11
                    m=m+1
                else:
                    s=20

        if s==8 and i==m:
            if matn[i]!=";":
                s=20

        if s==9 and i==m:
            if matn[i]!=";":
                s=20

        if (s==10 and i==m) or (s==12 and i==m) :
            if matn[i] in alphabet or matn[i] in number:
                s=12
                m=m+1
            else:
                s=20

        if (s==11 and i==m) or (s==13 and i==m):
            if matn[i] in alphabet or matn[i] in number:
                s=13
                m=m+1
            else:
                s=20

        if s==14:
            if matn=="if:;":
                s=15
                m=m+1
            else:
                if matn=="while:;":
                    s=16
                    m=m+1    
                else:
                    s=20    
        i+=1

    if s in ok:
        if s==1:
            print("accept and rule 1")
        if s==2:
            print("accept and rule 2")
        if s==3:
            print("accept and rule 3")
        if s==5:
            print("accept and rule 4")
        if s==8 or s==9 or s==12 or s==13:
            print("accept and rule 6")
        if s==15:
            print("accept and if: in rule 5")
        if s==16:
            print("accept and while: rule 5")                        
    else:
        print("error")

    z=input("mikhahid edame dahid?y/n")
    if z=="n":
        flag=1
    else:
        flag=0