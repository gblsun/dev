public class CreditCard {
    //Variáveis de instância
    private String number;
    private String name;
    private String bank;
    private double balance;
    private int limit;

    //Contrutor
    CreditCard(String no, String nm, String bk, double bal, int lim) {
        number = no;
        name = nm;
        bank = bk;
        balance = bal;
        limit = lim;
    }

    //Métodos de acesso:
    public String getNumber() {
        return number;
    }

    public String getName() {
        return name;
    }

    public String getBank() {
        return bank;
    }

    public double getBalance() {
        return balance;
    }

    public int getLimit() {
        return limit;
    }

    //Métodos de ação
    public boolean chargeIt(double price) { //Debita
        if (price + balance > (double) limit)
            return false; //Não há dinheiro suficiente para debitar
        balance += price;
        return true; //Neste caso, o débito foi efetivado
    }

    public void makePayment(double payment) { //Faz um pagamento
        balance -= payment;
    }

    public static void printCard(CreditCard c) { //Imprime informações sobre o cartão
        System.out.println("Number = " + c.getNumber());
        System.out.println("Name = " + c.getName());
        System.out.println("Bank = " + c.getBank());
        System.out.println("Balance = " + c.getBalance()); //Conversão implícita
        System.out.println("limit = " + c.getLimit()); //Conversão implícita

    }

}