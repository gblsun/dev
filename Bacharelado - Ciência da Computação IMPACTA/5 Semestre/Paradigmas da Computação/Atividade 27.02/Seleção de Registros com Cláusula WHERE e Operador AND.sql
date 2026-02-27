-- Seleciona a coluna "nome"
SELECT nome
-- Da tabela "funcionarios"
FROM funcionarios
-- Filtra apenas funcionários do departamento "Vendas"
-- E que tenham salário maior que 5000
WHERE departamento = 'Vendas' AND salario > 5000;

