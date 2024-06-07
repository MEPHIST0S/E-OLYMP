s = input().strip()
i, j = map(int, input().strip().split())

i -= 1
j -= 1

reversed = s[i:j+1][::-1]

s = s[:i] + reversed + s[j+1:]

print(s)