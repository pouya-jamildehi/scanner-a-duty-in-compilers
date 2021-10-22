import tkinter as Scanner

import os.path
def input_button(ent,length):
    input1 = ent
    length = length
    matn=ent
    alphabet={"a","b","c","d","e","f","g",'h',"i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
    symbol={"+","-","*","/","^"}
    number={"0","1","2","3","4","5","6","7","8","9"}
    ok=[1,2,3,5,8,9,12,13,15,16]
    s=0
    j=0
    m=0
    i=0
    reg_expr = matn
    for n in range (0,length):
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
            result = "  "+"Accept \nBY\n rule 1"
            res = "Accept BY rule 1"
        if s==2:
            result = "  "+"Accept \nBY\n rule 2"
            res = "Accept BY rule 2"
        if s==3:
            result = "  "+"Accept \nBY\n rule 3"
            res = "Accept BY rule 3"
        if s==5:
            result = "  "+"Accept \nBY\n rule 4"
            res = "Accept BY rule 4"
        if s==8 or s==9 or s==12 or s==13:
            result = "  "+"Accept \nBY\n rule 6"
            res = "Accept BY rule 6"
        if s==15:
            result = "  "+"Accept \nBY\n if: + rule 5"
            res = "Accept BY  if: + rule 5"
        if s==16:
            result = "  "+"Accept \nBY\n while: + rule 5" 
            res = "Accept BY  while: + rule 5"
    else:
        result = "Failed"
        res = "Failed"
    label["text"] = result
    file_exists = os.path.isfile("History.txt") 
    if file_exists:
        history = open("History.txt","a")
        history.write("regular expression : "+reg_expr+" Result : "+res+"\n")
        history.close
    else:
        history = open("History.txt","w")
        history.write("regular expression : "+reg_expr+" Result : "+res+"\n")
        history.close
def His_but():
    file_exists = os.path.isfile("History.txt") 
    if file_exists:
        os.startfile("History.txt")
    else:
        Error = Scanner.Tk()
        Error.title('Error')
        c = Scanner.Canvas(Error,height=90,width=200,)
        c.pack()
        l = Scanner.Label(Error,font=30,text="History is Epmty",fg="red",borderwidth=3)
        l.place(relx=0.5,rely=0.1,anchor="n") 
        b = Scanner.Button(Error,text="Ok!",borderwidth=2,font=40,command=Error.destroy)
        b.place(relx=0.37,rely=0.46) 
def Clr_but():
    file_exists = os.path.isfile("History.txt") 
    if file_exists:
        os.remove("History.txt")
        Result = Scanner.Tk()
        Result.title('Result')
        c1 = Scanner.Canvas(Result,height=90,width=200,)
        c1.pack()
        l1 = Scanner.Label(Result,font=30,text="Done!",fg="red",borderwidth=3)
        l1.place(relx=0.5,rely=0.1,anchor="n") 
        b1 = Scanner.Button(Result,text="Close",borderwidth=2,font=30,command=Result.destroy)
        b1.place(relx=0.34,rely=0.46)
    else:
        Error1 = Scanner.Tk()
        Error1.title('Error')
        c2 = Scanner.Canvas(Error1,height=90,width=200,)
        c2.pack()
        l2 = Scanner.Label(Error1,font=30,text="History is Epmty",fg="red",borderwidth=3)
        l2.place(relx=0.5,rely=0.1,anchor="n") 
        b2 = Scanner.Button(Error1,text="Ok!",borderwidth=2,font=40,command=Error1.destroy)
        b2.place(relx=0.37,rely=0.46)
window = Scanner.Tk()
window.title('Scanner')
canvas = Scanner.Canvas(window,height=600,width=650,bg="#cccc00")
canvas.pack()
upper_frame = Scanner.Frame(window,bg="#80c1ff",bd=5)
upper_frame.place(relx=0.5,rely=0.02,relwidth=0.75,relheight=0.1,anchor="n")
ent = Scanner.Entry(upper_frame,borderwidth=3,font=20)
ent.place(relwidth=0.65,relheight=1)
but = Scanner.Button(upper_frame,text="start",borderwidth=2,bg="#cccccc",fg="#cc3300",font=40,command=lambda: input_button(ent.get(),len(ent.get())))
but.place(relx=0.7,relheight=1,relwidth=0.3) 
lower_frame = Scanner.Frame(window,bg="#80c1ff",bd=5)
lower_frame.place(relx=0.5,rely=0.13,relwidth=0.75,relheight=0.3,anchor="n")
label = Scanner.Label(lower_frame,font=40)
label.place(relwidth=1,relheight=1)
down_frame = Scanner.Frame(window,bg="#80c1ff",bd=5)
down_frame.place(relx=0.5,rely=0.48,relwidth=0.75,relheight=0.4,anchor="n")
label2 = Scanner.Label(down_frame,text="HINT!\n1)letter(letter/digit)*: a65cf;\n2)identifier: x=;\n3)letter=letter/digit: x=5; , x=y;\n4)letter=letter/digit (+,-,*,/,^) letter/digit: x=x+y;\n5)use if , while : if:; , while:;\n6)letter ++,letter--,\nletter-=letter/digit,letter+=;etter/degeit: x++; ,x-=y;",font=30)
label2.place(relwidth=1,relheight=1)
his_but = Scanner.Button(window,text="History",borderwidth=2,bg="#cccccc",fg="#cc3300",font=30,command=His_but)
his_but.place(relx=0.29,rely=0.93,relheight=0.06,relwidth=0.15)
clr_but = Scanner.Button(window,text="Clear History",borderwidth=2,bg="#cccccc",fg="#cc3300",font=30,command=Clr_but)
clr_but.place(relx=0.49,rely=0.93,relheight=0.06,relwidth=0.19)
window.mainloop()
