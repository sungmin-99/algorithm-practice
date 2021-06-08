def painting(x,y):
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if bw1[i][j] != graph[x+i][y+j]:
                cnt1 += 1
            else:
                cnt2 += 1
    return min(cnt1,cnt2)

m, n = map(int,input().split())
graph = []
for _ in range(m):
    graph.append(input())
bw1 = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']

ans = painting(0,0)
for i in range(m-7):
    for j in range(n-7):
        ans = min(ans, painting(i,j))
print(ans)