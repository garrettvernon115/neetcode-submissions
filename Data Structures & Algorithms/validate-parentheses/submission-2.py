class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets
        stack = []
        
        # Map closing brackets to their matching opening brackets
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        # Check each character in the string
        for c in s:
            # If it's a closing bracket
            if c in closeToOpen:
                # Check if it matches the most recent opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # Valid match, remove from stack
                else: 
                    return False # No match or empty stack
            else:
                # It's an opening bracket, add to stack
                stack.append(c)

        # Valid if all brackets were matched (stack is empty)
        return True if not stack else False