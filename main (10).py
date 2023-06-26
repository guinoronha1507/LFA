#AUTÔMATO FINITO DETERMINÍSTICO - AFD

# M = {Q, Σ, σ, q0, F}   =   ESSE "M" É O NOSSO AUTÔMATO;

# Q = {q0, q1}           =   ESSE "Q" É O CONJUNTO DE ESTADOS;
# Σ = {0, 1}             =   ESSE "Σ" É O CONJUNTO DE SÍMBOLOS QUE SERÃO O INPUT DO AUTÔMATO;

# σ = {                  =   ESSE "σ - DELTA" SERÁ O CONJUNTO DE FUNÇÕES DE TRANSIÇÃO;
#       σ: (q0, 0) -> q1,
#       σ: (q0, 1) -> q1,
#       σ: (q1, 0) -> q1,
#       σ: (q1, 1) -> q1
#     }
# q0 = q0               =  ESSE "Q0" REPRESENTA O ESTADO INICIAL;
# F = {q1}              =  ESSE "F" É O CONJUNTO DE ESTADOS DE ACEITAÇÃO.
















#DEFININDO AS ESTRUTURAS
estados = []
alfabeto = []
func_transicao = {}
estado_inicial = ""
estados_aceitacao = []


#RECEBENDO OS DADOS DO AUTÔMATO
print("INFORME O CONJUNTO DE ESTADOS: ", end="")
estados = input().split()

print("INFORME O ALFABETO DE ENTRADA: ", end="")
alfabeto = input().split()

print("INFORME O ESTADO INICIAL: ", end="")
estado_inicial = input()

print("INFORME O CONJUNTO  DE ESTADOS DE ACEITAÇÃO: ", end="")
estados_aceitacao = input().split()

print("DEFINA AS FUNÇÕES DE TRANSIÇÃO: ")
for estado in estados:
    for simbolo in alfabeto:
        print(f"\t {simbolo}")
        print(f"{estado}\t----->\t", end="")
        proximo_estado = input()

        if proximo_estado == ".":
            func_transicao[(estado, simbolo)] = None
        else:
            func_transicao[(estado, simbolo)] = proximo_estado

#RECONHECENDO AS LINGUAGENS
print("INFORME A LINGUAGEM A SER RECONHECIDA: ", end="")
entrada = input()

estado_atual = estado_inicial

for simbolo in entrada:
    print(f"ESTADO ATUAL: {estado_atual}")
    print(f"ENTRADA ATUAL: {simbolo}")

    print(f"PRÓXIMO ESTADO: {func_transicao[(estado_atual, simbolo)]}")

    estado_atual = func_transicao[(estado_atual, simbolo)]

    if estado_atual == None:
        print("O AUTÔMATO NÃO RECONHECEU A LINGUAGEM!!!")
        break

    if estado_atual in estados_aceitacao:
        print("RECONHECEU!!!")

    else:
        print("NÃO RECONHECEU!!!")
