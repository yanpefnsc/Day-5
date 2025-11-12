#funcao para analisar notas 
def analisar_notas(lista):
    """
    Recebe uma lista de notas (podendo conter valores inválidos)
    e devolve um dicionário com estatísticas sobre as notas válidas.
    """
    total = 0
    count = 0
    maior = None
    menor = None

    #percorre cada item da lista recebida
    for nota in lista:
        try:
            valor = float(nota)  # tenta converter para número
        except (ValueError, TypeError):
            print(f"Aviso: '{nota}' não é uma nota válida e será ignorada.")
            continue  # pula para o próximo item

        # acumula as notas válidas
        total += valor
        count += 1

        # define a maior nota (se ainda não houver ou se a nova for maior)
        if maior is None or valor > maior:
            maior = valor

        # define a menor nota (se ainda não houver ou se a nova for menor)
        if menor is None or valor < menor:
            menor = valor

    # calcula media — evita divisão por zero
    media = total / count if count > 0 else 0

    # devolve tudo organizado num dicionario
    return {
        "notas_validas": count,
        "media": media,
        "maior_nota": maior,
        "menor_nota": menor,
    }


#funcao para salvar o resultado num arquivo 
def salvar_relatorio(resultado):
    """
    Recebe o dicionário com os resultados e grava num arquivo de texto.
    """
    #abre (ou cria) um arquivo chamado 'relatorio_notas.txt' no modo de escrita
    with open("relatorio_notas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("✅ Análise concluída:\n")
        arquivo.write(f"- Notas válidas: {resultado['notas_validas']}\n")
        arquivo.write(f"- Média: {resultado['media']:.2f}\n")
        arquivo.write(f"- Maior nota: {resultado['maior_nota']:.2f}\n")
        arquivo.write(f"- Menor nota: {resultado['menor_nota']:.2f}\n")

    print("\n📁 Relatório salvo com sucesso em 'relatorio_notas.txt'!")


#programa principal 
notas = []  #lista vazia para armazenar as notas digitadas

while True:
    entrada = input("Digite uma nota (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        break
    notas.append(entrada)

#processa as notas digitadas
resultado = analisar_notas(notas)

#mostra o resultado no terminal
print("\n✅ Análise concluída:")
print(f"- Notas válidas: {resultado['notas_validas']}")
print(f"- Média: {resultado['media']:.2f}")
print(f"- Maior nota: {resultado['maior_nota']:.2f}")
print(f"- Menor nota: {resultado['menor_nota']:.2f}")

#salva o resultado em arquivo
salvar_relatorio(resultado)

