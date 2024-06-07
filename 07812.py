arr = list(map(int,input().split()))

def greatest(array):
    array.sort()
    return array[-1]

print(greatest(arr))