import java.text.NumberFormat;
import java.util.Scanner;

// • Crie um programa que leia o nome e o salário de um funcionário,mostrando no final uma mensagem.
//Ex: Nome do Funcionário: Maria do Carmo Salário: 1850,45
//O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.

public class Main {
    public static void main(String[] args) {

        System.out.println("Informe o nome: ");
        Scanner no =new Scanner(System.in); // Scanner ---> Capturar algo do teclado / o que vc escreveu pelo teclado / INPUT
        String nome = no.nextLine(); // Adicionar o conteudo de uma variavel em uma variavel
        //no.close(); //Fechar o epaço de memoria para não aacessar mais //// Se VC FECHAR ESTA VARIAVEL A OUTRA NÃO ACONTECE,
        // ENTAO ESSEE COMANDO VAI FICAR COMO COMENTARIO PARA QUE O SALARIO.CLOSE(); FIQUE FECHADO E O PROGRAMA RODE NORMALMENTE
        // EXERCICIO 1

        System.out.println("Informe o salário: ");
        Scanner sa = new Scanner(System.in); // PERGUNTA
        Double salario = sa.nextDouble();
        sa.close();

        // RESPOSTA
        System.out.println("Olá " + nome + ", é um prazer te conhecer!"); // exercicio 1
        System.out.println("O funcionario " + nome + " tem um salario de " + NumberFormat.getCurrencyInstance().format(salario)); // exercicio 2
        // instancia pegar do contador do idioma que vc / sseu computador esta formatado


    }
}


// FALAR MAIS NA AULA TEÓRICA SOBRE OS TIPOS DE DADOS: PARA CONSEGUIR ACESSAR VALORES DAS VARIAVEIS E FAZER CONTAS COM OS SEUS CONTEUDOS
// Double é um float maior 64 bits o float é 32





//Desenvolva o código e o algoritmo ----> PROVA CAIR -------> Qual a diferença ?????????????????
// ?????????????????????????????????????????????????????????????????????????????????????????????







