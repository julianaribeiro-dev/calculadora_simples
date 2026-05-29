import math # import para operações extras na calculadora (raíz e exponenciação)

class Calculadora:
    # Classe que representa a calculadora com as 4 operações básicas.
    def somar(self, a, b):
        # Retorna a soma de a e b.
        return a + b
    def subtrair(self, a, b):
        # Retorna a diferença de a e b.
        return a - b
    def multiplicar(self, a, b):
        # Retorna a multiplicação de a e b.
        return a * b
    def dividir(self, a, b):
        # Retorna a divisão de a e b.
        return a / b
    def raiz(self, a):
        # Retorna a raiz de a.
        return math.sqrt(a)
    def exponenciar(self, a, b):
        # Retorna a exponenciação de a e b.
        return a ** b

def main():     # Função principal que interage com o usuário e realiza as operações.
    calc = Calculadora()
    print('CALCULADORA SIMPLES')
    # Loop que mantém o programa funcionando até o usuário desejar sair.
    while True:
        try:
            numero_1 = float(input('Digite o primeiro número: '))
            operador = input('Digite o operador +, -, *, /, r (raíz), ** (exponenciação) ou X para sair: ').strip().lower()

            # Adicionando uma forma do usuário encerrar o programa.
            if operador == 'x':
                print('Encerrando o programa. Até logo!')
                break

            # Para raíz quadrada só é preciso do primeiro número. Neste if, excluí-se a necessidade de colocar o segundo número.
            # Como a raíz já está sendo tratada nesta linha, não é necessário incluí-la nas definições de operadores abaixo.
            if operador.lower() == 'r':
                resultado = calc.raiz(numero_1)
                print(f'A raiz quadrada de {numero_1} = {resultado}')
                continue

            numero_2 = float(input('Digite o segundo número: '))

            # Definindo o caractere de entrada do usuário para determinar o operador.
            if operador == '+':
                resultado = calc.somar(numero_1, numero_2)
            elif operador == '-':
                resultado = calc.subtrair(numero_1, numero_2)
            elif operador == '*':
                resultado = calc.multiplicar(numero_1, numero_2)
            elif operador == '/':
                resultado = calc.dividir(numero_1, numero_2)
            elif operador == '**':
                resultado = calc.exponenciar(numero_1, numero_2)
            else:
                print('Operador inválido. Tente novamente.') # Adiciona uma exceção no else caso o operador seja inválido.
                continue

            print(f'O resultado de {numero_1} {operador} {numero_2} = {resultado}')

        # Adiciona tratamento de erros possíveis no programa.
        except ValueError:
            print('Entrada inválida. Digite números válidos.\n')
            continue
        except ZeroDivisionError:
            print('Não é possível divisão por 0. Tente novamente.')
            continue

main()