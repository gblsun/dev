#include <stdio.h>

int main() {
int numeros[8];
int soma = 0;

for(int i = 0; i < 8; i++) {
printf("Digite um numero: ");
scanf("%d", &numeros[i]);
soma += numeros[i];
}

printf("Soma: %d\n", soma);

return 0;
}








/*
- O que é um byte?
    Um Byte é a unidade básica de armazenamento de dados em um computador, geralmente composta por 8 bits. Ele pode representar um único caractere, como uma letra ou um número, ou uma parte de um dado maior, como um inteiro ou um float.
    1 Byte = 8 bits
    Um byte = 256 valores possíveis (0 a 255). 2^8 = 256

- Por que array começa no índice 0?
    O array começa no índice 0 porque é uma convenção adotada na maioria das linguagens de programação, incluindo C. Isso ocorre porque o índice 0 representa o primeiro elemento do array, e os índices subsequentes representam os elementos seguintes. Essa convenção facilita a manipulação de arrays e a implementação de algoritmos que dependem de índices.
    Além disso, o uso do array começando em 0 principalemente se deve ao fato de representar um deslocamento (offset) a partir do endereço de memória incial do array, não uma contagem ordinal (1°, 2°, 3° elemento). Assim, o primeiro elemento do array está localizado no endereço de memória inicial do array, e o índice 0 é usado para acessar esse elemento.
    (offset) -> endereço de memória inicial do array + (índice * tamanho do tipo de dado)

- O que é \0?
    /0 é conhecido como o caractere nulo (null character) em C. 
    Ele é usado para indicar o final de uma string (sequência de caracteres). Quando uma string é armazenada em um array de caracteres, o caractere nulo é adicionado ao final da string para marcar onde ela termina. Isso permite que as funções de manipulação de strings saibam onde a string termina, evitando a leitura de memória além do final da string.

- Por que é importante em C estudarmos a representação de dados em memória?
    Estudar a representação de dados em memória é importante em C porque a linguagem C é uma linguagem de baixo nível que permite acesso direto à memória. 
    Compreender como os dados são representados e armazenados em memória é crucial para escrever código eficiente e seguro. Isso inclui entender como os tipos de dados são representados, como os ponteiros funcionam, e como a alocação de memória é gerenciada. Além disso, o conhecimento da representação de dados em memória pode ajudar a evitar erros comuns, como estouros de buffer e vazamentos de memória, que podem levar a falhas de segurança e instabilidade do programa.

- Por que usamos & no scanf? 
    Usamos & no scanf para passar o endereço de memória da variável onde o valor lido deve ser armazenado. 
    O scanf precisa do endereço da variável para poder modificar seu valor, e o operador & é usado para obter esse endereço. Sem o &, o scanf tentaria modificar um valor literal ou uma constante, o que resultaria em um erro de compilação ou comportamento indefinido.

- O que faz o &?
    O operador & retorna o endereço de memória de uma variável.

- Por que tem espaço antes do %c?
    O espaço antes do %c no scanf é usado para ignorar quaisquer caracteres de espaço em branco (como espaços, tabulações ou quebras de linha) que possam estar presentes no buffer de entrada. 
    Isso é importante porque, ao ler um caractere com %c, o scanf pode capturar um caractere de nova linha (gerado quando o usuário pressiona Enter) ou outros caracteres de espaço em branco, em vez do caractere desejado. O espaço antes do %c garante que o scanf ignore esses caracteres e leia apenas o próximo caractere não branco.

- Se eu criar duas variáveis diferentes, o endereço será igual?
    Não, se você criar duas variáveis diferentes, elas terão endereços de memória diferentes. Cada variável é alocada em um local distinto na memória, e o operador & retornará o endereço específico de cada variável. Portanto, mesmo que as variáveis tenham o mesmo tipo e valor, seus endereços de memória serão diferentes.
    
- Por que usamos numeros[i]?
    Usamos numeros[i] para acessar o elemento do array "numeros" na posição "i". 

- O que aconteceria se usássemos indice 8 no exemplo abaixo? 
    Se usássemos o índice 8 no exemplo abaixo, estaríamos tentando acessar um elemento fora dos limites do array "numeros", que tem apenas 8 elementos (índices de 0 a 7). Isso resultaria em comportamento indefinido, pois estaríamos acessando uma área de memória que não foi alocada para o array.

*/