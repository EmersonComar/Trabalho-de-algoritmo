agenda = []
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
      compromisso[0].duracaoSet(duracao)
      compromisso[0].detalheSet(detalhes)
      print("\n=== Compromisso alterado com sucesso ===\n")


# === listar todos ===
def listar():
  if len(agenda) != 0:
    print("\n\t=== Todos os Compromissos Agendados ===")
    listar_todos()
  else:
    print("\n=== Nenhum Compromisso agendado ===\n")

def listar_todos(lista=agenda):
  for compromisso in lista:
    print("\n")
    print(compromisso)


# === consultar ===
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


  
def consulta_data():
  print("Data do Compromisso")
  dia, mes, ano = entrada_data()
  lista = []
  for compromisso in agenda:
    if compromisso.dia == dia and compromisso.mes == mes and compromisso.ano == ano:
      lista.append(compromisso)

  return lista


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

def entrada_horario():
  horas = valida_entrada("Hora: ", 0, 23)
  minutos = valida_entrada("Minutos: ", 0, 59)

  return horas, minutos

def entrada_data():
  while True:
    dia = valida_entrada("Dia: ", 1, 31)
    mes = valida_entrada("Mês: ", 1, 12)
    ano = valida_entrada("Ano: ", 2023, 2100)

    if valida_data(dia, mes, ano):
      return dia, mes, ano
    else:
      print("Data inválida. Tente novamente")

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
