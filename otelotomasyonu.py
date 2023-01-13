from tkinter import *
import pyodbc
from tkinter import messagebox

root = Tk()
root.geometry("500x500")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8AV32UP\SQLEXPRESS;'
                      'Database=onur_otel_otomasyon;'
                      'Trusted_Connection=True;')
cursor=conn.cursor()
                      
def birinciodafonk():
    def dbMusteriKaydet():
        cursor.execute("SELECT oda_kira_durumu FROM oda_bilgileri  WHERE oda_id = '1'")
        sonuc = cursor.fetchall()
        kiradurumu = sonuc[0][0]

        if (kiradurumu != "Boş"):
            pass
            # messagebox gözükecek
        else:
            adBilgisi = ad_var.get()
            soyadBilgisi = soyad_var.get()
            tcnoBilgisi = tcno_var.get()
            dogumTarihiBilgisi = dogumtarihi_var.get()
            telefonNoBilgisi = telefonno_var.get()
            kiralanacakGunSayisiBilgisi = kiralanacakgunsayisi_var.get()

            sorgu = f"INSERT INTO misafir_girisi(ad,soyad,tc_no,dogum_tarihi,telefon_no,kiralanacak_gun_sayisi) VALUES(?,?,?,?,?,?)"
            values = (f'{adBilgisi}', f'{soyadBilgisi}', f'{tcnoBilgisi}',f'{dogumTarihiBilgisi}',f'{telefonNoBilgisi}', f'{kiralanacakGunSayisiBilgisi}')
            ekle = cursor.execute(sorgu, values)
            conn.commit()

        
            cursor.execute("UPDATE oda_bilgileri SET oda_kira_durumu = 'Kirada'  WHERE oda_id = '1'")
            conn.commit()
        
        




    birinciodabilgi = Toplevel()
    birinciodabilgi.geometry("500x500")

    birinciodaadlabel = Label(birinciodabilgi,text="Adınız").place(x=100,y=20)
    ad_var=StringVar()
    birinciodaadentry = Entry(birinciodabilgi, textvariable=ad_var).place(x=100,y=40)


    birinciodasoyadlabel = Label(birinciodabilgi,text="Soyadınız").place(x=100,y=60)
    soyad_var=StringVar()
    birinciodasoyadentry = Entry(birinciodabilgi, textvariable=soyad_var).place(x=100,y=80)


    birinciodatcnolabel = Label(birinciodabilgi,text="TC No").place(x=100,y=100)
    tcno_var=StringVar()
    birinciodatcnoentry = Entry(birinciodabilgi, textvariable=tcno_var).place(x=100,y=120)


    birinciodadogumtarihilabel = Label(birinciodabilgi,text="Doğum Tarihi").place(x=100,y=140)
    dogumtarihi_var=StringVar()
    birinciodadogumtarihientry = Entry(birinciodabilgi, textvariable=dogumtarihi_var).place(x=100,y=160)


    birinciodatelefonnolabel = Label(birinciodabilgi,text="Telefon Numarası").place(x=100,y=180)
    telefonno_var=StringVar()
    birinciodatelefonnoentry = Entry(birinciodabilgi,textvariable=telefonno_var).place(x=100,y=200)


    birincikiralanacakgunsayisilabel = Label(birinciodabilgi,text="Kiralanacak gün sayısı").place(x=100,y=220)
    kiralanacakgunsayisi_var=StringVar()
    birincikiralanacakgunsayisientry = Entry(birinciodabilgi, textvariable=kiralanacakgunsayisi_var).place(x=100,y=240)

    cursor.execute("SELECT * FROM oda_bilgileri where oda_id = '1' ")
    sonuc = cursor.fetchall()
    for i in sonuc:
        
        gunlukKira = i[1]
        ozellik1 = i[2]
        ozellik2 = i[3]
        ozellik3 = i[4]
        ozellik4 = i[5]
        ozellik5 = i[6]
        odaKiraDurumu = i[7]

    variable = Label(birinciodabilgi, text = "ODA 1").place(x=100,y=300)
    variable = Label(birinciodabilgi, text = f"Günlük kira = {gunlukKira}").place(x=100,y=320)
    variable = Label(birinciodabilgi, text = f"Oda özelliği = {ozellik1}").place(x=100,y=340)
    variable = Label(birinciodabilgi, text = f"Oda özelliği = {ozellik2}").place(x=100,y=360)
    variable = Label(birinciodabilgi, text = f"Oda özelliği = {ozellik3}").place(x=100,y=380)
    variable = Label(birinciodabilgi, text = f"Oda özelliği = {ozellik4}").place(x=100,y=400)
    variable = Label(birinciodabilgi, text = f"Oda özelliği = {ozellik5}").place(x=100,y=420)
    variable = Label(birinciodabilgi, text = f"Oda özelliği = {odaKiraDurumu}").place(x=100,y=440)

    def musteriCikis():
        cursor.execute("UPDATE oda_bilgileri SET oda_kira_durumu = 'Boş'  WHERE oda_id = '1'")
        conn.commit()

    musteri_kaydet = Button(birinciodabilgi,text="Odayı Kirala",command=dbMusteriKaydet).place(x=280,y=180)
    silbtn = Button(birinciodabilgi,text="Misafir Çıkışı",command=musteriCikis).place(x=280,y=220)

btn1 = Button(root,text="1. Oda Bilgileri",command=birinciodafonk).place(x=100,y=100)


def ikinciodabilgifonk():
    def dbMusteriKaydet():
        cursor.execute("SELECT oda_kira_durumu FROM oda_bilgileri  WHERE oda_id = '2'")
        sonuc = cursor.fetchall()
        kiradurumu = sonuc[0][0]

        if (kiradurumu != "Boş"):
            pass
            # messagebox gözükecek
        else:
            adBilgisi = ad_var.get()
            soyadBilgisi = soyad_var.get()
            tcnoBilgisi = tcno_var.get()
            dogumTarihiBilgisi = dogumtarihi_var.get()
            telefonNoBilgisi = telefonno_var.get()
            kiralanacakGunSayisiBilgisi = kiralanacakgunsayisi_var.get()

            sorgu = f"INSERT INTO misafir_girisi(ad,soyad,tc_no,dogum_tarihi,telefon_no,kiralanacak_gun_sayisi) VALUES(?,?,?,?,?,?)"
            values = (f'{adBilgisi}', f'{soyadBilgisi}', f'{tcnoBilgisi}',f'{dogumTarihiBilgisi}',f'{telefonNoBilgisi}', f'{kiralanacakGunSayisiBilgisi}')
            ekle = cursor.execute(sorgu, values)
            conn.commit()


            cursor.execute("UPDATE oda_bilgileri SET oda_kira_durumu = 'Kirada'  WHERE oda_id = '2'")
            conn.commit()


    ikinciodabilgi = Toplevel()
    ikinciodabilgi.geometry("500x500")

    Label(ikinciodabilgi,text="Adınız").place(x=100,y=20)
    ad_var=StringVar()
    Entry(ikinciodabilgi, textvariable=ad_var).place(x=100,y=40)


    Label(ikinciodabilgi,text="Soyadınız").place(x=100,y=60)
    soyad_var=StringVar()
    Entry(ikinciodabilgi, textvariable=soyad_var).place(x=100,y=80)

    Label(ikinciodabilgi,text="TC No").place(x=100,y=100)
    tcno_var=StringVar()
    Entry(ikinciodabilgi, textvariable=tcno_var).place(x=100,y=120)


    Label(ikinciodabilgi,text="Doğum Tarihi").place(x=100,y=140)
    dogumtarihi_var=StringVar()
    Entry(ikinciodabilgi, textvariable=dogumtarihi_var).place(x=100,y=160)


    Label(ikinciodabilgi,text="Telefon Numarası").place(x=100,y=180)
    telefonno_var=StringVar()
    Entry(ikinciodabilgi,textvariable=telefonno_var).place(x=100,y=200)


    Label(ikinciodabilgi,text="Kiralanacak gün sayısı").place(x=100,y=220)
    kiralanacakgunsayisi_var=StringVar()
    Entry(ikinciodabilgi, textvariable=kiralanacakgunsayisi_var).place(x=100,y=240)

    cursor.execute("SELECT * FROM oda_bilgileri where oda_id = '2' ")
    sonuc = cursor.fetchall()
    for i in sonuc:
        
        gunlukKira = i[1]
        ozellik1 = i[2]
        ozellik2 = i[3]
        ozellik3 = i[4]
        ozellik4 = i[5]
        ozellik5 = i[6]
        odaKiraDurumu = i[7]

    variable = Label(ikinciodabilgi, text = "ODA 2").place(x=100,y=300)
    variable = Label(ikinciodabilgi, text = f"Günlük kira = {gunlukKira}").place(x=100,y=320)
    variable = Label(ikinciodabilgi, text = f"Oda özelliği = {ozellik1}").place(x=100,y=340)
    variable = Label(ikinciodabilgi, text = f"Oda özelliği = {ozellik2}").place(x=100,y=360)
    variable = Label(ikinciodabilgi, text = f"Oda özelliği = {ozellik3}").place(x=100,y=380)
    variable = Label(ikinciodabilgi, text = f"Oda özelliği = {ozellik4}").place(x=100,y=400)
    variable = Label(ikinciodabilgi, text = f"Oda özelliği = {ozellik5}").place(x=100,y=420)
    variable = Label(ikinciodabilgi, text = f"Oda özelliği = {odaKiraDurumu}").place(x=100,y=440)

    def musteriCikis():
        cursor.execute("UPDATE oda_bilgileri SET oda_kira_durumu = 'Boş'  WHERE oda_id = '2'")
        conn.commit()

    silbtn = Button(ikinciodabilgi,text="Misafir Çıkışı",command=musteriCikis).place(x=280,y=220)
    musteri_kaydet = Button(ikinciodabilgi,text="Odayı Kirala",command=dbMusteriKaydet).place(x=280,y=180)



btn2 = Button(root,text="2.Oda Bilgileri",command=ikinciodabilgifonk).place(x=200,y=100)

def ucuncuodabilgifonk():
    def dbMusteriKaydet():
        cursor.execute("SELECT oda_kira_durumu FROM oda_bilgileri  WHERE oda_id = '3'")
        sonuc = cursor.fetchall()
        kiradurumu = sonuc[0][0]

        if (kiradurumu != "Boş"):
            pass
            # messagebox gözükecek
        else:
            adBilgisi = ad_var.get()
            soyadBilgisi = soyad_var.get()
            tcnoBilgisi = tcno_var.get()
            dogumTarihiBilgisi = dogumtarihi_var.get()
            telefonNoBilgisi = telefonno_var.get()
            kiralanacakGunSayisiBilgisi = kiralanacakgunsayisi_var.get()

            sorgu = f"INSERT INTO misafir_girisi(ad,soyad,tc_no,dogum_tarihi,telefon_no,kiralanacak_gun_sayisi) VALUES(?,?,?,?,?,?)"
            values = (f'{adBilgisi}', f'{soyadBilgisi}', f'{tcnoBilgisi}',f'{dogumTarihiBilgisi}',f'{telefonNoBilgisi}', f'{kiralanacakGunSayisiBilgisi}')
            ekle = cursor.execute(sorgu, values)
            conn.commit()


            cursor.execute("UPDATE oda_bilgileri SET oda_kira_durumu = 'Kirada'  WHERE oda_id = '3'")
            conn.commit()

    ucuncuodabilgi = Toplevel()
    ucuncuodabilgi.geometry("500x500")

    Label(ucuncuodabilgi,text="Adınız").place(x=100,y=20)
    ad_var=StringVar()
    Entry(ucuncuodabilgi, textvariable=ad_var).place(x=100,y=40)


    Label(ucuncuodabilgi,text="Soyadınız").place(x=100,y=60)
    soyad_var=StringVar()
    Entry(ucuncuodabilgi, textvariable=soyad_var).place(x=100,y=80)

    Label(ucuncuodabilgi,text="TC No").place(x=100,y=100)
    tcno_var=StringVar()
    Entry(ucuncuodabilgi, textvariable=tcno_var).place(x=100,y=120)

    Label(ucuncuodabilgi,text="Doğum Tarihi").place(x=100,y=140)
    dogumtarihi_var=StringVar()
    Entry(ucuncuodabilgi, textvariable=dogumtarihi_var).place(x=100,y=160)


    Label(ucuncuodabilgi,text="Telefon Numarası").place(x=100,y=180)
    telefonno_var=StringVar()
    Entry(ucuncuodabilgi,textvariable=telefonno_var).place(x=100,y=200)


    Label(ucuncuodabilgi,text="Kiralanacak gün sayısı").place(x=100,y=220)
    kiralanacakgunsayisi_var=StringVar()
    Entry(ucuncuodabilgi, textvariable=kiralanacakgunsayisi_var).place(x=100,y=240)

    cursor.execute("SELECT * FROM oda_bilgileri where oda_id = '3' ")
    sonuc = cursor.fetchall()
    for i in sonuc:
        
        gunlukKira = i[1]
        ozellik1 = i[2]
        ozellik2 = i[3]
        ozellik3 = i[4]
        ozellik4 = i[5]
        ozellik5 = i[6]
        odaKiraDurumu = i[7]

    variable = Label(ucuncuodabilgi, text = "ODA 3").place(x=100,y=300)
    variable = Label(ucuncuodabilgi, text = f"Günlük kira = {gunlukKira}").place(x=100,y=320)
    variable = Label(ucuncuodabilgi, text = f"Oda özelliği = {ozellik1}").place(x=100,y=340)
    variable = Label(ucuncuodabilgi, text = f"Oda özelliği = {ozellik2}").place(x=100,y=360)
    variable = Label(ucuncuodabilgi, text = f"Oda özelliği = {ozellik3}").place(x=100,y=380)
    variable = Label(ucuncuodabilgi, text = f"Oda özelliği = {ozellik4}").place(x=100,y=400)
    variable = Label(ucuncuodabilgi, text = f"Oda özelliği = {ozellik5}").place(x=100,y=420)
    variable = Label(ucuncuodabilgi, text = f"Oda özelliği = {odaKiraDurumu}").place(x=100,y=440)

    def musteriCikis():
        cursor.execute("UPDATE oda_bilgileri SET oda_kira_durumu = 'Boş'  WHERE oda_id = '3'")
        conn.commit()

    silbtn = Button(ucuncuodabilgi,text="Misafir Çıkışı",command=musteriCikis).place(x=280,y=220)
    musteri_kaydet = Button(ucuncuodabilgi,text="Odayı Kirala",command=dbMusteriKaydet).place(x=280,y=180)


btn3 = Button(root,text="3. Oda Bilgileri",command=ucuncuodabilgifonk).place(x=100,y=150)

def dorduncuodabilgifonk():
    def dbMusteriKaydet():
        cursor.execute("SELECT oda_kira_durumu FROM oda_bilgileri  WHERE oda_id = '4'")
        sonuc = cursor.fetchall()
        kiradurumu = sonuc[0][0]

        if (kiradurumu != "Boş"):
            pass
            # messagebox gözükecek
        else:
            adBilgisi = ad_var.get()
            soyadBilgisi = soyad_var.get()
            tcnoBilgisi = tcno_var.get()
            dogumTarihiBilgisi = dogumtarihi_var.get()
            telefonNoBilgisi = telefonno_var.get()
            kiralanacakGunSayisiBilgisi = kiralanacakgunsayisi_var.get()

        sorgu = f"INSERT INTO misafir_girisi(ad,soyad,tc_no,dogum_tarihi,telefon_no,kiralanacak_gun_sayisi) VALUES(?,?,?,?,?,?)"
        values = (f'{adBilgisi}', f'{soyadBilgisi}', f'{tcnoBilgisi}',f'{dogumTarihiBilgisi}',f'{telefonNoBilgisi}', f'{kiralanacakGunSayisiBilgisi}')
        ekle = cursor.execute(sorgu, values)
        conn.commit()


        cursor.execute("UPDATE oda_bilgileri SET oda_kira_durumu = 'Kirada'  WHERE oda_id = '4'")
        conn.commit()

    dorduncuodabilgi = Toplevel()
    dorduncuodabilgi.geometry("500x500")

    Label(dorduncuodabilgi,text="Adınız").place(x=100,y=20)
    ad_var=StringVar()
    Entry(dorduncuodabilgi, textvariable=ad_var).place(x=100,y=40)


    Label(dorduncuodabilgi,text="Soyadınız").place(x=100,y=60)
    soyad_var=StringVar()
    Entry(dorduncuodabilgi, textvariable=soyad_var).place(x=100,y=80)

    Label(dorduncuodabilgi,text="TC No").place(x=100,y=100)
    tcno_var=StringVar()
    Entry(dorduncuodabilgi, textvariable=tcno_var).place(x=100,y=120)


    Label(dorduncuodabilgi,text="Doğum Tarihi").place(x=100,y=140)
    dogumtarihi_var=StringVar()
    Entry(dorduncuodabilgi, textvariable=dogumtarihi_var).place(x=100,y=160)


    Label(dorduncuodabilgi,text="Telefon Numarası").place(x=100,y=180)
    telefonno_var=StringVar()
    Entry(dorduncuodabilgi,textvariable=telefonno_var).place(x=100,y=200)


    Label(dorduncuodabilgi,text="Kiralanacak gün sayısı").place(x=100,y=220)
    kiralanacakgunsayisi_var=StringVar()
    Entry(dorduncuodabilgi, textvariable=kiralanacakgunsayisi_var).place(x=100,y=240)

    cursor.execute("SELECT * FROM oda_bilgileri where oda_id = '4' ")
    sonuc = cursor.fetchall()
    for i in sonuc:
        
        gunlukKira = i[1]
        ozellik1 = i[2]
        ozellik2 = i[3]
        ozellik3 = i[4]
        ozellik4 = i[5]
        ozellik5 = i[6]
        odaKiraDurumu = i[7]

    variable = Label(dorduncuodabilgi, text = "ODA 4").place(x=100,y=300)
    variable = Label(dorduncuodabilgi, text = f"Günlük kira = {gunlukKira}").place(x=100,y=320)
    variable = Label(dorduncuodabilgi, text = f"Oda özelliği = {ozellik1}").place(x=100,y=340)
    variable = Label(dorduncuodabilgi, text = f"Oda özelliği = {ozellik2}").place(x=100,y=360)
    variable = Label(dorduncuodabilgi, text = f"Oda özelliği = {ozellik3}").place(x=100,y=380)
    variable = Label(dorduncuodabilgi, text = f"Oda özelliği = {ozellik4}").place(x=100,y=400)
    variable = Label(dorduncuodabilgi, text = f"Oda özelliği = {ozellik5}").place(x=100,y=420)
    variable = Label(dorduncuodabilgi, text = f"Oda özelliği = {odaKiraDurumu}").place(x=100,y=440)

    def musteriCikis():
        cursor.execute("UPDATE oda_bilgileri SET oda_kira_durumu = 'Boş'  WHERE oda_id = '4'")
        conn.commit()

    silbtn = Button(dorduncuodabilgi,text="Misafir Çıkışı",command=musteriCikis).place(x=280,y=220)
    musteri_kaydet = Button(dorduncuodabilgi,text="Odayı Kirala",command=dbMusteriKaydet).place(x=280,y=180)



btn3 = Button(root,text="4. Oda Bilgileri",command=dorduncuodabilgifonk).place(x=200,y=150)



root.mainloop()