/*
Exercício 14 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 19/02/2025.

14 - A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um
programa em Python que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo
que o carro custa R$ 90,00 por dia e R$ 0,20 por Km rodado.

 */
package Lista;

import java.util.Scanner;

public class Exercício14 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.printf("Digite o modelo do carro alugado: ");
        String modelo = sc.nextLine();
        System.out.printf("Digite a quilometragem percorrida do veículo alugado: ");
        double quilometragem = sc.nextDouble();
        System.out.printf("Digite a quantidade de dias pelos quais o veículo foi alugado: ");
        int quantidadeDias = sc.nextInt();
        double valorTotal = (quilometragem*0.20) + (quantidadeDias*90);
        System.out.printf("Você deverá pagar: R$ %.2f, por usar por %d dias e rodar %.2f km.%n", valorTotal, quantidadeDias, quilometragem);
        sc.close();
    }
}
