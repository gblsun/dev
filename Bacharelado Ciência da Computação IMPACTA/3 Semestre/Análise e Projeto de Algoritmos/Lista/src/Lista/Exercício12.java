/*
Exercício 12 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 19/02/2025.

12 - Crie um programa em Python que leia o preço de um produto, calcule e mostre o
seu PREÇO PROMOCIONAL, com 5% de desconto.

 */
package Lista;

import java.util.Scanner;

public class Exercício12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.printf("Digite o nome do produto: ");
        String produto = sc.nextLine();
        System.out.printf("Digite o preço do produto: ");
        double preco = sc.nextDouble();
        double precoPromocional = preco - (preco * 0.05);
        System.out.println("O valor do produto " + produto + " possui o valor de: " + preco + ".\nPorém, com o desconto de 5%, o produto acaba saindo por: " + precoPromocional);
        sc.close();
    }
}
