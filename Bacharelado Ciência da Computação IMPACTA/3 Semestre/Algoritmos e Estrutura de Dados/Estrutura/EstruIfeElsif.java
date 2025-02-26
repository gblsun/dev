/*
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Algoritmos e Estrutura de dados IMPACTA 26 de Fevereiro de 2025                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

 */

package Estrutura;

public class EstruIfeElsif {
    public static void main(String[] args) {
        String nome = "Gabriel Muchon Pavanelli";
        int idade = 19;

        if(idade >= 18) {
            System.out.println("Maior de idade");
        } else if (idade < 18) {
            System.out.println("Menor de idade");
        } else if (idade == 18) {
            System.out.println("Igual a 18");
        }
        else{
            System.out.println("Você tem "+idade+" anos");
        }
    }
}
