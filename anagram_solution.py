# This function solves the anagram program in O(n) time by
# counting the occurrence of each letter in the two strings.
# It is a classic "time vs. memory" trade-off, requiring more
# space than other solutions, but taking less time.

def anagram_solver(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagram_solver('apple','pleip'))