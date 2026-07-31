class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)

        if n%2 == 1:
            return False

        st = []
        
        for curr in list(s):
            if curr == '{' or curr == '[' or curr == '(':
                st.append(curr)
            else:
                if len(st) == 0:
                    return False
                top=st.pop()

                if curr==']' and top!="[":
                    return False
                
                elif curr=='}' and top!="{":
                    return False

                elif curr==')' and top!="(":
                    return False
        
        return len(st)==0
        
