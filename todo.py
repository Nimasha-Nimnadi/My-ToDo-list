import tkinter
from tkinter import PhotoImage
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("My To-Do List")
window.configure(bg="light green")

def task_adding():
    todo = task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END, todo)
        task_add.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention !!", message="To add a task, please enter some task!!")


def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="Attention !!", message="To delete a task, you must select a task !!")


# def task_load():
#     try:
#         todo_list = pickle.load(open("tasks.dat", "rb"))
#         todo_box.delete(0, tkinter.END)
#         for todo in todo_list:
#             todo_box.insert(tkinter.END, todo)
#     except:
#         tkinter.messagebox.showwarning(title="Attention !!", message="Cannot find a task")


def task_save():
    todo_list = todo_box.get(0, todo_box.size())
    pickle.dump(todo_list, open("tasks.dat", "wb"))

image_path = "c.png"
bg_image = PhotoImage(file=image_path)

bg_label = tkinter.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)


list_frame = tkinter.Frame(window,)
list_frame.pack()

todo_box = tkinter.Listbox(list_frame, height=20, width=50,background="pink")
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)

task_add = tkinter.Entry(window, width=90)
task_add.pack()

button_style = {"font": ("Cavolini", 16, "bold"), "width": 37, "borderwidth": 5}

add_task_button = tkinter.Button(window, text="Click me for adding task", background="pink", command=task_adding, **button_style)
add_task_button.pack()

remove_task_button = tkinter.Button(window, text="Click me for delete task", background="pink", command=task_removing, **button_style)
remove_task_button.pack()

# load_task_button = tkinter.Button(window, text="Click me for load task", background="pink", command=task_load, **button_style)
# load_task_button.pack()

save_task_button = tkinter.Button(window, text="Click me to save task", background="pink", command=task_save, **button_style)
save_task_button.pack()

window.mainloop()
