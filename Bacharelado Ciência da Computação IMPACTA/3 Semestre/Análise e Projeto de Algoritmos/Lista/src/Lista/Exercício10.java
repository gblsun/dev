/*
Exercício 10 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 19/02/2025.

10 - Faça um programa em Python que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo
que cada litro de tinta pinta uma área de 2 metros quadrados.


 */
package Lista;

import java.util.Scanner;

public class Exercício10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Seja bem-vindo ao programa de calcular a tinta necessária para seu serviço!");
        System.out.println("Digite a largura de sua parede: ");
        double largura = sc.nextDouble();
        System.out.println("Digite a altura de sua parede: ");
        double altura = sc.nextDouble();
        double area = largura * altura;
        double qtdTinta = area / 2;
        System.out.println("Você precisará de: " + qtdTinta + " Litros de tinta.");
        sc.close();
    }
}
