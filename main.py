import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))


def solution(now):
    if len(now) == M:
        print(' '.join(map(str, now)))
        return
    for number in numbers:
        if number in now:
            continue
        solution(now + [number])


solution([])