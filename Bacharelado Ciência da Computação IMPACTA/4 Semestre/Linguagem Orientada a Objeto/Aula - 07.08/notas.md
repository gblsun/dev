# Notas da aula 07/08. Cópia Rasa ou Cópia Profunda

```lista = [1, 2, 3]

lista2 = lista

lista2[0] = 5
```

Tem que prestar atenção: os elementos podem ser: 
- #### mutáveis
- #### imutáveis

Lista encadenhada ou aninhada:

```lista = [[1, 2, 3], [4, 5, 6]] 

import copy

lista2 = copy.copy(lista)

lista

>>> [[1, 2, 3], [4, 5, 6]]
lista2
>>> [[1, 2, 3], [4, 5, 6]]```

**módulo copy é uma cópia rasa.** 1° Nível.

lista2 = copy.deepcopy(lista) → Cópia profunda. **(Qual nível???)**
```
Slice (fatiamente) ou o módulo copy
