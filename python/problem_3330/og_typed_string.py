class Solution:
    def possibleStringCount(self, word: str) -> int:
        n, count = len(word), 1

        for index in range(1, n):
            if word[index - 1] == word[index]:
                count += 1

        return count
