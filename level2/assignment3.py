'''
Power Hungry

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. You and your team of henchmen has been assigned to repair the solar panels, but you can't take them all down at once without shutting down the space station (and all those pesky life support systems!).

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is. Write a function answer(xs) that takes a list of integers representing the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30. So answer([2,-3,1,0,-5]) will be "30".

Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the answer as a string representation of the number.

Languages

To provide a Python solution, edit solution.py To provide a Java solution, edit solution.java

Test cases

Inputs: (int list) xs = [2, 0, 2, 2, 0] Output: (string) "8"

Inputs: (int list) xs = [-2, -3, 4, -5] Output: (string) "60"

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
'''


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
