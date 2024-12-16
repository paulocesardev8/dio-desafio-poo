class Calculadora:
    # Construtor para inicializar os números
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    # Método para somar os dois números
    def soma(self):
        return self.numero1 + self.numero2

# Função principal para testar a classe Calculadora
def main():
    # Lê os números inteiros fornecidos pelo usuário
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    
    # Cria uma instância da classe Calculadora
    calculadora = Calculadora(numero1, numero2)
    
    # Realiza a soma e exibe o resultado
    resultado = calculadora.soma()
    print(f"O resultado da soma é: {resultado}")

# Chama a função principal
if __name__ == "__main__":
    main()
