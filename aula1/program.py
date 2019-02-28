import inputs as inp


def main():
    
    variaveis = inp.input_variaveis()
    alfabeto = inp.input_alfabeto()
    variavel_inicial = inp.input_varivel_inicial(variaveis)
    regras = inp.input_regras(variaveis, alfabeto)
    sequencia = inp.input_sequencia(regras)
    
    palavra = variavel_inicial
    for sq in sequencia:
        sq = int(sq)
        key = list(regras[sq].keys())[0]
        palavra = palavra.replace(key, regras[sq][key],1)

    sucesso = True
    for char in list(palavra):
        if(not char in alfabeto):
            sucesso = False
            break
    
    if(sucesso):
        print("A palavra foi formada corretamente!")
    else:
        print("A palavra não foi formada corretamente!")

    print("Palavra: " + palavra + "\n")
    

if __name__ == "__main__":
    main()