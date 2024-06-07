class Solution:
    def isValid(self, s: str) -> bool:
        #to keep track of opening parentheses
        stack = []

        #create a mapping 
        mapping_this = {')': '(', ']' : '[', '}': '{'}

        #iterate each character in the string

        for character in s:
            #if the character is closing parentheses
            if character in mapping_this:
                #pop the top element from the stack
                top_element = stack.pop() if stack else '#'

                #the closing parentheses must match the top_element
                if mapping_this[character] != top_element:
                    return False

            else:
                stack.append(character)
        #if the stack is empty and all parentheses properly closed
        return not stack