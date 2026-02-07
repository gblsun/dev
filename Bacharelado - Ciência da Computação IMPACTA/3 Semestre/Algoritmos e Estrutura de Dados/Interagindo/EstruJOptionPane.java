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

public class EstruJOptionPane {
    public static void main(String[] args) {
        JOptionPane.showMessageDialog(null, "olá que bom você por aqui! ");
        String name = JOptionPane.showInputDialog("Digite seu nome:");
        JOptionPane.showMessageDialog(null, "Bom trabalho, " + name);
    }
}
