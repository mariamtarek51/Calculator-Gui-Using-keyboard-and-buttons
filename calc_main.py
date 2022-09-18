import tkinter as tk
import calc as c

import keyboard
""" 
Fucntion: caluculator using Keyboard and calc library
version 2: in this version i used different library which was much easier  but there are assumptions user needs to follow :
enter press :"=" 
p press : "^" 
s press : "sqrt" 
Date: 15/9/2022 2:41 Am 
authors :Mariam


"""
root = tk.Tk()
root.title('Centered window')
equn=""
window_height = 310
window_width = 570


def center_screen():
    """ gets the coordinates of the center of the screen """
    global screen_height, screen_width, x_cordinate, y_cordinate

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
def updatescreen():
    global lbl
    lbl["text"]=equn
    print(equn)


def show(input):
    global equn
    print("show",input)
    equn=equn+str(input)
    print("showequn",equn)
    updatescreen()
def clear():
    global equn
    equn=""
    updatescreen()
def solve():
    global  equn
    #split the string
    print("in solve",equn)


    if(equn.find('+')!=-1):
        x=equn.split("+")

        equn=c.add2(int(x[0]),int(x[1]));

        updatescreen()
    elif(equn.find('-')!=-1)  :
        x = equn.split("-",1)
        print(int(x[0]))
        print(x[1])

        equn = c.sub(int(x[0]), int(x[1]));
        updatescreen()
    elif (equn.find('x') != -1):
        x = equn.split("x")

        equn = c.mult(int(x[0]), int(x[1]));
        updatescreen()
    elif (equn.find('/') != -1):
        x = equn.split("/")

        equn = c.div(int(x[0]), int(x[1]));
        updatescreen()
    elif (equn.find('^') != -1):
        x = equn.split("^")

        equn = c.power(int(x[0]), int(x[1]));
        updatescreen()
    elif (equn.find('√') != -1):
        x = equn.split("√")

        equn = c.sqrt( int(x[1]),-1);
        updatescreen()








def create_buttons():

    bt1 = tk.Button(root, text="1", font=("Arial Bold", 15),command=lambda:show(1), bg="white", fg="blue", width=15)
    bt1.grid(column=0, row=2)
    bt2 = tk.Button(root, text="2", font=("Arial Bold", 15),command=lambda:show(2), bg="white", fg="blue", width=15)
    bt2.grid(column=1, row=2)
    bt3 = tk.Button(root, text="3", font=("Arial Bold", 15),command=lambda:show(3), bg="white", fg="blue", width=15)
    bt3.grid(column=2, row=2)
    bt4 = tk.Button(root, text="4", font=("Arial Bold", 15),command=lambda:show(4), bg="white", fg="blue", width=15)
    bt4.grid(column=0, row=3)
    bt5 = tk.Button(root, text="5", font=("Arial Bold", 15),command=lambda:show(5), bg="white", fg="blue", width=15)
    bt5.grid(column=1, row=3)
    bt6 = tk.Button(root, text="6", font=("Arial Bold", 15),command=lambda:show(6), bg="white", fg="blue", width=15)
    bt6.grid(column=2, row=3)
    bt7 = tk.Button(root, text="7", font=("Arial Bold", 15),command=lambda:show(7), bg="white", fg="blue", width=15)
    bt7.grid(column=0, row=4)
    bt8 = tk.Button(root, text="8", font=("Arial Bold", 15),command=lambda:show(8), bg="white", fg="blue", width=15)
    bt8.grid(column=1, row=4)
    bt9 = tk.Button(root, text="9", font=("Arial Bold", 15),command=lambda:show(9), bg="white", fg="blue", width=15)
    bt9.grid(column=2, row=4)

    btadd = tk.Button(root, text="+", font=("Arial Bold", 15),command=lambda:show("+"), bg="white", fg="blue", width=15)
    btadd.grid(column=0, row=5)
    btsub = tk.Button(root, text="-", font=("Arial Bold", 15), bg="white",command=lambda:show("-"), fg="blue", width=15)
    btsub.grid(column=1, row=5)
    btmult = tk.Button(root, text="x", font=("Arial Bold", 15),command=lambda:show("x"), bg="white", fg="blue", width=15)
    btmult.grid(column=2, row=5)
    btdiv = tk.Button(root, text="/", font=("Arial Bold", 15),command=lambda:show("/"), bg="white", fg="blue", width=15)
    btdiv.grid(column=0, row=6)
    btpow = tk.Button(root, text="^", font=("Arial Bold", 15),command=lambda:show("^"), bg="white", fg="blue", width=15)
    btpow.grid(column=1, row=6)
    btsqrt = tk.Button(root, text="√", font=("Arial Bold", 15),command=lambda:show("√"), bg="white", fg="blue", width=15)
    btsqrt.grid(column=2, row=6)
    btequal= tk.Button(root, text="=", font=("Arial Bold", 15),command=lambda:solve(), bg="white", fg="blue",
                       width=15)
    btequal.grid(column=0, row=7)
    btclear = tk.Button(root, text="clear", font=("Arial Bold", 15), command=lambda: clear(), bg="white", fg="blue",
                        width=15)
    btclear.grid(column=1, row=7)
    btzero = tk.Button(root, text="0", font=("Arial Bold", 15), command=lambda: show(0), bg="white", fg="blue",
                        width=15)
    btzero.grid(column=2, row=7)

center_screen()
lbl = tk.Label(root,textvariable=equn, font=("Times New Roman Bold", 35), fg="blue")
lbl.grid(column=0, row=0)
create_buttons()
root.title("Calculator")

keyboard.on_press_key('1', lambda _ :show(1))
keyboard.on_press_key('2', lambda _ :show(2))
keyboard.on_press_key('3', lambda _ :show(3))
keyboard.on_press_key('4', lambda _ :show(4))
keyboard.on_press_key('5', lambda _ :show(5))
keyboard.on_press_key('6', lambda _ :show(6))
keyboard.on_press_key('7', lambda _ :show(7))
keyboard.on_press_key('8', lambda _ :show(8))
keyboard.on_press_key('9', lambda _ :show(9))
keyboard.on_press_key('0', lambda _ :show(0))
keyboard.on_press_key('+', lambda _ :show("+"))
keyboard.on_press_key('-', lambda _ :show("-"))
keyboard.on_press_key('x', lambda _ :show("x"))
keyboard.on_press_key('/', lambda _ :show("/"))
keyboard.on_press_key('s', lambda _ :show("√"))
keyboard.on_press_key('p', lambda _ :show("^"))
keyboard.on_press_key('enter', lambda _ :solve())
keyboard.on_press_key('c', lambda _ :clear())



root.mainloop()

