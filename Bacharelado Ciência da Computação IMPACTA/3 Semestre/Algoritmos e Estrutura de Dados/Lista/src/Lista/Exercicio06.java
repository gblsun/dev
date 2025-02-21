/* Exercício 6 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 18/02/2025.
6- Faça um programa em Python que leia um número inteiro e mostre o seu antecessor e seu
sucessor.
Ex:
Digite um número: 9
O antecessor de 9 é 8
O sucessor de 9 é 10*/
//|\\<------------->//|\\<------------->//|\\<------------->//|\\

package Lista;

import java.util.Scanner;

public class Exercicio06 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite um valor:");
        int valor = sc.nextInt();

        System.out.println("O valor digitado é: " + valor);
        System.out.println("O antecessor de " + valor + " é: " + (valor - 1));
        System.out.println("O sucessor de " + valor + " é: " + (valor + 2));

    }
}
