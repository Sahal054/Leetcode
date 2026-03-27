"""

so to find out how this works we use a combination of both a stack and a hasmap 

we put in all the closing brackets in the hasmap. and we scan through the string and if there a opening bracket we add that to the stack. 

when we find a closing braket then, we will  check stack[-1] if thats the same was the value of the closing bracket then we pop.


eg. (([))] 


Step,Char (c),Action,Stack State,Result
1,(,Not in hashmap keys.,['('],Push to stack.
2,(,Not in hashmap keys.,"['(', '(']",Push to stack.
3,[,Not in hashmap keys.,"['(', '(', '[']",Push to stack.
4,),Is in hashmap keys!,"['(', '(', '[']",Check Match...\


The Moment of Failure (Step 4)
This is where the code detects the error. Let's look at the logic on Line 8:
if stack and stack[-1] == hashmap[c]:

Is the stack empty? No, it has 3 items.

What is stack[-1]? This looks at the very top (the last item added), which is [.

What is hashmap[')']? According to your dictionary, a ) expects to find a ( at the top of the stack.

The Comparison: Does [ equal (?

No. Because they don't match, the code enters the else block on Line 11 and immediately executes:




"""


class Solution(object):
    def isValid(self, s):
        stack = []
        hashmap = {")":"(","]":"[","}":"{"}

        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False                                