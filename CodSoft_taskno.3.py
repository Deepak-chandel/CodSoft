import random, string
from tkinter import *
import pyperclip

root =Tk()

root.geometry("500x500")

root.title("Random Password Generator")

output_password = StringVar()

all_combination = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]

def randompwd():
    password = "" 
    for y in range(password_len.get()):
        char_type = random.choice(all_combination)   
        password = password + random.choice(char_type)
    
    output_password.set(password)

def copypwd():
    pyperclip.copy(output_password.get())

# Front End GUI
password_head = Label(root, text = 'Password Length', font = 'arial 12 bold').pack(pady=20) 

password_len = IntVar() 
length = Spinbox(root, from_ = 4, to_ = 12 , textvariable = password_len , width = 24, font='arial 16').pack()


Button(root, command = randompwd, text = "Generate Password", font="Arial 10", bg='lightblue', fg='blue', activebackground="green", padx=6, pady=6 ).pack(pady= 30)

password_label = Label(root, text = 'Random Generated Password', font = 'arial 12 bold').pack(pady="30 10")
Entry(root , textvariable = output_password, width = 24, font='arial 16').pack()


Button(root, text = 'Copy to Clipboard', command = copypwd, font="Arial 10", bg='lightblue', fg='red', activebackground="yellow", padx=5, pady=5 ).pack(pady= 20)

root.mainloop()  
