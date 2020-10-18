class Solution(object):
    def letterCombinations(self, digits):
        def helper(digits, digit, partial, result):
            if digit == len(digits):
                result.append(partial)
            else:
                for i in range(len(mapping[digits[digit]])):
                    c = mapping[digits[digit]][i]
                    partial += c
                    helper(digits, digit+1, partial, result)
        result = []
        partial = ''
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        helper(digits, 0, partial, result)
        return result
