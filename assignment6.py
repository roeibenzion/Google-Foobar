def compare_large_numbers(s, t):
    # Compare the lengths of the numbers first
    if len(s) < len(t):
        return -1
    elif len(s) > len(t):
        return 1

    # If lengths are equal, compare the numbers character by character
    for i in range(len(s)):
        if s[i] < t[i]:
            return -1
        elif s[i] > t[i]:
            return 1

    return 0  # Numbers are equal


def solution(M, F):
    #The observation is that the numbers has to be coprime.
    #If they are not, after backward cycles we'll get to M=F, there is no solution from there.
    #Thus we run the Euclidean algorithm, and count how many steps.
    count = -1
    comp = compare_large_numbers(M, F)
    if comp == -1:
        M, F = F, M
    while F != '0':
        count += int(M)//int(F)
        M, F = F, str(int(M)%(int(F)))
    if M == '1':
        return str(count)
    return 'impossible'


'''
print(solution('4','7'))

print(solution('2','1'))

print(solution('2','4'))
'''

print(solution('9', '17'))