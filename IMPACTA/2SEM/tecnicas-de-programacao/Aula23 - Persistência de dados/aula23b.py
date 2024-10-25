'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 23: técnicas de programação IMPACTA 11 de Outubro de 2024                       |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

continuando...

Leitura dos arquivos

→ Função integrada open
→ Diferentes formas de abrir um arquivo

Caractere | Significado
'r'       |abre para leitura (padrão)
'w'       |abre para escrita truncando o arquivo primeiro caso ele exista
'x'       |abre para criação exclusiva falhando caso o arquivo exista
'a'       |abre para escrita anexando ao final do arquivo caso ele exista
'b'       |modo binário
't'       |modo texto (padrão)
'+'       |abre para atualização (leitura e escrita)
'''
# %%
f = open('teste.txt', 'w')
f.write('Olá Mundo!\n')
f.close()
