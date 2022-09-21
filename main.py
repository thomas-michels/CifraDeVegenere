from criptografia import CifraDeVegenere
from banco_de_letras import BancoDeLetras
from letras import Letra
import re


def entrada_valida(mensagem: str) -> bool:
    return bool(re.fullmatch(r"[A-Z\u00C0-\u00FF ]+", mensagem))

banco_letras = BancoDeLetras()
banco_letras.add_letra(Letra("A"))
banco_letras.add_letra(Letra("B"))
banco_letras.add_letra(Letra("C"))
banco_letras.add_letra(Letra("D"))
banco_letras.add_letra(Letra("E"))
banco_letras.add_letra(Letra("F"))
banco_letras.add_letra(Letra("G"))
banco_letras.add_letra(Letra("H"))
banco_letras.add_letra(Letra("I"))
banco_letras.add_letra(Letra("J"))
banco_letras.add_letra(Letra("K"))
banco_letras.add_letra(Letra("L"))
banco_letras.add_letra(Letra("M"))
banco_letras.add_letra(Letra("N"))
banco_letras.add_letra(Letra("O"))
banco_letras.add_letra(Letra("P"))
banco_letras.add_letra(Letra("Q"))
banco_letras.add_letra(Letra("R"))
banco_letras.add_letra(Letra("S"))
banco_letras.add_letra(Letra("T"))
banco_letras.add_letra(Letra("U"))
banco_letras.add_letra(Letra("V"))
banco_letras.add_letra(Letra("W"))
banco_letras.add_letra(Letra("X"))
banco_letras.add_letra(Letra("Y"))
banco_letras.add_letra(Letra("Z"))


if __name__ == "__main__":
    opcao = 0

    while opcao != 3:
        print("=" * 50)
        print("1 - Cifrar")
        print("2 - Decifrar")
        print("3 - Sair")
        try:
            opcao = int(input("Opção desejada: "))
            if opcao != 3:
                chave = input("Digite a chave: ")
                mensagem = input("Digite a mensagem: ")
                if entrada_valida(mensagem) and entrada_valida(chave):
                    cifra_de_vegenere = CifraDeVegenere(banco_letras, chave)
                    if opcao == 1:
                        print("="*50)
                        print("Mensagem Cifrada")
                        print(cifra_de_vegenere.cifrar(mensagem))

                    elif opcao == 2:
                        print("="*50)
                        print("Mensagem Decifrada")
                        print(cifra_de_vegenere.decifrar(mensagem))

                else:
                    print("Chave ou Entrada invalida")

        except Exception as error:
            print("Opção inválida")
