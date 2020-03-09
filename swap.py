def swap(a, b):
	c = a
	a = b
	b = c
	return(a,b)

A = input("Masukkan angka #1 : ")
B = input("Masukkan angka #2 : ")

print("Anda memasukkan bilangan A = ", A)
print("dan bilangan B = ", B)

A, B = swap(A, B)

print("Setelah swap, bilangan A = ", A)
print("dan bilangan B = ", B)
