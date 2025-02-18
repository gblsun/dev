package Exemplos;

import java.util.Scanner;

public class media2 {
    public static void main(String[] args) {
        int numero;
        int cont = 0;
        int soma = 0;

        Scanner in = new Scanner(System.in);
        System.out.println("Entre com um numero positivo, um numero negativo encerra: ");

        while ((numero = in.nextInt()) >= 0) {
            soma += numero;
            cont++;
        }

        in.close();

        int media = soma/cont;
        System.out.println("\nA média dos numeros digitados é de: " + media + "\nForam digitados " + cont + " números.");
    }
}