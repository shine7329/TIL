import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
game = []
for _ in range(N):
    game.append(list(map(int, input().split())))

max_game = game[0][:]
min_game = game[0][:]

for index in range(1, N):
    max_game_temp = [0, 0, 0]
    min_game_temp = [0, 0, 0]

    max_game_temp[0] += game[index][0] + max(max_game[0:2])
    max_game_temp[1] += game[index][1] + max(max_game[0:3])
    max_game_temp[2] += game[index][2] + max(max_game[1:3])

    min_game_temp[0] += game[index][0] + min(min_game[0:2])
    min_game_temp[1] += game[index][1] + min(min_game[0:3])
    min_game_temp[2] += game[index][2] + min(min_game[1:3])

    max_game = max_game_temp
    min_game = min_game_temp


print(max(max_game), min(min_game))