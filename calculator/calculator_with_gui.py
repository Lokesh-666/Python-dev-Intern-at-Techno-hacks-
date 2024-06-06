from tkinter import *
root = Tk()

ProgramTitle = "My Calculator"
root.title(ProgramTitle)

UserEntry = Entry(root, width=35, borderwidth=5)
UserEntry.grid(row=0,column=0,columnspan=4, padx=10, pady=10)



def AddNewClick(click):
    currentNumberInBox = UserEntry.get()
    UserEntry.delete(0, END)
    UserEntry.insert(0,str(currentNumberInBox)+str(click))

def ClearTheScreen():
    UserEntry.delete(0, END)
    UserEntry.insert(0,'')

def CalculateIt():
    from calculator.simple import SimpleCalculator
    calc = SimpleCalculator()
    string = str(UserEntry.get())
    calc.run(string)
    output = str(float(calc.lcd))
    UserEntry.delete(0, END)
    UserEntry.insert(0," = " + output)
    

def Actions(Action):
    match Action:
        case 'clear':
            UserEntry.delete(0, END)
        case 'LeftArrow':
            import pyautogui
            pyautogui.press("left")
        case 'RightArrow':
            import pyautogui
            pyautogui.press("right")
            



button_1 = Button(root, text='1', padx = 40, pady = 20, command = lambda: AddNewClick(1))
button_2 = Button(root, text='2', padx = 40, pady = 20, command = lambda: AddNewClick(2))
button_3 = Button(root, text='3', padx = 40, pady = 20, command = lambda: AddNewClick(3))
button_4 = Button(root, text='4', padx = 40, pady = 20, command = lambda: AddNewClick(4))
button_5 = Button(root, text='5', padx = 40, pady = 20, command = lambda: AddNewClick(5))
button_6 = Button(root, text='6', padx = 40, pady = 20, command = lambda: AddNewClick(6))
button_7 = Button(root, text='7', padx = 40, pady = 20, command = lambda: AddNewClick(7))
button_8 = Button(root, text='8', padx = 40, pady = 20, command = lambda: AddNewClick(8))
button_9 = Button(root, text='9', padx = 40, pady = 20, command = lambda: AddNewClick(9))
button_0 = Button(root, text='0', padx = 40, pady = 20, command = lambda: AddNewClick(0))

button_Dot = Button(root, text='.', padx = 40, pady = 20, command = lambda: AddNewClick('.'))

button_add = Button(root, text='+', padx = 39, pady = 20, command = lambda: AddNewClick('+'))
button_subtract = Button(root, text='-', padx = 39, pady = 20, command = lambda: AddNewClick('-'))
button_multiply = Button(root, text='*', padx = 39, pady = 20, command = lambda: AddNewClick('*'))
button_divide = Button(root, text='/', padx = 39, pady = 20, command = lambda: AddNewClick('/'))

button_equal = Button(root, text='=', padx = 39, pady = 20, command = CalculateIt)
button_clear = Button(root, text='X', padx = 39, pady = 20, command = lambda: Actions('clear'))
button_space = Button(root, text='_', padx = 39, pady = 20, command = lambda: AddNewClick(' '))

button_leftArrow = Button(root, text='<', padx = 39, pady = 20, command = lambda: Actions('LeftArrow'))
button_rightArrow = Button(root, text='>', padx = 39, pady = 20, command = lambda: Actions('RightArrow'))


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_Dot.grid(row=4, column=2)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)


button_equal.grid(row=4, column=0)
button_clear.grid(row=5, column=0)

button_space.grid(row = 5, column = 1)

button_leftArrow.grid(row = 5, column = 2)
button_rightArrow.grid(row = 5, column = 3)





if __name__ == "__main__":
    root.mainloop()