/* Exercício 7 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 18/02/2025.

7 Crie um programa em Python que leia um número real e mostre na tela o seu dobro e a
sua terça parte.
Ex: Digite um número: 3.5
O dobro de 3.5 é 7.0
A terça parte de 3.5 é 1.16666*/

package Lista;

import java.util.Scanner;

public class Exercício07 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite um valor: ");
        double N = sc.nextDouble();
        System.out.println("O dobro de " + N + " é " + (N * 2));
        System.out.println("A terça parte de " + N + " é " + (N / 3));
        sc.close();
    }
}
