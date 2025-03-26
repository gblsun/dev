/*
Aula 25/03/2025 - Anotações por Gabriel Muchon Pavanelli.
Faculdade Impacta 25/05/2025.

 */

package Aula25_03.ExercicioTabelaLinear;

public class ExercicioTabelaLinear {
    public static String[] insert(String[] array, String value, int insertIndex) {
        String[] tempArray = new String[array.length + 1];
        for (int i = 0; i < array.length; i++) {
            if (i < insertIndex) {
                tempArray[i] = array[i];
            } else {
                tempArray[i + 1] = array[i];
            }
        }
        tempArray[insertIndex] = value;
        return tempArray;
    }

    public static void main(String[] args) {
        // Definindo tabela Linear
        String[] array = {"A", "B", "C", "D", "E", "F"};
        array = insert(array, "Aqui foi adicionado um valor", 2);
        for (int i = 0; i < array.length; i++) {
            if (i == array.length - 1) {
                System.out.print(array[i] + "."); // Último elemento com ponto
            } else {
                System.out.print(array[i] + ", "); // Elementos normais com vírgula
            }
        }
    }
}
