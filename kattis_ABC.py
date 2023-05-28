n = map(int, input().split())
seq = input()
m = {key: value for key, value in zip('ABC', sorted(n))}
print(*[m[i] for i in seq])