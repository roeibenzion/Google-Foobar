import functools
def compare(s1, s2):
    l1 = [int(i) for i in str.split(s1, '.')]
    l2 = [int(i) for i in str.split(s2, '.')]
    n = min(len(l1), len(l2))
    for i in range(n):
        if l1[i] > l2[i]:
            return 1
        elif l1[i] < l2[i]:
            return -1
    if len(l1) > len(l2):
        return 1
    elif len(l1) < len(l2):
        return -1
    else:
        return 0
    

def solution(l):
    return sorted(l, key=functools.cmp_to_key(compare))

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
