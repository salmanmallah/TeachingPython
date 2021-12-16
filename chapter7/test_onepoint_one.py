"""
    CHAPTER 7
    TUTORIAL NO. 122

        Word counter with dictionary.
        word = salman
        {s: 1, a : 2, l: 1, m: 1, n: 1}
"""


def word_counter(word):
    empty_dict = {}
    for i in word:
        empty_dict[i] = word.count(i)
    return empty_dict


print(
    word_counter('salmanmallah')
)