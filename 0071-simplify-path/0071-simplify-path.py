class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directory = ""
        
        for c in path + "/":
            if c == "/":
                if directory == "..":
                    if stack:
                        stack.pop()
                elif directory != "" and directory != ".":
                    stack.append(directory)
                directory = ""
            else:
                directory += c
        return "/" + "/".join(stack)
                
        