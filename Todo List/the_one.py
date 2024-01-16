import tkinter as tk
from tkinter import *

#main loop
window = Tk()
window.title("To-Do List")
window.geometry("400x650+30+25")
window.resizable(False,False)

task_list = []

def add_task():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as task_file:
            task_file.write (f"\n{task}")
        task_list.append(task)
        list_box.insert (END, task)

def delete_task():
    global task_list
    task = str(list_box.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open ("tasklist.txt", "w") as task_file:
            for task in task_list:
                task_file.write(task + "\n")

        list_box.delete(ANCHOR)

def open_task_file():

    try:
        global task_list
        with open("tasklist.txt", "r") as task_file:
            tasks = task_file.readlines() 

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                list_box.insert(END, task)
    
    except:
        file= open ("tasklist.txt", 'w')
        file.close()






#Icon photo
image_icon = PhotoImage(file= "Todo List/task.png")
window.iconphoto (False, image_icon)

#Top bar
top_image = PhotoImage(file = "Todo List/topbar.png")
add_label = Label(window, image= top_image)
add_label.pack()

dock_image = PhotoImage(file= "Todo List/dock.png")
create_label = Label (window, image=dock_image, bg= "#32405b")
create_label.place(x=30, y=25)

note_image = PhotoImage(file= "Todo List/task.png")
make_label = Label(window, image=note_image, bg="#32405b")
make_label.place (x= 30, y= 25)

heading = Label(window, text= "ALL TASKS", font= "Helvetica 20 bold", fg= "white", bg= "#32405b")
heading.place(x= 130, y=20)

#main
frame = Frame(window, width= 400, height= 50, bg= "white")
frame.place (x= 0, y= 180)

task = StringVar()
task_entry = Entry (frame, width=18, font= "Helvetica 20", bd= 0) 
task_entry.place(x= 10, y= 7)
task_entry.focus()

button = Button(frame, text= "ADD TASK", font= "Helvetica 20 bold", width= 10, bg= "#5a95ff", fg= "#fff", bd=0, command= add_task)
button.place(x= 230, y= 0)


#listbox
list_frame=  Frame(window, bd= 3, width=700, height=280, bg="#32405b")
list_frame.pack(pady=(160,0))

list_box = Listbox(list_frame, font= ('Helvetica', 12), width= 40, height= 16, bg= "#32405b", fg= "white", cursor= "hand2", selectbackground="#5a95ff")
list_box.pack(side= LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(list_frame)
scrollbar.pack (side= RIGHT, fill=  BOTH)

list_box.config(yscrollcommand= scrollbar.set)
scrollbar.config(command= list_box.yview)

open_task_file()

#delete

delete_icon = PhotoImage(file= "Todo List/delete.png")
delete_button= Button (window, image= delete_icon, bd=0, command= delete_task)
delete_button.pack(side= BOTTOM, pady= 13)

window.mainloop()