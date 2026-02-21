import sys

N, M = map(int, sys.stdin.readline().split())

not_hear = set()
not_see = set()

for _ in range(N):
    name = sys.stdin.readline().strip()
    not_hear.add(name)

for _ in range(M):
    name = sys.stdin.readline().strip()
    not_see.add(name)


not_hear_see = list(not_hear & not_see)
not_hear_see.sort()

print(len(not_hear_see))
print(*not_hear_see, sep="\n")
