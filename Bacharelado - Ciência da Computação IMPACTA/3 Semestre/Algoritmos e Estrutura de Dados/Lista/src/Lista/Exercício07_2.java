package Lista;

import java.util.Scanner;
import java.util.Locale;

public class Exercício07_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in).useLocale(Locale.US);  // Configura o Scanner para aceitar ponto como separador decimal
        System.out.println("Digite um valor: ");
        double N = sc.nextDouble();
        System.out.println("O dobro de " + N + " é " + (N * 2));
        System.out.println("A terça parte de " + N + " é " + (N / 3));
        sc.close();
    }
}
