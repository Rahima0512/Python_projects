#Calculator
#ADD
def add(n1,n2):
    return n1+n2
#SUBTRACT
def sub(n1,n2):
    return n1-n2
#MULTIPLY
def mul(n1,n2):
    return n1*n2
#DIVIDE
def div(n1,n2):
    return n1/n2

Operations={'+':add,'-':sub,'*':mul,'/':div}

def calculator_func():
    continue1 = True
    num1 = float(input("Enter the first number\t"))
    while (continue1 == True):
        for key in Operations:
            print(key)
        symbol = input("Enter the operation to be performed:\t")
        num2 = float(input("Enter the second number\t"))
        func_perform = Operations[symbol]
        answer_1 = func_perform(num1, num2)
        print(f"\t {num1} {symbol} {num2}\t=\t {answer_1}")

        continue1 = input("Do you wanna continue? y/n or start a new calculation : new\t")
        if continue1=='n':
            exit()
        if continue1=='new':
            continue1=True
            calculator_func()
        if continue1=='y':
            continue1 = True
            num1=answer_1
continue1=True
calculator_func()


