from tkinter import *
import sqlite3
from backend import Database

database = Database("bookshop.db")

window=Tk()
window.resizable(width=False, height=False)
window.wm_title("I'll take you to the bookshop")
class Functions:
    def get_selected_row(event):
        if BS.t1.curselection() == ():
            pass
        else:
            print(BS.t1.curselection())
            global selected_tuple
            index=BS.t1.curselection()[0]
            selected_tuple=BS.t1.get(index)
            Entries.e1.delete(0,END)
            Entries.e1.insert(END,selected_tuple[1])
            Entries.e2.delete(0,END)
            Entries.e2.insert(END,selected_tuple[2])
            Entries.e3.delete(0,END)
            Entries.e3.insert(END,selected_tuple[3])
            Entries.e4.delete(0,END)
            Entries.e4.insert(END,selected_tuple[4])

    def view_command():
        BS.t1.delete(0,END)
        for r in database.view():
            BS.t1.insert(END,r)


    def search_command():
        BS.t1.delete(0,END)
        for r in database.search(Entries.vtitle.get(),Entries.vauthor.get(),Entries.vyear.get(),Entries.vISBN.get()):
            BS.t1.insert(END,r)

    def add_command():
        BS.t1.delete(0,END)
        database.insert(Entries.vtitle.get(),Entries.vauthor.get(),Entries.vyear.get(),Entries.vISBN.get())
        BS.t1.insert(END,(Entries.vtitle.get(),Entries.vauthor.get(),Entries.vyear.get(),Entries.vISBN.get()))

    def update_command():
        BS.t1.delete(0,END)
        database.update(selected_tuple[0], Entries.vtitle.get(),Entries.vauthor.get(),Entries.vyear.get(),Entries.vISBN.get())
        BS.t1.delete(0,END)
        for r in database.view():
            BS.t1.insert(END,r)

    def delete_command():
        database.deleteit(selected_tuple[0])
        BS.t1.delete(0,END)
        for r in database.view():
            BS.t1.insert(END,r)

class Labels:
    l1=Label(window, text="Title")
    l1.grid(row=0,column=0)

    l2=Label(window, text="Author")
    l2.grid(row=0,column=2)

    l3=Label(window, text="Year")
    l3.grid(row=1,column=0)

    l4=Label(window, text="ISBN")
    l4.grid(row=1,column=2)

class Buttons:
    b1=Button(window, width = 15 , text="View All", command=Functions.view_command)
    b1.grid(row=3, column=3)

    b2=Button(window, width = 15, text="Search Entry", command=Functions.search_command)
    b2.grid(row=4, column=3)

    b3=Button(window, width = 15, text="Add Entry", command=Functions.add_command)
    b3.grid(row=5, column=3)

    b4=Button(window, width = 15, text="Update Selected", command=Functions.update_command)
    b4.grid(row=6, column=3)

    b5=Button(window, width = 15, text="Delete Selected", command=Functions.delete_command)
    b5.grid(row=7, column=3)

    b6=Button(window,width = 15, text="Close", command=window.destroy)
    b6.grid(row=8, column=3)

class Entries:
    vtitle = StringVar()
    e1=Entry(window, textvariable=vtitle)
    e1.grid(row=0,column=1)

    vauthor = StringVar()
    e2=Entry(window, textvariable=vauthor)
    e2.grid(row=0,column=3)

    vyear = StringVar()
    e3=Entry(window, textvariable=vyear)
    e3.grid(row=1,column=1)

    vISBN = StringVar()
    e4=Entry(window, textvariable=vISBN)
    e4.grid(row=1,column=3)

class BS:
    t1=Listbox(window, height=7, width=25)
    t1.grid(row=4,column=0, columnspan=2, rowspan=4)

    t1.bind("<<ListboxSelect>>", Functions.get_selected_row)

    sy = Scrollbar(window)
    sy.grid(row=4, column=2, rowspan=4, sticky="ns")
    sx = Scrollbar(window,orient="horizontal")
    sx.grid(row=8, column=0, columnspan=2, sticky=W+E)
    sx.configure(command=t1.xview)
    t1.configure(yscrollcommand=sx.set)
    sy.configure(command=t1.yview)
    t1.configure(yscrollcommand=sy.set)


window.mainloop()
