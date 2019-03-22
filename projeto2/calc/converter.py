from myStack import MyStack


class Converter:

    # Converte uma expressão infixa em prefixa
    def converterPreFixa(self, expr):
        P = MyStack(len(expr))
        prefixa = ""

        for c in expr:
            if (c >= 'A' and c <= 'Z'):
                prefixa += c
            if (self.ehOperador(c)):
                pr = self.prioridade(c)
                while (not P.vazia() and self.prioridade((P.top())) >= pr):
                    prefixa = self.adicionarSaida(prefixa, P.pop())
                P.push(c)
            if (c == '(' or c == '[' or c == '{'):
                P.push('(')
            if (c == ')' or c == ']' or c == '}'):
                x = P.pop()
                while (x != '('):
                    prefixa = self.adicionarSaida(prefixa, x)
                    x = P.pop()

        while (not P.vazia()):
            prefixa = self.adicionarSaida(prefixa, P.pop())

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
        temp = ""
        if len(prefixa)-2 > 0:
            prefixa2 = len(prefixa)-2
        else:
            prefixa2 = 0
        if len(prefixa)-2 > 0:
            prefixa3 = len(prefixa)-3
        else:
            prefixa3 = 0
        if len(prefixa)-2 > 0:
            prefixa4 = len(prefixa)-4
        else:
            prefixa4 = 0
        for i in range(prefixa3):
            temp += prefixa[i]
        if ((len(prefixa) >= 3 and self.ehOperador(prefixa[prefixa3]))
            or
                (len(prefixa) >= 4 and self.ehOperador(prefixa[prefixa4]))):
            temp = str(op) + temp + prefixa[prefixa3]
        else:
            temp = temp + prefixa[prefixa3] + op
        for i in range(prefixa2, len(prefixa)):
            temp += prefixa[i]
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
