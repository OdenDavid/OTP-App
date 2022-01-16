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
        self.phone = tk.Entry(self.master,width=30,font=("poppins",10),fg='#000000',bd=2,relief='groove')
        self.phone.place(relx=0.14,rely=0.57,width=237,height=29)
        self.phone_lbl = tk.Label(self.master, text="Enter your phone number", font=('poppins',9,'bold'),bg='#ffffff')
        self.phone_lbl.place(relx=0.095,rely=0.535)
        
        
        def selected(event):
            value = event.widget.get()
            index = countries.index(value)
            self.code_lbl.configure(text=codes[index])
        self.country.bind("<<ComboboxSelected>>", selected)
        
        def send():
            
            def change(*args,**kwargs):
                if number1.get() != "" and isinstance(int(number1.get()), int):
                    self.code2.focus()
                if number2.get() != "" and isinstance(int(number2.get()), int):
                    self.code3.focus()
                if number3.get() != "" and isinstance(int(number3.get()), int):
                    self.code4.focus()
                if number4.get() != "" and isinstance(int(number4.get()), int):
                    self.code5.focus()
                if number5.get() != "" and isinstance(int(number5.get()), int):
                    self.code6.focus()
                if number6.get() != "" and isinstance(int(number6.get()), int):
                    self.send_btn.focus()
            
            number1 = tk.StringVar()
            number2 = tk.StringVar()
            number3 = tk.StringVar()
            number4 = tk.StringVar()
            number5 = tk.StringVar()
            number6 = tk.StringVar()

            number1.trace("w", lambda l, idx, mode: change())
            number2.trace("w", lambda l, idx, mode: change())
            number3.trace("w", lambda l, idx, mode: change())
            number4.trace("w", lambda l, idx, mode: change())
            number5.trace("w", lambda l, idx, mode: change())
            number6.trace("w", lambda l, idx, mode: change())

            self.code1 = tk.Entry(self.master,font=("poppins",13,'bold'),textvariable=number1,bd=2,relief='groove')
            self.code1.place(relx=0.095,rely=0.68,width=30,height=40)
            self.code1.focus()
            self.code2 = tk.Entry(self.master,font=("poppins",13,'bold'),textvariable=number2,bd=2,relief='groove')
            self.code2.place(relx=0.15,rely=0.68,width=30,height=40)
            self.code3 = tk.Entry(self.master,font=("poppins",13,'bold'),textvariable=number3,bd=2,relief='groove')
            self.code3.place(relx=0.205,rely=0.68,width=30,height=40)
            self.code4 = tk.Entry(self.master,font=("poppins",13,'bold'),textvariable=number4,bd=2,relief='groove')
            self.code4.place(relx=0.26,rely=0.68,width=30,height=40)
            self.code5 = tk.Entry(self.master,font=("poppins",13,'bold'),textvariable=number5,bd=2,relief='groove')
            self.code5.place(relx=0.315,rely=0.68,width=30,height=40)
            self.code6 = tk.Entry(self.master,font=("poppins",13,'bold'),textvariable=number6,bd=2,relief='groove')
            self.code6.place(relx=0.37,rely=0.68,width=30,height=40)


            # Download the helper library from https://www.twilio.com/docs/python/install
            import os
            from twilio.rest import Client

            # Find your Account SID and Auth Token at twilio.com/console
            # and set the environment variables. See http://twil.io/secure
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)
            
            # =====Extract phone number======
            number = self.phone.get()
            if number[0] == "0":
                removezero = number[1:]
                phonenumber = self.code_lbl.cget("text")+removezero
            else:
                phonenumber = self.code_lbl.cget("text")+number
            #======Send verification code============
            verification = client.verify \
                                .services('VA0aa639a4f3fffa332050d2e1f49496ba') \
                                .verifications \
                                .create(to=phonenumber, channel='sms')

            self.verification_lbl = tk.Label(self.master,text='',font=('poppins',9),fg='#ffffff',bg='#ffffff',relief='groove',bd=0)
            self.verification_lbl.place(relx=0,rely=0.96,width=452,height=20)
            
            if verification.status == 'pending':
                self.verification_lbl.configure(text='Sent successfully',fg='#3d7e3b',bg='#7ae176',bd=1)
            elif verification.status == 'canceled':
                self.verification_lbl.configure(text='Send failed',fg='#3d7e3b',bg='#c01111',bd=1)

            def verify():
                code_input = number1.get() + number2.get() + number3.get() + number4.get() + number5.get() + number6.get()
                print(code_input)
                verification_check = client.verify \
                           .services('VA0aa639a4f3fffa332050d2e1f49496ba') \
                           .verification_checks \
                           .create(to=phonenumber, code=code_input)

                if verification_check.status == 'approved':
                    self.verification_lbl.configure(text='Confirmed',fg='#3d7e3b',bg='#7ae176',bd=1)
                elif verification.status == 'canceled':
                    self.verification_lbl.configure(text='Send failed',fg='#3d7e3b',bg='#c01111',bd=1)

            self.send_btn.place_configure(relx=0.095,rely=0.8)
            self.send_btn.configure(text='Verify',command=verify)

        self.send_btn = tk.Button(self.master, text="Send OTP", fg='#ffffff',font=('poppins',11,'bold'),bg='#2ae5d8',relief='groove',bd=0,width=30,height=1,activebackground='#2ae5d8',activeforeground='#ffffff',command=send)
        self.send_btn.place(relx=0.095,rely=0.7)

if __name__=='__main__':
    root = tk.Tk() 

    app = App(root)
    
    root.mainloop()