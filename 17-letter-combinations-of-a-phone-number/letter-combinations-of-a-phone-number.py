class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res=[]
        def help(i,tem):
            if len(tem)==len(digits):
                res.append(tem)
                return
            for ch in digit_to_letters[digits[i]]:
                help(i+1,tem+ch)
        help(0,"")
        return res

        