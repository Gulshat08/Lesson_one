pol = input()
pol1 = pol[0]
pol2 = pol[1]
pol2 = int(pol2)
k = 0
for i in range(ord(pol1)-96):
    for j in range(pol2):
        k += 1
    if (k % 2) == 0:
        print("black")
    else:
        print("white")
