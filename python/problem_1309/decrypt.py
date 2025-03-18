#!/usr/bin/env python3

class Solution:
    """Leetcode 1309: Decrypt String from Alphabet to Integer Mapping

    You are given a string s formed by digits and '#'. We want to map s
    to English lowercase characters as follows:

    Characters ('a' to 'i') are represented by ('1' to '9')
        respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#')
        respectively.
    Return the string formed after mapping.

    The test cases are generated so that a unique mapping will always exist.

    Example 1:
        Input: s = "10#11#12"
        Output: "jkab"
        Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

    Example 2:
        Input: s = "1326#"
        Output: "acz"

    Constraints:
        1 <= s.length <= 1000
        s consists of digits and the '#' letter.
        s will be a valid string such that mapping is always possible.
    """

    def decryptString(self, s: str) -> str:
        """Function to decrypt a string with Alphabet to Integer Mapping.

        How it works:
            Since the encryption codes come in two lengths, we want to
            be able to increment the index dynamically, depending on
            the case. For this reason, we use a while loop to traverse
            s, since it will allow for easy manipulation of the looping
            index.

            For each character in the loop, a check is performed to see
            if two indeces ahead is a '#'. If a '#' is two indeces
            ahead, we know that the characters at the current and next
            indeces form our encryption code. Otherwise, the current
            character is the encryption code.

            With the encryption code in hand, we then need to increment
            the index correctly - by 3 for double-digit codes (which
            always end with a '#') and by 1 for single-digit codes
            (which never end with a '#').

            Finally, since the encryption codes conveniently represent
            the positions of their alphabetical counterparts, we can
            use the built-in chr() to grab the correct character in
            ASCII. The letter 'a' starts at 97, so we just need to add
            96 to the encryption code, plug it into chr(), and append
            the returned value into the result string.
        """

        result = ""

        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                code = int(s[i:i + 2])
                i += 3
            else:
                code = int(s[i])
                i += 1

            result += chr(code + 96)

        return result
