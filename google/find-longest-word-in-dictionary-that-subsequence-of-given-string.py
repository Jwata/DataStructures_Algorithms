# https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string/
# Subsequence(Wikipedia): https://en.wikipedia.org/wiki/Subsequence

# brute force
def find_longest_word(string, dictionary):
    str_len = len(string)
    word_len = 1
    count = 0
    longest_word = None
    while word_len < str_len:
        print(str_len, word_len, str_len - word_len + 1)
        for i in range(0, str_len - word_len + 1):
            start = i
            end = i + word_len - 1
            print(string[start:end])
            if string[start:end] in dictionary:
                longest_word = string[start:end]
        word_len += 1

    return longest_word


string = 'abppplee'
dictionary = set(['able', 'ale', 'apple', 'bale', 'kangaroo'])
print(find_longest_word(string, dictionary))

## Brute force approach
#
# a
#  b
#   p
#    p
#     p
#      l
#       e
#        e
# ab
#  bp
#   pp
#    pp
#     pl
#      le
#       ee
# abp
#
#   ...
#
# abppple
#  bppplee
#
# Complexity: (2 + 3 + .... + n ) * (n - 1) / 2 = O(n^2)
