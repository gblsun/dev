/* Exercício 8 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 18/02/2025.

8 - Desenvolva um programa em Python que leia uma distância em metros e mostre os
valores relativos em outras medidas.
Ex:
Digite uma distância em metros: 100
Distância de 10000 Cm*/

package Lista;

import java.util.Scanner;

public class Exercício08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.printf("Digite uma distância em metros: ");
        int valor = sc.nextInt();
        System.out.println("Distância de " + (valor * 100) + " Cm");
        sc.close();
    }
}
