package Exemplos;

import java.util.Scanner;

public class media {

    public static void main(String[] args) {

        System.out.println("Digite a primeira nota:");
        Scanner n1 =new Scanner(System.in);
        double nota1 = n1.nextDouble();

        System.out.println("Digite a segunda nota:");
        Scanner n2 =new Scanner(System.in);
        double nota2 = n2.nextDouble();


        System.out.println("Digite a terceira nota:");
        Scanner n3 =new Scanner(System.in);
        double nota3 = n3.nextDouble();

        double media = ( nota1 + nota2 + nota3)/3;

        //
        if(media >=6){
            System.out.println("Você foi aprovado com média: " + media);
        }else
        {
            System.out.println("Você foi reprovado com média: " + media);
        }
    }
}
