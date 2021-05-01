N = int(input())
arrN = sorted(list(map(int,input().split())), reverse=True)
M = int(input())
arrM = sorted(list(map(int,input().split())), reverse=True)

if arrN[0] < arrM[0]:
    print(-1)
else:
    count=0
    while arrM:
        count+=1
        for i in arrN:
            if not arrM:
                break
            else:
                for j in range(len(arrM)):
                    if arrM[j] <= i:
                        arrM.pop(j)
                        break
    print(count)