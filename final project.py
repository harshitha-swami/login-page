
import tkinter as tk
import CC as CC

def file_read():
    typing = e_type.get()
    naming = e_file_name.get()
    whole_file = naming + typing
    if whole_file[-4:] == '.txt' and whole_file[0].islower() == True:
        lbl_textbox.configure(text=f'File {whole_file} opened successfully!', fg='yellow', bg='green', font=('Arial', 16, 'bold'))
        lbl_display.configure(state='active')
    else:
        lbl_textbox.configure(text=f'File {whole_file} failed to open successfully!', fg='black', bg='red', font=('Arial', 16, 'bold'))
    return whole_file

def log_in():
    pass

def log_out():
    clear_display()
    lbl_login.configure(state='active')
    lbl_display.configure(state='disable')
    e_username.configure(fg='blue', bg='white')
    e_password.configure(fg='blue', bg='white')
    e_username.delete(0, 'end')
    e_password.delete(0, 'end')

def file_display():
    lbl_display.configure(state='disable')
    lbl_clear.configure(state='active')
    text2.insert('1.0', 'Encrypted Data:')
    text2.insert('2.0', CC.encrypt_or_decrypt(file_read(),'encrypt'))
    file = open(file_read())
    file_text = file.readlines()
    text.insert('1.0', 'Filtered Data:')
    text.insert('2.0', file_text)
    
    file.close()

def clear_display():
    text.delete('1.0', 'end')
    text2.delete('1.0', 'end')

window = tk.Tk()
window.title('DSS - Login Page')
window.geometry('800x600')
window.resizable(True, True)
window.configure(bg='darkgrey')

num_columns = 6
num_rows = 12

for column in range(num_columns):
    window.columnconfigure(column, weight=1)

for row in range(num_rows):
    window.rowconfigure(row, weight=1)

#HEADERS
lbl_header = tk.Label(window, text='Data Security Services\n Schwindull, DeCevem, & Hydette, LLC', width=600, bg='green', fg='yellow', font=('Arial', 24, 'bold'))
lbl_header.grid(row=0, columnspan=7)

lbl_textbox = tk.Label(window, width=600, bg='green')
lbl_textbox.grid(row=4, rowspan=3, columnspan=7, padx=25)

#WIDGET LABELS
lbl_username = tk.Label(window, text="User Name:", font=('Arial', 16, 'bold'), bg='darkgrey')
lbl_username.grid(row=1, column=0, sticky='ns', padx=25)

lbl_password = tk.Label(window, text="Password:", font=('Arial', 16, 'bold'), bg='darkgrey')
lbl_password.grid(row=2, column=0, sticky='ns', padx=25)

lbl_file_name = tk.Label(window, text="File Name:", font=('Arial', 16, 'bold'), bg='darkgrey')
lbl_file_name.grid(row=3, column=0, sticky='ns', padx=25)

lbl_class = tk.Label(window, text="Class:", font=('Arial', 16, 'bold'), bg='darkgrey')
lbl_class.grid(row=2, column=3, sticky='e')

lbl_type = tk.Label(window, text="Type:", font=('Arial', 16, 'bold'), bg='darkgrey')
lbl_type.grid(row=3, column=3, sticky='e')

#ENTRY BOXES
e_username = tk.Entry(window, fg='blue', font=('Arial', 16, 'bold'), width=15)
e_username.grid(row=1, column=1, sticky='w')

e_password = tk.Entry(window, fg='blue', font=('Arial', 16, 'bold'), width=15)
e_password.grid(row=2, column=1, sticky='w')

e_file_name = tk.Entry(window, fg='blue', font=('Arial', 16, 'bold'), width=15)
e_file_name.grid(row=3, column=1, sticky='w')

e_class = tk.Entry(window, fg='blue', font=('Arial', 16, 'bold'), width=8)
e_class.grid(row=2, column=4)

e_type = tk.Entry(window, fg='blue', font=('Arial', 16, 'bold'), width=8)
e_type.grid(row=3, column=4)

#BUTTONS
lbl_login = tk.Button(window, text='Login', font=('Arial', 16, 'bold'), fg='green', command=log_in)
lbl_login.grid(row=1, column=3, sticky='ew',)

lbl_logout = tk.Button(window, text='Log Out', font=('Arial', 16, 'bold'), state='disable', command=log_out)
lbl_logout.grid(row=1, column=4)

lbl_display = tk.Button(window, text='Display', font=('Arial', 16, 'bold'), state='disable', command=file_display)
lbl_display.grid(row=2, column=6, sticky='ew', padx=25)

lbl_clear = tk.Button(window, text='Clear Display', font=('Arial', 16, 'bold'), state='disable', command=clear_display)
lbl_clear.grid(row=3, column=6, sticky='ew', padx=25)

lbl_read = tk.Button(window, text='Read File', font=('Arial', 16, 'bold'), state='active', command=file_read)
lbl_read.grid(row=1, column=6, sticky='ew', padx=25)

lbl_exit = tk.Button(window, text="Exit", font=('Arial', 16, 'bold'))
lbl_exit.grid(row=12, column=0, sticky='ew', padx=25, pady=10)

#TEXTBOXES
frame = tk.Frame(window, bg='lightgrey')
frame.grid(row=7, rowspan=4, column=4, columnspan=4, padx=25)

text = tk.Text(frame, height=10, width=80)
text.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=0, pady=10)

frame2 = tk.Frame(window, width=600, height=200, bg='lightgrey')
frame2.grid(row=7, rowspan=4, column=0, columnspan=4, padx=25)

text2 = tk.Text(frame2, height=10, width=80)
text2.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=0, pady=10)

window.mainloop()
