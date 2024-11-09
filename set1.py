#TYPE MAHASISWA (MHS) 
#DEFINISI DAN SPESIFIKASI TYPE 
#type Mhs: <nim: string, nama: string, kelas: character, nilai: list of integer> 
#{type Mhs terdiri atas nim, nama, dan kelas mahasiswa, serta kumpulan nilai kuis yang pernah dikerjakan,
#dengan maksimal jumlah mengerjakan adalah 10 kali. Nilai mahasiswa memiliki rentang antara 0-100} 
#Konstruktor menambahkan elemen di awal, notasi prefix
#type List:[] atau [e o List]
#Konstruktor menambahkan elemen di akhir, notasi postfis
# type List: [] atau [List o e]

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

#MakeMhs : string, string, character,list of Integer -> Mhs 
#MakeMhs(nim, nama, kelas, nilai) adalah sebuah set  
#Realisasi
def MakeMhs(nim, nama, kelas, nilai):
    return [nim, nama, kelas, nilai]


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
    
#SumElmt: Mhs of integer -> integer
#SumElmt (L) menghasilkan jumlahan dari setiap elemen di list Mhs L
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L)+SumElmt(Tail(L))

#MaxElmt (L): Mhs of integer -> integer
#MaxElmt (L) mengembalikan elemen maksimum dari list Mhs L
def max2(a, b):
    if a>b:
        return a
    else:
        return b
    
def maxElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return max2(FirstElmt(L), maxElmt(Tail(L)))
    
#SelectNIM : Mhs -> string
#SelectNIM(Mhs) memberikan NIM Mhs
#Realisasi
def SelectNIM(Mhs):
    return Mhs[0]

#SelectNama: Mhs -> string
#SelectNama(Mhs) memberikan Nama Mhs
#Realisasi
def SelectNama(Mhs):
    return Mhs[1]

#SelectKelas: Mhs -> character
#SelectKelas(Mhs) memberikan kelas Mhs
#Realisasi
def SelectKelas(Mhs):
    return Mhs[2]

#SelectNilai: Mhs -> string
#SelectNilai(Mhs) memberikan nilai Mhs
#Realisasi
def SelectNilai(Mhs):
    return Mhs[3]

#RataRata: Mhs -> string
#RataRata(Mhs) memberikan rata rata nilai Mhs
#Realisasi
def RataRata(Mhs):
    if IsEmpty(Mhs):
        return 0
    else:
        return SumElmt(SelectNilai(Mhs))/NbElmt(SelectNilai(Mhs))
    
def max2(a, b):
    if a>b :
        return a
    else:
        return b

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
     
#IsNimMemberSetMhs: elemen, Mhs -> boolean
#IsNimMemberSetMhs(nim, SetMhs)adalah benar jika NIM nim adalah elemen NIM X list setMhs L
#Realisasi
def IsNimMemberSetMhs(nim, SetMhs):
    if IsEmpty(SetMhs):
        return False
    else:
        if nim == SelectNIM(FirstElmt(SetMhs)):
            return True
        else:
            return IsNimMemberSetMhs(nim, Tail(SetMhs))
    
#DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN MHS
#SetMhs: Mhs -> set
#SetMhs(Mhs) mengembalikan NIM yang unik(tidak boleh sama dengan NIM yang sudah ada)
#Realisasi
def SetMhs(Mhs):
    if IsEmpty(Mhs):
        return []
    else:
        if IsNimMemberSetMhs(SelectNIM(FirstElmt(Mhs)), Tail(Mhs)):
            return SetMhs(Tail(Mhs))
        else:
            return Konso(FirstElmt(Mhs), SetMhs(Tail(Mhs)))


#Lulus: Mhs -> set
#Lulus(Mhs) mengembalikan mahasiswa yang lulus(yang nilai rata rata nya lebih dari sama dengan 70)
#Realisasi
def Lulus(SetMhs):
    if IsEmpty(SetMhs):
        return []
    else:
        if RataRata(FirstElmt(SetMhs)) >= 70:
            return Konso(FirstElmt(SetMhs), Lulus(Tail(SetMhs)))
        else:
            return Lulus(Tail(SetMhs)) 

#TidakMengerjakanKuisKelas: string, Mhs -> set
#TidakMengerjakanKuisKelas(kelas, Mhs) mengembalikan himpunan mahasiswa yang tidak mengerjakan kuis sama 
#sekali di suatu kelas tertentu sesuai dengan nama kelas di-input-kan sebagai parameter.
#Realisasi 
def TidakMengerjakanKuisKelas(kelas, SetMhs):
    if IsEmpty(SetMhs):
        return []
    else:
        if kelas == SelectKelas(FirstElmt(SetMhs)) and IsEmpty(SelectNilai(FirstElmt(SetMhs))):
            return Konso(FirstElmt(SetMhs), TidakMengerjakanKuisKelas(kelas, Tail(SetMhs)))
        else:
            return TidakMengerjakanKuisKelas(kelas, Tail(SetMhs))

#NilaiTertinggi : Mhs -> 
def NilaiTertinggi(SetMhs):
    if IsEmpty(SelectNilai(FirstElmt(SetMhs))):
        return NilaiTertinggi(Tail(SetMhs))
    else:
        if IsOneElmt(SetMhs):
            return RataRata(SelectNilai(FirstElmt(SetMhs)))
        else :
            return max2(RataRata(SelectNilai(FirstElmt(SetMhs))),NilaiTertinggi(Tail(SetMhs)))
