

min = 4
cart = {}
f = []

with open('product.txt', 'r',encoding='utf-8') as file:
    for line in file:
        if line.split()[0].isdigit():
            if int(line.split()[0]) in cart:
                cart[int(line.split()[0])].append(line.split()[1]) 
            else:
                cart[int(line.split()[0])] = [line.split()[1]]
            
            if not line.split()[1] in f:
                f.append(line.split()[1])

f.sort()

def go(f, k):
    newF = []

    if k == 0:
        for item in f:
            count = 0
            for transaction in cart.values():
                if item in transaction:
                    count += 1
            if count >= min:
                newF.append(item)
        return newF

    if k == 1:
        tempF = []
        
    
        for comb1 in range(len(f)):
            for comb2 in range (comb1 + 1, len(f)):
                tempF.append([f[comb1], f[comb2]])

        for combination in tempF:
            count = 0
            for transaction in cart.values():
                if combination[0] in transaction and combination[1] in transaction:
                    count += 1
            if count >= min:
                newF.append(combination)
        return newF
    
    if k == 2:
        tempF = []

        for comb1 in range(len(f)):
            for comb2 in range(comb1 + 1, len(f)):
                if f[comb1][0] == f[comb2][0] and f[comb1][1] != f[comb2][1]:
                    tempF.append([f[comb1][0], f[comb1][1], f[comb2][1]])

        for comb in tempF:
            count = 0
            for trans in cart.values():
                if comb[0] in trans and comb[1] in trans and comb[2] in trans:
                    count += 1
            if count >= min:
                newF.append(comb)
        return newF

    
def sup(f, k):
    if k == 1:
        for item in f:
            countAB = 0
            countA = 0
            countB = 0
            for trans in cart.values():
                if item[0] in trans and item[1] in trans:
                    countAB += 1
                if item[0] in trans:
                    countA += 1
                if item[1] in trans:
                    countB += 1
            S = round(countAB/len(cart), 3)
            C = round(countAB/countA, 3)
            L = round(C / (countB/len(cart)) , 3)
            print(item, S, C, L)

    if k == 2:
        for item in f:
            countAB = 0
            countA = 0
            countB = 0
            for trans in cart.values():
                if item[0] in trans and item[1] in trans and item[2] in trans:
                    countAB += 1
                if item[0] in trans and item[1] in trans:
                    countA += 1
                if item[2] in trans:
                    countB += 1
            S = round(countAB/len(cart), 3)
            C = round(countAB/countA, 3)
            L = round(C / (countB/len(cart)) , 3)
            print(item, S, C, L)


f = go(f, 0)
for item in f:
    print(item)
print("================================================")
f = go(f, 1)
sup(f, 1)
print("================================================")
f = go(f, 2)
sup(f, 2)
