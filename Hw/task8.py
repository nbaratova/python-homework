a = 2
b = 4
c = 3
d = 7

# for i in range(a-1, b + 1):
#     matrix = [str(i)]
#     for j in range(c, d + 1):
#         if i == a-1:
#             matrix[0] = " "
#             matrix.append(str(j))
#         else:
#             matrix.append(str(i * j))
#     print("  ".join(matrix))


for i in range(a - 1, b + 1):
    if i == 1:
        print(" ", end="\t")
    else:
        print(i, end="\t")
    for j in range(c, d + 1):
        if i == a - 1:
            print(j, end="\t")
        else:
            print(i * j, end="\t")
    print()
