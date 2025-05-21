package aula3.tiposdedadosvaloresliteraisevariaveis;

/***
 * Tipos de dados, Valores literais e variáveis.
 *
 * Tipos primitivos.
 */
public class ExemploLiterais {
    public static void main(String[] args) {

        int exemplo = 10;
        System.out.println(exemplo);
        int exemplo2 = 010654; // Notação octal
        System.out.println(exemplo2);
        int exemplo3 = 0xA7F9; // Notação Hexadecimal
        System.out.println(exemplo3);

        double salario = 0.00000000215;
        System.out.println(salario);
        double tamanhoMolecula = 2.34e-10;
        System.out.println(tamanhoMolecula);

        boolean fumante = false;
        System.out.println(fumante);

        char sexo = 'M';
        System.out.println(sexo);



    }
}
