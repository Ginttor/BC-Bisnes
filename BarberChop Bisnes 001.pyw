from cProfile import label
from cgitb import text
import os
import string
from tkinter import*
from datetime import datetime
#----------------------------------------
import webbrowser as wb
import random
from io import open
#-----------------------------------------------------------------------
# py -m pyinstaller --onefile proyecto.py

if 0<1<10:print("Hello, world")
now=datetime.now()
global desp;desp=0;ts=[0,0,0,0,0,0,0];te=[0,0,0,0,0,0,0];betun=[""];lnm=[]
lat=["t-0.txt","t-1.txt","t-2.txt","t-3.txt","t-4.txt","t-5.txt","t-6.txt","t-7.txt","t-8.txt","t-9.txt","t-10.txt"];vt=0
reg=open("catalogo Barber Chop 2023.html", "r",encoding='utf-8');catP=["0"];catC=["0"]
TDLU=[];TDMA=[];TDMI=[];TDJU=[];TDVI=[];TDSA=[];TDDO=[];Tp=[0,0,0,0,0,0,0];Tt=[0,0,0,0,0,0,0]
r=reg.readlines();vc=False;i=0
while i<len(r):
    if 0<r[i].count("<!--inbentariooooooo-->"):vc=True
    if vc==True and 0<r[i].count("NOMBRE-->"):
        mm=r[i].replace("</td><!--NOMBRE-->\n", "");mm=mm.replace("      <td>", "");mm=mm.replace("<!--", "");mm=mm.replace("NOMBRE-->\n", "")
        catP.append(mm)
        mm1=r[i+2].replace("</td><!--PRESIO-->\n", "");mm1=mm1.replace("<td>$", "");mm1=mm1.replace("<!--", "");mm1=mm1.replace("-->\n", "");mm1=mm1.replace("  ", "")
        catC.append(mm1);print(mm, mm1)
    i+=1
reg.close()
for i in lat:
    vbd=open(i, "r",encoding='utf-8')
    vi=vbd.readlines()
    lnm.append(vi[0])
    reg.close()

def close():
    global te;now=datetime.now();global betun
    cc.set("CANTIDADES\n.\n.\n.\n.\n.\n.")
    te=[0,0,0,0,0,0,0];betun=[""]

    s1()
    if servisio.get()==str(now.day)+str(now.month)+str(now.year):
        reg=open(lat[vt], "r",encoding='utf-8')
        r=reg.readlines();reg.close()
        bro=open("bro.txt", "w",encoding='utf-8')
        mm=""
        for i in r:mm+=i
        bro.write(mm)
        reg.close()
        reg=open(lat[vt], "w",encoding='utf-8')
        reg.write(r[0]+r[1].replace("\n", ""));reg.close()
        os.startfile("BR00.txt")
        C_error.place(x="0", y="1000")
        servisio.set("Sbr./N.")
        #------------------------------------------    
        mm="\n"+(nm.get()).replace("\n", "")+"\t"+(cc.get()).replace("\n", "")
        ttf()
        mm+=cc.get()
        reg=open("BR00.txt", "r",encoding='utf-8')
        r=reg.readlines()
        for i in betun:
            if 0<i.count("<o>"):print("8-[3]::",i);r.append("\n"+i.replace("\n", ""))
        r.append(mm)
        reg.close()
        NTM=""
        reg=open("BR00.txt", "w",encoding='utf-8')
        for i in r:NTM+=i
        reg.write(NTM)
        reg.close()        
    else:C_error.place(x="485", y="46")
def s0():
    print("S0...on-----------------------------------------------------------------------------------------------------------------+")
    C_error.place(x="0", y="1000")
    now=datetime.now()
    print("dia de la semana:",now.weekday())
    B_subir.place(x="0", y="1000");global ts;global te;global betun
    global TDLU;global TDMA;global TDMI;global TDJU;global TDVI;global TDSA;global Tp;global Tt
    lis.delete(0, END);TT=0;tse=[0,0,0,0,0,0,0];tee=[0,0,0,0,0,0,0];Tpe=[0,0,0,0,0,0,0];Tte=[0,0,0,0,0,0,0]
    reg=open(lat[vt], "r",encoding='utf-8');global ver
    r=reg.readlines();nm.set(str(r[0]));v=False
    lis.insert(END, r[0]);betun.append(r[0])
    lis.insert(END, r[1]);betun.append(r[1])
    aiii=0
    for i in r:
        if v==True:
            da=i.split("\t");daf=da[1].split("/")
            aiii+=float(da[0].replace("_", ""))
            if (0==da[3].count("T")):lis.insert(END, i);betun.append(i)############################
        if 0<i.count("+---+"):v=True
    print("TOTALIDAD TOTALL <",aiii,">",nm.get())
    lis.insert(END, "+-------------------------------------------------------------------------------------------------------------+")
    betun.append("+-------------------------------------------------------------------------------------------------------------+");v=False
    for i in r:
        if v==True:
            da=i.split("\t");daf=da[1].split("/")
            dafe=daf[0].split("-")
            if (0<da[3].count("T")):lis.insert(END, i);betun.append(i) ############################
            if now.weekday()-(now.day-int(dafe[0]))==0:TDLU.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==1:TDMA.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==2:TDMI.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==3:TDJU.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==4:TDVI.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==5:TDSA.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==6:TDDO.append(i)

            #print(daf[0],"><",now.day)#;print("COMP>>>>",da)
            if now.day-int(dafe[0])<=now.weekday():
                #print("---->o<",now.weekday(),"-",now.day,"-",int(daf[0]),"-",cont)
                print("d-s-t:: en ejecusion corectas")
                if (0< da[3].count("T")):Tte[int(dafe[1])]+=float(da[0].replace("_", ""))
                if (0==da[3].count("T")):Tpe[int(dafe[1])]+=float(da[0].replace("_", ""))
                tse[int(dafe[1])]+=float(da[0].replace("_", ""))
                tee[int(dafe[1])]+=1
            TT+=float(da[0].replace("_", ""))
        if 0<i.count("+---+"):v=True
    #print(now)
    reg.close();x=0
    while x<len(tse):
        ts[x]+=tse[x];Tt[x]+=Tte[x]
        te[x]+=tee[x];Tp[x]+=Tpe[x]
        x+=1
    tsest=tse[0]+tse[1]+tse[2]+tse[3]+tse[4]+tse[5]+tse[6]
    tsest2=0
    #if 0<r[1].count("b"):tsest2=(tsest/10)*5
    tsest2=(tsest/10)*5
    mm="lun:"  +str(Tte[0])+"$t + "+str(Tpe[0])+"$p = "+str(tse[0])+"$ de-("+str(tee[0])+") "+"\nmar:"+str(Tte[1])+"$t + "+str(Tpe[1])+"$p = "+str(tse[1])+"$ de-("+str(tee[1])+") "+"\nmie:"+str(Tte[2])+"$t + "+str(Tpe[2])+"$p = "+str(tse[2])+"$ de-("+str(tee[2])+") "+"\njue:"+str(Tte[3])+"$t + "+str(Tpe[3])+"$p = "+str(tse[3])+"$ de-("+str(tee[3])+") "+"\nvie:"+str(Tte[4])+"$t + "+str(Tpe[4])+"$p = "+str(tse[4])+"$ de-("+str(tee[4])+") "+"\nsab:"+str(Tte[5])+"$t + "+str(Tpe[5])+"$p = "+str(tse[5])+"$ de-("+str(tee[5])+") "+"\ndom:"+str(Tte[6])+"$t + "+str(Tpe[6])+"$p = "+str(tse[6])+"$ de-("+str(tee[6])+") "+"\nTT="+str(tsest)+"   (P)="+str(round(tsest2,2))
    cc.set(mm)
    #print("TT=",TT, "   (P)=",TT/2)
    ver=r;nm.set("t-")
def s1():
    print("S0...on-----------------------------------------------------------------------------------------------------------------+")
    C_error.place(x="0", y="1000")
    now=datetime.now()
    print("dia de la semana:",now.weekday())
    B_subir.place(x="0", y="1000");global ts;global te;global betun
    global TDLU;global TDMA;global TDMI;global TDJU;global TDVI;global TDSA;global Tp;global Tt
    lis.delete(0, END);TT=0;tse=[0,0,0,0,0,0,0];tee=[0,0,0,0,0,0,0];Tp=[0,0,0,0,0,0,0];Tt=[0,0,0,0,0,0,0]
    reg=open(lat[vt], "r",encoding='utf-8');global ver
    r=reg.readlines();nm.set(str(r[0]));v=False
    lis.insert(END, r[0]);betun.append(r[0])
    lis.insert(END, r[1]);betun.append(r[1])
    aiii=0
    for i in r:
        if v==True:
            da=i.split("\t");daf=da[1].split("/")
            aiii+=float(da[0].replace("_", ""))
            if (0==da[3].count("T")):lis.insert(END, i);betun.append(i)############################
        if 0<i.count("+---+"):v=True
    print("TOTALIDAD TOTALL <",aiii,">",nm.get())
    lis.insert(END, "+-------------------------------------------------------------------------------------------------------------+")
    betun.append("+-------------------------------------------------------------------------------------------------------------+");v=False
    for i in r:
        if v==True:
            da=i.split("\t");daf=da[1].split("/")
            dafe=daf[0].split("-")
            if (0<da[3].count("T")):lis.insert(END, i);betun.append(i) ############################
            if now.weekday()-(now.day-int(dafe[0]))==0:TDLU.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==1:TDMA.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==2:TDMI.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==3:TDJU.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==4:TDVI.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==5:TDSA.append(i)
            if now.weekday()-(now.day-int(dafe[0]))==6:TDDO.append(i)

            #print(daf[0],"><",now.day)#;print("COMP>>>>",da)
            if now.day-int(dafe[0])<=now.weekday():
                #print("---->o<",now.weekday(),"-",now.day,"-",int(daf[0]),"-",cont)
                print("d-s-t:: en ejecusion corectas")
                if (0<da[3].count("T")):Tt[int(dafe[1])]+=float(da[0].replace("_", ""))
                if (0==da[3].count("T")):Tp[int(dafe[1])]+=float(da[0].replace("_", ""))
                tse[int(dafe[1])]+=float(da[0].replace("_", ""))
                tee[int(dafe[1])]+=1
            TT+=float(da[0].replace("_", ""))
        if 0<i.count("+---+"):v=True
    #print(now)
    reg.close();x=0
    while x<len(tse):
        ts[x]+=tse[x]
        te[x]+=tee[x]
        x+=1
    tsest=tse[0]+tse[1]+tse[2]+tse[3]+tse[4]+tse[5]+tse[6]
    tsest2=0
    #if 0<r[1].count("b"):tsest2=(tsest/10)*5
    tsest2=(tsest/10)*5
    mm="lun:["  +str(tse[0])+"$/("+str(tee[0])+")] "+"\nmar:["+str(tse[1])+"$/("+str(tee[1])+")] "+"\nmie:["+str(tse[2])+"$/("+str(tee[2])+")] "+"\njue:["+str(tse[3])+"$/("+str(tee[3])+")] "+"\nvie:["+str(tse[4])+"$/("+str(tee[4])+")] "+"\nsab:["+str(tse[5])+"$/("+str(tee[5])+")] "+"\ndom:["+str(tse[6])+"$/("+str(tee[6])+")] "+"\nTT="+str(tsest)+"...(P)="+str(round(tsest2,2))
    cc.set(mm)
    #print("TT=",TT, "   (P)=",TT/2)
    ver=r
def intnw():
    now=datetime.now();acc=0;global vt
    cc.set("CANTIDADES\n.\n.\n.\n.\n.\n.")
    x=0
    while x<len(lnm):
        if lnm[x].count(nm.get()):
            nm.set(lnm[x])
            vt=x
        x+=1
    dati.set(lat[vt])
    if servisio.get()=="" or servisio.get=="Sbr./N.":
        C_error.place(x="485", y="46")
    else:
        C_error.place(x="0", y="1000")
        i=0;lis.delete(0, END)
        while i<len(catP):
            if (catP[i] +":$:"+catC[i]).count(servisio.get()):
                lis.insert(END, (catP[i] +":$:"+catC[i]))
                presio.set(catC[i])
                print(catP[i]);acc+=1
            i+=1
    print("A_servidio:",servisio.get()!="", servisio!="Sbr./N.","\tA_datos:", datos.get()!="...(){}", 0==nm.get().count("t-"), acc<2,"\tPresio:", float(presio.get())-float(cpresio.get())==0)
    if servisio.get()!="" and servisio!="Sbr./N." and datos.get()!="...(){}" and 0==nm.get().count("t-") and acc<2 and float(presio.get())-float(cpresio.get())==0:
        B_subir.place(x="460", y="46")
    else:B_subir.place(x="0", y="1000")
def sub():
    now=datetime.now()
    B_subir.place(x="0", y="1000")
    #print(now)
    mm="\n"+presio.get()+"_\t"+str(now.day)+"-"+str(now.weekday())+"/"+str(now.month)+"/"+str(now.year)+"_\t"+str(now.hour)+":"+str(now.minute)+"_\t"+datos.get()+" -:- "+bas.get()+"_\t"+servisio.get();print(mm)

    reg=open(lat[vt], "r",encoding='utf-8')
    r=reg.readlines()
    r.append(mm)
    reg.close()
    NTM=""
    reg=open(lat[vt], "w",encoding='utf-8')
    for i in r:NTM+=i
    reg.write(NTM)
    reg.close()
    s0();presio.set("0");datos.set("...(){}");servisio.set("Sbr./N.");nm.set("t-")
def cvt():
    now=datetime.now()
    global vt;vt+=1
    if vt>len(lat)-1:vt=0
    reg=open(lat[vt], "r",encoding='utf-8');global ver
    r=reg.readlines()
    reg.close()
    nm.set(r[0])
    dati.set(lat[vt])
def rvt():
    now=datetime.now()
    global vt;vt-=1
    if vt<0:vt=len(lat)-1
    reg=open(lat[vt], "r",encoding='utf-8');global ver
    r=reg.readlines()
    reg.close()
    nm.set(r[0])
    dati.set(lat[vt])
def ttf():
    now=datetime.now()
    global vt;vt=0;global te;global betun
    global TDLU;global TDMA;global TDMI;global TDJU;global TDVI;global TDSA;global Tp;global Tt
    global ts;ts=[0,0,0,0,0,0,0];te=[0,0,0,0,0,0,0];Tp=[0,0,0,0,0,0,0];Tt=[0,0,0,0,0,0,0]
    TDLU=[];TDMA=[];TDMI=[];TDJU=[];TDVI=[];TDSA=[]
    for i in lat:
        s0()
        cvt()
    mm="T-lun=["+str(Tt[0])+"$t + "+str(Tp[0])+"$p = "+str(ts[0])+"$ de-("+str(te[0])+") "+"]\nT-mar=["+str(Tt[1])+"$t + "+str(Tp[1])+"$p = "+str(ts[1])+"$ de-("+str(te[1])+") "+"]\nT-mie=["+str(Tt[2])+"$t + "+str(Tp[2])+"$p = "+str(ts[2])+"$ de-("+str(te[2])+") "+"]\nT-jue=["+str(Tt[3])+"$t + "+str(Tp[3])+"$p = "+str(ts[3])+"$ de-("+str(te[3])+") "+"]\nT-vie=["+str(Tt[4])+"$t + "+str(Tp[4])+"$p = "+str(ts[4])+"$ de-("+str(te[4])+") "+"]\nT-sav=["+str(Tt[5])+"$t + "+str(Tp[5])+"$p = "+str(ts[5])+"$ de-("+str(te[5])+") "+"]\nT-dom=["+str(Tt[6])+"$t + "+str(Tp[6])+"$p = "+str(ts[6])+"$ de-("+str(te[6])+") "+"]\nTT-S="+str(ts[0]+ts[1]+ts[2]+ts[3]+ts[4]+ts[5]+ts[6])+"$"
    cc.set(mm)
    for i in TDLU:
        da=i.split("\t");daf=da[1].split("/")
        if (0==da[3].count("T")):lis.insert(END, i);betun.append(i)
    for i in TDMA:
        da=i.split("\t");daf=da[1].split("/")
        if (0==da[3].count("T")):lis.insert(END, i);betun.append(i)
    for i in TDMI:
        da=i.split("\t");daf=da[1].split("/")
        if (0==da[3].count("T")):lis.insert(END, i);betun.append(i)
    for i in TDJU:
        da=i.split("\t");daf=da[1].split("/")
        if (0==da[3].count("T")):lis.insert(END, i);betun.append(i)
    for i in TDVI:
        da=i.split("\t");daf=da[1].split("/")
        if (0==da[3].count("T")):lis.insert(END, i);betun.append(i)
    for i in TDSA:
        da=i.split("\t");daf=da[1].split("/")
        if (0==da[3].count("T")):lis.insert(END, i);betun.append(i)
    lis.insert(END, "+-------------------------------------------------------------------------------------------------------------+")
    betun.append("+-------------------------------------------------------------------------------------------------------------+")
    for i in TDLU:
        da=i.split("\t");daf=da[1].split("/")
        if (0<da[3].count("T")):lis.insert(END, i);betun.append(i)
    for i in TDMA:
        da=i.split("\t");daf=da[1].split("/")
        if (0<da[3].count("T")):lis.insert(END, i);betun.append(i)
    for i in TDMI:
        da=i.split("\t");daf=da[1].split("/")
        if (0<da[3].count("T")):lis.insert(END, i);betun.append(i)
    for i in TDJU:
        da=i.split("\t");daf=da[1].split("/")
        if (0<da[3].count("T")):lis.insert(END, i);betun.append(i)
    for i in TDVI:
        da=i.split("\t");daf=da[1].split("/")
        if (0<da[3].count("T")):lis.insert(END, i);betun.append(i)
    for i in TDSA:
        da=i.split("\t");daf=da[1].split("/")
        if (0<da[3].count("T")):lis.insert(END, i);betun.append(i)

#----------------------------
Pan=Tk()
Pan.title("BarberChop Bisnes")
Pan.config(bg="#bc345a")
Pan.geometry("800x700")
Pan.resizable(1,1)#bloquea ono la dimenion

nm=StringVar();nm.set(lat[vt])
d=Entry(Pan, textvariable=nm, fg="#ffffff",bg="#000000", insertbackground='#ffffff', font=("Roman SD",12)).place(x="10", y="20")
cc=StringVar();cc.set("CANTIDADES\n.\n.\n.\n.\n.\n.")
c=Label(Pan, textvariable=cc, fg="#ffffff", bg="#000000", font=("Roman SD",12)).place(x="0", y="150")


lis=Listbox()
lis.config(fg="#ffffff", font=("Roman SD",12), bg="#000000",  width="70", height="25")
lis.pack()
lis.place(x="300", y="150")

CC_presio=Label(Pan, text="C_PRESIO", fg="#ffffff",bg="#bc345a", font=("Roman SD",10)).place(x="200", y="20")
C_presio=Label(Pan, text="PRESIO", fg="#ffffff",bg="#bc345a", font=("Roman SD",10)).place(x="200", y="40")
C_serbisio=Label(Pan, text="SERVICIO", fg="#ffffff",bg="#bc345a", font=("Roman SD",10)).place(x="200", y="60")
C_datos=Label(Pan, text="PAGO", fg="#ffffff",bg="#bc345a", font=("Roman SD",10)).place(x="200", y="80")
B_agregar=Button(Pan, text="AGREGAR",fg="#00ff00",bg="#000000", command=intnw).place(x="400", y="46")
B_subir=Button(Pan, text="->",fg="#00ff00",bg="#000000", command=sub)
C_error=Label(Pan, text="ALGO NO ESTA BIEN!", fg="#ff0000",bg="#bc345a", font=("Roman SD",10))

dati=StringVar();dati.set(".../..")
C_datos=Label(Pan, textvariable=dati, fg="#ffffff",bg="#000000", font=("Roman SD",10)).place(x="80", y="46")
ctvd=Button(Pan, text="->-",fg="#00ff00",bg="#000000", command=cvt).place(x="150", y="46")
ctvi=Button(Pan, text="-<-",fg="#00ff00",bg="#000000", command=rvt).place(x="20", y="46")

cpresio=StringVar();cpresio.set("0")
ccg=Entry(Pan, textvariable=cpresio, fg="#ffffff", bg="#000000", insertbackground='#ffffff').place(x="275", y="20")
presio=StringVar();presio.set("0")
cg=Entry(Pan, textvariable=presio, fg="#ffffff", bg="#000000", insertbackground='#ffffff').place(x="275", y="40")
servisio=StringVar();servisio.set("Sbr./N.")
ser=Entry(Pan, textvariable=servisio, fg="#ffffff",bg="#000000", insertbackground='#ffffff').place(x="275", y="60")
datos=StringVar();datos.set("...(){}")
cob=Entry(Pan, textvariable=datos, fg="#ffffff",bg="#000000", insertbackground='#ffffff').place(x="275", y="80")

bas=StringVar();bas.set("Base:")
base=Entry(Pan, textvariable=bas, fg="#ffffff", bg="#000000", insertbackground='#ffffff').place(x="10", y="350")
base=StringVar()

f0=Button(Pan, text="F.",fg="#00ff00",bg="#000000", command = s0).place(x="1", y="120")

cerrar=Button(Pan, text="CERRAR->>",fg="#00ff00",bg="#000000", command = close).place(x="20", y="600")

ff=Button(Pan, text="<FF>",fg="#00ff00",bg="#000000", command = ttf).place(x="10", y="300")

Pan.mainloop()