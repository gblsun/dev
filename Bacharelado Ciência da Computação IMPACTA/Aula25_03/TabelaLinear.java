/*
Aula 25/03/2025 - Anotações por Gabriel Muchon Pavanelli.
Faculdade Impacta 25/05/2025.

 */
package Aula25_03;

public class TabelaLinear {
    public static int[] insert(int[] array, int value, int insertIndex) {
        int[] tempArray = new int[array.length + 1];
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
        int[] array = {90, 70, 50, 80, 60, 85};
        array = insert(array, 75, 2);
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + ", ");
        }
    }
}
