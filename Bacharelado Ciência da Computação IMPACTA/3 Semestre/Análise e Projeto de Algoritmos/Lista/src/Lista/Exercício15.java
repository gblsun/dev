/*

Exercício 15 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 20/02/2025.

15 - Crie um programa Java que leia o número de dias trabalhados em um mês e mostre o
salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por
hora trabalhada.
 */
package Lista;

import java.util.Scanner;

public class Exercício15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.printf("Digite o número de dias trabalhado em um mês: ");
        int n = sc.nextInt();
        double salario = (25 * (n * 8));
        sc.close();
        System.out.printf("Seu salário é: %.2f%n", salario);
    }
}
