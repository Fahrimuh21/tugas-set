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

#DEFINISI, SPESIFIKASI DAN REALISASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
#Head: Mhs tidak kosong -> Mhs
#Head(L): Menghasilkan Mhs tanpa elemen terakhir Mhs, mungkin kosong
#Realisasi
def Head(L):
    return L[:-1]

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
    
#Head: Mhs tidak kosong -> Mhs
#Head(L): Menghasilkan Mhs tanpa elemen terakhir Mhs, mungkin kosong
#Realisasi
def Head(L):
    return L[:-1]
