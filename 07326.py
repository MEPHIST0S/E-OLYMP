def GreatestNum(train):
    greatest = 0
    curr = 0
    
    for i in range(len(train)):
        if train[i] == "k":
            curr += 1
            if curr > greatest:
                greatest = curr
        else:
            curr = 0
            
    return greatest

train = input()
print(GreatestNum(train))