/*
Exercício 11 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 19/02/2025.

11 - Desenvolva um programa em Python que leia os valores de A, B e C de uma
equação do segundo grau e mostre o valor de Delta. (formula Δ = b2 – 4ac)


 */
package Lista;

import java.util.Scanner;

public class Exercício11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Seja bem vindo ao programa de calcular o Δ (Delta)!");
        System.out.printf("Digite o valor de A: ");
        double a = sc.nextDouble();
        System.out.printf("Digite o valor de B: ");
        double b = sc.nextDouble();
        System.out.printf("Digite o valor de C: ");
        double c = sc.nextDouble();
        double delta = (b * b) - (4 * a * c);
        System.out.println("O valor de Δ (Delta) é: " + delta);
        sc.close();
    }
}
