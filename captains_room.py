# HackerRank Task: Captain's Room

k = int(input())
rooms = list(map(int, input().split()))
r_s = set(rooms)

out = ((k * (sum(r_s))) - sum(rooms)) // (k - 1)
print(out)
