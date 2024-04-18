import customtkinter as ctk
from builtins import *
import re
import csv
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
                    login_label.destroy()
                    wrong_password.destroy()
                except:
                    pass
                home_page()
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
                if "@admin.ad.com" in mail:
                    admin_panel()
                    quit()
                with open("users.csv", "r")as f:
                    reader = csv.reader(f, delimiter=",")
                    for row in reader:
                        if row[0] == mail:
                            password_control()

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


def admin_panel():
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
        login_label.destroy()
        signin_label.destroy()
        signin_button.destroy()
        signin_password_again.destroy()
        signin_password.destroy()
        signin_mail.destroy()
        wrong_password2.destroy()
        wrong_mail.destroy()
    except:
        pass

    add_books = ctk.CTkButton(master=sidebar_frame, text="Add book", command=lambda: add_book())
    add_books.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
    remove_books = ctk.CTkButton(master=sidebar_frame, text="Revome book", command=lambda: remove_book())
    remove_books.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)


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


    look_books = ctk.CTkButton(master=sidebar_frame, text="View of books", command = lambda: view_books(0))
    look_books.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
    borrow_a_book = ctk.CTkButton(master=sidebar_frame, text="Borrow a book", command = lambda: view_books(1))
    borrow_a_book.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
    give_back = ctk.CTkButton(master=sidebar_frame, text="Give back books", command = give_back_book)
    give_back.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)


global selected_option


def show_value(selected_option):
    global title_label, author_label, publisher_label, page_label
    global row0, row1, row2, row3, row_index
    try:
        title_label.destroy()
        author_label.destroy()
        publisher_label.destroy()
    except:
        pass
    print(selected_option)
    with open("library.csv", "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        row_index = 0
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
                row0 = row[0]
                row1 = row[1]
                row2 = row[2]
                row3 = row[3]
                break
            row_index += 1


def view_books(a):
    global borrow_button, books_listbox
    try:
        borrow_button.destroy()
        borrow_label.destroy()
        title_label.destroy()
        author_label.destroy()
        publisher_label.destroy()
        page_label.destroy()
    except:
        pass

    if a == 0:
        pass
    elif a == 1:
        borrow_button = ctk.CTkButton(master = window, text = "Borrow a book", command = borrow_book)
        borrow_button.place(relx = 0.65, rely = 0.80)

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
    '''
    search_str = StringVar()
    search_bar = Entry(master=window, textvariable=search_str, width=38)
    search_bar.place(relx = 0.3, rely = 0.80)
    '''
    i = 0
    with open("library.csv", "r", newline = "") as f:
        reader = csv.reader(f, delimiter = ",")
        for row in reader:
            books_listbox.insert(i, row[1])
            i += 1


def borrow_book():
    global title_label, author_label, publisher_label, page_label, borrow_label
    try:
        borrow_label.destroy()
        title_label.destroy()
        author_label.destroy()
        publisher_label.destroy()
        page_label.destroy()
        give_back_button.destroy()
    except:
        pass
    with open("borrow_books.csv", "a", newline = "") as f:
        writer = csv.writer(f, delimiter = ",")
        borrow_list = [row0, row1, row2, row3, row_index, mail]
        writer.writerow(borrow_list)

    with open("library.csv", "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)

    del data[row_index]

    with open("library.csv", "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(data)

    borrow_label= ctk.CTkLabel(master = window, text = row1 + " was borrowed")
    borrow_label.place(relx = 0.65, rely = 0.90)


def give_back_book():
    global mail_listbox
    try:
        title_label.destroy()
        author_label.destroy()
        publisher_label.destroy()
        borrow_button.destroy()
        books_listbox.destroy()
        borrow_label.destroy()
        page_label.destroy()
    except:
        pass

    mail_listbox = CTkListbox(master=window, height=300, width=200, command = give_back_book_list)
    mail_listbox.place(relx=0.3, rely=0.1)
    title_label_word1 = ctk.CTkLabel(master=window, text="Book Name", font=ctk.CTkFont(weight="bold"))
    title_label_word1.place(relx = 0.65, rely = 0.20)
    title_label_word2 = ctk.CTkLabel(master=window, text="Book Author", font=ctk.CTkFont(weight="bold"))
    title_label_word2.place(relx = 0.65, rely = 0.35)
    title_label_word3 = ctk.CTkLabel(master=window, text="Published Year", font=ctk.CTkFont(weight="bold"))
    title_label_word3.place(relx = 0.65, rely = 0.50)
    title_label_word4 = ctk.CTkLabel(master=window, text="Pages", font=ctk.CTkFont(weight="bold"))
    title_label_word4.place(relx = 0.65, rely = 0.65)
    i = 0
    with open("borrow_books.csv", "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row[-1] == mail:
                mail_listbox.insert(i, row[1])
                i += 1


def give_back_book_list(select_option):
    global title_label, author_label, publisher_label, page_label, borrow_label, borrow_index
    global give_back_button
    global row1, row2, row3, row0, borrow_index
    try:
        title_label.destroy()
        author_label.destroy()
        publisher_label.destroy()
        borrow_button.destroy()
        books_listbox.destroy()
        borrow_label.destroy()
        page_label.destroy()
    except:
        pass
    with open("borrow_books.csv", "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        borrow_index = 0
        for row in reader:
            if row[1] == select_option:
                title_label = ctk.CTkLabel(master=window, text=row[1], font=ctk.CTkFont(size=12))
                title_label.place(relx=0.65, rely=0.25)
                author_label = ctk.CTkLabel(master=window, text=row[0], font=ctk.CTkFont(size=12))
                author_label.place(relx=0.65, rely=0.4)
                publisher_label = ctk.CTkLabel(master=window, text=row[2], font=ctk.CTkFont(size=12))
                publisher_label.place(relx=0.65, rely=0.55)
                page_label = ctk.CTkLabel(master=window, text=row[3], font=ctk.CTkFont(size=12))
                page_label.place(relx=0.65, rely=0.70)
                row0 = row[0]
                row1 = row[1]
                row2 = row[2]
                row3 = row[3]
                break
            borrow_index += 1
    give_back_button = ctk.CTkButton(master=window, text="Borrow a book", command = give_back_book_pressed)
    give_back_button.place(relx=0.65, rely=0.80)


def give_back_book_pressed():
    global give_back_label, give_back_data
    try:
        give_back_label.destroy()
    except:
        pass

    with open("borrow_books.csv", "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)

    give_back_index = int(data[borrow_index][4])
    data0 = data[borrow_index][0]
    data1 = data[borrow_index][1]
    data2 = data[borrow_index][2]
    data3 = data[borrow_index][3]
    mini_liste = [data0, data1, data2, data3]

    with open("borrow_books.csv", "r", newline="") as f:
        reader1 = csv.reader(f)
        data = list(reader1)

    del data[borrow_index]

    with open("borrow_books.csv", "w", newline="") as f:
        writer1 = csv.writer(f, delimiter=",")
        writer1.writerows(data)

    with open("library.csv", "a", newline="") as f:
        writer2 = csv.writer(f)
        writer2.writerow(mini_liste)

    give_back_label = ctk.CTkLabel(master = window, text = row1 + " was returned")
    give_back_label.place(relx = 0.65, rely = 0.90)
    give_back_book()


def add_book():
    global search1, search2, search3, search4
    global label1, label2, label3, label4, search1, search2, search3, search4
    global add_book_button

    try:
        name_search.destroy()
        name_label.destroy()
        delete_book_button.destroy()
    except:
        pass

    label1 = ctk.CTkLabel(master=window, text="Book name:")
    label1.place(relx = 0.3, rely = 0.25)
    search1 = ctk.CTkEntry(master=window, width=200)
    search1.place(relx = 0.42, rely = 0.25)
    label2 = ctk.CTkLabel(master=window, text="Book author:")
    label2.place(relx = 0.3, rely = 0.35)
    search2 = ctk.CTkEntry(master=window, width=200)
    search2.place(relx = 0.42, rely = 0.35)
    label3 = ctk.CTkLabel(master=window, text="Year published:")
    label3.place(relx = 0.3, rely = 0.45)
    search3 = ctk.CTkEntry(master=window, width=200)
    search3.place(relx = 0.42, rely = 0.45)
    label4 = ctk.CTkLabel(master=window, text="Book pages:")
    label4.place(relx = 0.3, rely = 0.55)
    search4 = ctk.CTkEntry(master=window, width=200)
    search4.place(relx = 0.42, rely = 0.55)
    add_book_button = ctk.CTkButton(master=window, text="Add Book", width=200, command=lambda: add_book_pressed())
    add_book_button.place(relx=0.42, rely=0.65)


def add_book_pressed():
    global add_book_label
    try:
        add_book_label.destroy()
    except:
        pass

    add_book_label = ctk.CTkLabel(master=window, text=search1.get() + " was added")
    add_book_label.place(relx=0.3, rely=0.75)

    add_book_list = [search2.get(), search1.get(), search3.get(), search4.get()]
    print(add_book_list)
    with open("library.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(add_book_list)


def remove_book():
    global name_search, name_label, delete_book_button
    try:
        label1.destroy()
        label2.destroy()
        label3.destroy()
        label4.destroy()
        search1.destroy()
        search2.destroy()
        search3.destroy()
        search4.destroy()
        add_book_button.destroy()
        add_book_label.destroy()
    except:
        pass

    name_label = ctk.CTkLabel(master=window, text="Name of the book to be deleted")
    name_label.place(relx = 0.3, rely = 0.25)
    name_search = ctk.CTkEntry(master=window, width=200)
    name_search.place(relx = 0.3, rely = 0.35)
    delete_book_button = ctk.CTkButton(master=window, text="Delete Book", width=200, command= lambda: remove_book_pressed())
    delete_book_button.place(relx=0.3, rely=0.45)


def remove_book_pressed():
    with open("library.csv", "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        data = []

        remove_index = 0
        for row in reader:
            if name_search.get().lower() == row[1].lower():
                remove_book_label = ctk.CTkLabel(master=window, text=name_search.get() + " was deleted")
                remove_book_label.place(relx=0.3, rely=0.55)
                continue

            data.append(row)
            remove_index += 1

    with open("library.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)




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