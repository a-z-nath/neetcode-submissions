class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in "[{(":
                match c:
                    case "[":
                        st.append("]")
                    case "{":
                        st.append("}")
                    case "(":
                        st.append(")")
            elif len(st) > 0 and c == st[-1]:
                st.pop()
            else:
                return False
            
        
        return True if len(st) == 0 else False