from tkinter import *
import webbrowser


class login:

    def __init__(self):
        self.geometry       = '666x666'
        self.title          = 'Pandemic Dice'
        self.window         = None
        self.user_entry     = None
        self.password_entry = None

        self.tutorials_link = 'https://www.google.com'
        self.new_user_link  = 'https://www.google.com'
        self.website_link   = 'https://www.google.com'
        self.help_link      = 'https://www.google.com'

    def verify_user_password(self):
        user = self.user_entry.get()
        password = self.password_entry.get()
        print(f'El usuario es: {user} y la contraseña es: {password}')
        return 0

    def hyperlink_callback(self,url):
        webbrowser.open_new_tab(url)

    def create_window(self):

        self.window = Tk()
        self.window.geometry(self.geometry)
        self.window.title(self.title)
        self.window.configure(bg='white')

        # User label [X=180] [Y=200] A
        user_label = Label(self.window, text='User',bg='white')
        user_label.place(x=130,y=200)

        # User entry [X=200] [Y=200] A
        self.user_entry = Entry(self.window, width=25,bg='white')
        self.user_entry.place(x=200, y=200)

        # Password label [x=180] [Y=220] B
        password_label = Label(self.window, text='Password',bg='white')
        password_label.place(x=130,y=220)

        # Password entry [X=200] [Y=220] B
        self.password_entry = Entry(self.window, width=25, show='*',bg='white')
        self.password_entry.place(x=200, y=220)

        # Login button [X=200] [Y=240] C
        login_button = Button(self.window, text='Login', command=self.verify_user_password,bg='white')
        login_button.place(x=200,y=240)

        # New user hyperlink [X=336] [Y=244] D
        new_user_label = Label(self.window, text='New user?', bg='white', height=1, fg='blue')
        new_user_label.place(x=336,y=244)
        new_user_label.bind('<Button-1>', lambda e:self.hyperlink_callback(self.new_user_link))

        # Tutorials hyperlink [X=15] [Y=640] E
        tutorials_label = Label(self.window, text='Tutorials', bg='white', height=1, fg='blue')
        tutorials_label.place(x=15,y=640)
        tutorials_label.bind('<Button-1>', lambda e:self.hyperlink_callback(self.tutorials_link))

        # Website hyperlink [X=15] [Y=640] E
        website_label = Label(self.window, text='Visit our website!', bg='white', height=1, fg='blue')
        website_label.place(x=290,y=640)
        website_label.bind('<Button-1>', lambda e:self.hyperlink_callback(self.website_link))

        # HELP hyperlink [X=15] [Y=640] E
        HELP_LABEL = Label(self.window, text='HELP!', bg='white', height=1, fg='blue')
        HELP_LABEL.place(x=600,y=640)
        HELP_LABEL.bind('<Button-1>', lambda e:self.hyperlink_callback(self.help_link))



        self.window.mainloop()


prueba = login()
prueba.create_window()


