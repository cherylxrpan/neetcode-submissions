class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_number = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(i, characters):
            if len(characters) == len(digits):
                res.append(characters)
                return
            for c in phone_number[digits[i]]:
                backtrack(i+1, characters + c)

        if digits:
            backtrack(0, "")

        return res