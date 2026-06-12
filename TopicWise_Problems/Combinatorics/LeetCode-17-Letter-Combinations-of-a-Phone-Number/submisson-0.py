from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = { 2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 
                 5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 
                 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"] }

        res = [""]
        for digit in digits:
            temp = mapping.get(int(digit))
            res = ["".join(p) for p in product(res, temp)]

        return res
    

# Time Complexity: O(4^N) since the maximum number of letters for any digit is 4 (for digits 7 and 9), and we are generating combinations for N digits.
# Space Complexity: O(4^N) for the output list of combinations.
'''
The idea is to use a mapping of digits to their corresponding letters based on a phone keypad.
We start with a list containing an empty string as the initial combination.
For each digit in the input string, we retrieve the corresponding letters from the mapping and 
create new combinations by taking the Cartesian product of the existing combinations and the new letters.
We use the itertools.product function to generate all possible combinations of the existing combinations 
and the new letters.
Finally, we return the list of combinations as the result.
'''