import customtkinter as ctk
from builtins import *
import re
import csv
import tkinter as tk
from CTkListbox import *


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
global mail

window = ctk.CTk()

ctk.set_default_color_theme("green")
window.title("Home Page")
window.geometry("800x500")


def password_control():
    global wrong_password
    with open("users.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row[1] == login_password.get():
                try:
                    wrong_password.destroy()
                except:
                    pass
                home_page()
            else:
                wrong_password = ctk.CTkLabel(master=window, text="Wrong password", font=ctk.CTkFont(size=20, weight="bold"),
                                          text_color="red")
                wrong_password.place(relx=0.59, rely=0.75, anchor=ctk.CENTER)


def sign_in_password():
    global wrong_password2, login_again

    with open("users.csv", "a") as f:
        writer = csv.writer(f, delimiter=",")
        if signin_password.get() == signin_password_again.get():
            try:
                wrong_password2.destroy()
            except:
                pass
            user_list = [mail, signin_password.get()]
            writer.writerow(user_list)
            login_again = ctk.CTkLabel(master=window, text="Log in again",
                                       font=ctk.CTkFont(size=20, weight="bold"),
                                       text_color="green")
            login_again.place(relx=0.59, rely=0.75, anchor=ctk.CENTER)
            login()
        else:
            wrong_password2 = ctk.CTkLabel(master=window, text="Wrong password", font=ctk.CTkFont(size=20, weight="bold"),
                                          text_color="red")
            wrong_password2.place(relx=0.59, rely=0.75, anchor=ctk.CENTER)



def mail_control():
    global wrong_mail, mail
    try:
        wrong_mail.destroy()
    except:
        pass

    try:
        mail = signin_mail.get()
    except:
        pass

    try:
        mail = login_mail.get()
    except:
        pass

    if (re.fullmatch(regex, mail)):
        try:
            if mail == login_mail.get():
                with open("users.csv", "r")as f:
                    reader = csv.reader(f, delimiter=",")
                    for row in reader:
                        if row[0] == mail:
                            password_control()
                        else:
                            wrong_mail = ctk.CTkLabel(master=window, text="Wrong mail",
                                                      font=ctk.CTkFont(size=20, weight="bold"), text_color="red")
                            wrong_mail.place(relx=0.59, rely=0.75, anchor=ctk.CENTER)
        except:
            pass

        try:
            if mail == signin_mail.get():
                with open("users.csv", "r") as f:
                    print(mail)
                    reader = csv.reader(f, delimiter=",")
                    for row in reader:
                        print(row[0])
                        if row[0] == mail:
                            wrong_mail = ctk.CTkLabel(master=window, text="e-mail is used",
                                                      font=ctk.CTkFont(size=20, weight="bold"), text_color="red")
                            wrong_mail.place(relx=0.59, rely=0.75, anchor=ctk.CENTER)
                            exit(mail_control)
                    sign_in_password()
        except:
            pass
    else:
        wrong_mail = ctk.CTkLabel(master=window, text="Wrong mail", font=ctk.CTkFont(size=20, weight="bold"), text_color="red")
        wrong_mail.place(relx=0.59, rely=0.75, anchor=ctk.CENTER)


def login():
    global mail
    global login_mail, login_password, login_button, login_label
    welcome_label.destroy()
    try:
        wrong_mail.destroy()
    except:
        pass

    try:
        wrong_password.destroy()
    except:
        pass

    try:
        signin_password_again.destroy()
        signin_mail.destroy()
        signin_password.destroy()
        signin_button.destroy()
        signin_label.destroy()
        login_again.destroy()
    except:
        pass
    login_label = ctk.CTkLabel(master = window, text="LOGIN", font=ctk.CTkFont(size=60, weight="bold"))
    login_label.place(relx = 0.475, rely = 0.1)
    login_mail = ctk.CTkEntry(placeholder_text="Email", master=window)
    login_mail.place(relx = 0.5, rely = 0.3)
    mail = login_mail.get()
    login_password = ctk.CTkEntry(placeholder_text="Password", master=window)
    login_password.place(relx=0.5, rely=0.4)
    login_button = ctk.CTkButton(master = window, text="Login", command = mail_control)
    login_button.place(relx=0.5, rely=0.5)


def sign_in():
    global mail
    global signin_mail, signin_password, signin_password_again, signin_button, signin_label
    welcome_label.destroy()
    try:
        wrong_mail.destroy()
    except:
        pass

    try:
        wrong_password.destroy()
    except:
        pass

    try:
        login_mail.destroy()
        login_password.destroy()
        login_button.destroy()
        login_label.destroy()
    except:
        pass
    signin_label = ctk.CTkLabel(master=window, text="SIGN IN", font=ctk.CTkFont(size=60, weight="bold"))
    signin_label.place(relx=0.455, rely=0.1)
    signin_mail = ctk.CTkEntry(placeholder_text="Email", master=window)
    signin_mail.place(relx = 0.5, rely = 0.3)
    mail = signin_mail.get()
    signin_password = ctk.CTkEntry(placeholder_text="Password", master=window)
    signin_password.place(relx=0.5, rely=0.4)
    signin_password_again = ctk.CTkEntry(placeholder_text="Password again", master=window)
    signin_password_again.place(relx=0.5, rely=0.5)
    signin_button = ctk.CTkButton(master=window, text="Sign in", command=mail_control)
    signin_button.place(relx=0.5, rely=0.6)
    '''
    entry = ctk.CTkEntry(placeholder_text="Email", master=window)
    entry.place(relx = 0.5, rely = 0.3)
    '''


def home_page():
    try:
        login_mail.destroy()
        login_password.destroy()
        login_button.destroy()
        wrong_password.destroy()
        wrong_mail.destroy()
        sidebar_button_1.destroy()
        sidebar_button_2.destroy()
        login_label.destroy()

    except:
        pass

    try:
        signin_label.destroy()
        signin_button.destroy()
        signin_password_again.destroy()
        signin_password.destroy()
        signin_mail.destroy()
        wrong_password2.destroy()
        wrong_mail.destroy()
    except:
        pass


    look_books = ctk.CTkButton(master=sidebar_frame, text="View of books", command = view_books)
    look_books.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
    borrow_a_book = ctk.CTkButton(master=sidebar_frame, text="Borrow a book")
    borrow_a_book.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
    give_back = ctk.CTkButton(master=sidebar_frame, text="Give back books")
    give_back.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)


def show_value(selected_option):
    global title_label, author_label, publisher_label
    try:
        title_label.destroy()
        author_label.destroy()
        publisher_label.destroy()
    except:
        pass
    print(selected_option)
    with open("library.csv", "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row[1] == selected_option:
                title_label = ctk.CTkLabel(master=window, text=selected_option, font=ctk.CTkFont(size=12))
                title_label.place(relx=0.65, rely=0.25)
                author_label = ctk.CTkLabel(master=window, text=row[0], font=ctk.CTkFont(size=12))
                author_label.place(relx=0.65, rely=0.4)
                publisher_label = ctk.CTkLabel(master=window, text=row[2], font=ctk.CTkFont(size=12))
                publisher_label.place(relx=0.65, rely=0.55)
                page_label = ctk.CTkLabel(master=window, text=row[3], font=ctk.CTkFont(size=12))
                page_label.place(relx=0.65, rely=0.70)


def view_books():
    books_listbox = CTkListbox(master = window, command = show_value, height=300, width=200)
    books_listbox.place(relx = 0.3, rely = 0.1)
    title_label_word1 = ctk.CTkLabel(master=window, text="Book Name", font=ctk.CTkFont(weight="bold"))
    title_label_word1.place(relx = 0.65, rely = 0.20)
    title_label_word2 = ctk.CTkLabel(master=window, text="Book Author", font=ctk.CTkFont(weight="bold"))
    title_label_word2.place(relx = 0.65, rely = 0.35)
    title_label_word3 = ctk.CTkLabel(master=window, text="Published Year", font=ctk.CTkFont(weight="bold"))
    title_label_word3.place(relx = 0.65, rely = 0.50)
    title_label_word4 = ctk.CTkLabel(master=window, text="Pages", font=ctk.CTkFont(weight="bold"))
    title_label_word4.place(relx = 0.65, rely = 0.65)

    i = 0
    with open("library.csv", "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            books_listbox.insert(i, row[1])
            i += 1

def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)


sidebar_frame = ctk.CTkFrame(width = 200,height=500, corner_radius = 0, master = window)
sidebar_frame.grid(row = 0, column = 0, rowspan = 4, sticky = "nsew")
sidebar_frame.grid_rowconfigure(4, weight=1)
sidebar_button_1 = ctk.CTkButton(master = sidebar_frame, command=login,text="Login")
sidebar_button_1.place(relx = 0.5, rely = 0.1, anchor = ctk.CENTER)
sidebar_button_2 = ctk.CTkButton(master=sidebar_frame, command=sign_in, text="Sign in")
sidebar_button_2.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
welcome_label = ctk.CTkLabel(master = window ,text="Welcome", font=ctk.CTkFont(size=60, weight="bold"))
welcome_label.place(relx = 0.59 ,rely=0.5, anchor=ctk.CENTER)
appearance_mode_label = ctk.CTkLabel(sidebar_frame, text="Appearance Mode:", anchor="w")
appearance_mode_label.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)
appearance_mode_optionemenu = ctk.CTkOptionMenu(sidebar_frame, values=["Light", "Dark", "System"],
                                                               command=change_appearance_mode_event)
appearance_mode_optionemenu.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)
appearance_mode_optionemenu.set("Dark")

window.mainloop()