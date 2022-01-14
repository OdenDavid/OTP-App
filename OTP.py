import tkinter as tk
from tkinter import ttk
import json

#=========================Main Window=============================
class App:
    def __init__(self, master):
        w = 900 # window width
        h = 500 # window height

        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen    

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) 

        master.iconbitmap("icon.ico")
        self.master = master
        self.master.title("OTP")
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.master.configure(background="#ffffff")
        self.master.resizable(False,False)

        self.image1 = tk.PhotoImage(file="background2.png")
        self.background_lbl = tk.Label(self.master,image=self.image1,relief='flat',bd=0)
        self.background_lbl.place(relx=0.5,rely=0)

        self.twilio_lbl = tk.Label(self.master,text='Twilio',font=('poppins',18,'bold'), fg='#2ae5d8',bg='#ffffff')
        self.twilio_lbl.place(relx=0.095,rely=0.05)
        self.sms_lbl = tk.Label(self.master,text='SMS',font=('poppins',13,'bold'), bg='#ffffff')
        self.sms_lbl.place(relx=0.175,rely=0.064)

        self.signin_lbl = tk.Label(self.master,text='Sign Up',font=('poppins',20,'bold'), bg='#ffffff')
        self.signin_lbl.place(relx=0.095,rely=0.25)

        self.signin_lbl = tk.Label(self.master,text='Lets get you started to receive your OTP',font=('poppins',12), fg='#6b6b6b',bg='#ffffff')
        self.signin_lbl.place(relx=0.095,rely=0.32)

        #-------Country code---------
        json_data = open("country_dial_info.json")
        data = json.load(json_data)

        countries = []
        codes = []
        for item in data:
            countries.append(item['name'])
            codes.append(item['dial_code'])
        self.country = ttk.Combobox(self.master,width=30,font=("poppins",10))
        self.country['values'] = (countries)                        
        self.country.insert(0,"Nigeria")
        self.country.place(relx=0.095,rely=0.45,width=275,height=30)

        self.country_lbl = tk.Label(self.master, text="Enter your country", font=('poppins',9,'bold'),bg='#ffffff')
        self.country_lbl.place(relx=0.094,rely=0.41)

        self.code_lbl = tk.Label(self.master, text='+234', font=('poppins',9),relief='groove',bd=1)
        self.code_lbl.place(relx=0.095,rely=0.567,width=40,height=30)
        self.phone = tk.Entry(self.master,width=30,font=("poppins",10),fg='#6b6b6b',bd=2,relief='groove')
        self.phone.place(relx=0.14,rely=0.57,width=237,height=29)
        self.phone_lbl = tk.Label(self.master, text="Enter your phone number", font=('poppins',9,'bold'),bg='#ffffff')
        self.phone_lbl.place(relx=0.095,rely=0.535)
        # Place Holder for text widget
        self.phone.insert(tk.END,'81-5454-9452')
        self.phone.bind("<FocusIn>", lambda args: (self.phone.delete("0",tk.END),self.phone.configure(fg='#000000')))
        self.phone.bind("<FocusOut>", lambda args: (self.phone.insert(tk.END,'81-5454-9452'),self.phone.configure(fg='#6b6b6b')))
        
        def selected(event):
            value = event.widget.get()
            index = countries.index(value)
            self.code_lbl.configure(text=codes[index])
        self.country.bind("<<ComboboxSelected>>", selected)

        self.code1 = tk.Entry(self.master,font=("poppins",10),fg='#6b6b6b',bd=2,relief='groove').place(relx=0.14,rely=0.68,width=30,height=40)

        self.send_btn = tk.Button(self.master, text="Send OTP", fg='#ffffff',font=('poppins',11,'bold'),bg='#2ae5d8',relief='groove',bd=0,width=30,height=1,activebackground='#2ae5d8',activeforeground='#ffffff')
        self.send_btn.place(relx=0.095,rely=0.7)

if __name__=='__main__':
    root = tk.Tk() 

    app = App(root)
    
    root.mainloop()