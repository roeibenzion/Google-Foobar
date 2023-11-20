#find the subset with maxsimum product.
    #Observation 1 - always want to take positive numbers.
    #Observation 2 - want to take even number of negative numebrs.
    #Obviously never take 0 (unless the array leaves no choise).
    #Reduce the taks to find the maxs multiply of negative numbers.
    #Consider the list of negatives a1, a2, ... ,an.
    #If n is even - take them all.
    #If n is odd - remove ai such that |ai| <= |aj| for all other j's.




def multiply_str(s, xs):
    res = ''
    carry = 0
    sign = ''
    if s[0] == '-':
        s = s[1:]
        sign = '-'
    if xs < 0:
        xs = abs(xs)
        if sign == '-':
            sign = ''
        else: 
            sign = '-'
    for i in range(len(s)-1, -1, -1):
        temp = int(s[i]) * xs + carry
        res = str(temp %10) + res
        carry = temp//10
    if carry > 0:
         res = str(carry) + res
    return sign + res

def find_count_min(xs):
    min_negative = float('-inf')
    max_positive = float('-inf')
    count_negative = 0
    for i in range(len(xs)):
        if xs[i] < 0:
            min_negative = max(xs[i], min_negative)
            count_negative += 1
        elif xs[i] > max_positive:
            max_positive = xs[i]
    return min_negative, count_negative, max_positive
def solution(xs):
    prod = '0'
    min_negative, count_negative, max_positive = find_count_min(xs)
    if max_positive == 0:
        return '0'
    if max_positive < 0:
        return str(min_negative)
    found = False
    for i in range(len(xs)):
        if xs[i] != 0:
            if prod == '0':
                prod = '1'
        if (xs[i] == min_negative) and (not found) and (count_negative %2 == 1):
            found = not found
        else:
            if xs[i] != 0:
                prod = multiply_str(prod, xs[i])
    return str(prod)


print(solution([0,-1]))
print(solution([-1]))