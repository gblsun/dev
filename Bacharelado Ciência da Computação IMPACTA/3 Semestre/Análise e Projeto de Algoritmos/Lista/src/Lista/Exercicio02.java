/*
2- Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-
vindas para ela:

Ex:
Qual é o seu nome? João da Silva
Olá João da Silva, é um prazer te conhecer!
 */
package Lista;

import java.util.Scanner;

public class Exercicio02 {
    public static void main(String[] args) {
        System.out.print("Qual seu nome? ");
        Scanner nome = new Scanner(System.in);
        String nome1 = nome.nextLine();
        System.out.print("Olá "+nome1+", é um prazer te conhecer! ");
    }
}
