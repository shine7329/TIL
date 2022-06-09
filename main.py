import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
M = int(input())
if M:
    brokens = set(input().split())
else:
    brokens = set()
answer = abs(N - 100)

for number in range(1000001):
    for temp in str(number):
        if temp in brokens:
            break
    else:
        answer = min(answer, len(str(number)) + abs(number - N))

print(answer)
