# python 3.8+
from typing import List

prefix_length: int = 3
wordlist_path: str = 'wordlist.txt'

with open(wordlist_path, 'r') as f:
    wordlist: List[str] = f.read().split('\n')

prefixes: List[str] = [word[:prefix_length] for word in wordlist]
unique_prefixes: List[str] = list(set(prefixes))

if len(prefixes) != len(unique_prefixes):
    print(f"WARNING: Found {len(prefixes) - len(unique_prefixes)} prefix collisions!")
else:
    print("No duplicate prefixes found!")