/*
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Algoritmos e Estrutura de dados IMPACTA 26 de Fevereiro de 2025                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

 */

package Estrutura;

import java.util.Scanner;

public class EstruSwitch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.printf("Digite um valor: ");
        int num = sc.nextInt();

        switch (num) {

            case 1:
                System.out.println(" Número teste é " + num);
                break;
            case 2:
                System.out.println(" Número teste é " + num);
                break;
            case 3:
                System.out.println(" Número teste é " + num);
                break;
            case 20:
                System.out.println(" Número teste é " + num);
                break;
            case 10:
                System.out.println(" Número teste é " + num);
                break;

            default:
                System.out.println("A opção " + num + " não foi encontrada");
        }
    }
}
