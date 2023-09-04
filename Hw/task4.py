a = 60
i = 1
divisors = []
count = 1
for i in range(1, a + 1):
    if a % i == 0:
        divisors.append(i)
    i += 1
print(divisors)
