class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
                return 'empty list'
        msg = []
        for stri in strs:
            msg.append(f'{len(stri)}' + '#' + stri)
        return ''.join(msg)
    def decode(self, s: str) -> List[str]:
        if s == 'empty list':
            return []
        msg = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i: j])
            msg.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return msg