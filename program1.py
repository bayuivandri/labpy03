print ( 'Jumlah Laba hasil investasi seorang pengusaha selama 8 bulan')

#modal awal
x=100000000
print ("Modal Awal :",x )

#presentase keuntungan
a=0*x
b=0*x
c=0.01*x
d=0.01*x
e=0.05*x
f=0.05*x
g=0.05*x
h=0.03*x

y=[a,b,c,d,e,f,g,h]

for i in range (len(y)):
    print ("Laba Bulan Ke-",i+1 ,"Sebesar :" ,y[i])

z= (a+b+c+d+e+f+g+h)
print ("Jumlah Laba Selama 8 Bulan adalah : ",z)
