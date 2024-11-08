#TYPE MAHASISWA (MHS) 
#DEFINISI DAN SPESIFIKASI TYPE 
#type Mhs: <nim: string, nama: string, kelas: character, nilai: list of integer> 
#{type Mhs terdiri atas nim, nama, dan kelas mahasiswa, serta kumpulan nilai kuis yang pernah dikerjakan,
#dengan maksimal jumlah mengerjakan adalah 10 kali. Nilai mahasiswa memiliki rentang antara 0-100} 

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR 
#MakeMhs: <string, string, character, list of integer>  → Mhs 
#{MakeMhs(nim, nama, kelas, nilai) membentuk sebuah mahasiswa
#dengan dengan nim, nama, kelas dan nilai berbentuk list of integer. 
#Contoh:  
#MakeMhs('234', 'Andi', 'C', []) membentuk mahasiswa dengan nim '234', nama 'Andi' dari kelas C, 
#dan belum pernah mengerjakan kuis (nilainya berupa list kosong). MakeMhs('123', 'Caca', 'C', [90,80,100]) membentuk mahasiswa dengan nim '123', nama 'CC' dari kelas C, 
#dan telah mengerjakan kuis sebanyak tiga kali dengan nilai masing-masing adalah 90, 80, dan 100. }

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#Konso: elemen, Mhs-> element Mhs
#Konso(e,L) menghasilkan sebuah Mhs dari e dan L dengan e sebagai elemen pertama
#Realisasi
def Konso(e, L):
    return [e]+L

#Konsi: Mhs -> elemen Mhs
#Konsi (L, e)-> menghasilkan sebah Mhs dari L dan e dengan e sebagai elemen terakhir
#Realisasi
def Konsi(L, e):
    return L+[e]


#DEFINISI DAN SPESIFIKASI SELEKTOR
#Head: Mhs tidak kosong -> Mhs
#Head(L): Menghasilkan Mhs tanpa elemen terakhir Mhs, mungkin kosong
#Realisasi
def Head(L):
    return L[:-1]

#Tail: Mhs tidak kosong -> List
#Tail(L): Menghasilkan Mhs tanpa elemen pertama Mhs, mungkin kosong
#Realisasi
def Tail(L):
    return L[1:]

#FirstElmt: Mhs tidak kosong -> elemen
#FirstElmt(L) Menghasilkan elemen pertama Mhs L
#Realisasi
def FirstElmt(L):
    return L[0]

#LastElmt: Mhs tidak kosong -> elemen
#LastElmt(L): mengembalikan elemen terakhir terakhir Mhs L
#Realisasi
def LastElmt(L):
    return L[-1]

#NbElmt: Mhs -> integer
#NbElmt(L): Menghasilkan banyaknya elemen Mhs, nol jika kosong
#Realisasi
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else :
        return 1+NbElmt(Tail(L))

#DEFINISI DAN SPESIFIKASI PREDIKAT
#IsEmpty : Mhs -> boolean
#IsEmpty(L) benar jika Mhs kosong
#Realisasi
def IsEmpty(L):
    return L == [] or L == [[]]

#IsOneElmt: Mhs -> boolean
#IsOneElmt (L) adalah benar jika Mhs L hanya mempunyai satu elemen
#Realisasi
def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []
