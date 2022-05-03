from tkinter import *
top=Tk()
top.title("calculator")
top.geometry("500x500")
def addnumber():
    res1=int(entry1.get())+int(entry2.get())
    mytext.set(res1)
def subnumber():
    res1=int(entry1.get())-int(entry2.get())
    mytext.set(res1)
    
def mulnumber():
    res1=int(entry1.get())*int(entry2.get())
    mytext.set(res1)
        
def divnumber():
    res1=int(entry1.get())/int(entry2.get())
    mytext.set(res1)

mytext=StringVar()

Label(top,text="First").grid(row=0,sticky=W)
Label(top,text="second").grid(row=1,sticky=W)
Label(top,text="Result").grid(row=3,sticky=W)
result=Label(top,text="",textvariable=mytext).grid(row=3,column=1)
entry1=Entry(top)
entry2=Entry(top)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

button1=Button(top,text="+",command=addnumber)
button1.grid(row=0,column=10,columnspan=1,rowspan=1,padx=5,pady=5)
button2=Button(top,text="-",command=subnumber)
button2.grid(row=0,column=11,columnspan=1,rowspan=1,padx=5,pady=5)
button3=Button(top,text="*",command=mulnumber)
button3.grid(row=0,column=12,columnspan=1,rowspan=1,padx=5,pady=5)
button4=Button(top,text="/",command=divnumber)
button4.grid(row=0,column=13,columnspan=1,rowspan=1,padx=5,pady=5)

top.main()
