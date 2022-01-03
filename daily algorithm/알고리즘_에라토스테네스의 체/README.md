# 에라토스테네스의 체

-------------
## 1) 정의
> 소수판별 알고리즘으로 다른 알고리즘보다 시간복잡도가 유리하다.
-------------
## 2) 구현
<img src = "https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif">
   
100 이하의 소수를 판별하고 싶다면 10까지의 소수를 구한 후 소수들의 배수를 삭제한다.   
```python
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
```