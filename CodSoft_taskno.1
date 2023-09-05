import tkinter as tk                    
from tkinter import ttk                 
from tkinter import messagebox          
import sqlite3 as sql                   
  
def addtasks():  
    task_string = task_field.get()  

    if len(task_string) == 0:  
        messagebox.showinfo('The Field is Empty.')  
    else:    
        tasks.append(task_string)  
        
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        
        listupdate()  
        
        task_field.delete(0, 'end')  
  
def listupdate():  
    
    clearthelist()  
    
    for task in tasks:  
        
        task_listbox.insert('end', task)  
  
def deletetasks():  

    try:  
        the_value = task_listbox.get(task_listbox.curselection())  
        
        if the_value in tasks:  
            
            tasks.remove(the_value)  
            
            listupdate()  
 
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
         
        messagebox.showinfo('No Task Selected to Delete.')        
  
def deletealltasks():  
     
    message_box = messagebox.askyesno('Are you sure you want to Delete all the tasks?')  
      
    if message_box == True:  
        
        while(len(tasks) != 0):  
             
            tasks.pop()  

        the_cursor.execute('delete from tasks')  
    
        listupdate()  
  
def clearthelist():  
 
    task_listbox.delete(0, 'end')  
  
def close():  
    print(tasks)  
     
    guiWindow.destroy()  
  
def retrievedatabase():   
    while(len(tasks) != 0):  
    
        tasks.pop()  

    for row in the_cursor.execute('select title from tasks'):  
        
        tasks.append(row[0])  
  
if __name__ == "__main__":  
    
    guiWindow = tk.Tk()  
    
    guiWindow.title("To-Do Task List ")  

    guiWindow.geometry("600x550+450+250")  

    guiWindow.resizable(0, 0)  

    guiWindow.configure(bg = "yellow")  
   
    the_connection = sql.connect('listOfTasks.db')  
    
    the_cursor = the_connection.cursor()  
     
    the_cursor.execute('create table if not exists tasks (title text)')  
  
    tasks = []  
      
    header_frame = tk.Frame(guiWindow, bg = "yellow")  
    functions_frame = tk.Frame(guiWindow, bg = "yellow")  
    listbox_frame = tk.Frame(guiWindow, bg = "yellow")  
  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
    header_label = ttk.Label(  
        header_frame,  
        text = "The To-Do List",  
        font = ("Times New Roman", "30"),  
        background = "yellow",  
        foreground = "red"  
    )  
    
    header_label.pack(padx = 20, pady = 20)  
  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "11", "bold"),  
        background = "yellow",  
        foreground = "blue"  
    )   
    task_label.place(x = 40, y = 50)  
      
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "lightyellow",  
        foreground = "red"  
    )  
    task_field.place(x = 40, y = 80)  
  
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,
        command = addtasks
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,
        command = deletetasks  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,
        command = deletealltasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,
        command = close  
    )  
    add_button.place(x = 40, y = 130)  
    del_button.place(x = 40, y = 170)  
    del_all_button.place(x = 40, y = 200)  
    exit_button.place(x = 40, y = 250)  
  
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "white",  
        foreground = "black",  
        selectbackground = "blue",  
        selectforeground = "white"  
    )  
    task_listbox.place(x = 20, y = 30)  
  
    
    retrievedatabase()  
    listupdate()  

    guiWindow.mainloop()  
 
    the_connection.commit()  
    the_cursor.close()  
