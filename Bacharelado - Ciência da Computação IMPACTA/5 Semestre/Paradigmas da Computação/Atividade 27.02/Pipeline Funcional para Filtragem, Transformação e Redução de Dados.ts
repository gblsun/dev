// ================================================
// Processamento Funcional de Produtos
// Objetivo: Filtrar eletrônicos, aplicar desconto
// e calcular o total final sem alterar os dados originais
// ================================================


// 1️ - Definição do Tipo (Estrutura do Produto)
// Define como um objeto Product deve ser estruturado
type Product = {
  name: string;      // Nome do produto
  price: number;     // Preço do produto
  category: string;  // Categoria do produto
};


// 2️ - Lista de Produtos (Dados Iniciais)
// Array tipado como Product[]
// "const" impede reatribuição da variável
const products: Product[] = [
  { name: 'Notebook', price: 2000, category: 'eletronics' },
  { name: 'Mouse', price: 100, category: 'eletronics' },
  { name: 'Livro', price: 50, category: 'books' },
  { name: 'Monitor', price: 1000, category: 'eletronics' },
];


// 3️ - Função Pura: Verifica se o produto é da categoria "eletronics"
// Retorna true ou false
const isElectronics = (p: Product) => 
  p.category === 'eletronics';


// 4️ - Função Pura: Aplica 10% de desconto
// Cria um NOVO objeto (imutabilidade)
// Spread operator (...) copia todas as propriedades
// Apenas o preço é modificado
const applyDiscount = (p: Product): Product => ({
  ...p,
  price: p.price * 0.9
});


// 5️ -  Função Pura: Soma os preços
// acc = acumulador
// p = produto atual
// Retorna o acumulador somado ao preço do produto
const sumPrices = (acc: number, p: Product) => 
  acc + p.price;


// 6️ - Pipeline Funcional (Processamento Principal)
// Encadeamento declarativo das operações
const totalDiscountedElectronics = products

  // Filtra apenas produtos da categoria "eletronics"
  .filter(isElectronics)

  // Aplica desconto de 10% em cada produto filtrado
  // Retorna um novo array com preços atualizados
  .map(applyDiscount)

  // Soma todos os preços do array resultante
  // O valor inicial do acumulador é 0
  .reduce(sumPrices, 0);


// 7️ - Exibe o total final com desconto aplicado
console.log('Total:', totalDiscountedElectronics);
// Saída esperada: 2790


// 8️ - Verifica que o array original não foi alterado
// Mostra que o preço do primeiro produto continua 2000
console.log('Original intacto:', products[0].price);
// Saída esperada: 2000