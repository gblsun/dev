/*
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Algoritmos e Estrutura de dados IMPACTA 26 de Fevereiro de 2025                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

*/

package Interagindo;

import java.util.Scanner;

public class EstruScanner {
    public static void main(String[] args) {

        Scanner ler = new Scanner(System.in);
        Scanner ler2 = new Scanner(System.in);

        //Utilizando somente o next se colocar mais que uma plavra, somente a primeira sera capturada
        System.out.println("Digite seu nome");
        String nome = ler.next();

        System.out.println("Digite sua idade");
        int idade = ler2.nextInt();

        System.out.println("Digite seu numero de telefone");
        int tel = ler2.nextInt();


        System.out.println(nome + idade + tel);


    }
}