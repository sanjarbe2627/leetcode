# 1768 You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# Example 1: # Input: word1 = "abc", word2 = "pqr" # Output: "apbqcr"
# Example 2: # Input: word1 = "ab", word2 = "pqrs" # Output: "apbqrs"

class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = []
        i = 0
        while i < len(word1) and i < len(word2):
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1
        merged.append(word1[i:])
        merged.append(word2[i:])

        return ''.join(merged)


data = Solution()

print(data.mergeAlternately("ABABAB", "ABAB"))