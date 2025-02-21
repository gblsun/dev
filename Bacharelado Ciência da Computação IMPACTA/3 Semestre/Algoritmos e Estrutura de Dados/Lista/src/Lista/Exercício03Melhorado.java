package Lista;

import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.Locale;
import java.util.Scanner;

public class Exercício03Melhorado {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();

        System.out.print("Digite seu salário: ");
        double salario = scanner.nextDouble();

        // Obtém o nome do mês atual em português
        String mesAtual = LocalDate.now().getMonth().getDisplayName(TextStyle.FULL, new Locale("pt", "BR"));

        // Exibe os resultados formatados corretamente
        System.out.println("Nome do funcionário: " + nome);
        System.out.printf("O funcionário %s tem um salário de R$%.2f em %s.%n", nome, salario, mesAtual);

        scanner.close(); // Fecha o scanner para evitar vazamento de memória
    }
}

/*
O que foi melhorado no código?

→ Uso correto do Scanner:
    ↳ Antes, o código criava dois objetos Scanner desnecessários.
    ↳ Agora, usa apenas um, tornando o código mais eficiente e evitando erros.

Antes:

Scanner nome = new Scanner(System.in);
String nome1 = nome.nextLine();

Scanner salario = new Scanner(System.in);
Double salario1 = nome.nextDouble(); // ERRO: Scanner errado

Depois:

Scanner scanner = new Scanner(System.in);
String nome = scanner.nextLine();
double salario = scanner.nextDouble();

<------------->//|\\<------------->//|\\<------------->

→ Correção na leitura do salário:
    ↳ O código antes tentava ler o salário usando o scanner errado.
    ↳ Agora, o Scanner correto é utilizado.

Antes:

Scanner nome = new Scanner(System.in);
String nome1 = nome.nextLine();

Scanner salario = new Scanner(System.in);
Double salario1 = nome.nextDouble(); // ERRO: nome ao invés de salario

Depois:

Scanner scanner = new Scanner(System.in);
String nome = scanner.nextLine();
double salario = scanner.nextDouble();

<------------->//|\\<------------->//|\\<------------->

→ Formatação do salário:
    ↳ O salário era exibido sem formatação adequada.
    ↳ Agora, é garantido que apareça com duas casas decimais.

Antes:

System.out.println("O funcionário " + nome1 + " tem um salário de R$" + salario1 + " em junho");

Depois:

System.out.println("O funcionário " + nome1 + " tem um salário de R$" + salario1 + " em junho");

<------------->//|\\<------------->//|\\<------------->

→ Automatização da data:
    ↳ Antes, o mês era fixo no código.
    ↳ Agora, o código utiliza LocalDate para exibir automaticamente o mês atual.

Antes:

System.out.println("O funcionário " + nome1 + " tem um salário de R$" + salario1 + " em junho");

Depois:

import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.Locale;

String mesAtual = LocalDate.now().getMonth().getDisplayName(TextStyle.FULL, new Locale("pt", "BR"));
System.out.printf("O funcionário %s tem um salário de R$%.2f em %s.%n", nome, salario, mesAtual);

<------------->//|\\<------------->//|\\<------------->

→ Fechamento do Scanner:
    ↳ O Scanner ficava aberto, podendo causar vazamento de memória.
    ↳ Agora, é fechado corretamente.

Antes:

Scanner scanner = new Scanner(System.in);
// Nenhum scanner.close() no final

Depois:

scanner.close();

<------------->//|\\<------------->//|\\<------------->

 */
