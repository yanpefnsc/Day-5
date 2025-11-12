# Day-5
--------------------------------------------------------------------------------------------------------
🇺🇸 English:
You will find the code explanation in English in the first part and in Portuguese in the second.

🇧🇷 Português:
Você vai encontrar a explicação do código em inglês na primeira parte e em português na segunda.
--------------------------------------------------------------------------------------------------------

Purpose of the program

The script aims to analyze a list of grades provided by the user, filtering out invalid values and generating basic statistics:

How many grades are valid

Average grade

Highest grade

Lowest grade

After the analysis, the program displays the results in the terminal and also generates a report file (relatorio_notas.txt) containing the same information.

 The code is divided into three main parts:

Function analisar_notas(lista) → processes the data and calculates statistics.

Function salvar_relatorio(resultado) → writes the results into a text file.

Main block (program entry point) → interacts with the user, collects grades, and calls the functions above.

Receives a list with values provided by the user (which may contain invalid numbers or text).
Initializes variables to sum valid grades, count how many there are, and identify the highest and lowest ones.
def analisar_notas(lista):
    """
    Receives a list of grades (which may include invalid values)
    and returns a dictionary with statistics about the valid grades.
    """

If the value can be converted to float, it is considered valid.
Otherwise, the program warns the user and ignores the invalid value using continue.
for nota in lista:
    try:
        valor = float(nota)
    except (ValueError, TypeError):
        print(f"Warning: '{nota}' is not a valid grade and will be ignored.")
        continue

Adds valid grades to the total sum.
Updates the counter count.
Defines the highest and lowest grade found so far.
total += valor
count += 1
if maior is None or valor > maior:
    maior = valor
if menor is None or valor < menor:
    menor = valor

Prevents division by zero if no valid grades exist.
media = total / count if count > 0 else 0

Returns a dictionary with the final statistics:
return {
    "notas_validas": count,
    "media": media,
    "maior_nota": maior,
    "menor_nota": menor,
}

Receives the dictionary returned by the previous function.
Opens (or creates) the file relatorio_notas.txt in write mode.
Writes formatted data with emojis and rounded decimal places.
def salvar_relatorio(resultado):
    """
    Receives the dictionary with the results and writes them into a text file.
    """

Example output in the file:
 Analysis completed:
- Valid grades: 4
- Average: 7.25
- Highest grade: 9.00
- Lowest grade: 5.50

Empty list to store user input (main program)
notas = []  # empty list to store the entered grades

Loop that collects grades until the user types "sair" ("exit")
while True:
    entrada = input("Enter a grade (or type 'sair' to finish): ")
    if entrada.lower() == "sair":
        break
    notas.append(entrada)

The function is called to process the grades.
resultado = analisar_notas(notas)

The results are displayed in a formatted way in the terminal.

###########################################################################################################################

Propósito do programa

O script tem como objetivo analisar uma lista de notas fornecidas pelo usuário, filtrando valores inválidos e gerando estatísticas básicas:

Quantas notas são válidas

Média das notas

Maior nota

Menor nota

Após a análise, o programa exibe os resultados no terminal e também gera um arquivo de relatório (relatorio_notas.txt) com as mesmas informações.

O código está dividido em três partes principais:

Função analisar_notas(lista) → processa e calcula as estatísticas.

Função salvar_relatorio(resultado) → grava os resultados em um arquivo de texto.

Bloco principal (main) → interage com o usuário, coleta as notas e chama as funções acima.

=============================================================================================================================

#Recebe uma lista com valores informados pelo usuário (que podem ser números ou textos inválidos).

#Inicializa variáveis para somar notas válidas, contar quantas existem e identificar maior e menor valor.

def analisar_notas(lista):
    """
    Recebe uma lista de notas (podendo conter valores inválidos)
    e devolve um dicionário com estatísticas sobre as notas válidas.
    """
=============================================================================================================================

#Se for possível converter para float, é considerado válido.

#Caso contrário, o programa avisa e ignora o valor inválido usando continue.

for nota in lista:
    try:
        valor = float(nota)
    except (ValueError, TypeError):
        print(f"Aviso: '{nota}' não é uma nota válida e será ignorada.")
        continue
=============================================================================================================================

#Soma as notas válidas em total.

#Atualiza o contador count.

#Define a maior e menor nota encontradas até o momento.

total +=valor
count += 1
if maior is None or valor > maior:
    maior = valor
if menor is None or valor < menor:
    menor = valor

=============================================================================================================================

#Evita erro de divisão por zero se nenhuma nota for válida.

media = total / count if count > 0 else 0
============================================================================
#Retorna um dicionário com as estatísticas finais:

return {
    "notas_validas": count,
    "media": media,
    "maior_nota": maior,
    "menor_nota": menor,
}
=============================================================================================================================

#Recebe o dicionário retornado pela função anterior.

#Abre (ou cria) o arquivo relatorio_notas.txt no modo de escrita.

#Escreve os dados formatados, com emojis e arredondamento de casas decimais.

def salvar_relatorio(resultado):
    """
    Recebe o dicionário com os resultados e grava num arquivo de texto.
    """
===================================================================================================================
Exemplo de saída no arquivo:

✅ Análise concluída:
- Notas válidas: 4
- Média: 7.25
- Maior nota: 9.00
- Menor nota: 5.50

=======================================================================================================================

notas = []  # lista vazia para armazenar as notas digitadas (programa principal)

=======================================================================================================================
#loop que coleta notas ate o usuario digitar "sair"

while True:
    entrada = input("Digite uma nota (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        break
    notas.append(entrada)
========================================================================================================================

resultado = analisar_notas(notas) #A função é chamada para processar as notas.

#Os resultados são exibidos formatados no terminal:

=========================================================================================================================






