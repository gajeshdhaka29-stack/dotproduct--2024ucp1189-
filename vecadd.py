n = int(input("Enter the number of elements in each vector: "))

print("Enter elements of the first vector:")
v1 = [float(input()) for _ in range(n)]


print("Enter elements of the second vector:")
v2 = [float(input()) for _ in range(n)]


dot_product = sum(v1[i] * v2[i] for i in range(n))

print("Dot product is :", dot_product)


