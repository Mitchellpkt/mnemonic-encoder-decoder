# python 3.8+
# (NEVER type any seed into a device that you do not know to be secure)
from typing import List


def words_to_indices(words: List[str], word_list: List[str], index_from: int = 1) -> List[int]:
    word_list.sort()
    return [wordlist.index(word) + index_from for word in words]


def indices_to_words(indices: List[int], word_list: List[str], index_from: int = 1) -> List[str]:
    word_list.sort()
    return [wordlist[i - index_from] for i in indices]


if __name__ == '__main__':
    lowest_index: int = 1  # determine whether to count (0, 1, 2, ...) or (1, 2, 3, ...)

    # Load the wordlist
    with open('wordlist.txt', 'r') as f:
        wordlist: List[str] = f.read().split('\n')
    if not (actual := len(wordlist)) == (expected := 1626):
        raise ValueError(f"ERROR: Expected wordlist length {expected} but got length {actual}.")

    # Example of indices_to_words:
    inds: List[int] = [2, 4, 6, 8, 1000]
    print(f"--\nIndices: {inds}\nmap to seed phrase: {indices_to_words(inds, wordlist, lowest_index)}\n")

    # Example of words_to_indices
    seed_phrase: List[str] = ['zero', 'slower', 'recipe', 'oxygen', 'ozone']
    print(f"--\nSeed phrase: {seed_phrase}\nmaps to indices: {words_to_indices(seed_phrase, wordlist, lowest_index)}")

    # Little test showing that you get the same result mapping from indices to words and back
    assert words_to_indices(indices_to_words([1, 3, 4, 500, 1200], word_list=wordlist), word_list=wordlist)
