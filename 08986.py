def Spacing(string, f, l):
    beginning = string[:f]
    end = string[l+1:]
    return beginning + end

string = input()
f, l = map(int, input().split())
print(Spacing(string, f, l))