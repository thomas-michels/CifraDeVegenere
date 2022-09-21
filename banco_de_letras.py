from typing import List
from letras import Letra

class BancoDeLetras:

    def __init__(self) -> None:
        self.letras: List[Letra] = []

    def add_letra(self, letra: Letra):
        self.letras.append(letra)

    def get_tamanho_banco_de_letras(self) -> int:
        return len(self.letras)

    def get_letra(self, posicao: int) -> Letra:
        tamanho = self.get_tamanho_banco_de_letras()
        if posicao >= tamanho:
            qtd = posicao // tamanho
            posicao -= (tamanho * qtd)

        return self.letras[posicao]

    def get_posicao_da_letra(self, caracter: str) -> int:
        for i, letra in enumerate(self.letras):
            if letra.get_caracter() == caracter:
                return i

        return -1
