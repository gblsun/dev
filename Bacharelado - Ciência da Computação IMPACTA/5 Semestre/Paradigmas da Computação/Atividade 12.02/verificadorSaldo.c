#include <stdio.h>  
// Inclui a biblioteca padrão de entrada e saída (printf e scanf)

int main() {  
// Função principal do programa (onde tudo começa)

    float saldo;  
    // Cria uma variável do tipo float para guardar o saldo

    printf("Digite o saldo: ");  
    // Mostra uma mensagem na tela pedindo o valor do saldo

    scanf("%f", &saldo);  
    // Lê o número digitado pelo usuário
    // %f indica que é um float
    // &saldo passa o endereço da variável para o scanf

    if (saldo > 0) {  
    // Verifica se o saldo é maior que zero

        printf("Saldo positivo\n");  
        // Executa se a condição for verdadeira

    } else {  
    // Executa se a condição for falsa (saldo zero ou negativo)

        printf("Saldo insuficiente\n");  
        // Mostra essa mensagem quando não há saldo positivo
    }

    return 0;  
    // Finaliza o programa com sucesso
}
