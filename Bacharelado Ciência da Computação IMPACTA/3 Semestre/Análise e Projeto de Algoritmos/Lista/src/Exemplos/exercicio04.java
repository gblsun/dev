package Exemplos;

import java.util.Scanner;

public class exercicio04 {

    public void imprime(){     //FUNCTION LINEAR

       // System.out.println("Digite o primeiro número: ");
        //Scanner n1 = new Scanner /// OQUE EU IA FAZER DA MANEIRA BÁSICA SEM USAR FUNÇÃO,,, QUE NEM OS EXERCICCIOS ANTERIORES

        //FUNCTION LINEAR
        //  EXPLORAR A CHAMADA DE FUNÇÃO // O QUE VAMOS FAZER
        // A FUNCTION MAIN É A MESMA ESTRUTURA DE QUALQUER OUTRA E NÃO É A MESMA COISA

        System.out.println("Bem Vindo ao Java!");
        System.out.println("Nome do funcionario: ");
        Scanner no =new Scanner(System.in);
        String nome = no.nextLine();
    }
    public static void main(String[] args) {
        exercicio04 acessa = new exercicio04();
        acessa.imprime();
    }
}
