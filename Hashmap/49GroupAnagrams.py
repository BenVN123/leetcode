class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            key = "".join(sorted(i))
            if not hashmap.get(key):
                hashmap[key] = []
            hashmap[key].append(i)
        
        return list(hashmap.values())
