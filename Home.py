import tkinter as tk
from tkinter import font  as tkfont
import backend


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, AdminPage, UserPage, login):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='BELL BOOKSTORE',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#3d3d5c')
        space_label.pack()

        user_label = tk.Label(self,
                              text='Enter your password',
                              font=('orbitron', 13),
                              bg='#3d3d5c',
                              fg='white')
        user_label.pack(pady=10)

        my_user = tk.StringVar()
        user_entry_box = tk.Entry(self,
                                  textvariable=my_user,
                                  font=('orbitron', 12),
                                  width=22)
        user_entry_box.focus_set()
        user_entry_box.pack(ipady=7)

        password_label = tk.Label(self,
                                  text='Enter your password',
                                  font=('orbitron', 13),
                                  bg='#3d3d5c',
                                  fg='white')
        password_label.pack(pady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self,
                                      textvariable=my_password,
                                      font=('orbitron', 12),
                                      width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)

        def handle_focus_in(_):
            password_entry_box.configure(fg='black', show='*')

        password_entry_box.bind('<FocusIn>', handle_focus_in)

        def check_password():
            if my_password.get() == '123' and my_user.get() == "lbell":
                my_password.set('')
                incorrect_password_label['text'] = ''
                controller.show_frame('AdminPage')
            else:
                incorrect_password_label['text'] = 'Incorrect Password or Username'

        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=check_password,
                                 relief='raised',
                                 borderwidth=3,
                                 width=40,
                                 height=3)
        enter_button.pack(pady=10)

        incorrect_password_label = tk.Label(self,
                                            text='',
                                            font=('orbitron', 13),
                                            fg='white',
                                            bg='#33334d',
                                            anchor='n')
        incorrect_password_label.pack(fill='both', expand=True)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        self.controller.title("Book Store")
        self.controller.state('zoomed')
        self.controller.iconphoto(False, tk.PhotoImage(
            file='C:/Users/chiko/Desktop/Projects B4 Repo/Python/Book_Store/bk.png'))

        Heading1 = tk.Label(self,
                            text='BELL BOOKSTORE',
                            font=('orbitron', 45, 'bold'),
                            foreground='white',
                            background='#3d3d5c')
        Heading1.pack(pady=25)

        space = tk.Label(self, height=4, bg='#3d3d5c')
        space.pack()

        user = tk.Label(self,
                        text='Choose to Login',
                        font=('orbitron', 13),
                        bg='#3d3d5c',
                        fg='white'
                        )
        user.pack(pady=10)

        def loginuser():
            controller.show_frame('login')

        Admin = tk.Button(self,
                          text='Admin',
                          command=loginuser,
                          relief='raised',
                          borderwidth=4,
                          width=40,
                          height=3)
        Admin.pack(pady=10)

        User = tk.Button(self,
                         text='User',
                         command=lambda: controller.show_frame("UserPage"),
                         relief='raised',
                         borderwidth=4,
                         width=40,
                         height=3)
        User.pack()

        incorrect_password_label = tk.Label(self,
                                            text='',
                                            font=('orbitron', 13),
                                            fg='white',
                                            bg='#33334d',
                                            anchor='n')
        incorrect_password_label.pack(fill='both', expand=True)


class AdminPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='BELL BOOKSTORE',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                   text='Administrator',
                                   font=('orbitron', 13),
                                   fg='white',
                                   bg='#3d3d5c')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='Admin Panel',
                                   font=('orbitron', 13),
                                   fg='white',
                                   bg='#3d3d5c',
                                   anchor='w')
        selection_label.pack(fill='x')

        Input_frame = tk.Frame(self, bg='#33334d')
        Input_frame.pack(fill='both', expand=True)
        Label1 = tk.Label(Input_frame,
                          text="Title",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label1.grid(row=0, column=1, pady=5)

        Label2 = tk.Label(Input_frame,
                          text="Author",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label2.grid(row=1, column=1, pady=5)

        Label3 = tk.Label(Input_frame,
                          text="Year",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label3.grid(row=2, column=1, pady=5)

        Label4 = tk.Label(Input_frame,
                          text="ISBN",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label4.grid(row=3, column=1, pady=5)

        Label5 = tk.Label(Input_frame,
                          text="Category",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label5.grid(row=4, column=1, pady=5)

        Label6 = tk.Label(Input_frame,
                          text="List",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label6.grid(row=5, column=1, pady=5)

        title_text = tk.StringVar()
        e1 = tk.Entry(Input_frame, textvariable=title_text)
        e1.grid(row=0, column=2, pady=5)

        author_text = tk.StringVar()
        e2 = tk.Entry(Input_frame, textvariable=author_text)
        e2.grid(row=1, column=2, pady=5)

        year_text = tk.StringVar()
        e3 = tk.Entry(Input_frame, textvariable=year_text)
        e3.grid(row=2, column=2, pady=5)

        isbn_text = tk.StringVar()
        e4 = tk.Entry(Input_frame, textvariable=isbn_text)
        e4.grid(row=3, column=2, pady=5)

        cat_text = tk.StringVar()
        e5 = tk.Entry(Input_frame, textvariable=cat_text)
        e5.grid(row=4, column=2, pady=5)

        list1 = tk.Listbox(Input_frame, height=6, width=35)
        list1.grid(row=5, column=2, rowspan=6, columnspan=2, pady=5)

        sb1 = tk.Scrollbar(Input_frame)
        sb1.grid(row=5, column=3, rowspan=6, pady=5)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        def get_selected_row(event):
            global selected_turple
            index = list1.curselection()[0]
            selected_turple = list1.get(index)
            e1.delete(0, tk.END)
            e1.insert(tk.END, selected_turple[1])
            e2.delete(0, tk.END)
            e2.insert(tk.END, selected_turple[2])
            e3.delete(0, tk.END)
            e3.insert(tk.END, selected_turple[3])
            e4.delete(0, tk.END)
            e4.insert(tk.END, selected_turple[4])
            e5.delete(0, tk.END)
            e5.insert(tk.END, selected_turple[5])

        list1.bind('<<ListboxSelect>>', get_selected_row)

        def view_command():
            list1.delete(0, tk.END)
            for row in backend.view():
                list1.insert(tk.END, row)

        b2 = tk.Button(Input_frame, text="View", width=12, command=view_command)
        b2.grid(row=24, column=3)

        def search_command():
            list1.delete(0, tk.END)
            for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get(),
                                      cat_text.get()):
                list1.insert(tk.END, row)

        b3 = tk.Button(Input_frame, text="Search entry", width=12, command=search_command)
        b3.grid(row=25, column=3)

        def add_command():
            backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get(),
                           cat_text.get())
            list1.delete(0, tk.END)
            list1.insert(tk.END,
                         (title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), cat_text.get()))

        b4 = tk.Button(Input_frame, text="add book", width=12, command=add_command)
        b4.grid(row=26, column=3)

        def update_command():
            backend.update(selected_turple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get(),
                           cat_text.get())

        b5 = tk.Button(Input_frame, text="update book", width=12, command=update_command)
        b5.grid(row=27, column=3)

        def delete_command():
            backend.delete(selected_turple[0])

        b6 = tk.Button(Input_frame, text="Delete book", width=12, command=delete_command)
        b6.grid(row=28, column=3)

        b6 = tk.Button(Input_frame, text="back", width=12, command=lambda: controller.show_frame("StartPage"))
        b6.grid(row=30, column=3)

        b6 = tk.Button(Input_frame, text="exit", width=12)
        b6.grid(row=31, column=3)


class UserPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='BELL BOOKSTORE',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                   text='User',
                                   font=('orbitron', 13),
                                   fg='white',
                                   bg='#3d3d5c')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='User Panel',
                                   font=('orbitron', 13),
                                   fg='white',
                                   bg='#3d3d5c',
                                   anchor='w')
        selection_label.pack(fill='x')

        Input_frame = tk.Frame(self, bg='#33334d')
        Input_frame.pack(fill='both', expand=True)
        Label1 = tk.Label(Input_frame,
                          text="Title",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label1.grid(row=0, column=30, pady=5)

        Label2 = tk.Label(Input_frame,
                          text="Author",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label2.grid(row=1, column=30, pady=5)

        Label3 = tk.Label(Input_frame,
                          text="Year",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label3.grid(row=2, column=30, pady=5)

        Label4 = tk.Label(Input_frame,
                          text="ISBN",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label4.grid(row=3, column=30, pady=5)

        Label5 = tk.Label(Input_frame,
                          text="Category",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label5.grid(row=4, column=30, pady=5)

        Label6 = tk.Label(Input_frame,
                          text="List",
                          font=('orbitron', 13),
                          fg='white',
                          bg='#33334d'
                          )
        Label6.grid(row=5, column=30, pady=5)

        title_text = tk.StringVar()
        e1 = tk.Entry(Input_frame, textvariable=title_text)
        e1.grid(row=0, column=32, pady=5)

        author_text = tk.StringVar()
        e2 = tk.Entry(Input_frame, textvariable=author_text)
        e2.grid(row=1, column=32, pady=5)

        year_text = tk.StringVar()
        e3 = tk.Entry(Input_frame, textvariable=year_text)
        e3.grid(row=2, column=32, pady=5)

        isbn_text = tk.StringVar()
        e4 = tk.Entry(Input_frame, textvariable=isbn_text)
        e4.grid(row=3, column=32, pady=5)

        cat_text = tk.StringVar()
        e5 = tk.Entry(Input_frame, textvariable=cat_text)
        e5.grid(row=4, column=32, pady=5)

        list1 = tk.Listbox(Input_frame, height=6, width=35)
        list1.grid(row=5, column=32, rowspan=6, columnspan=2, pady=5)

        sb1 = tk.Scrollbar(Input_frame)
        sb1.grid(row=5, column=34, rowspan=6, pady=10)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        def get_selected_row(event):
            global selected_turple
            index = list1.curselection()[0]
            selected_turple = list1.get(index)
            e1.delete(0, tk.END)
            e1.insert(tk.END, selected_turple[1])
            e2.delete(0, tk.END)
            e2.insert(tk.END, selected_turple[2])
            e3.delete(0, tk.END)
            e3.insert(tk.END, selected_turple[3])
            e4.delete(0, tk.END)
            e4.insert(tk.END, selected_turple[4])
            e5.delete(0, tk.END)
            e5.insert(tk.END, selected_turple[5])

        list1.bind('<<ListboxSelect>>', get_selected_row)

        def view_command():
            list1.delete(0, tk.END)
            for row in backend.view():
                list1.insert(tk.END, row)

        b2 = tk.Button(Input_frame, text="View All", width=12, command=view_command)
        b2.grid(row=24, column=32)

        def search_command():
            list1.delete(0, tk.END)
            for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get(),
                                      cat_text.get()):
                list1.insert(tk.END, row)

        b3 = tk.Button(Input_frame, text="Search entry", width=12, command=search_command)
        b3.grid(row=25, column=32)

        b6 = tk.Button(Input_frame, text="back", width=12, command=lambda: controller.show_frame("StartPage"))
        b6.grid(row=30, column=32)

        b6 = tk.Button(Input_frame, text="exit", width=12)
        b6.grid(row=31, column=32)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
