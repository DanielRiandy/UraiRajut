def urai(text):             # membuat sebuah function dengan nama urai, dengan parameter text. dimana text nanti akan berisi kata/kalimat yang mau di proses sesuai soal
    folder = [] #sebuah variabel dengan nama folder(tipe list), yang nanti akan di isi oleh variabel sub(tipe string)
    sub = '' # sebuah variabel dengan nama sub(tipe string), nanti akan di isi oleh i dari looping
    for i in text: #dilakukan looping terhadap text
       sub+=i # memasukkan nilai dari i ke dalam sub
       folder.append(sub) # kemudian, sub di append ke dalam folder. namun dalam proses looping,nilai sub selalu bertambah(tidak dikosongkan). iterasi pertama : 'C', iterasi ke dua 'Co' ,dst. dan yang di append ke dalam folder sesuai dgn isi sub. iterasi pertama : ['C'], iterasi kedua ['C','Co'], dst
    final = "".join(folder) # kemudian folder yang hasil akhrinya adalah list dengan isi : [''C','Co','Cod','Code'], akan digabungkan menjadi sebuah string dengan fungsi .join dengan separatornya ""(tidak ada), akan dimasukkan ke dalam variabel final
    print(final) # untuk mengeluarkan nilai dari variabel final
urai('Code') # untuk menampilkan function urai, dengan parameter text nya adalah "code"
urai('Python')
urai('Purwadhika') 

def rajut(kata): #membuat sebuah function dengan nama rajut, dengan parameter kata.
    folder = [] # membuat variabel folder(list) , yang nanti akan di isi dengan variabel sub(string).
    sub = ''
    for i in kata: #melakukan looping terhadap kata, untuk setiap indeks di dalam kata
            sub+=i # memasukkan masing masing indeks, ke dalam sub
            folder.append(sub) # memasukkan sub ke dalam folder
            sub='' #mengosongkkan kembali sub menjadi '', agar pada saat dilakukkan looping, i nya tidak akan tergabung dengan i sblmnya.
    temp =[] # disini cara saya masih salah
    # print(folder) # saya memikirkan,untuk menghilangkan nilai unik di dalam variabel folder,dan dimasuukan ke dalam temp, dengan cara :
    for i in folder: # saya lakukan looping di dalam folder ,
        if i not in temp: #apabila untuk setiap i didalam folder, belum ada di temp, maka i dimasukkan ke dalam temp
            temp.append(i)
    # print(temp)
    final = ''.join(temp) # kemudian dilakukan penggabungan agar menjadi 1 string, dengan .join. kedalam variabel final
    print(final) # tapi masih salah, karena emang harusnya ga pake logika hilangin unik number :( 
rajut('CCoCodCode') # mungkin disini berhasil karena ga ada huruf yg berulang
rajut('PPyPytPythPythoPython') # disini jf berhasil karena ga berulang
rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika') # tapi disini gagal, karena ada huruf berulang 
