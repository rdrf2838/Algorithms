import collections
from typing import Optional


class TrieNode():
    def __init__(self):
        self.children = dict()
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        u = self.root
        for w in word:
            if w not in u.children:
                u.children[w] = TrieNode()
            u = u.children[w]
        u.isWord = True

    def search(self, word: str) -> bool:
        u = self.root
        for i in range(len(word) + 1):
            if u is None:
                return False
            elif i == len(word):
                return u.isWord
            else:
                u = u.children.get(word[i])

    def startsWith(self, prefix: str) -> bool:
        u = self.root
        for i in range(len(prefix) + 1):
            if u is None:
                return False
            elif i == len(prefix):
                return True
            else:
                u = u.children.get(prefix[i])
