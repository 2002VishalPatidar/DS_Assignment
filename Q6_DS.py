'''Infix: The typical mathematical form of expression that we encounter generally is known as infix notation. In infix form, an operator is written in between two operands
Example:(A+B) * (C-D)
Postfix: An expression is called the postfix expression if the operator appears in the expression after the operands. Simply of the form (operand1 operand2 operator). 
Example : AB+CD-* (Infix : (A+B) * (C-D) )

Prefix : An expression is called the prefix expression if the operator appears in the expression before the operands. Simply of the form (operator operand1 operand2). 
Example : *+AB-CD (Infix : (A+B) * (C-D) )'''

#Program to convert postfix to prefix

def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
def postToPre(post_exp):
    s = []
    length = len(post_exp)
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])
    ans = ""
    for i in s:
        ans += i
    return ans
if __name__ == "__main__":
    post_exp = "AB+CD-"
    print("Prefix : ", postToPre(post_exp))
