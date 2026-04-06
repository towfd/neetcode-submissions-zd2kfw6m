class Solution:

    def encode(self, strs: List[str]) -> str:
        # Time Complexity: O(N), where N is the total number of characters across all strings.
        # Space Complexity: O(N), to store the encoded string components in the list.
        
        # Explicitly handle the edge case of an empty list to distinguish [] from [""]
        if len(strs) == 0:
                return 'empty list'
                
        msg = []
        for stri in strs:
            # Format: "length#string_content". 
            # This ensures safe decoding regardless of what special characters the string contains.
            msg.append(f'{len(stri)}' + '#' + stri)
            
        # Using ''.join() is highly optimized in Python for string concatenation
        return ''.join(msg)

    def decode(self, s: str) -> List[str]:
        # Time Complexity: O(N), where N is the length of the encoded string.
        # Space Complexity: O(N), to store the decoded strings in the result list.
        
        # Intercept the specific 'empty list' message and return an actual empty list
        if s == 'empty list':
            return []
            
        msg = []
        i = 0  # Main pointer (i) tracks the start of the current string's length integer
        
        while i < len(s):
            j = i  # Explorer pointer (j) starts from i to find the delimiter '#'
            while s[j] != '#':
                j += 1
            
            # Extract the length of the string using the slice between i and j
            length = int(s[i: j])
            
            # Extract the actual string content precisely using the parsed length
            msg.append(s[j + 1: j + 1 + length])
            
            # Jump the main pointer directly to the start of the next encoded string
            i = j + 1 + length
            
        return msg