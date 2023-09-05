import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
 
window = tk.Tk()
window.title('Basic Arithmatic Calculator')
frame = tk.Frame(master=window, bg="black", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=6, width=60)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)
 
 
def byclick(number):
    entry.insert(tk.END, number)
 
 
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Syntax Error")
 
 
def clear():
    entry.delete(0, tk.END)
 
 
button_1 = tk.Button(master=frame, text='1', padx=15,
                     pady=5, width=3, bg="grey", command=lambda: byclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15,
                     pady=5, width=3, bg="grey", command=lambda: byclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15,
                     pady=5, width=3, bg="grey", command=lambda: byclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15,
                     pady=5, width=3, bg="grey", command=lambda: byclick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15,
                     pady=5, width=3, bg="grey", command=lambda: byclick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15,
                     pady=5, width=3, bg="grey", command=lambda: byclick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15,
                     pady=5, width=3, bg="grey", command=lambda: byclick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15,
                     pady=5, width=3, bg="grey", command=lambda: byclick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15,
                     pady=5, width=3, bg="grey", command=lambda: byclick(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15,
                     pady=5, width=3, bg="grey", command=lambda: byclick(0))
button_0.grid(row=4, column=1, pady=2)
 
button_add = tk.Button(master=frame, text="+", padx=15, pady=5, width=3, bg="yellow", command=lambda: byclick('+'))
button_add.grid(row=5, column=0, pady=2)
 
button_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=3, bg="blue", command=lambda: byclick('-'))
button_subtract.grid(row=5, column=1, pady=2)
 
button_multiply = tk.Button(master=frame, text="*", padx=15, pady=5, width=3, bg="orange", command=lambda: byclick('*'))
button_multiply.grid(row=5, column=2, pady=2)
 
button_div = tk.Button(master=frame, text="/", padx=15, pady=5, width=3, bg="green",  command=lambda: byclick('/'))
button_div.grid(row=6, column=0, pady=2)
 
button_clear = tk.Button(master=frame, text="clear", padx=15, pady=5, width=12, bg="red", fg="white", command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)
 
button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=9, bg="lightblue", fg="brown", command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)
 
window.mainloop()
