from tkinter import *
from tkinter import messagebox
import tempfile
import math,random,os

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.title('Billing Manangement System')
        self.root.geometry('1260x680')
        bg_color = 'cyan'
        # =====================variables===================
        self.Ba = IntVar()
        self.ol = IntVar()
        self.ha = IntVar()
        self.mc = IntVar()
        self.ma = IntVar()

        self.de = IntVar()
        self.bl = IntVar()
        self.ta = IntVar()
        self.gl = IntVar()
        self.gla = IntVar()

        self.wo = IntVar()
        self.bi = IntVar()
        self.kas = IntVar()
        self.su = IntVar()
        self.yo = IntVar()

        self.ki = IntVar()
        self.tu = IntVar()
        self.cal = IntVar()
        self.hu = IntVar()
        self.bro = IntVar()


        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.search_bill=StringVar()
        self.total_bill = StringVar()
        self.find_bill=StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 99999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        title = Label(root, pady=5, text="Wine Billing System", bd=10, bg=bg_color, fg='blue',
                      font=('times new roman', 22, 'bold'), relief="groove", justify=CENTER)
        title.pack(fill=X)
        f1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 13, 'bold'),
                        bg=bg_color, fg="blue")
        f1.place(x=0, y=62,width=910,height=55)
        cname = Label(f1, text="Customer Name", font=("times new roman", 8, 'bold'), bg=bg_color, fg="blue").grid(
            row=0, column=0)
        cname = Entry(f1, font="arial 10", textvariable=self.c_name, width=20, bd=4, relief=SUNKEN).grid(row=0,
                                                                                                         column=1,
                                                                                                         padx=10)

        phono = Label(f1, text="Phone No", font=("times new roman", 8, 'bold'), bg=bg_color, fg="blue").grid(row=0,
                                                                                                               column=2)
        phono = Entry(f1, font="arial 10", textvariable=self.c_phone, width=20, bd=4, relief=SUNKEN).grid(row=0,
                                                                                                          column=3,
                                                                                                          padx=20
                                                                                                          )
        billno = Label(f1, text="Bill No", font=("times new roman", 8, 'bold'), bg=bg_color, fg="blue").grid(row=0,
                                                                                                               column=4)
        billno = Entry(f1, font="arial 10", textvariable=self.search_bill, width=20, bd=4, relief=SUNKEN).grid(row=0,
                                                                                                               column=5,
                                                                                                              padx=20)
        btn = Button(f1, text="search", command=self.find_bill, bd=4, fg="black", width=17,
                     font=("times new roman", 10, 'bold')).grid(row=0, column=6, padx=10)


        # ....COSMATICES....#
        F1 = LabelFrame(root, text='Product Details', font=('times new romon', 18, 'bold'), fg='blue', bg=bg_color,
                        bd=15, relief=RIDGE)
        F1.place(x=5, y=120, width=900, height=460)

        rum_f = LabelFrame(F1, text='RUM', font=('times new romon', 14, 'bold'), fg='blue', bg=bg_color, bd=6,
                           relief=GROOVE)
        rum_f.place(x=5, y=5, width=210, height=260)
        b = Label(rum_f, text='Bacardi', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        b.grid(row=0, column=0, padx=5, pady=10)
        b_txt = Entry(rum_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.Ba, justify=CENTER)
        b_txt.grid(row=0, column=1, pady=10)

        o = Label(rum_f, text='Old monk', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        o.grid(row=1, column=0, padx=10, pady=10)
        o_txt = Entry(rum_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.ol, justify=CENTER)
        o_txt.grid(row=1, column=1, pady=10)

        h = Label(rum_f, text='Havana club', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        h.grid(row=2, column=0, padx=10, pady=10)
        h_txt = Entry(rum_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.ha, justify=CENTER)
        h_txt.grid(row=2, column=1, pady=10)

        no1 = Label(rum_f, text='McD No1', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        no1.grid(row=3, column=0, padx=10, pady=10)
        no1_txt = Entry(rum_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.mc, justify=CENTER)
        no1_txt.grid(row=3, column=1, pady=10)

        m = Label(rum_f, text='Malibu', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        m.grid(row=4, column=0, padx=10, pady=10)
        m_txt = Entry(rum_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.ma, justify=CENTER)
        m_txt.grid(row=4, column=1, pady=10)
        # 2
        um_f = LabelFrame(F1, text='Whisky', font=('times new romon', 14, 'bold'), fg='blue', bg=bg_color, bd=6,
                          relief=GROOVE)
        um_f.place(x=220, y=5, width=210, height=260)

        b1 = Label(um_f, text='Dewars 18', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        b1.grid(row=0, column=0, padx=5, pady=10)
        b1_txt = Entry(um_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.de, justify=CENTER)
        b1_txt.grid(row=0, column=1, pady=10)

        o1 = Label(um_f, text='Block Dog ', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        o1.grid(row=1, column=0, padx=10, pady=10)
        o1_txt = Entry(um_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.bl, justify=CENTER)
        o1_txt.grid(row=1, column=1, pady=10)

        h1 = Label(um_f, text='Talisker 10', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        h1.grid(row=2, column=0, padx=10, pady=10)
        h1_txt = Entry(um_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.ta, justify=CENTER)
        h1_txt.grid(row=2, column=1, pady=10)

        no11 = Label(um_f, text='Glenmoragie', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        no11.grid(row=3, column=0, padx=10, pady=10)
        no11_txt = Entry(um_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.gl, justify=CENTER)
        no11_txt.grid(row=3, column=1, pady=10)

        m1 = Label(um_f, text='Glenlivet', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        m1.grid(row=4, column=0, padx=10, pady=10)
        m1_txt = Entry(um_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.gla, justify=CENTER)
        m1_txt.grid(row=4, column=1, pady=10)
        # 3
        um1_f = LabelFrame(F1, text='Wine', font=('times new romon', 14, 'bold'), fg='blue', bg=bg_color, bd=6,
                           relief=GROOVE)
        um1_f.place(x=430, y=5, width=210, height=260)
        b2 = Label(um1_f, text='Wolftrap red', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        b2.grid(row=0, column=0, padx=5, pady=10)
        b2_txt = Entry(um1_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.wo, justify=CENTER)
        b2_txt.grid(row=0, column=1, pady=10)

        o2 = Label(um1_f, text='BigBanyan', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        o2.grid(row=1, column=0, padx=10, pady=10)
        o2_txt = Entry(um1_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.bi, justify=CENTER)
        o2_txt.grid(row=1, column=1, pady=10)

        h2 = Label(um1_f, text='Kasma sang', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        h2.grid(row=2, column=0, padx=10, pady=10)
        h2_txt = Entry(um1_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.kas, justify=CENTER)
        h2_txt.grid(row=2, column=1, pady=10)

        no12 = Label(um1_f, text='Sula Rasa', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        no12.grid(row=3, column=0, padx=10, pady=10)
        no12_txt = Entry(um1_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.su, justify=CENTER)
        no12_txt.grid(row=3, column=1, pady=10)

        m2 = Label(um1_f, text='York Arros', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        m2.grid(row=4, column=0, padx=10, pady=10)
        m2_txt = Entry(um1_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.yo, justify=CENTER)
        m2_txt.grid(row=4, column=1, pady=10)
        # 4
        um3_f = LabelFrame(F1, text='Beer', font=('times new romon', 14, 'bold'), fg='blue', bg=bg_color, bd=6,
                           relief=GROOVE)
        um3_f.place(x=650, y=5, width=210, height=260)
        b3 = Label(um3_f, text='Kingfisher', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        b3.grid(row=0, column=0, padx=5, pady=10)
        b3_txt = Entry(um3_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.ki, justify=CENTER)
        b3_txt.grid(row=0, column=1, pady=10)

        o3 = Label(um3_f, text='Tuborg', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        o3.grid(row=1, column=0, padx=10, pady=10)
        o3_txt = Entry(um3_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.tu, justify=CENTER)
        o3_txt.grid(row=1, column=1, pady=10)

        h3 = Label(um3_f, text='Calsberg', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        h3.grid(row=2, column=0, padx=10, pady=10)
        h3_txt = Entry(um3_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.cal, justify=CENTER)
        h3_txt.grid(row=2, column=1, pady=10)

        no13 = Label(um3_f, text='Budweiser', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        no13.grid(row=3, column=0, padx=10, pady=10)
        no13_txt = Entry(um3_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.hu, justify=CENTER)
        no13_txt.grid(row=3, column=1, pady=10)

        m3 = Label(um3_f, text='Bro Code', font=('times new rommon', 10, 'bold'), fg='red', bg=bg_color)
        m3.grid(row=4, column=0, padx=10, pady=10)
        m3_txt = Entry(um3_f, font='arial 6 bold', relief=SUNKEN, bd=4, textvariable=self.bro, justify=CENTER)
        m3_txt.grid(row=4, column=1, pady=10)
        # ===============================end product======================
        pri_f = LabelFrame(F1, text='Price Details', font=('times new romon', 14, 'bold'), fg='red', bg=bg_color, bd=6,
                           relief=GROOVE)
        pri_f.place(x=5, y=260, width=860, height=190)
        m31 = Label(pri_f,
                    text='Bacardi:     Rs.750                          Dewars 18:     Rs.860                  wolfstrap red     Rs.1200           kingfisher     Rs.99  ',
                    font=('times new rommon', 10, 'bold'), fg='blue', bg=bg_color)
        m31.grid(row=0, column=0, padx=10)
        m32 = Label(pri_f,
                    text='old monk:    Rs.770                          black dog:     Rs.880                   big banyan       Rs.1400           tuborg         Rs.100  ',
                    font=('times new rommon', 10, 'bold'), fg='blue', bg=bg_color)
        m32.grid(row=1, column=0, padx=10, pady=5)
        m33 = Label(pri_f,
                    text='havana club: Rs.750                          talisker:      Rs.860                   kasma sang       Rs.1400           casvorg        Rs.99  ',
                    font=('times new rommon', 10, 'bold'), fg='blue', bg=bg_color)
        m33.grid(row=2, column=0, padx=10, pady=5)
        m34 = Label(pri_f,
                    text='mcs no1:     Rs.750                          glenmeragle:   Rs.864                   sula rasa        Rs.1700           budweier       Rs.99  ',
                    font=('times new rommon', 10, 'bold'), fg='blue', bg=bg_color)
        m34.grid(row=3, column=0, padx=10, pady=5)
        m35 = Label(pri_f,
                    text='mulibu:      Rs.750                          glanlivef:     Rs.860                   york arros       Rs.1300           bro code       Rs.99  ',
                    font=('times new rommon', 10, 'bold'), fg='blue', bg=bg_color)
        m35.grid(row=4, column=0, padx=10, pady=5)

        # ===========================bill area======
        f5 = Frame(self.root, bd=10, relief=GROOVE)

        f5.place(x=920, y=62, width=340, height=500)
        bill_title = Label(f5, text='Bill Area', font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_bar = Scrollbar(f5, orient=VERTICAL)
        self.txtarea = Text(f5, yscrollcommand=scrol_bar.set)
        scrol_bar.pack(side=RIGHT, fill=Y)
        scrol_bar.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # =========================end billing area============
        F3 = Frame(root, bg=bg_color, bd=15, relief=RIDGE)
        F3.place(x=5, y=560, width=1270, height=90)

        btn1 = Button(F3, text='Total', font='arial 16 bold', padx=5, pady=5, bg='yellow', fg='red', width=8)
        btn1.grid(row=0, column=0, pady=0, padx=10)

        btn2 = Button(F3, text='Receipt', font='arial 16 bold',command=self.bill_area, padx=5, pady=5, bg='yellow', fg='red', width=8)
        btn2.grid(row=0, column=1, padx=30, pady=10)

        btn3 = Button(F3, text='Print', font='arial 16 bold',command=self.save_bill, padx=5, pady=5, bg='yellow', fg='red', width=8)
        btn3.grid(row=0, column=2, padx=30, pady=10)

        btn4 = Button(F3, text='Reset', font='arial 16 bold',command=self.clear_data, padx=5, pady=5, bg='yellow', fg='red', width=8)
        btn4.grid(row=0, column=3, padx=30, pady=10)

        btn5 = Button(F3, text='Exit', font='arial 16 bold',command=self.exit_app, padx=5, pady=5, bg='yellow', fg='red', width=8)
        btn5.grid(row=0, column=4, padx=30, pady=10)
        self.welcome_bill()

    def total(self):
        self.so = self.Ba.get() * 750
        self.f_c = self.ol.get() * 755
        self.f_w = self.ha.get() * 750
        self.h_s = self.mc.get() * 750
        self.g = self.ma.get() * 750

        self.total_rum_price = float(
            self.so +
            self.f_c +
            self.f_w +
            self.h_s +
            self.g

        )

        self.r = self.de.get() * 860
        self.f = self.bl.get() * 880
        self.d = self.ta.get() * 860
        self.w = self.gl.get() * 864
        self.s = self.gla.get() * 860
        self.total_whiky_price = float(
            self.r +
            self.f +
            self.d +
            self.w +
            self.s
        )
        self.m = self.wo.get() * 1200
        self.co = self.bi.get() * 1400
        self.fr = self.kas.get() * 1400
        self.tr1 = self.su.get() * 1700
        self.li = self.yo.get() * 1300

        self.total_wine_price = float(
            self.m +
            self.co +
            self.fr +
            self.tr1 +
            self.li

        )
        self.m1 = self.ki.get() * 99
        self.co1 = self.tu.get() * 100
        self.fr1 = self.cal.get() * 99
        self.tu1 = self.hu.get() * 99
        self.li1 = self.bro.get() * 180

        self.total_beer_price = float(
            self.m1+
            self.co1 +
            self.fr1 +
            self.tu1 +
            self.li1

        )
        self.total=self.total_rum_price+self.total_whiky_price+self.total_wine_price+self.total_beer_price
        self.cgst=round((self.total * 0.005), 2)
        self.sgst=round((self.total * 0.005), 2)


        self.total_bill =int (self.total +  self.cgst +self.sgst)





    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome Webcode Reatil")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number:  {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n ====================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\tprice")
        self.txtarea.insert(END, f"\n ====================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are must")

        else:
            self.welcome_bill()
            self.total()
            if self.Ba.get() != 0:
                self.txtarea.insert(END, f"\n Bacardi\t\t{self.Ba.get()}\tRs.{self.so}")
            if self.ol.get() != 0:
                self.txtarea.insert(END, f"\n Old Monk\t\t{self.ol.get()}\tRs.{self.f_c}")
            if self.ha.get() != 0:
                self.txtarea.insert(END, f"\n Havana\t\t{self.ha.get()}\tRs.{self.f_w}")
            if self.mc.get() != 0:
                self.txtarea.insert(END, f"\n Mcs No1\t\t{self.mc.get()}\tRs.{self.h_s}")
            if self.ma.get() != 0:
                self.txtarea.insert(END, f"\n Malibu\t\t{self.ma.get()}\tRs.{self.g}")


            if self.de.get() != 0:
                self.txtarea.insert(END, f"\n Dewars 18\t\t{self.de.get()}\tRs.{self.r}")
            if self.bl.get() != 0:
                self.txtarea.insert(END, f"\n Block Dog\t\t{self.bl.get()}\tRs.{self.f}")
            if self.ta.get() != 0:
                self.txtarea.insert(END, f"\n Talisker 10\t\t{self.ta.get()}\tRs.{self.d}")
            if self.gl.get() != 0:
                self.txtarea.insert(END, f"\n Glenmeragle \t\t{self.gl.get()}\tRs.{self.w}")
            if self.gla.get() != 0:
                self.txtarea.insert(END, f"\n glanlivef \t\t{self.gla.get()}\tRs.{self.s}")

            if self.wo.get() != 0:
                self.txtarea.insert(END, f"\n wolfstrap red \t\t{self.wo.get()}\tRs.{self.m}")
            if self.bi.get() != 0:
                self.txtarea.insert(END, f"\n big banyan\t\t{self.bi.get()}\tRs.{self.co}")
            if self.kas.get() != 0:
                self.txtarea.insert(END, f"\n kasma sang \t\t{self.kas.get()}\tRs.{self.fr}")
            if self.su.get() != 0:
                self.txtarea.insert(END, f"\n sula rasa  \t\t{self.su.get()}\tRs.{self.tr1}")
            if self.yo.get() != 0:
                self.txtarea.insert(END, f"\n york arros \t\t{self.yo.get()}\tRs.{self.li}")

            if self.ki.get() != 0:
                self.txtarea.insert(END, f"\n kingfisher  \t\t{self.ki.get()}\tRs.{self.m1}")
            if self.tu.get() != 0:
                self.txtarea.insert(END, f"\n tuborg \t\t{self.tu.get()}\tRs.{self.co1}")
            if self.cal.get() != 0:
                self.txtarea.insert(END, f"\n calsberg \t\t{self.cal.get()}\tRs.{self.fr1}")
            if self.hu.get() != 0:
                self.txtarea.insert(END, f"\n budweier    \t\t{self.hu.get()}\tRs.{self.tu1}")
            if self.bro.get() != 0:
                self.txtarea.insert(END, f"\n Bro Code \t\t{self.bro.get()}\tRs.{self.li1}")

            self.txtarea.insert(END, f"\n ---------------tax-----------------")
            self.txtarea.insert(END, f"\n Cgst :\t\t\tRs. {round((self.cgst), 2)}")
            self.txtarea.insert(END, f"\n Sgst :\t\t\tRs. {round((self.sgst), 2)}")
            self.txtarea.insert(END, f"\n ----------------------------------")
            self.txtarea.insert(END, f"\n Total Bill:\t\t\tRs. {round((self.total_bill), 2)}")


    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do yoy want to save the bill?")
        if op > 0:

            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("C:/users/paresh/bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved", "bill saved successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("C:/users/paresh/bills"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"C:/bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                   self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","invalid Bill no")

    def clear_data(self):
        self.Ba .set(0)
        self.ol .set(0)
        self.ha .set(0)
        self.mc .set(0)
        self.ma .set(0)

        self.de .set(0)
        self.bl .set(0)
        self.ta .set(0)
        self.gl .set(0)
        self.gla .set(0)

        self.wo .set(0)
        self.bi .set(0)
        self.kas .set(0)
        self.su .set(0)
        self.yo .set(0)

        self.ki .set(0)
        self.tu .set(0)
        self.cal .set(0)
        self.hu .set(0)
        self.bro .set(0)

        self.c_name .set(0)
        self.c_phone.set(0)
        self.bill_no.set("")
        x = random.randint(1000, 99999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do You really Want to exit?")
        if op > 0:
            self.root.destroy()
root=Tk()
obj=Bill_App(root)
root.mainloop()