class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch in ['(', '{', '[']:
                st.append(ch)
            else:
                if ch == ')':
                    if not st or st[-1] != '(': return False
                    st.pop()
                if ch == '}':
                    if not st or st[-1] != '{': return False
                    st.pop()
                if ch == ']':
                    if not st or st[-1] != '[': return False
                    st.pop()
        return not st
                