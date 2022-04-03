# python 3.8+
from typing import List


def words_to_indices(words: List[str], word_list: List[str]) -> List[int]:
    wordlist.sort()
    return [wordlist.index(word) for word in words]


def indices_to_words(indices: List[int], word_list: List[str]) -> List[str]:
    wordlist.sort()
    return [wordlist[i] for i in indices]


if __name__ == '__main__':

    # Load the wordlist
    with open('wordlist.txt', 'r') as f:
        wordlist: List[str] = f.read().split('\n')
    if not (actual := len(wordlist)) == (expected := 1626):
        raise ValueError(f"ERROR: Expected wordlist length {expected} but got length {actual}. Wordlist:\n{wordlist}")

    # Example of indices_to_words:
    inds: List[int] = [2, 4, 6, 8, 1000]
    print(f"Indices: {inds}\ncorrespond to seed phrase: {indices_to_words(inds, wordlist)}\n\n")

    # Example of words_to_indices
    seed_phrase: List[str] = ['zero', 'slower', 'recipe', 'oxygen', 'ozone']
    print(f"Seed phrase: {seed_phrase}\ncorresponds to indices {words_to_indices(seed_phrase, wordlist)}")
