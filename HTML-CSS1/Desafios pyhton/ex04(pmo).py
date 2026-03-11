class Carro:
    def __init__(self, marca, modelo, ano, cor, preço):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__preço = preço

    def get_marca(self):
        return self.__marca

    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def set_ano(self, novo_ano):
        self.__ano = novo_ano

    def get_ano(self):
        return self.__ano

    def set_cor(self, nova_cor):
        self.__cor = nova_cor  # ✅ Correção aqui

    def get_cor(self):
        return self.__cor

    def get_preço(self):
        return self.__preço

    def set_preço(self, novo_preço):
        self.__preço = novo_preço  # ✅ Correção aqui


# TESTES
meu_carro = Carro("Ferrari", "Slim", "1999", "Azul", "100.000")

print("----------VALORES INICIAIS-------------")
print("Marca:" + meu_carro.get_marca())
print("Modelo:" + meu_carro.get_modelo())
print("Ano:" + meu_carro.get_ano())
print("Cor:" + meu_carro.get_cor())
print("Preço: R$" + meu_carro.get_preço())

# Modificando valores usando os setters
meu_carro.set_marca("Ferrari")
meu_carro.set_modelo("F1")
meu_carro.set_ano("2023")
meu_carro.set_cor("Vermelho")
meu_carro.set_preço("500.000")

# Exibindo os valores modificados
print("----------VALORES MODIFICADOS-------------")
print("Marca:", meu_carro.get_marca())
print("Modelo:", meu_carro.get_modelo())
print("Ano:", meu_carro.get_ano())
print("Cor:", meu_carro.get_cor())
print("Preço: R$", meu_carro.get_preço())

