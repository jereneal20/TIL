class Solution:
    def simplifyPath(self, path: str) -> str:
        path = self.remove_redundant_slashes(path)
        path = self.apply_dot_dot(path)
        return "/" + path
    
    
    def remove_redundant_slashes(self, path):
        return "/".join(p for p in path.split('/') if p != "" and p != ".")
    
    def apply_dot_dot(self, path): 
        stk = []
        for p in path.split('/'):
            if p == "..":
                if len(stk) == 0:
                    continue
                stk.pop()
                continue
            stk.append(p)
        return "/".join(stk)