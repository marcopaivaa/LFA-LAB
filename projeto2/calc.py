from pilha import *

class Calc:

    def analisar(self, expr):
        S = Pilha(expr.Length)
        for c in expr:
            if (c == '(' or c == '[' or c == '{'): 
                S.push(c);
            if (c == ')' or c == ']' or c == '}'):
                if S.vazia():
                    return False
                p = S.pop();
                if (p == '(' and c != ')'): 
                    return False;
                if (p == '[' and c != ']'): 
                    return False;
                if (p == '{' and c != '}'):
                    return False;

        # Passou por tudo e expressão é válida
        return S.vazia();


    # Converte uma expressão infixa em pósfixa
    def converter(self, expr):
        P = Pilha(len(expr))
        posfixa = ""

        for c in expr:
            if (c >= 'A' and c <= 'Z'): 
                posfixa += c
            if (ehOperador(c)):
                pr = prioridade(c);
                while (not P.vazia() and prioridade(P.top()) >= pr):
                    posfixa += P.pop()
                P.push(c)
            if (c == '(' or c == '[' or c == '{'):
                P.push('(');
            if (c == ')' or c == ']' or c == '}'):
                x = P.pop()
                while (x != '('):
                    posfixa += x;
                    x = P.pop();

        while (not P.vazia()):
            posfixa += P.pop();

        return posfixa;


    def adicionarSaida(self, prefixa, op):
        temp = ""
        for i in range(prefixa.Length-3):
            temp += prefixa[i]
        if ((prefixa.Length >=3 and ehOperador(prefixa[prefixa.Length - 3]))
            or
            (prefixa.Length >=4 and ehOperador(prefixa[prefixa.Length - 4]))):
            temp = op + temp + prefixa[prefixa.Length - 3];
        else:
            temp = temp + prefixa[prefixa.Length - 3] + op;
        for i in range(prefixa.Length - 2, i < prefixa.Length):
            temp += prefixa[i]
        return temp

    def ehOperador(self, c):
        return ((c == '+' or 
            c == '-' or 
            c == '*' or 
            c == '/' or 
            c == '^' or
            c == '@'));

    # Converte uma expressão infixa em prefixa 
    def converterPre(self, expr):
        P = Pilha(len(expr))
        prefixa = ""

        for c in expr:
            if (c >= 'A' and c <= 'Z'): 
                prefixa += c
            if (ehOperador(c)):
                pr = prioridade(c);
                while (not P.vazia() and prioridade((P.top()) >= pr)):
                    prefixa = adicionarSaida(prefixa, P.pop())
                P.push(c);
            if (c == '(' or c == '[' or c == '{'):
                P.push('(')
            if (c == ')' or c == ']' or c == '}'):
                x = P.pop()
                while (x != '('):
                    prefixa = adicionarSaida(prefixa, x.ToString());
                    x = P.pop();

        while (not P.vazia()):
            prefixa = adicionarSaida(prefixa, P.pop().ToString());

        return prefixa;

    
    def prioridade(self, c):
        if c == '(':
            return 1
        elif c == '+':
            return 0
        elif c == '-':
            return 2
        elif c == '*':
            return 0
        elif c == '/':
            return 3
        elif c == '^':
            return 4
        elif c == '@':
            return 1
        return 0

    # Calcula o valor de uma expressão pósfixa
    def calcular(self, posfixa, vars):
        P = Pilha(len(posfixa))
        for c in posfixa:
            if (c >= 'A' and c <= 'Z'):
                for v in vars:
                    if (v.Nome == c.ToString()):
                        P.push(v.Valor);
            else:
                if (c == '@'):
                    y1 = P.pop();
                    y0 = P.pop();
                    x1 = P.pop();
                    x0 = P.pop();
                    P.Push((x1 - x0) / (y1 - y0));
                else:
                    y = P.pop();
                    x = P.pop();
                    if c == '+':
                        P.push(x + y)
                    elif c == '-':
                        P.push(x - y)
                    elif c == '*':
                        P.Push(x * y)
                    elif c == '/':
                        P.Push(x / y)
                    elif c == '^':
                        P.Push(Math.Pow(x, y))

        return P.pop();



# Classe com os nomes e valores das variáveis
class Variavel:
    def __init__(self):
        nome
        valor

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

