/*
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Algoritmos e Estrutura de dados IMPACTA 26 de Fevereiro de 2025                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

 */

package Interagindo;

import javax.swing.*;

public class EstruJOptionPane2 {
    public static void main(String[] args) {

        String ex = "";

        for(int a =1;a<=10;a++){
            for(int b=1;b<=5;b++){
                ex +=(b+ "x" +a+ "=" +(b*a)+" \t");
            }
            ex +=(" ");
            ex +=("\n");

        }
        ex +=(" ");
        ex +=("\n");
        for(int a =1;a<=10;a++){
            for(int b=6;b<=10;b++){
                ex +=(b+ "x" +a+ "=" +(b*a)+" \t");
            }
            ex +=(" ");

            ex +=("\n");

        }
        JTextArea JtxArea = new JTextArea(ex);
        JOptionPane.showMessageDialog(null, JtxArea);
    }

}