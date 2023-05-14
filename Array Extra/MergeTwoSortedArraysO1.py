# Approach 1 use extra arr 

# Approach 2

def sortList(a1, a2):
    for i in range(len(a1)):
        for j in range(len(a2)):
            if a1[i]>a2[j]:
                a1[i], a2[j] = a2[j], a1[i]
                break
        a2.sort()

    print(a1)
    print(a2)



a1, a2 = [], []
for i in range(int(input())):
    a1.append(int(input()))

for i in range(int(input())):
    a2.append(int(input()))
sortList(a1, a2)