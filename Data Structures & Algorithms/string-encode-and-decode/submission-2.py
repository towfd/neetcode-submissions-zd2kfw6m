class Solution:

    def encode(self, strs: List[str]) -> str:
        # Time Complexity: O(n), where n is the total number of characters across all strings.
        # Space Complexity: O(n), to store the newly created encoded string.
        
        # Explicitly handle the edge case of an empty list to distinguish [] from [""]
        if len(strs) == 0:
            return 'empty list'
        # Use a rare non-ASCII Unicode character (\u2556) as a delimiter.
        # This prevents the delimiter from conflicting with normal characters in the input strings.
        msg = '\u2556'.join(strs)
        return msg
    def decode(self, s: str) -> List[str]:
        # Time Complexity: O(n), where n is the length of the encoded string.
        # Space Complexity: O(n), to store the resulting list of strings.
        
        # Intercept the specific 'empty list' message and return an actual empty list
        if s == 'empty list':
            return []
            
        # Split the encoded string back into the original list using the same unique delimiter
        s_list = s.split('\u2556')
        return s_list 