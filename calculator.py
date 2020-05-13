from tkinter import *

root = Tk()
root.title('My Calculator')

e = Entry(root, width=25, font=('Verdana', 16), borderwidth=10)
e.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

prevSymbol = None
prevAnswer = None

def button_click(symbol):
     global prevSymbol

     if not symbol:
          return

     if prevSymbol == '=':
          e.delete(0, END)

     prevSymbol = symbol
     
     e.insert(END, symbol)

def button_clear():
     e.delete(0, END)

def equals():
     global prevSymbol
     global prevAnswer

     expression = e.get()
     e.delete(0, END)

     evaluation = None
     try:
          evaluation = eval(expression)
     except:
          print('Syntax Error')
     
     if not evaluation:
          evaluation = 'Syntax Error'
     else:
          prevAnswer = evaluation

     e.insert(0, evaluation)
     prevSymbol = '='


buttonZero = Button(root, text='0', padx=40, pady=40, command=lambda: button_click('0'), font=('Verdana', 12))
buttonOne = Button(root, text='1', padx=40, pady=40, command=lambda: button_click('1'), font=('Verdana', 12))
buttonTwo = Button(root, text='2', padx=40, pady=40, command=lambda: button_click('2'), font=('Verdana', 12))
buttonThree= Button(root, text='3', padx=40, pady=40, command=lambda: button_click('3'), font=('Verdana', 12))
buttonFour = Button(root, text='4', padx=40, pady=40, command=lambda: button_click('4'), font=('Verdana', 12))
buttonFive = Button(root, text='5', padx=40, pady=40, command=lambda: button_click('5'), font=('Verdana', 12))
buttonSix = Button(root, text='6', padx=40, pady=40, command=lambda: button_click('6'), font=('Verdana', 12))
buttonSeven = Button(root, text='7', padx=40, pady=40, command=lambda: button_click('7'), font=('Verdana', 12))
buttonEight = Button(root, text='8', padx=40, pady=40, command=lambda: button_click('8'), font=('Verdana', 12))
buttonNine = Button(root, text='9', padx=40, pady=40, command=lambda: button_click('9'), font=('Verdana', 12))


buttonOne.grid(row=4, column=0)
buttonTwo.grid(row=4, column=1)
buttonThree.grid(row=4, column=2)
buttonFour.grid(row=3, column=0)
buttonFive.grid(row=3, column=1)
buttonSix.grid(row=3, column=2)
buttonSeven.grid(row=2, column=0)
buttonEight.grid(row=2, column=1)
buttonNine.grid(row=2, column=2)
buttonZero.grid(row=5, column=1)


buttonAdd = Button(root, text='+', padx=40, pady=40, command=lambda: button_click('+'), font=('Verdana', 12))
buttonEqual = Button(root, text='=', padx=40, pady=40, command=equals, font=('Verdana', 12))
buttonPeriod = Button(root, text='.', padx=42, pady=40, command=lambda: button_click('.'), font=('Verdana', 12))
buttonMinus = Button(root, text='-', padx=43, pady=40, command=lambda: button_click('-'), font=('Verdana', 12))
buttonMultiply = Button(root, text='*', padx=42, pady=40, command=lambda: button_click('*'), font=('Verdana', 12))
buttonDivide = Button(root, text='/', padx=41, pady=40, command=lambda: button_click('/'), font=('Verdana', 12))
buttonLParen = Button(root, text=' ( ', padx=35, pady=40, command=lambda: button_click('('), font=('Verdana', 12))
buttonRParen = Button(root, text=')', padx=42, pady=40, command=lambda: button_click(')'), font=('Verdana', 12))
buttonClear = Button(root, text='Clear', padx=24, pady=40, command=button_clear, font=('Verdana', 12))
buttonAnswer = Button(root, text='Ans', padx=30, pady=40, command=lambda: button_click(prevAnswer), font=('Verdana', 12))

buttonAdd.grid(row=4, column=3)
buttonEqual.grid(row=5, column=3)
buttonPeriod.grid(row=5, column=2)
buttonMinus.grid(row=3, column=3)
buttonMultiply.grid(row=2, column=3)
buttonDivide.grid(row=1, column=3)
buttonRParen.grid(row=1, column=2)
buttonLParen.grid(row=1, column=1)
buttonClear.grid(row=1, column=0)
buttonAnswer.grid(row=5, column=0)

root.mainloop()
