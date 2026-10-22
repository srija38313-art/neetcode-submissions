class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s):04d}" + s)
        return "".join(encoded)    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            length = int(s[i:i+4])
            i += 4
            res.append(s[i:i+length])
            i += length
        return res    