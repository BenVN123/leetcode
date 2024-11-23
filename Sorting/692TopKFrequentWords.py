class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[0], reverse=True)
        sorted_freq = zip(*sorted(sorted_freq, key=lambda x: x[1]))[0] 
        return sorted_freq[:-k - 1: -1]
