from tkinter import *
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()

    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)

    return "".join(dec)

def save_encrypt_all():
    title = input_title.get()
    text = input_text.get('1.0', END)
    master_key = input_master_key.get()

    if len(title) == 0 or len(text) == 0 or len(master_key) == 0:
        messagebox.showwarning(title="Warning!", message="Please fill all of boxes...")
    else:
        #encryption
        text_encrypted = encode(master_key, text)

        try:
            #save
            with open("secret.txt", 'a') as data_file:
                data_file.write(f"\n{title}\n{text_encrypted}")

        except FileNotFoundError:
            with open("secret.txt", 'w') as data_file:
                data_file.write(f"\n{title}\n{text_encrypted}")

        finally:
            input_title.delete(0, END)
            input_text.delete('1.0', END)
            input_master_key.delete(0, END)

def decrypt_note():
    text_encrypted = input_text.get('1.0', END)
    master_key = input_master_key.get()

    if len(text_encrypted.strip()) == 0 or len(master_key) == 0:
        messagebox.showwarning(title="Warning!", message="Please fill all of boxes...")
    else:
        try:
            text_decrypted = decode(master_key, text_encrypted.strip())

            input_text.delete('1.0', END)
            input_text.insert('1.0', text_decrypted)

        except:
            messagebox.showwarning(title="Warning!", message="Please don't try do decrypted text to decrypt!")

#UI
FONT = ("Verdana", 15, "normal")
window = Tk()
window.title("Secret Notes")
window.config(padx=25, pady=25)
window.geometry('400x750')
window.resizable(width=False, height=False)

#image
image = PhotoImage(file='TopSecret.png')
image = image.subsample(5, 5)
image_label = Label(image=image, width=250, height=100)
image_label.pack(side = TOP)

#title
title_info_label = Label(text="Enter your title", font=FONT)
title_info_label.pack()

input_title = Entry(width=30)
input_title.pack()

#text
input_info_label = Label(text="Enter your secret", font=FONT)
input_info_label.pack()

input_text = Text(width=45, height=25)
input_text.pack()

#password
master_key_label = Label(text="Enter master key", font=FONT)
master_key_label.pack()

input_master_key = Entry(width=30)
input_master_key.pack()

#button
save_button = Button(text="Save & Encrypt", command=save_encrypt_all)
save_button.pack()

decrypt_button = Button(text="Decrypt", command=decrypt_note)
decrypt_button.pack()

window.mainloop()