#Dalam tugas 1 ini kita akan mengidentifikasi gender dengan mengidentifikasi huruf dari nama yang sering digunakan oleh laki-laki/perempuan
nama = input("Masukkan nama yang akan di identifikasi : ").lower()
#in#inputkan nama yang akan diidentifikasi, huruf besar dan kecil tidak mempengaruhi
lakilaki=0
perempuan=0
tidakada=0
n=0
#penampung dibuat menjadi 0 terlebih dahulu

for n in range(len(nama)) : #dengan for, n akan bertambah 1 dan berpindah pindah karakter
    if(nama[n]=='a'):
        perempuan= perempuan+1
    elif(nama[n] =='i'):
        perempuan= perempuan+1
    elif (nama[n] == 'u'):
        perempuan = perempuan + 1
    elif (nama[n] == 'e'):
        perempuan = perempuan + 1
    elif (nama[n] == 't'):
        perempuan = perempuan + 1
    elif (nama[n] == 'l'):
        perempuan = perempuan + 1
    elif (nama[n] == 'b'):
        lakilaki = lakilaki + 1
    elif (nama[n] == 'd'):
        lakilaki = lakilaki + 1
    elif (nama[n] == 'o'):
        lakilaki = lakilaki + 1
    else:
        tidakada=tidakada+1
# lakukan pengecekan apakah huruf itu lebih sering digunakan laki laki atau perempuan
#jika laki laki masuk penambahan prediksi ke laki laki, begitu juga dengan perempuan dan tidak ada prediksi jika jika hurufnya tidak ada di perempuan/ laki laki

print("Prediksi Laki laki: ",lakilaki)
print("Prediksi Perempuan: ",perempuan)
print("Tidak ada prediksi: ",tidakada)

if(lakilaki)>(perempuan):               #membandingkan jumlah laki laki dan perempuan
    print(nama,"Bergender Laki laki")
elif(lakilaki)<(perempuan):
    print(nama,"Bergender Perempuan")
# akan dibandingkan dan menentukan apakah laki-laki atau perempuan
