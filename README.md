# mnemonic-encoder-decoder

Inspired by this reddit
post: https://www.reddit.com/r/Monero/comments/ttvn6a/a_printable_mnemonic_monero_word_list_with_numbers/

Encoder / decoder: https://github.com/Mitchellpkt/mnemonic-encoder-decoder/blob/main/encoder_decoder.py

Example use:

```
# Load the wordlist
with open('wordlist.txt', 'r') as f:
    wordlist: List[str] = f.read().split('\n')
if not (actual := len(wordlist)) == (expected := 1626):
    raise ValueError(f"ERROR: Expected wordlist length {expected} but got length {actual}. Wordlist:\n{wordlist}")

# Example of indices_to_words:
inds: List[int] = [2, 4, 6, 8, 1000]
print(f"--\nIndices: {inds}\nmap to seed phrase: {indices_to_words(inds, wordlist)}\n")

# Example of words_to_indices:
seed_phrase: List[str] = ['zero', 'slower', 'recipe', 'oxygen', 'ozone']
print(f"--\nSeed phrase: {seed_phrase}\nmaps to indices: {words_to_indices(seed_phrase, wordlist)}")
```

Example output:

```
--
Indices: [2, 4, 6, 8, 1000]
map to seed phrase: ['abducts', 'ablaze', 'abort', 'absorb', 'opacity']

--
Seed phrase: ['zero', 'slower', 'recipe', 'oxygen', 'ozone']
maps to indices: [1618, 1278, 1146, 1029, 1031]
```
