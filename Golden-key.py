from tkinter import *
import customtkinter
import os
import csv
from hashlib import sha224, sha384, sha512, md5, sha256
from tkinter import filedialog as fd
import tkinter as tk


def select_file():
    global fin
    fieltype = (('text files', '*.txt'), ('All files', False))
    fin = fd.askopenfilename(title='Select a file', initialdir='/', filetypes=fieltype)
    file_loead.place(x=1129, y=240)


def find_file_select():
    global find_fin
    fieltype = (('text files', '*.csv'), ('All files', False))
    find_fin =fd.askopenfilename(title='select a CSV file',initialdir='/', filetypes=fieltype)
    print(find_fin)


def finding():
    search = f_entry.get()


    
    with open(find_fin , 'r') as csvfile :
        reader = csv.reader(csvfile)
        for line in reader:
            if search in line[0]:
                print(line[0])
                result_entry.insert(line[0])

            

def num_start():
    if num_v.get() == 1:

        try:

            x = int(num_entry.get()) + 1
            with open('number hashed 224.csv', 'a', newline='', encoding='UTF8') as f:
                writer = csv.writer(f, delimiter=':')
                passhash = ["Pass", "Hash"]
                writer.writerow(passhash)
                for i in range(1, x):
                    pas = str(i)
                    in_pass = pas.encode()
                    out_pass = sha224(in_pass).hexdigest()
                    out_pass.rstrip()
                    to_csv = [i, out_pass]
                    writer.writerow(to_csv)
                    print(to_csv)
            print("Done")
            fut = os.getcwd()
            os.system('explorer  "%s"'%fut)

        except:
            error_num_1.place(x=430, y=230)

    elif num_v.get() == 2:

        try:
            x = int(num_entry.get()) + 1


            with open('number hashed 256.csv', 'a', newline='', encoding='UTF8') as f:
                writer = csv.writer(f, delimiter=':')
                passhash = ["Pass", "Hash"]
                writer.writerow(passhash)
                for i in range(1, x):
                    pas = str(i)
                    in_pass = pas.encode()
                    out_pass = sha256(in_pass).hexdigest()
                    out_pass.rstrip()
                    to_csv = [i, out_pass]
                    writer.writerow(to_csv)
                    print(to_csv)
            print("Done")
            fut = os.getcwd()
            os.system('explorer  "%s"'%fut)

        except:
            error_num_1.place(x=430, y=230)

    elif num_v.get() == 3:
        try:
            x = int(num_entry.get()) + 1


            with open('number hashed 384.csv', 'a', newline='', encoding='UTF8') as f:
                writer = csv.writer(f, delimiter=':')
                passhash = ["Pass", "Hash"]
                writer.writerow(passhash)
                for i in range(1, x):
                    pas = str(i)
                    in_pass = pas.encode()
                    out_pass = sha384(in_pass).hexdigest()
                    out_pass.rstrip()
                    to_csv = [i, out_pass]
                    writer.writerow(to_csv)
                    print(to_csv)
            print("Done")
            fut = os.getcwd()
            os.system('explorer  "%s"'%fut)

        except:
            error_num_1.place(x=430, y=230)

    elif num_v.get() == 4:
        try:
            x = int(num_entry.get()) + 1
            with open('number hashed 512.csv', 'a', newline='', encoding='UTF8') as f:
                writer = csv.writer(f, delimiter=':')
                passhash = ["Pass", "Hash"]
                writer.writerow(passhash)
                for i in range(1, x):
                    pas = str(i)
                    in_pass = pas.encode()
                    out_pass = sha512(in_pass).hexdigest()
                    out_pass.rstrip()
                    to_csv = [i, out_pass]
                    writer.writerow(to_csv)
                    print(to_csv)

            print("Done")
            fut = os.getcwd()
            os.system('explorer  "%s"'%fut)

        except:
            error_num_1.place(x=430, y=230)

    elif num_v.get() == 5:
        try:
            x = int(num_entry.get()) + 1


            with open('number hashed md5.csv', 'a', newline='', encoding='UTF8') as f:
                writer = csv.writer(f, delimiter=':')
                passhash = ["Pass", "Hash"]
                writer.writerow(passhash)
                for i in range(1, x):
                    pas = str(i)
                    in_pass = pas.encode()
                    out_pass = md5(in_pass).hexdigest()
                    out_pass.rstrip()
                    to_csv = [i, out_pass]
                    writer.writerow(to_csv)
                    print(to_csv)

            print("Done")
            fut = os.getcwd()
            os.system('explorer  "%s"'%fut)

        except:
            error_num_1.place(x=430, y=230)


def pass_start():
    if pass_v.get() == 1:
        with open(fin, 'r') as paslist:
            reader = csv.reader(paslist)
            for row in reader:
                if row:
                    word = row[0]
                    hash_obj = sha224(word.encode())
                    hex_dig = hash_obj.hexdigest()
                    out_put = [[word, hex_dig]]
                    print(out_put)
                    with open("password hashed 224.csv", mode='a', newline='') as f:
                        writer = csv.writer(f, delimiter=':')
                        for inner_pass in out_put:
                            writer.writerow(inner_pass)
                        f.close()
                    fut = os.getcwd()
                    os.system('explorer  "%s"' % fut)

    elif pass_v.get() == 2:
        with open(fin, 'r') as paslist:
            reader = csv.reader(paslist)
            for row in reader:
                if row:
                    word = row[0]
                    hash_obj = sha256(word.encode())
                    hex_dig = hash_obj.hexdigest()
                    out_put = [[word, hex_dig]]
                    print(out_put)
                    with open("hashpass/pass hashed 256.csv", mode='a', newline='') as f:
                        writer = csv.writer(f, delimiter=':')
                        for inner_pass in out_put:
                            writer.writerow(inner_pass)
                        f.close()
                    fut = os.getcwd()
                    os.system('explorer  "%s"' % fut)

    elif pass_v.get() == 3:

        with open(fin, 'r') as paslist:
            reader = csv.reader(paslist)
            for row in reader:
                if row:
                    word = row[0]
                    hash_obj = sha384(word.encode())
                    hex_dig = hash_obj.hexdigest()
                    out_put = [[word, hex_dig]]
                    print(out_put)
                    with open("pass hashed 384.csv", mode='a', newline='') as f:
                        writer = csv.writer(f, delimiter=':')
                        for inner_pass in out_put:
                            writer.writerow(inner_pass)
                        f.close()
                    fut = os.getcwd()
                    os.system('explorer  "%s"' % fut)

    elif pass_v.get() == 4:
        with open(fin, 'r') as paslist:
            reader = csv.reader(paslist)
            for row in reader:
                if row:
                    word = row[0]
                    hash_obj = sha512(word.encode())
                    hex_dig = hash_obj.hexdigest()
                    out_put = [[word, hex_dig]]
                    print(out_put)
                    with open("pass hashed 512.csv", mode='a', newline='') as f:
                        writer = csv.writer(f, delimiter=':')
                        for inner_pass in out_put:
                            writer.writerow(inner_pass)
                        f.close()
                    fut = os.getcwd()
                    os.system('explorer  "%s"' % fut)

    elif pass_v.get() == 5:
        with open(fin, 'r') as paslist:
            reader = csv.reader(paslist)
            for row in reader:
                if row:
                    word = row[0]
                    hash_obj = md5(word.encode())
                    hex_dig = hash_obj.hexdigest()
                    out_put = [[word, hex_dig]]
                    print(out_put)
                    with open("pass hashed md5.csv", mode='a', newline='') as f:
                        writer = csv.writer(f, delimiter=':')
                        for inner_pass in out_put:
                            writer.writerow(inner_pass)
                        f.close()
                    fut = os.getcwd()
                    os.system('explorer  "%s"' % fut)



def root():
    global num_entry
    global progressbar1
    global error_num_1
    global file_loead
    global num_v
    global pass_v
    global result_entry
    global paste_find
    global f_entry
    global result_entry
    root = customtkinter.CTk()
    root.title("Golden Key developed by NUC")
    root.iconbitmap('Golden-key-main\icon.ico')
    root.geometry("1440x800")
    root.resizable(width=False, height=False)
    customtkinter.deactivate_automatic_dpi_awareness()
    root.config(bg='#041C32')

    bg2 = customtkinter.CTkLabel(root, text="", fg_color="#04293A", bg_color='#041C32', width=1320, height=620,
                                 corner_radius=37)
    bg2.place(x=60, y=100)

    twin_bg2 = customtkinter.CTkLabel(root, text="", bg_color="#04293A", fg_color="#064663", width=500, height=380,
                                      corner_radius=37)
    twin_bg2.place(x=820, y=170)



    ######----------HEADER AND FOOTER-------#######

    golden_text = Label(root, text="Golden key", bg="#041C32", fg="#ECB365", font=("Airstrike Platinum", 56))
    golden_text.place(x=475, y=5)
    NUC_text = Label(root, text="NUC", bg="#041C32", fg="#ECB365", font=("Airstrike Platinum", 56))
    NUC_text.place(x=630, y=720)
    progressbar1 = customtkinter.CTkProgressBar(root, mode='indetermiante', width=450, indeterminate_speed=1,
                                                fg_color="#041C32", progress_color="#ECB365")
    progressbar1.place(x=490, y=80)
    progressbar1.start()
    progressbar2 = customtkinter.CTkProgressBar(root, mode='indetermiante', width=160, indeterminate_speed=1,
                                                fg_color="#041C32", progress_color="#ECB365")
    progressbar2.place(x=630, y=790)
    progressbar2.start()

    #####----------PASS TO HASH-------#######

    pass_text = Label(root, text="Passworld's List To Hash", bg="#04293A", fg="#ECB365", font=("Anaheim", 25))
    pass_text.place(x=895, y=110)
    file_text = Label(root, text="Please select file : ", bg="#064663", fg="#ECB365", font=("Anaheim", 25))
    file_text.place(x=850, y=190)
    fin_btn = customtkinter.CTkButton(root, text="SELECT"
                                      , corner_radius=50
                                      , height=40, width=130
                                      , command=select_file
                                      , fg_color="#ECB365"
                                      , bg_color="#064663"
                                      , font=("Anaheim", 25)
                                      , text_color="#000000"
                                      , hover="Flase")
    fin_btn.place(x=1145, y=195)

    sha_mode_file_text = Label(root, text="sha224\nsha256\nsha384\nsha512\nmd5   ", bg="#064663", fg="#ECB365",
                               font=("Anaheim", 25))
    sha_mode_file_text.place(x=850, y=260)
    file_loead = Label(root, text="File loaded successfully", bg="#064663", fg="#ECB365", font=("Anaheim", 12))
    pass_v = tk.IntVar()

    pass_radio_button1 = customtkinter.CTkRadioButton(root, text="224", bg_color="#064663", text_color="#ECB365",
                                                      font=("Anaheim", 25), variable=pass_v, value=1).place(x=1175,
                                                                                                            y=271)
    pass_radio_button2 = customtkinter.CTkRadioButton(root, text="256", bg_color="#064663", text_color="#ECB365",
                                                      font=("Anaheim", 25), variable=pass_v, value=2).place(x=1175,
                                                                                                            y=312)
    pass_radio_button3 = customtkinter.CTkRadioButton(root, text="384", bg_color="#064663", text_color="#ECB365",
                                                      font=("Anaheim", 25), variable=pass_v, value=3).place(x=1175,
                                                                                                            y=352)
    pass_radio_button4 = customtkinter.CTkRadioButton(root, text="512", bg_color="#064663", text_color="#ECB365",
                                                      font=("Anaheim", 25), variable=pass_v, value=4).place(x=1175,
                                                                                                            y=395)
    pass_radio_button5 = customtkinter.CTkRadioButton(root, text="md", bg_color="#064663", text_color="#ECB365",
                                                      font=("Anaheim", 25), variable=pass_v, value=5).place(x=1175,
                                                                                                            y=440)

    pass_btn = customtkinter.CTkButton(root, text="Generate"
                                       , corner_radius=50
                                       , height=40, width=130
                                       , command=pass_start
                                       , fg_color="#ECB365"
                                       , bg_color="#064663"
                                       , font=("Anaheim", 25)
                                       , text_color="#000000"
                                       , hover="Flase")

    pass_btn.place(x=1000, y=483)

    #####----------NUMBER TO HASH-------#######

    twin_bg1 = customtkinter.CTkLabel(root, text="", bg_color="#04293A", fg_color="#064663", width=500, height=380,
                                      corner_radius=37)
    twin_bg1.place(x=120, y=170)
    num_text = Label(root, text="Generate Pin Code To hash", bg="#04293A", fg="#ECB365", font=("Anaheim", 25))
    num_text.place(x=180, y=110)
    sha_mode_file_text = Label(root, text="sha224\nsha256\nsha384\nsha512\nmd5   ", bg="#064663", fg="#ECB365",
                               font=("Anaheim", 25))
    sha_mode_file_text.place(x=150, y=260)
    num_v = tk.IntVar()
    num_radio_button1 = customtkinter.CTkRadioButton(root, text="224", bg_color="#064663", text_color="#ECB365",
                                                     font=("Anaheim", 25), variable=num_v, value=1).place(x=480, y=271)
    num_radio_button2 = customtkinter.CTkRadioButton(root, text="256", bg_color="#064663", text_color="#ECB365",
                                                     font=("Anaheim", 25), variable=num_v, value=2).place(x=480, y=312)
    num_radio_button3 = customtkinter.CTkRadioButton(root, text="384", bg_color="#064663", text_color="#ECB365",
                                                     font=("Anaheim", 25), variable=num_v, value=3).place(x=480, y=352)
    num_radio_button4 = customtkinter.CTkRadioButton(root, text="512", bg_color="#064663", text_color="#ECB365",
                                                     font=("Anaheim", 25), variable=num_v, value=4).place(x=480, y=395)
    num_radio_button5 = customtkinter.CTkRadioButton(root, text="md", bg_color="#064663", text_color="#ECB365",
                                                     font=("Anaheim", 25), variable=num_v, value=5).place(x=480, y=440)
    error_num_1 = Label(root, text="Please Enter number", bg="#064663", fg="#ECB365", font=("Anaheim", 12))
    num_much = Label(root, text=" How many ?", bg="#064663", fg="#ECB365", font=("Anaheim", 25))
    num_much.place(x=139, y=190)
    num_entry = customtkinter.CTkEntry(root, placeholder_text="Enter number", bg_color="#064663", fg_color="#ECB365",
                                       text_color="#000000", placeholder_text_color="#000000")
    num_entry.place(x=430, y=205)
    num_btn = customtkinter.CTkButton(root, text="Generate"
                                      , corner_radius=50
                                      , height=40, width=130
                                      , command=num_start
                                      , fg_color="#ECB365"
                                      , bg_color="#064663"
                                      , font=("Anaheim", 25)
                                      , text_color="#000000"
                                      , hover="Flase")
    num_btn.place(x=300, y=483)

###### ----- FIND TABLE ------- ######
    Find_bg = customtkinter.CTkLabel(root, text="", bg_color="#04293A", fg_color="#064663", width=1200, height=140,
                                      corner_radius=37)
    Find_bg.place(x=120 , y=560)
    file_text = Label(root, text="Please select file : ", bg="#064663", fg="#ECB365", font=("Anaheim", 20))
    file_text.place(x=150, y=570)
    find_fin_btn = customtkinter.CTkButton(root, text="SELECT"
                                      , corner_radius=50
                                      , height=30, width=70
                                      , command=find_file_select
                                      , fg_color="#ECB365"
                                      , bg_color="#064663"
                                      , font=("Anaheim", 20)
                                      , text_color="#000000"
                                      , hover="Flase").place(x=400, y= 576)

    paste_find = Label(root, text="Please Paste Hash : ", bg="#064663", fg="#ECB365", font=("Anaheim", 20))
    paste_find.place(x=150, y=630)

    f_entry = customtkinter.CTkEntry(root, placeholder_text="Paste Hash (CTRL + V)", bg_color="#064663", fg_color="#ECB365",
                                       text_color="#000000", placeholder_text_color="#000000",width=150)
    f_entry.place(x=390, y=640)


    find_hash = customtkinter.CTkButton(root , text="Find", corner_radius=50
                                      , height=30, width=70
                                      , command=finding
                                      , fg_color="#ECB365"
                                      , bg_color="#064663"
                                      , font=("Anaheim", 20)
                                      , text_color="#000000"
                                      , hover="Flase").place(x=680, y= 610)


    result = Label(root, text="Result : ", bg="#064663", fg="#ECB365", font=("Anaheim", 20))
    result.place(x=1019, y=575)

    result_entry = customtkinter.CTkTextbox(root, bg_color="#064663", fg_color="#ECB365",width=420, height=20,border_width=1,border_color='#04293A').place(x=860, y=630)

    root.mainloop()


root()
