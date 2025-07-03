from string import ascii_lowercase

class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) < k:
            word += "".join(
                ascii_lowercase[(ascii_lowercase.index(c) + 1) % 26] for c in word
            )

        return word[k - 1]
