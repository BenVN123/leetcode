class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}
        for product in products:
            space = trie 
            for letter in product:
                if not space.get(letter):
                    space[letter] = {"words": []}
                space = space[letter]
                w_len = len(space["words"])
                i = 0
                while i < w_len and product > space["words"][i]:
                    i += 1
                if i < 3:
                    space["words"].insert(i, product)

        space = trie
        res = []
        for s in searchWord:
            curr = []
            if space.get(s):
                space = space[s]
                curr = space["words"][:3]
            else:
                space = {}
            res.append(curr)
        return res
