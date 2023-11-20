def find_couple(l, i):
    y = l[i]
    count = 0
    for j in range(i+1, len(l)):
        if l[j] % y == 0:
            count+=1
    return count

        

def solution(l):
    #Notice - x*q = y and y*p = z => x*q*p = z.
    couples = [0 for _ in range(len(l))]
    count = 0
    for i in range(len(l)-2, -1, -1):
        couples[i] = (find_couple(l, i))
    
    for j in range(len(l)-1):
        for k in range(j+1, len(l)):
            if l[k]%l[j] == 0:
                count+=couples[k]

    return count
        

