ops=set(['+', '-', '*', '/', '(', ')'])  # operatori
priority={'+':1, '-':1, '*':2, '/':2}  #precedence ze high=1., low=2. priorita

#OPERAND = cislo
#OPERATOR = znamienko

def InfToPost(vyraz):
    stack=[] #prazdny stack
    output='' #prazdny output nech je kam pisat output

    for char in vyraz:
        if char not in ops:  # ak operand/cis tak prdnut priamo do postfix
            output+= char
        elif char=='(':
            stack.append('(')
        elif char==')':
            while stack and stack[-1]!= '(': # pop a append operatori/zn zo stacku do outputu pokial nebude (
                output+=stack.pop()
            stack.pop()
        else: # ak mame operator/zn, append pokial nemame empty stack
            while stack and stack[-1]!='(' and priority[char]<=priority[stack[-1]]:
                # zaciatok stacku nie je (
                # low priorita nemoze byt v stacku vyssie ako high
                output+=stack.pop()# takze pop a prdnut do outputu
            stack.append(char)
    while stack:
        output+=stack.pop() #sup so zvyskom do outputu
    return output

def vypocitaj(vyr):
    try:
        result=eval(vyr)
        return result
    except SyntaxError:
        pass

vyraz=input('zadaj mi vyraz: ')
print('postfix: ',InfToPost(vyraz))
result=vypocitaj(vyraz)
print("vysledok: ", result)

# 1.3.6





