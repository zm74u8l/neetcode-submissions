from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()
        closing = [")", "]", "}"]

        if len(s)< 2:
            return False


        for i in s:

            if i in closing and stack:
                if stack.pop() != i:
                    return False
            else:
                if i == "[":
                    stack.append("]")                     
                elif i == "{":
                    stack.append("}")
                elif i == "(":
                    stack.append(")")
                else:
                    return False
            
        if not stack:
            return True 
        else:
            return False