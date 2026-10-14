# Kunci = "Python"
# password = input("Masukan Pasword :")
# if password == Kunci :
#     print("Password Benar!")
# else:
#     print ("Password Salah!")


# #Program perintah if-elif-else
# angka = int (input("Masukan sebuah bilangan :"))
# if angka > 0:
#     print("Angka merupakan bilangan positif")
# elif angka < 0:
#     print("Angka merupakan bilangan negatif")
# else:
#     print("Angka merupakan 0")


# #Program If bersarang
# x = int(input("Masukkan nilai x="))
# y = int(input("Masukkan nilai y="))
# if x == y:
#     print("Nilai", x , "dan" , y ,"Mempunyai nilai yang sama")
# else:
#     if x > y:
#         print(x, "lebih besar dari", y)
#     if x < y:
#         print(x, "lebih kecil dari", y)

# #if ternary
# umur = 18

# status = "Dewasa" if umur >= 17 else "Belum Dewasa"
# print(status)

# #===================

# #Program Tebak Nomor Acak
# nomor_acak = 7

# print('Tebak nomor acak dari 1 - 10')
# tebakan = int(input('Tebakan anda (bil bulat): '))

# if tebakan == nomor_acak:
#     print('Selamat! tebakan anda benar')
#     print('Tapi tidak ada hadiah untuk anda :(')
# elif tebakan < nomor_acak:
#     print('Tebakan anda terlalu kecil')
# else:
#     print('Tebakan anda terlalu besar')

# print('Selesai')


# #Program Penyelesaian Kondisi
# a = int(input("Masukan umur: "))

# if a <= 15:
#     print("Muda")
# elif a <= 20:
#     print("Remaja")
# else:
#     print("Tua")


# #ganjil genap
# nilai = int(input("masukkan angka: "))

# if nilai % 2:
#     print("bilangan ganjil")
# else:
#     print("bilangan genap")




# #angka ke kata
# a = int(input("masukan angka (0-9): "))

# if a == 0:
#     print("angka anda nol")
# elif a == 1:
#     print("angka anda satu")
# elif a == 2:
#     print("angka anda dua")
# elif a == 3:
#     print("angka anda tiga")
# elif a == 4:
#     print("angka anda empat")
# elif a == 5:
#     print("angka anda lima")
# elif a == 6:
#     print("angka anda enam")
# elif a == 7:
#     print("angka anda tujuh")
# elif a == 8:
#     print("angka anda delapan")
# elif a == 9:
#     print("angka anda sembilan")
# else:
#     print("angka anda not found")

# #if ternary
# a = 10
# b = 20

# #contoh mengembalikan nilai pada ternary
# opet = "opet harus belajar" if a < b else "opet tak perlu belajar"

# print(opet)


# for i in range(5):
#     print(i)

# i = 1

# while i <= 5:
#     print(i)
#     i = i + 1

# #perintah break, continue, pass
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)


# n = 10
# while n:
#     n = n - 1
#     if n % 2 != 0:
#         continue
#     print (n)

# nilai = 80

# if nilai >= 75:
#     pass
# else:
#     print("Tidak lulus")

for i in range(1, 6):
    if i == 3:
        break
    print(i)
