/* Exercício 9 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 18/02/2025.

9 - Faça um programa em Python que leia quanto dinheiro uma pessoa tem na carteira (em
R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45. (ou cotação
atual)*/
package Lista;

import java.util.Scanner;

public class Exercício09 {
    public static void main(String[] args) {

        // 1 Real = 5,6973 Doláres 
        Scanner sc = new Scanner(System.in);
        System.out.println("Quantos Reais você possui na carteira?: ");
        double reais = sc.nextDouble();
        double dolar = reais / 5.6973;
        System.out.println("Você possui: R$" + reais + ". Ou seja: $" + dolar);
        sc.close();
    }
}
