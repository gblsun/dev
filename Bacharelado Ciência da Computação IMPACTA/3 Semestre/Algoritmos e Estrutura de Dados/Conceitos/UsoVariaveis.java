package Conceitos;

import java.util.Scanner;

public class UsoVariaveis {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean menina = false;

        System.out.println("Escolha entre menino ou menina ");
        boolean escolha = sc.nextLine().equalsIgnoreCase("menina");
        if (menina) {
            System.out.println(" Sou Menina. ");
        } else {
            System.out.println(" Sou Menino. ");
        }

    }
}

/**
 * Tipos de variáveis que vamos aprender ao longo do curso
 * byte
 * short
 * int
 * long
 * float
 * double
 * char
 * boolean
 */