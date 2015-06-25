# https://algospot.com/judge/problem/read/BRACKETS2

n = int(input())

for i in range(n):
    input_str = input()

    # Make an empty queue
    q = []
    answer="YES"

    # Iterate through the string
    for char in input_str:

        # Opening parenthesis
        if char in ['(', '[', '{']:
            q.append(char)

        # Closing parenthesis, but nothing's left
        elif len(q)==0:
            answer="NO"
            break

        # Matching cases
        elif char==')' and q[-1]=='(':
            q.pop()
        elif char==']' and q[-1]=='[':
            q.pop()
        elif char=='}' and q[-1]=='{':
            q.pop()

        # Non-matching cases
        else:
            answer="NO"
            break

    if len(q)>0:
        answer="NO"

    print(answer)
