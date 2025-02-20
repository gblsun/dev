/*
Exercício 13 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 19/02/2025.

13 - Faça um programa em Python que leia o salário de um funcionário, calcule e mostre o
seu novo salário, com 15% de aumento.
 */
package Lista;

import java.util.Scanner;

public class Exercício13 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.printf("Digite o seu nome: ");
        String nome = sc.nextLine();
        System.out.printf("Digite o seu salário: ");
        double salario = sc.nextDouble();
        double salarioNovo = salario + (salario * 0.15);
        System.out.printf(nome+", seu novo salário com reajuste, será de: %.2f\n",salarioNovo);
        sc.close();
    }
}
