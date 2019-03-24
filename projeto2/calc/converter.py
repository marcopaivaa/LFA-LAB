from myQueue import MyQueue
from myStack import MyStack


class Converter:

    # Converte uma expressão infixa em prefixa
    def converterPreFixa(self, expr):
        expression = MyQueue()
        operator = MyStack(len(expr))
        prefixa = ""
        i=0
        while(i<len(expr)):
            if (expr[i] >= 'A' and expr[i] <= 'Z'):
                prefixa += expr[i]
            elif (expr[i] == '*' or expr[i] == '+'):
                aux = prefixa[-1]
                prefixa = prefixa[:-1]
                prefixa += expr[i]
                prefixa += aux
            elif (expr[i] == '.' or expr[i] == '|'):
                # if(operator.size() > 0):
                #     prefixa = operator.dequeue() + prefixa
                #     expression.enqueue(prefixa)
                #     prefixa = ""
                operator.push(expr[i])
            elif (expr[i] == '('):
                if(i>0 and expr[i-1] != '.' and expr[i-1] != '|'):
                    # if(operator.size() > 0):
                    #     prefixa = operator.dequeue() + prefixa
                    #     expression.enqueue(prefixa)
                    #     prefixa = ""
                    operator.push('.')
                j = i
                cont = 1
                while(cont >= 1):
                    j=j+1
                    if(expr[j] == '('):
                        cont = cont+1
                    elif(expr[j] == ')'):
                        cont = cont-1
                aux = self.converterPreFixa(expr[i+1:j])
                i = j+1
                if(i < len(expr) and (expr[i] == '*' or expr[i] == '+')):
                    aux = expr[i] + aux
                    i =i+1
                i= i-1
                prefixa += aux
            i = i+1      
        while(not operator.vazia()):
            prefixa = operator.pop() + prefixa
            if(operator.vazia()):
                expression.enqueue(prefixa)
                prefixa = ""
        while(len(prefixa) > 0):
            expression.enqueue(prefixa)
            prefixa = ""
        while (expression.size() > 0):
            prefixa += expression.dequeue()
        return prefixa

    # Converte uma expressão infixa em pósfixa
    # def converterPosFixa(self, expr):
    #     P = MyStack(len(expr))
    #     posfixa = ""

    #     for c in expr:
    #         if (c >= 'A' and c <= 'Z'):
    #             posfixa += c
    #         if (self.ehOperador(c)):
    #             pr = self.prioridade(c)
    #             while (not P.vazia() and self.prioridade(P.top()) >= pr):
    #                 posfixa += P.pop()
    #             P.push(c)
    #         if (c == '(' or c == '[' or c == '{'):
    #             P.push('(')
    #         if (c == ')' or c == ']' or c == '}'):
    #             x = P.pop()
    #             while (x and x != '('):
    #                 posfixa += x
    #                 x = P.pop()

    #     while (not P.vazia()):
    #         posfixa += P.pop()

    #     return posfixa

    def adicionarSaida(self, prefixa, op):
        for i in range(len(prefixa)):
            temp += prefixa[-i]
        return temp

    def ehOperador(self, c):
        return ((c == '+' or
                 c == '.' or
                 c == '*' or
                 c == '|'
                 ))

    def prioridade(self, c):
        if c == '(':
            return 2
        elif c == '+':
            return 0
        elif c == '*':
            return 0
        elif c == '|':
            return 1
        elif c == '.':
            return 1
        return 0
