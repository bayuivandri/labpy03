print ('Menampilkan Bilangan Terbesar dari N Buah Data Yang Diinputkan')
max = 0
while True:
    a=int(input("Masukan Bilangan :"))
    if max < a:
        max = a
    if a==0:
        break
print("Bilangan Terbesar Adalah :", max)