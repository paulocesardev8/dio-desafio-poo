# Explicação do Código: Classe Calculadora em Python

Este documento explica o funcionamento de uma classe `Calculadora` desenvolvida em Python utilizando o paradigma de **Programação Orientada a Objetos (POO)**. A classe permite somar dois números fornecidos pelo usuário.

---

## **Descrição do Código**

### **Classe `Calculadora`**
A classe `Calculadora` é composta por:

1. **Construtor `__init__`**:
   - Responsável por inicializar dois atributos: `numero1` e `numero2`.
   - Estes atributos representam os dois números que serão somados.

   **Exemplo**:
   ```python
   calculadora = Calculadora(5, 7)  # Cria uma instância da classe
   ```

2. **Método `soma`**:
   - Realiza a soma dos dois números armazenados nos atributos `numero1` e `numero2`.
   - Retorna o resultado da soma.

   **Exemplo**:
   ```python
   resultado = calculadora.soma()  # Retorna 12
   ```

---

### **Função `main`**
A função `main` é responsável por gerenciar a interação com o usuário:
1. Solicita dois números inteiros do usuário via `input`.
2. Cria uma instância da classe `Calculadora` com os números fornecidos.
3. Chama o método `soma` para calcular a soma.
4. Exibe o resultado no formato especificado.

---

### **Controle de Fluxo**
A linha abaixo garante que o código só execute a função `main` se o script for executado diretamente:
```python
if __name__ == "__main__":
    main()
```

---

## **Fluxo de Execução**
1. O programa solicita dois números inteiros ao usuário.
2. A classe `Calculadora` é instanciada com os dois números.
3. O método `soma` é chamado para calcular a soma.
4. O resultado é exibido no console.

---

## **Exemplo de Execução**

### Entrada:
```
Digite o primeiro número: 5
Digite o segundo número: 7
```

### Saída:
```
O resultado da soma é: 12
```

---

## **Resumo do Programa**
- **Classe**: `Calculadora`.
- **Método**: `soma`.
- **Objetivo**: Calcular a soma de dois números inteiros fornecidos pelo usuário.
- **Execução**: O programa solicita entrada do usuário, realiza o cálculo e exibe o resultado formatado.

Caso deseje adicionar mais funcionalidades (como subtração, multiplicação ou divisão), basta expandir a classe com novos métodos.

