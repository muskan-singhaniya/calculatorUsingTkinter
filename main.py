import tkinter as tk

mainScreen = tk.Tk()
mainScreen.title("Calculator")

canvas = tk.Canvas(mainScreen, width = 600, height = 500,bg="RoyalBlue4")
canvas.pack()

heading = tk.Label(mainScreen, text= "Calculator", bg="RoyalBlue4", fg="White",font=("Helvetica",25,"bold","underline"))
canvas.create_window(300, 50, window=heading)

num1Label = tk.Label(mainScreen, text= "Enter number 1 : ", bg="RoyalBlue4", fg="White",font=("Helvetica",15))
canvas.create_window(200, 120, window=num1Label)
num2Label = tk.Label(mainScreen, text= "Enter number 2 : ", bg="RoyalBlue4", fg="White",font=("Helvetica",15))
canvas.create_window(200, 170, window=num2Label)

num1Entry = tk.Entry (mainScreen,fg="RoyalBlue4", bg="White",font=("Helvetica",12),width=14)
num2Entry = tk.Entry (mainScreen,fg="RoyalBlue4", bg="White",font=("Helvetica",12),width=14)
canvas.create_window(400, 120, window=num1Entry)
canvas.create_window(400, 170, window=num2Entry)

result = tk.StringVar()

def getSquareRoot():  
    x1 = num1Entry.get()
    result.set(float(x1)**0.5)

def getsum():
  x1 = num1Entry.get()
  x2 = num2Entry.get()
  result.set(int(x1) + int(x2))

def getdifference():
  x1 = num1Entry.get()
  x2 = num2Entry.get()
  result.set(int(x1) - int(x2))

def getproduct():
  x1 = num1Entry.get()
  x2 = num2Entry.get()
  result.set(int(x1) * int(x2))

def getquotient():
  x1 = num1Entry.get()
  x2 = num2Entry.get()
  result.set(int(x1) / int(x2))

def getmodulus():
  x1 = num1Entry.get()
  x2 = num2Entry.get()
  result.set(int(x1) % int(x2))

def getSquare():
  x1 = num1Entry.get()
  result.set(float(x1)**2)

addbutton = tk.Button(text='+', command=getsum,fg="darkBlue", bg="White",font=("Helvetica",15),width=2)
subbutton = tk.Button(text='-', command=getdifference,fg="darkBlue", bg="White",font=("Helvetica",15),width=2)
mulbutton = tk.Button(text='X', command=getproduct,fg="darkBlue", bg="White",font=("Helvetica",15),width=2)
divbutton = tk.Button(text='÷', command=getquotient,fg="darkBlue", bg="White",font=("Helvetica",15),width=2)
rootbutton = tk.Button(text='√x1', command=getSquareRoot,fg="darkBlue", bg="White",font=("Helvetica",15),width=2)
modbutton = tk.Button(text='%', command=getmodulus,fg="darkBlue", bg="White",font=("Helvetica",15),width=2)
squarebutton = tk.Button(text='x1^2', command=getSquare,fg="darkBlue", bg="White",font=("Helvetica",15),width=2)

canvas.create_window(80, 250, window=addbutton)
canvas.create_window(155, 250, window=subbutton)
canvas.create_window(230, 250, window=mulbutton)
canvas.create_window(305, 250, window=divbutton)
canvas.create_window(380, 250, window=rootbutton)
canvas.create_window(455, 250, window=modbutton)
canvas.create_window(530, 250, window=squarebutton)

resultLabel = tk.Label(mainScreen, text= "Result : ", bg="RoyalBlue4", fg="White",font=("Helvetica",15))
canvas.create_window(200, 370, window=resultLabel)
resultEntry = tk.Entry (mainScreen,textvariable=result,fg="RoyalBlue4", bg="White",font=("Helvetica",12),width=14)
canvas.create_window(350, 370, window=resultEntry)

mainScreen.mainloop()