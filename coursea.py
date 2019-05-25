from tkinter import *
import tkinter.messagebox

controller = False

root = Tk()

root.title("Coursea")

root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

#a=Label(root, text=tip2ort)
#b=Label(root, text=q)


class Test:
    secilenler = []

    def __init__(self):
        self.isimler = ['Matematik',
'Fen',
'Kodlama',
'Yapay Zeka',
'Java',
'C++',
'Python',
'Web_Tasarım',
'Görüntü İşleme',
'Biyoloji',
'Fizik',
'Kimya',
'Robotik',
'Mühendislik',
'Sosyal',
'Resim',
'Animasyon',
'Sanat',
'Müzik',
'Felsefe',
'Aşçılık',
'Spor',
'Edebiyat',
'İnovasyon',
'Liderlik']
        self.array = []

        for i in range(len(self.isimler)-1):
            boos=1
            self.array.append(boos)
            boos +=1

        self.vars = []

        self.doCheckbutton()

    def doCheckbutton(self):
        for i in range(len(self.array)):
            self.vars.append(StringVar())
            self.vars[-1].set(0)
            c = Checkbutton(root,
                            text=self.isimler[i],
                            variable=self.vars[-1],
                            command=lambda i=i: self.printSelection(i),
                            onvalue=1,
                            offvalue=0)
            c.pack()


    def printSelection(self, i):
        w = int(self.vars[i].get())
        se = self.isimler[i]

        if w == 1:

            if self.isimler[i] in self.secilenler:
                tutucu = True
            else:
                tutucu = False
                self.secilenler.append(self.isimler[i])
        if w == 0:
            self.secilenler.remove(se)

Test()

#etkinlikler
secilmisler = Test.secilenler
e1 =['Sosyal', 'Felsefe', 'Liderlik', 'İnovasyon', 'YGA Zirvesi 2019']
e11 =0
e2 =['Matematik','Robotik','Fizik','Kodlama','Java','Fen','Görüntü İşleme', 'Mühendislik', 'FRC Robotik Turnuvası']
e22=0
e3 = ['Aşçılık','Sosyak', 'SAC Aşçılık Kursları']
e33=0
e4 = ['Aşçılık','Sosyal', 'SAC Aşçılık Kursları']
e44=0
e5 = ['Sosyal','Resim','Animasyon','SAC Animasyon Kursları']
e55=0
e6 = ['Spor', 'SAC Spor Festivali']
e66=0
e7 = ['Yapay Zeka','Görüntü İşleme', 'Kodlama', 'Python', 'SAC Yapay Zeka Çalıştayı']
e77=0
e8 = ['Fen','Biyoloji', 'Kodlama','Yapay Zeka', 'Yapay Zeka ile Biyoloji Çalıştayı']
e88=0

def run():
    global e1, e2, e3, e4, e5, e6, e7, e8, secilmisler, e11, e22, e33, e44, e55, e66, e77, e88
    for i in range(len(secilmisler)):
        if secilmisler[i] in e1:
            e11 +=1
        if secilmisler[i] in e2:
            e22 +=1
        if secilmisler[i] in e3:
            e33 +=1
        if secilmisler[i] in e4:
            e44 +=1
        if secilmisler[i] in e5:
            e55 +=1
        if secilmisler[i] in e6:
            e66 +=1
        if secilmisler[i] in e7:
            e77 +=1
        if secilmisler[i] in e8:
            e88 +=1
    e11 = e11 / len(e1)
    e1.append(e11)

    e22 = e22 / len(e2)
    e2.append(e22)

    e33= e33 / len(e3)
    e3.append(e33)

    e44 = e44 / len(e4)
    e4.append(e44)

    e55 = e55 / len(e5)
    e5.append(e55)

    e66 = e66 / len(e6)
    e1.append(e11)

    e77 = e77 / len(e7)
    e7.append(e77)

    e88 = e88 / len(e8)
    e8.append(e88)
    print(e1, e2, e3, e4, e5, e6 ,e7 ,e8)



button = Button(root, text='Etkinlik Bul', width=25,  command=run)

#packleme kısmı
packlenecekler =[button]
packu = int(len(packlenecekler))


for i in range(packu):
    placeholder = packlenecekler[i]

    placeholder.pack()
#packleme kısmı bitiş

root.mainloop( )

e1 = [mat, fen, kodlama, din, sosyal]
e2 = [sosyal, müzik]
e3 = []

uz1veri= len(e1)
uz2veri = len(e2)

#tiplere göre for döngüleri, her tip için farklı döngü yerine iç içe döngüye al
#for i in range(uzveri):
 #   if veriler[i] in e1:
  #      tip1say = tip1say + 1

#for j in range(uzveri):
 #   if veriler[j] in e2:
  #      tip2say = tip2say + 1

#tip1ort = tip1say/(uz1veri+1)
#tip2ort = tip2say/(uz2veri+1)

#troubleshooting



