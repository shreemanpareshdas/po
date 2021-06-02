from tkinter import *
from tkinter import messagebox
import tempfile
import os

root=Tk()


#=====================variables===================
Ba=IntVar()
ol=IntVar()
ha=IntVar()
mc=IntVar()
ma=IntVar()

de=IntVar()
bl=IntVar()
ta=IntVar()
gl=IntVar()
gla=IntVar()

wo=IntVar()
bi=IntVar()
kas=IntVar()
su=IntVar()
yo=IntVar()

ki=IntVar()
tu=IntVar()
cal=IntVar()
hu=IntVar()
bro=IntVar()

cb=StringVar()
cw=StringVar()
cr=StringVar()
cg=StringVar()
total_cost=StringVar()
#=========================================fuction===========================


#=======================end==================fuction===========================
title=Label(root,pady=5,text="Wine Billing System",bd=10,bg=bg_color,fg='blue',font=('times new roman', 22,'bold'),relief="groove",justify=CENTER)
title.pack(fill=X)
F1 = LabelFrame(root, text='Product Details', font=('times new romon', 18, 'bold'), fg='blue',bg=bg_color,bd=15,relief=RIDGE)
F1.place(x=5, y=62,width=900,height=500)

rum_f = LabelFrame(F1, text='RUM', font=('times new romon', 14, 'bold'), fg='blue',bg=bg_color,bd=6,relief=GROOVE)
rum_f.place(x=5, y=10,width=210,height=260)
b=Label(rum_f, text='Bacardi', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
b.grid(row=0,column=0,padx=5,pady=10)
b_txt=Entry(rum_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=Ba,justify=CENTER)
b_txt.grid(row=0,column=1,pady=10)

o=Label(rum_f, text='Old monk', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
o.grid(row=1,column=0,padx=10,pady=10)
o_txt=Entry(rum_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=ol,justify=CENTER)
o_txt.grid(row=1,column=1,pady=10)

h=Label(rum_f, text='Havana club', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
h.grid(row=2,column=0,padx=10,pady=10)
h_txt=Entry(rum_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=ha,justify=CENTER)
h_txt.grid(row=2,column=1,pady=10)

no1=Label(rum_f, text='McD No1', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
no1.grid(row=3,column=0,padx=10,pady=10)
no1_txt=Entry(rum_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=mc,justify=CENTER)
no1_txt.grid(row=3,column=1,pady=10)

m=Label(rum_f, text='Malibu', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
m.grid(row=4,column=0,padx=10,pady=10)
m_txt=Entry(rum_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=ma,justify=CENTER)
m_txt.grid(row=4,column=1,pady=10)
#2
um_f = LabelFrame(F1, text='Whisky', font=('times new romon', 14, 'bold'), fg='blue',bg=bg_color,bd=6,relief=GROOVE)
um_f.place(x=220, y=10,width=210,height=260)

b1=Label(um_f, text='Dewars 18', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
b1.grid(row=0,column=0,padx=5,pady=10)
b1_txt=Entry(um_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=de,justify=CENTER)
b1_txt.grid(row=0,column=1,pady=10)

o1=Label(um_f, text='Block Dog ', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
o1.grid(row=1,column=0,padx=10,pady=10)
o1_txt=Entry(um_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=bl,justify=CENTER)
o1_txt.grid(row=1,column=1,pady=10)

h1=Label(um_f, text='Talisker 10', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
h1.grid(row=2,column=0,padx=10,pady=10)
h1_txt=Entry(um_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=ta,justify=CENTER)
h1_txt.grid(row=2,column=1,pady=10)

no11=Label(um_f, text='Glenmoragie', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
no11.grid(row=3,column=0,padx=10,pady=10)
no11_txt=Entry(um_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=gl,justify=CENTER)
no11_txt.grid(row=3,column=1,pady=10)

m1=Label(um_f, text='Glenlivet', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
m1.grid(row=4,column=0,padx=10,pady=10)
m1_txt=Entry(um_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=gla,justify=CENTER)
m1_txt.grid(row=4,column=1,pady=10)
#3
um1_f = LabelFrame(F1, text='Wine', font=('times new romon', 14, 'bold'), fg='blue',bg=bg_color,bd=6,relief=GROOVE)
um1_f.place(x=430, y=10,width=210,height=260)
b2=Label(um1_f, text='Wolftrap red', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
b2.grid(row=0,column=0,padx=5,pady=10)
b2_txt=Entry(um1_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=wo,justify=CENTER)
b2_txt.grid(row=0,column=1,pady=10)

o2=Label(um1_f, text='BigBanyan', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
o2.grid(row=1,column=0,padx=10,pady=10)
o2_txt=Entry(um1_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=bi,justify=CENTER)
o2_txt.grid(row=1,column=1,pady=10)

h2=Label(um1_f, text='Kasma sang', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
h2.grid(row=2,column=0,padx=10,pady=10)
h2_txt=Entry(um1_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=kas,justify=CENTER)
h2_txt.grid(row=2,column=1,pady=10)

no12=Label(um1_f, text='Sula Rasa', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
no12.grid(row=3,column=0,padx=10,pady=10)
no12_txt=Entry(um1_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=su,justify=CENTER)
no12_txt.grid(row=3,column=1,pady=10)

m2=Label(um1_f, text='York Arros', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
m2.grid(row=4,column=0,padx=10,pady=10)
m2_txt=Entry(um1_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=yo,justify=CENTER)
m2_txt.grid(row=4,column=1,pady=10)
#4
um3_f = LabelFrame(F1, text='Beer', font=('times new romon', 14, 'bold'), fg='blue',bg=bg_color,bd=6,relief=GROOVE)
um3_f.place(x=650, y=10,width=210,height=260)
b3=Label(um3_f, text='Kingfisher', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
b3.grid(row=0,column=0,padx=5,pady=10)
b3_txt=Entry(um3_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=ki,justify=CENTER)
b3_txt.grid(row=0,column=1,pady=10)

o3=Label(um3_f, text='Tuborg', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
o3.grid(row=1,column=0,padx=10,pady=10)
o3_txt=Entry(um3_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=tu,justify=CENTER)
o3_txt.grid(row=1,column=1,pady=10)

h3=Label(um3_f, text='Calsberg', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
h3.grid(row=2,column=0,padx=10,pady=10)
h3_txt=Entry(um3_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=cal,justify=CENTER)
h3_txt.grid(row=2,column=1,pady=10)

no13=Label(um3_f, text='Budweiser', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
no13.grid(row=3,column=0,padx=10,pady=10)
no13_txt=Entry(um3_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=hu,justify=CENTER)
no13_txt.grid(row=3,column=1,pady=10)

m3=Label(um3_f, text='Bro Code', font=('times new rommon',10, 'bold'), fg='red',bg=bg_color)
m3.grid(row=4,column=0,padx=10,pady=10)
m3_txt=Entry(um3_f,font='arial 6 bold',relief=SUNKEN,bd=4,textvariable=bro,justify=CENTER)
m3_txt.grid(row=4,column=1,pady=10)
#===============================end product======================
pri_f = LabelFrame(F1, text='Price Details', font=('times new romon', 14, 'bold'), fg='red',bg=bg_color,bd=6,relief=GROOVE)
pri_f.place(x=5,y=260,width=880,height=190)
m31=Label(pri_f, text='Bacardi:     Rs.750                          Dewars 18:     Rs.860                  wolfstrap red     Rs.1200           kingfisher     Rs.99  ', font=('times new rommon',10, 'bold'), fg='blue',bg=bg_color)
m31.grid(row=0,column=0,padx=10)
m32=Label(pri_f, text='old monk:    Rs.770                          black dog:     Rs.880                   big banyan       Rs.1400           tuborg         Rs.100  ', font=('times new rommon',10, 'bold'), fg='blue',bg=bg_color)
m32.grid(row=1,column=0,padx=10,pady=5)
m33=Label(pri_f, text='havana club: Rs.750                          talisker:      Rs.860                   kasma sang       Rs.1400           casvorg        Rs.99  ', font=('times new rommon',10, 'bold'), fg='blue',bg=bg_color)
m33.grid(row=2,column=0,padx=10,pady=5)
m34=Label(pri_f, text='mcs no1:     Rs.750                          glenmeragle:   Rs.864                   sula rasa        Rs.1700           budweier       Rs.99  ', font=('times new rommon',10, 'bold'), fg='blue',bg=bg_color)
m34.grid(row=3,column=0,padx=10,pady=5)
m35=Label(pri_f, text='mulibu:      Rs.750                          glanlivef:     Rs.860                   york arros       Rs.1300           bro code       Rs.99  ', font=('times new rommon',10, 'bold'), fg='blue',bg=bg_color)
m35.grid(row=4,column=0,padx=10,pady=5)

#===========================bill area======
F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=910,y=60,width=350,height=500)
bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F2,orient=VERTICAL)
scrol_y.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol_y.set)
textarea.pack(fill=BOTH)
scrol_y.config(command=textarea.yview)
#=========================end billing area============
F3 =Frame(root,bg=bg_color,bd=15,relief=RIDGE)
F3.place(x=5, y=560,width=1270,height=90)

btn1 = Button(F3, text='Total', font='arial 16 bold', padx=5, pady=5, bg='yellow',fg='red',width=8)
btn1.grid(row=0,column=0,pady=0,padx=10)

btn2 = Button(F3, text='Receipt', font='arial 16 bold', padx=5, pady=5, bg='yellow',fg='red',width=8)
btn2.grid(row=0,column=1,padx=30,pady=10)

btn3 = Button(F3, text='Print', font='arial 16 bold', padx=5, pady=5, bg='yellow',fg='red',width=8)
btn3.grid(row=0,column=2,padx=30,pady=10)

btn4 = Button(F3, text='Reset', font='arial 16 bold', padx=5, pady=5, bg='yellow',fg='red',width=8)
btn4.grid(row=0,column=3,padx=30,pady=10)

btn5 = Button(F3, text='Exit', font='arial 16 bold', padx=5, pady=5, bg='yellow',fg='red',width=8)
btn5.grid(row=0,column=4,padx=30,pady=10)
root.mainloop()