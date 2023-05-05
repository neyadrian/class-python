class Carro:
  def __init__(self, marca: str, modelo: str, ano: int):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def dizer_ola(self):
    print(f'Olá, o meu carro é um {self.marca} {self.modelo} {self.ano}.')

  def potencia(self, cavalaria: str):
    print(f'Tem de potência: {cavalaria} cv')

  def valor(self, preco: int):
    print(f'Ele está avalidado no valor de {preco} US$.')


carro = carro(marca='Audi', modelo='RSQ8', ano=2023)

carro.dizer_ola()
carro.potencia('600')
carro.valor(192.986)