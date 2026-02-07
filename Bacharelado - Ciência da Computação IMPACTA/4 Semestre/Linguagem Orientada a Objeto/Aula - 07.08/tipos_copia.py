import copy

# Exemplo de estrutura de dados aninhada
original = [[1, 2, 3], [4, 5, 6]]

# Cópia Fake - Apenas outra referência ao mesmo objeto
copia = original
copia[0][0] = 99  # Modifica também o original
print("Original:", original)
print("Cópia Fake:", copia)

# Restaurando o original para evitar interferência
original = [[1, 2, 3], [4, 5, 6]]

# Cópia Rasa - copia apenas a estrutura de nível superior
copia_rasa = copy.copy(original)
copia_rasa[0] = 99
print("Original:", original)
print("Cópia Rasa:", copia_rasa)
copia_rasa[1][0] = 99  # Modifica o original, porque listas internas são compartilhadas
print("Original:", original)
print("Cópia Rasa:", copia_rasa)

# Restaurando o original para evitar interferência
original = [[1, 2, 3], [4, 5, 6]]

# Cópia Profunda - copia toda a estrutura recursivamente
copia_profunda = copy.deepcopy(original)
copia_profunda[0][0] = 99  # Não modifica o original
print("Original:", original)
print("Cópia Profunda:", copia_profunda)