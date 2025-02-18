# Melhorias no Código

## 1. Uso correto do Scanner
**Antes:** O código criava dois objetos Scanner desnecessários.
```java
Scanner nome = new Scanner(System.in);
String nome1 = nome.nextLine();

Scanner salario = new Scanner(System.in);
Double salario1 = nome.nextDouble(); // ERRO: Scanner errado
```
**Agora:** Usa apenas um Scanner para todas as entradas.
```java
Scanner scanner = new Scanner(System.in);
String nome = scanner.nextLine();
double salario = scanner.nextDouble();
```

## 2. Correção na leitura do salário
**Antes:** O código tentava ler o salário usando o Scanner errado (`nome.nextDouble()`).
```java
Scanner nome = new Scanner(System.in);
String nome1 = nome.nextLine();

Scanner salario = new Scanner(System.in);
Double salario1 = nome.nextDouble(); // ERRO: nome ao invés de salario
```
**Agora:** O código usa o Scanner correto (`scanner.nextDouble()`).
```java
Scanner scanner = new Scanner(System.in);
String nome = scanner.nextLine();
double salario = scanner.nextDouble();
```

## 3. Formatação do salário
**Antes:** O salário era exibido sem formatação adequada, podendo aparecer como `1850.0`.
```java
System.out.println("O funcionário " + nome1 + " tem um salário de R$" + salario1 + " em junho");
```
**Agora:** O código usa `printf` para garantir duas casas decimais.
```java
System.out.printf("O funcionário %s tem um salário de R$%.2f em junho.%n", nome, salario);
```

## 4. Automatização da data
**Antes:** O mês era fixo no código, exigindo edição manual.
```java
System.out.println("O funcionário " + nome1 + " tem um salário de R$" + salario1 + " em junho");
```
**Agora:** O código usa `LocalDate` para obter automaticamente o mês atual.
```java
import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.Locale;

String mesAtual = LocalDate.now().getMonth().getDisplayName(TextStyle.FULL, new Locale("pt", "BR"));
System.out.printf("O funcionário %s tem um salário de R$%.2f em %s.%n", nome, salario, mesAtual);
```

## 5. Fechamento do Scanner
**Antes:** O `Scanner` nunca era fechado, podendo gerar vazamento de memória.
```java
Scanner scanner = new Scanner(System.in);
// Nenhum scanner.close() no final
```
**Agora:** O código fecha o `Scanner` corretamente após o uso.
```java
scanner.close();
```

Com essas melhorias, o código ficou mais eficiente, organizado e sem erros.

