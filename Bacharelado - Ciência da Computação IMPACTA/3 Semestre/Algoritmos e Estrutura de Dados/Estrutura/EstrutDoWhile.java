/*
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Algoritmos e Estrutura de dados IMPACTA 26 de Fevereiro de 2025                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

 */

package Estrutura;

public class EstrutDoWhile {
    public static void main(String[] args) {
        int multiplicador = 0;
        int mult = 2;
        int resultado = 0;
        do{
            System.out.println(multiplicador + " X " + mult + " = " + resultado);
            multiplicador++;
            resultado = resultado + mult;
            mult = mult + 1;
        }
        while (multiplicador <= 10);{
            System.out.println("Tabuada finalizada");
        }
    }
}
