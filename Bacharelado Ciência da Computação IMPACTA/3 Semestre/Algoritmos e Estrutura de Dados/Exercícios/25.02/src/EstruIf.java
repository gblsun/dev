import java.util.Scanner;

public class EstruIf {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Digite um valor inteiro: ");
        int X = sc.nextInt();
        if (X == 20) {
            System.out.println(" X é igual a 20 ");
        }
        if (X != 50) {
            System.out.println("X é diferente de 50.");
        }
        if (X <= 5) {
            System.out.println("X é menor ou igual a 5");
        }
    }
}
