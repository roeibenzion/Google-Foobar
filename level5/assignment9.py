'''
Disorderly Escape
=================
Oh no! You've managed to free the bunny workers and escape Commander Lambdas exploding space station, but Lambda's team of elite starfighters has flanked your ship. 
If you dont jump to hyperspace, and fast, youll be shot out of the sky!

Problem is, to avoid detection by galactic law enforcement, Commander Lambda planted the space station in the middle of a quasar quantum flux field. 
In order to make the jump to hyperspace, you need to know the configuration of celestial bodies in the quadrant you plan to jump through. In order to do *that*, you need to figure out how many configurations each quadrant could possibly have, so that you can pick the optimal quadrant through which youll make your jump.

There's something important to note about quasar quantum flux fields' configurations: when drawn on a star grid, configurations are considered equivalent by grouping 
rather than by order. That is, for a given set of configurations, if you exchange the position of any two columns or any two rows some number of times, 
youll find that all of those configurations are equivalent in that way -- in grouping, rather than order.

Write a function solution(w, h, s) that takes 3 integers and returns the number of unique, non-equivalent configurations that can be found on a star 
grid w blocks wide and h blocks tall where each celestial body has s possible states. Equivalency is defined as above: any two star grids with each celestial body 
in the same state where the actual order of the rows and columns do not matter (and can thus be freely swapped around). 
Star grid standardization means that the width and height of the grid will always be between 1 and 12, inclusive. And while there are a variety of celestial bodies 
in each grid, the number of states of those bodies is between 2 and 20, inclusive. The solution can be over 20 digits long, so return it as a decimal string. 
The intermediate values can also be large, so you will likely need to use at least 64-bit integers.

For example, consider w=2, h=2, s=2. We have a 2x2 grid where each celestial body is either in state 0 (for instance, silent) or state 1 (for instance, noisy). 
We can examine which grids are equivalent by swapping rows and columns.

00
00

In the above configuration, all celestial bodies are "silent" - that is, they have a state of 0 - so any swap of row or column would keep it in the same state.

00 00 01 10
01 10 00 00

1 celestial body is emitting noise - that is, has a state of 1 - so swapping rows and columns can put it in any of the 4 positions. 
All four of the above configurations are equivalent.

00 11
11 00

2 celestial bodies are emitting noise side-by-side. Swapping columns leaves them unchanged, and swapping rows simply moves them between the top and bottom. 
In both, the *groupings* are the same: one row with two bodies in state 0, one row with two bodies in state 1, and two columns with one of each state.

01 10
01 10

2 noisy celestial bodies adjacent vertically. This is symmetric to the side-by-side case, but it is different because there's no way to transpose the grid.

01 10
10 01

2 noisy celestial bodies diagonally. Both have 2 rows and 2 columns that have one of each state, so they are equivalent to each other.

01 10 11 11
11 11 01 10

3 noisy celestial bodies, similar to the case where only one of four is noisy.

11
11

4 noisy celestial bodies.

There are 7 distinct, non-equivalent grids in total, so solution(2, 2, 2) would return 7.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(2, 2, 2)
Output:
    7

Input:
Solution.solution(2, 3, 4)
Output:
    430

-- Python cases --
Input:
solution.solution(2, 3, 4)
Output:
    430

Input:
solution.solution(2, 2, 2)
Output:
    7
'''


from __future__ import division
import math
from decimal import Decimal , getcontext, ROUND_DOWN
from copy import deepcopy

getcontext().prec = 1000

def round_if_almost_whole(number):
    decimal_number = Decimal(str(number))  # Convert the input to Decimal
    # Check if the fractional part is very close to 1 (within a small tolerance)
    if abs(decimal_number % 1 - 1) < Decimal('1e-10'):
        # Round up using ROUND_HALF_UP strategy
        return decimal_number.quantize(Decimal('1'), rounding='ROUND_HALF_UP')
    else:
        # No rounding needed
        return decimal_number

def factorial_precision(n):
    '''
    Returns n! with precision
    '''
    result = Decimal(1)
    for i in range(1, n+1):
        result *= Decimal(i)
    return result
class Polynomial:
    def __init__(self, terms=None):
        """
        The polynomial is represented as a list of tuples, where each tuple contains a coefficient
        and a dictionary representing the powers of each variable.
        """
        if terms is None:
            terms = []
        self.terms = terms

    def __mul__(self, other):
        result = Polynomial()
        for term1 in self.terms:
            for term2 in other.terms:
                new_term = Decimal(term1[0]) * Decimal(term2[0])
                new_powers = {i: term1[1].get(i, 0) + term2[1].get(i, 0) for i in set(term1[1]) | set(term2[1])}
                result.terms.append((new_term, new_powers))
        return result

    def __add__(self, other):
        result = Polynomial(deepcopy(self.terms))
        for term2 in other.terms:
            found = False
            for i, term1 in enumerate(result.terms):
                if term1[1] == term2[1]:
                    result.terms[i] = (term1[0] + term2[0], term1[1])
                    found = True
                    break
            if not found:
                result.terms.append(term2)
        return result

    def __pow__(self, exponent):
        result = Polynomial([(1, {})])
        for _ in range(exponent):
            result *= self
        return result
    
    def divide_by_constant(self, constant):
        """
        Divide each term's coefficient by the given constant.
        """
        result = Polynomial()
        for term in self.terms:
            new_coefficient = Decimal(term[0]) / Decimal(constant)
            new_powers = deepcopy(term[1])
            result.terms.append((new_coefficient, new_powers))
        return result
    
    def evaluate(self, value):
        """
        Evaluate the polynomial by substituting each variable with the given value.
        """
        result = 0
        for term in self.terms:
            term_result = term[0]
            for _, power in term[1].items():
                term_result *= value ** power
            result += term_result

        result = round_if_almost_whole(result)
        return str(int(result))
      
    
def generate_sums(n, sums=None, coeffs=None, curr=0, curr_sum = None):
    '''
    Input n: number of elements to sum
    Input s: number of states
    Input sums: list of sums
    Input coeffs: list of coefficients, when eventually the sum of the coefficients is n, we add the sum to sums
    Input curr: current index of coeffs

    output sums: list of sums representing all sums in the form j1 + 2j2 + 3j3 + ... + njn = n when ji in [0...s]
    '''
    if sums is None:
        sums = []
    if coeffs is None:
        coeffs = []
    if curr_sum is None:
        curr_sum = []

    if curr == n:
        if sum(curr_sum) == n:
            sums.append(deepcopy(coeffs))
        return sums
    
    if sum(curr_sum) > n:
        return sums
    
    for i in range(n+1):
        new_coeffs = coeffs + [i]
        new_curr_sum = curr_sum + [i * (curr + 1)]
        generate_sums(n, sums, new_coeffs, curr + 1, new_curr_sum)

    return sums

def cycle_index_s_n(n):
    '''
    input s: number of states
    input n: number of elements to sum

    output: polynomial representing the cycle index of the symmetric group S_n
    '''
    sums = generate_sums(n)
    cycle_index_s_n = Polynomial()
    for comb in sums:
        #polynomial of n variables
        monomial = {}
        denominator = 1
        for j in range(1, n+1):
            if comb[j-1] != 0:
                #the variable term j in poly xj is now xj^comb[j-1]
                monomial[j] = comb[j-1]
                denominator *= Decimal(factorial_precision(comb[j-1])) * Decimal(j)**comb[j-1]
                
        poly = Polynomial([(1, monomial)])    
        cycle_index_s_n += poly.divide_by_constant(denominator)
    return cycle_index_s_n

def euclid(a, b):
    if b == 0:
        return a
    return Decimal(euclid(b, a % b))

def lcm(a, b):
    return a * b // Decimal(euclid(a, b))

def get_variables(poly):
    '''
    Returns vars and their powers
    '''
    variables = {}
    for term in poly:
        for var, power in term[1].items():
            variables[var] = power
    return variables

def get_monomials(poly):
    return [term for term in poly.terms]

def pair_wei_xu(l, m, power_var1, power_var2):
    '''
    Special multiplication from the paper, equation 2.8
    Input: 2 variables, one from each polynomial
    Output: 1 variable represented as index and power
    '''
    lcm_l_m = lcm(l, m)
    power = l*power_var1*m*power_var2 // lcm_l_m
    idx = lcm_l_m
    return (idx, power)

def multiplication_wei_xu(poly1, poly2):
    '''
    Implementation of the multiplication algorithm by Wei Xu
    '''
    result = Polynomial()
    for monomial1 in get_monomials(poly1):
        for monomial2 in get_monomials(poly2):
            coefficient = Decimal(monomial1[0]) * Decimal(monomial2[0])
            new_monomial = {}
            variables1 = get_variables([monomial1])
            variables2 = get_variables([monomial2])
            for var1, power_var1 in variables1.items():
                for var2, power_var2 in variables2.items():
                    idx, power = pair_wei_xu(Decimal(var1), Decimal(var2), Decimal(power_var1), Decimal(power_var2))
                    new_monomial[idx] = Decimal(new_monomial.get(idx, 0)) + Decimal(power)
            result.terms.append((coefficient, new_monomial))
    return result
            
 
def solution(w, h, s):
    '''
    using Poyla's theorem.

    Input w: width of grid
    Input h: height of grid
    Input s: number of states

    Output: number of unique, non-equivalent configurations that can be found on a star grid w blocks wide and h blocks tall where each celestial body has s possible states 
    ''' 
    if s == 0 or s == 1:
        #all equivalent
        return str(s)
    
    elif w == 1 or h == 1:
        #we have a line, the number of configurations is cycle_index_s_n(max(w,h))
        return cycle_index_s_n(max(w,h)).evaluate(s)
    
    index_w = cycle_index_s_n(w)
    if w == h:
        index_h = deepcopy(index_w)
    else:
        index_h = cycle_index_s_n(h)
    index_w_h = multiplication_wei_xu(index_w, index_h)
    result = index_w_h.evaluate(s)
    
    return result
