import smtplib, csv
from hugchat import hugchat
from CTkMessagebox import CTkMessagebox
from customtkinter import CTk, CTkFrame, CTkEntry, CTkTextbox, CTkComboBox, CTkLabel, CTkButton
from CTkToolTip import *

chatbot_instance = hugchat.ChatBot(cookie_path="./assets/cookie.json")
print(chatbot_instance)
chatbot_instance.switch_llm(6)
id_ = chatbot_instance.new_conversation()
chatbot_instance.change_conversation(id_)

def chatbot():
    user_input = Textbox_1.get("0.0", "end")
    user_input = "write a email's body. " + user_input.lower() + ". Don't use emoji and '**'."
    Textbox_2.delete("0.0", "end")
    response = chatbot_instance.chat(user_input)
    Textbox_2.insert("0.0", response)

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(str(Entry_1.get()), str(Entry_2.get()))
    server.sendmail(str(Entry_1.get()), str(combobox.get()), str(Textbox_2.get("0.0", "end")))
    server.close()
    CTkMessagebox(message="The email is successfully sent!", icon="check", option_1="Thanks")

root = CTk()
root.title("Darius Mail")
root.resizable(0,0)
root.geometry("900x600+40+40")

frame = CTkFrame(root, bg_color="black", fg_color="black")
frame.pack(fill="both", expand=1)

filename = r'./Database/contacts.csv'

emails = []

with open(filename, mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        email = row['email']
        
        if email:
            emails.append(email)

combobox = CTkComboBox(master=frame, height=30, width=300, fg_color="black", values=emails, border_width=1, border_color="blue", dropdown_fg_color="black", button_hover_color="dark blue", button_color="blue")
combobox.place(x=45, y=120)

tooltip_cb = CTkToolTip(combobox, message="Receiver's Email ID")

with open(r"./Database/owners.csv", mode='r') as file:
   reader = csv.reader(file)
   for row in reader:
      name, email, password = row

Entry_1 = CTkEntry(master=frame, height=30, width=300, fg_color="black", border_width=1, border_color="blue", placeholder_text="sender's email id")
Entry_1.place(x=45, y=30)

tooltip_e1 = CTkToolTip(Entry_1, message="Sender's Email ID")

Entry_2 = CTkEntry(master=frame, height=30, width=300, fg_color="black", border_width=1, border_color="blue", placeholder_text="Password")
Entry_2.place(x=45, y=70)

tooltip_e2 = CTkToolTip(Entry_2, message="App Password")

Entry_1.insert(0, email)
Entry_2.insert(0, password)

Textbox_1 = CTkTextbox(master=frame, height=90, width=450, fg_color="black", border_width=1, border_color="blue")
Textbox_1.place(x=400, y=60)

tooltip_1 = CTkToolTip(Textbox_1, message="Tell Darius what you want to write.")

label = CTkLabel(master=frame, bg_color="black", fg_color="black", text="What DARIUS should write?")
label.place(x=400, y=30)

Textbox_2 = CTkTextbox(master=frame, height=350, width=800, fg_color="black", border_width=1, border_color="blue")
Textbox_2.place(x=50, y=190)

tooltip_2 = CTkToolTip(Textbox_2, message="Your Email")

Button_gen = CTkButton(master=frame, fg_color="black", hover_color="dark blue", text="Generate ✧˚₊‧", corner_radius=50, border_width=1, border_color="blue")
Button_gen.place(x=700, y=20)
Button_gen.configure(command=chatbot)

Button_ = CTkButton(master=frame, fg_color="black", hover_color="dark blue", text="Send", corner_radius=50, border_width=1, border_color="blue")
Button_.place(x=(900/2)-100, y=550)
Button_.configure(command=sendEmail)


root.mainloop()
