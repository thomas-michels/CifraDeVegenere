from letras import Letra
from banco_de_letras import BancoDeLetras




class CifraDeVegenere:

    def __init__(self, banco_de_letras: BancoDeLetras, chave: str) -> None:
        self.banco_letras = banco_de_letras
        self.chave = chave
        self.__posicao_chave = 0

    def __proxima(self):
        if self.__posicao_chave >= len(self.chave) - 1:
            self.__posicao_chave = 0

        else:
            self.__posicao_chave += 1

    def cifrar(self, mensagem: str) -> str:
        return self.converter(mensagem)

    def decifrar(self, mensagem: str) -> str:
        return self.converter(mensagem, True)

    def converter(self, mensagem, inverso=False):
        nova_mensagem = ""

        for caracter in mensagem:
            if caracter == " ":
                nova_mensagem += " "

            else:
                caracter_posicao = self.banco_letras.get_posicao_da_letra(caracter)
                chave_posicao = self.banco_letras.get_posicao_da_letra(self.chave[self.__posicao_chave])
                if not inverso:
                    nova_posicao = caracter_posicao + chave_posicao

                else:
                    nova_posicao = caracter_posicao - chave_posicao

                self.__proxima()

                nova_letra = self.banco_letras.get_letra(nova_posicao)
                nova_mensagem += nova_letra.get_caracter()

        return nova_mensagem
