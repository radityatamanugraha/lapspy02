 #masukan input
bil1 = int (input("bilangan ke-1: "))
bil2 = int (input("bilangan ke-2: "))
bil3 = int (input("bilangan ke-3: "))

#buat variable data
data = [bil1,bil2,bil3]

#menampilkan data
print("data sebelum di urutkan :", data)
list.sort(data)
print("data setelah di urutkan :", data)