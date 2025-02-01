import sys
input = sys.stdin.readline

n, m = map(int,(input().split())) # 수열의 개수, 나누어 떨어져야 하는 수

A = list(map(int,input().split())) # 원본 리스트

S = [0] * n # 합 배열

C = [0] * m # 나머지 인덱스 카운트

answer = 0 # 정답

# 합 배열
for i in range(n):
    S[i] = S[i-1] + A[i]


for i in range(n):
    remainer = S[i] % m # % 연산
    if remainer == 0: # 0~i까지 구간 합 자체가 0일 때 정답에 대하기
        answer += 1
    C[remainer] += 1 # 나머지가 같은 인덱스의 개수 값 증가시키기


for i in range(m):
    if C[i] > 1:
        answer += (C[i]*(C[i]-1) // 2)

print(answer)




