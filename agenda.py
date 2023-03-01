agenda = []

"""
"Compromisso" é uma classe que representa um compromisso agendado. Ele tem vários atributos, 
incluindo data (dia, mês e ano), horário (horas e minutos), duração (em horas), detalhes (uma 
descrição do compromisso) e um ID exclusivo gerado a partir da data e do horário. O método __str__ 
retorna uma string formatada que contém todas essas informações para exibir um compromisso de forma 
legível.
"""
class Compromisso:
  def __init__(self, dia, mes, ano, horas, minutos, duracao, detalhes):
    self.dia = dia
    self.mes = mes
    self.ano = ano
    self.horas = horas
    self.minutos = minutos
    self.duracao = duracao
    self.detalhes = detalhes
    self.id = int(f"{ano}{mes}{dia}{horas}{minutos}")
    
  def __str__(self):
    return f"""Data: {self.dia:02}/{self.mes:02}/{self.ano:04}
Horário: {self.horas:02}:{self.minutos:02}
duração: {self.duracao} hora(s)
Detalhes: {self.detalhes}"""

# === ordena ====

"""
A função "ordena" recebe como parâmetro uma lista de objetos e ordena a lista de forma 
ascendente com base no atributo "id" de cada objeto. Para isso, a função utiliza o algoritmo de 
ordenação conhecido como Bubble Sort.
"""
def ordena(lista):
  index = 0
  while index < (len(lista) - 1):

    index_int = index + 1
    while index_int < len(lista):
      valorAtual = lista[index].id
      valorProximo = lista[index_int].id

      if valorAtual > valorProximo:
        lista[index], lista[index_int] = lista[index_int], lista[index]

      
      index_int += 1
    
    index += 1

# === excluir ===
"""
A função "excluir" primeiro verifica se a agenda possui algum compromisso, caso
não exista nenhum compromisso inserido, a função apenas printa uma mensagem avisando que não
posui nenhum compromisso salvo.
Caso a agenda contenha algum compromisso salvo, ela irá pesquisar através de duas funções
a data e a hora do compromisso que se deseja excluir. Caso encontre um compromisso
com exatamente a mesma data e a mesma hora, ele será excluido.
"""
def excluir():

  if len(agenda) == 0:
    print("\n=== Nenhum compromisso agendado ===\n")
  else:
    print("\t=== Excluir ===\n")
    lista = consulta_hora(consulta_data())
    if len(lista) == 0:
      print("\n=== Compromisso não encontrado ===\n")
    else:
      for compromisso in agenda:
        if compromisso == lista[0]:
          agenda.remove(compromisso)

      print("\n=== Compromisso removido com sucesso ===")


# === alterar ===
"""
A função "alterar" primeiro verifica se a agenda possui algum compromisso, caso
não exista nenhum compromisso inserido, a função apenas printa uma mensagem avisando que não
posui nenhum compromisso salvo.
Caso a agenda contenha algum compromisso salvo, ela irá pesquisar através de duas funções
a data e a hora do compromisso que se deseja alterar. Caso encontre um compromisso
com exatamente a mesma data e a mesma hora, será pedido uma nova duração e novos detalhes
para serem alterados no compromisso.
"""
def alterar():
  if len(agenda) == 0:
    print("\n=== Nenhum Compromisso agendado ===\n")
  else:
    print("\t=== Alterar ===\n")
    compromisso = consulta_hora(consulta_data())
    if len(compromisso) == 0:
      print("\n=== Compromisso não encontrado ===")
    else:

      duracao = float(input("Nova Duração: "))
      detalhes = input("Nova descrição: ")
      compromisso[0].duracao = duracao
      compromisso[0].detalhes = detalhes
      print("\n=== Compromisso alterado com sucesso ===\n")


# === listar todos ===
"""
A função "listar" irá validar se existe algum compromisso salvo na agenda; caso tenha, a
função "listar_todos" irá ser executada; caso não tenha, apenas será mostrado
uma mensagem avisando que não possui compromissos salvos.
"""
def listar():
  if len(agenda) != 0:
    print("\n\t=== Todos os Compromissos Agendados ===")
    listar_todos()
  else:
    print("\n=== Nenhum Compromisso agendado ===\n")

"""
A função "lista_todos" irá listar a agenda como parâmetro default.
Será atraés de um for em que cada um dos compromissos da lista serão apresentados.
O print(compromisso) utiliza o método especial __str__ do python para apresentar
cada um dos compromissos de forma na qual foi ajustado na classe Compromisso
"""
def listar_todos(lista=agenda):
  for compromisso in lista:
    print("\n")
    print(compromisso)


# === consultar ===
"""
A função "consulta_hora" recebe uma lista como parâmetros que irá conter alguma data em
específico e, se caso a lista da data estiver vazio, a função irá retornar uma lista vazia
para quem chamá-la. Caso a lista da data não esteja vazia, será pesquisado através dela se 
existe algum compromisso com a hora e o minuto informado e será retornado para quem esse
vetor para quem a chamou.
"""
def consulta_hora(lista):
  if len(lista) == 0:
    return []
  print("\nHorário do Compromisso")
  horas, minutos = entrada_horario()
  lista_hora =[]
  for compromisso in lista:
    if compromisso.horas == horas and compromisso.minutos == minutos:
      lista_hora.append(compromisso)

  return lista_hora


"""
A função "consulta_data" primeiro irá requisitar um dia, mês e ano e, após informados,
será pesquisado se existe algum compromisso que contenha essa data na agenda.
Se existir algum compromisso com a determinada data, esse será adicionado em um vetor
que será retornado a quem chamou.
"""  
def consulta_data():
  print("Data do Compromisso")
  dia, mes, ano = entrada_data()
  lista = []
  for compromisso in agenda:
    if compromisso.dia == dia and compromisso.mes == mes and compromisso.ano == ano:
      lista.append(compromisso)

  return lista

"""
A função "consultar" primeiro irá validar se na agenda existe algum compromisso salvo e, 
caso tenha, apresentar um menu onde será possível escolher se deseja pesquisar por data 
ou por data e horas.
Caso o usuário escolher pesquisar apenas por data, a função "consuta_data" será acionada,
caso escolha pesquisar por data e hora, o retorno da função "consulta_data" será o 
parãmetro da função "consulta_hora". 
"""
def consultar():
  
  if len(agenda) == 0:
    print("\n=== Nenhum Compromisso agendado ===\n")
    return
  opt = valida_entrada("""
\t=== Consultar por ===
1. Data
2. Data e Hora
--> """, 1, 2) 

  lista = []
  if opt == 1:
    lista = consulta_data()  
  else:
    lista = consulta_hora(consulta_data())

  if len(lista) != 0:
    print("\n\t=== Todos os Compromissos encontrados ===")
    listar_todos(lista)
  else:
    print("\n=== Nenhum compromisso encontrado ===\n")

# === incluir ===

"""
A função "incluir" é responsável por obter as informações necessárias para criar um novo compromisso 
e adicioná-lo à lista agenda.
"""
def incluir():
  print("\t=== Novo Compromisso ===")
  print("Data do Compromisso")
  dia, mes, ano = entrada_data()

  print("\nHorário do compromisso")
  horas, minutos = entrada_horario()

  duracao = valida_entrada("Duração do evento (em horas): ", 0, 36, float)
  descricao = input("Descrição do evento: ")

  registro = Compromisso(dia, mes, ano, horas, minutos, duracao, descricao)
  agenda.append(registro)
  
  print(f"""
\n\t=== Compromisso Agendado ===

{registro}""")


# === menu ===
"""
A função "menu" é responsável por exibir um menu para o usuário com várias opções 
relacionadas a uma agenda.
A função utiliza a função "valida_entrada" para obter a escolha do usuário. Se o usuário 
digitar um número válido (entre 1 e 6), a função verifica qual opção foi escolhida e 
chama a função correspondente (incluir, consultar, alterar, excluir, listar) ou sai do 
loop e exibe a mensagem "Bye".
A função "ordena" é chamada após cada operação de inserção, alteração ou exclusão na
agenda.  
"""
def menu():
  while True:
    opt = valida_entrada("""
\n\t=== Agenda - Menu Inicial ===
1. Incluir
2. Consultar
3. Alterar
4. Excluir
5. Listar todos
6. Sair
-> """, 1, 6)

    if opt == 1:
      incluir()
    elif opt == 2:
      consultar()
    elif opt == 3:
      alterar()
    elif opt == 4:
      excluir()
    elif opt == 5:
      listar()
    elif opt == 6:
      break
    ordena(agenda)
  print("Bye")

# === Ferramentas ===

"""
A função "valida_data" tem como objetivo verificar se uma data é válida, considerando o 
número de dias de cada mês e se o ano é bissexto ou não. A função retorna True se a data 
for válida e False se a data for inválida.
"""
def valida_data(dia, mes, ano):
  if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
      return True
    else:
      return False
  elif mes == 2:
    if dia <= 28:
      return True
    else:
      if dia == 29 and ano%4 == 0:
        return True
      else:
        return False
      
  return True


"""
A função "entrada_horario" tem como objetivo obter do usuário uma entrada de horário 
válida, utilizando a função "valida_entrada" para validar cada campo do horário. A função 
retorna uma tupla contendo os valores de hora e minutos válidos.
"""
def entrada_horario():
  horas = valida_entrada("Hora: ", 0, 23)
  minutos = valida_entrada("Minutos: ", 0, 59)

  return horas, minutos
  
"""
A função "entrada_data" tem como objetivo obter do usuário uma entrada de data válida, 
utilizando a "função valida_entrada" para validar cada campo da data e a função 
"valida_data" para verificar se a data é válida. A função mantém a execução em loop até 
que uma data válida seja fornecida pelo usuário.
"""
def entrada_data():
  while True:
    dia = valida_entrada("Dia: ", 1, 31)
    mes = valida_entrada("Mês: ", 1, 12)
    ano = valida_entrada("Ano: ", 2023, 2100)

    if valida_data(dia, mes, ano):
      return dia, mes, ano
    else:
      print("Data inválida. Tente novamente")


"""
A função "valida_entrada" tem como objetivo validar a entrada de dados do usuário.
A função utiliza um loop while para manter a execução até que uma entrada válida seja 
fornecida pelo usuário. Dentro do loop, a função utiliza a função input para receber a 
entrada do usuário e, em seguida, tenta converter essa entrada para o tipo de dado 
especificado pelo parâmetro tipo usando a função tipo. Se a conversão for bem-sucedida e 
o valor estiver dentro do intervalo definido pelos parâmetros minimo e maximo, a função 
retorna o valor.
"""
def valida_entrada(mensagem, minimo, maximo, tipo=int):
  while True:
    try:
      valor = tipo(input(mensagem))
      if valor >= minimo and valor <= maximo:
        return valor
      else:
        print(f"\nO valor digitado deve estar entre {minimo} e {maximo}\n")
    except ValueError:
      print(f"\nO valor digitado deve estar entre {minimo} e {maximo}\n")

if __name__ == "__main__":
  menu()
