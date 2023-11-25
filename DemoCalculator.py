from tkinter import *

root = Tk()
root.title("Demo Calculator")
root.iconbitmap("Calculator.ico")
root.resizable(width=False, height=False)


# button click korle Entry field a Dekhabe ai function
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


#Entry fild a j Calculation ba number ja clear korte chai. tar fungtion
def button_clear():
    entry.delete(0,END)


def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)

def subtraction():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0,END)

def multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    entry.delete(0,END)

def division():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    entry.delete(0,END)





def equal():
    second_number = entry.get()
    entry.delete(0,END)
    if math == "addition":
        entry.insert(0, f_num + int(second_number))

    if math == "subtraction":
        entry.insert(0, f_num - int(second_number))

    if math == "multiply":
        entry.insert(0, f_num * int(second_number))

    if math == "division":
        entry.insert(0,f_num / int(second_number))


#Entry Field
entry = Entry(root, width=35,bd=2,font="ds-digital",fg="blue")

#button
button_1 = Button(root,text="1",padx=43,pady=20,command=lambda:button_click(1))
button_2 = Button(root,text="2",padx=43,pady=20,command=lambda:button_click(2))
button_3 = Button(root,text="3",padx=43,pady=20,command=lambda:button_click(3))
button_4 = Button(root,text="4",padx=43,pady=20,command=lambda:button_click(4))
button_5 = Button(root,text="5",padx=43,pady=20,command=lambda:button_click(5))
button_6 = Button(root,text="6",padx=43,pady=20,command=lambda:button_click(6))
button_7 = Button(root,text="7",padx=43,pady=20,command=lambda:button_click(7))
button_8 = Button(root,text="8",padx=43,pady=20,command=lambda:button_click(8))
button_9 = Button(root,text="9",padx=43,pady=20,command=lambda:button_click(9))
button_0 = Button(root,text="0",padx=43,pady=20,command=lambda:button_click(0))
button_clear = Button(root,text="Clear",padx=135,pady=20,command=button_clear)
button_add = Button(root,text="+",padx=43,pady=20,command=button_add)
button_subtraction = Button(root,text="-",padx=43,pady=20,command=subtraction)
button_multiply = Button(root,text="*",padx=43,pady=20,command=multiply)
button_division = Button(root,text="/",padx=43,pady=20,command=division)
button_equal = Button(root,text="=",padx=43,pady=20,bg="cyan",command=equal)





#Entry Grid
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#button Grid
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_0.grid(row=4,column=1)
button_add.grid(row=4,column=0)
button_subtraction.grid(row=4,column=2)
button_division.grid(row=5,column=0)
button_equal.grid(row=5,column=1)
button_multiply.grid(row=5,column=2)
button_clear.grid(row=6,column=0,columnspan=3)


root.mainloop()
