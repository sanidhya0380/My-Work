import base64
from tkinter import messagebox
from tkinter import *

def encrypt():
    password = code.get()

    if password == "1234":
        message = text1.get(1.0, "end-1c")
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypted_message = base64_bytes.decode("ascii")
        result_text.delete(1.0, END)
        result_text.insert(END, "Encrypted Message:\n" + encrypted_message)
    else:
        messagebox.showerror("Error", "Incorrect password")

def decrypt():
    password = code.get()

    if password == "1234":
        decrypted_message = text1.get(1.0, "end-1c")
        try:
            base64_bytes = base64.b64decode(decrypted_message)
            decrypted_message = base64_bytes.decode("ascii")
            # Display the decrypted message in a label (assuming 'result_label' is a Label widget)
            result_text.delete(1.0, END)
            result_text.insert(END, "Decrypted Message:\n" + decrypted_message)
        except base64.binascii.Error:
            messagebox.showerror("Error", "Invalid base64-encoded message")
    else:
        messagebox.showerror("Error", "Incorrect password")

root = Tk()

#GUI
def reset():
        code.set("")
        text1.delete(1.0,END)

root.title("Encryption ")
root.geometry("375x500")



Label(text="Enter the Text or Encrypted data",fg="black",font=("calbri",13)).place(x=10,y=10)
text1 = Text(font="Robote 20",bg="white", relief=GROOVE,wrap=WORD,bd=0)
text1.place(x=10,y=50,width=355,height=100)
Label(text="Enter the secret Key",fg="black",font=("calibri",13)).place(x=10,y=170)

code=StringVar()
Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

encrypt_button = Button(root,text="Encrypt",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
decrypt_button = Button(root,text="Decrypt",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)

Label(text="Output",fg="black",font=("calbri",13)).place(x=10,y=350)

result_text = Text(root, font=("Robote", 20), bg="white", relief=GROOVE, bd=0)
result_text.place(x=10, y=375, width=355, height=100)
result_text.config(state=NORMAL)

root.mainloop()
