def createstack():
    stack=[]
    return stack
def isempty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    return stack
def pop(stack):
    return stack.pop()
def display(stack):
    if isempty(stack):
        return None
    size=len(stack)
    for i in range(size):
        print(stack[i])
def peek(stack):
    size=len(stack)
    top=stack[size-1]
    return top
def bottompush(stack,item):
    temp=createstack()
    size=len(stack)
    for i in range(size):
        temp.append(pop(stack))
    push(stack,item)
    for i in range(size):
        stack.append(pop(temp))
    return stack

def allpop(stack):
    size=len(stack)
    for i in range(size):
        pop(stack)
    return stack
if __name__=='__main__':
    stack=createstack()
    push(stack,1)
    push(stack,2)
    push(stack,3)
    print()
    display(stack)
    print()
    bottompush(stack, 2)
    display(stack)