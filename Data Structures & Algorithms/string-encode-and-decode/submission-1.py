class Solution:

    def encode(self, strs: List[str]) -> str:
        # brute solution
        # use ' '.join to turn strs list into string
        if len(strs) == 0:
            return 'empty list'
        msg = '\u2556'.join(strs)
        return msg
    def decode(self, s: str) -> List[str]:
        # use .split cut string back to list
        if s == 'empty list':
            return []
        s_list = s.split('\u2556')
        return s_list 