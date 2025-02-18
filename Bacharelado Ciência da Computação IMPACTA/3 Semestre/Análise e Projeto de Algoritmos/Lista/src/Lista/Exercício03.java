/*
3- Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma
mensagem.
Ex:
Nome do Funcionário: Maria do Carmo Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em junho.*/
package Lista;

import java.util.Scanner;

public class Exercício03 {
    public static void main(String[] args) {
        System.out.println("Digite seu nome: ");
        Scanner nome = new Scanner(System.in);
        String nome1 = nome.nextLine();
        System.out.println("Digite seu salário: ");
        Scanner salario = new Scanner(System.in);
        Double salario1 = nome.nextDouble();
        System.out.println("Nome do funcionário: "+nome1+": "+salario1);
        System.out.println("O funcionario: "+nome1+" tem um salário de R$"+salario1+" em junho");
    }
}
