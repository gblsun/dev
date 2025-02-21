/*
5 - Faça um programa em Python que leia as duas notas de um aluno em uma matéria e
mostre na tela a sua média na disciplina.
Ex:
Nota 1: 4.5
Nota 2: 8.5
A média entre 4.5 e 8.5 é igual a 6.5*/

package Lista;

import java.util.Scanner;

public class Exercicio05 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite a primeira nota:");
        Double nota1 = scanner.nextDouble(); //essa forma scanner.nextDouble(); é mais eficiênte

        Double nota2 = scanner.nextDouble();
        System.out.println("Digite a segunda nota:");

        double media = (nota1 + nota2) / 2;

        System.out.println("A média entre " + nota1 + " e " + nota2 + " é igual a " + media);

    }
}