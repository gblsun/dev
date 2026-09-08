### Anotações 25/08

#### Modelagem 3D
- Reaproveita o mesmo formato das Aulas 4 e 5: o cubo é uma lista de **vértices** mais uma lista de **arestas** (pares de índices), desenhado em **wireframe** (`pygame.draw.line`).
- Cada objeto é um dicionário com `pos`, `escala` e `rot`, o que facilita animar e resetar o estado.

#### Hierarquia pai-filho
- `objeto` (pai) e `filho` guardam a posição/rotação do filho em **coordenadas locais ao pai**, não em coordenadas do mundo.
- Antes de desenhar, o filho é convertido para o mundo somando pai + filho componente a componente:
  - `filho_mundo['pos'] = objeto['pos'] + filho['pos']`
  - `filho_mundo['rot'] = objeto['rot'] + filho['rot']`
- Isso é uma hierarquia simplificada (soma direta, sem matriz de transformação do pai): mover ou girar o pai também desloca o filho junto, mas a escala do filho não é composta com a do pai.

#### Rotação por eixo (sem matrizes)
- Igual à Aula 5, `rotacionar()` aplica trigonometria diretamente, um eixo por vez (X → Y → Z), equivalente a multiplicar as três matrizes de rotação nessa ordem.

#### Transformação de modelo e projeção
- `transformar()` aplica, na ordem: **escala** → **rotação** → **translação**.
- `projetar()` usa projeção em perspectiva com `foco=520`, limitando `z` a no mínimo `0.1` como plano de recorte simplificado.

#### Seleção e controles
| Tecla | Ação |
|---|---|
| `TAB` | Alterna o objeto selecionado (pai ⇄ filho) |
| Setas | Move o objeto selecionado no plano XZ |
| `A` / `D` | Rotaciona o objeto selecionado no eixo Y |
| `W` / `S` | Rotaciona o objeto selecionado no eixo X |
| `Q` / `E` | Diminui / aumenta a escala do objeto selecionado |
| `J` / `L` | Move a câmera lateralmente (eixo X) |
| `I` / `K` | Move a câmera para cima / baixo (eixo Y) |
| `R` | Restaura posição, rotação e escala de pai e filho |

#### Correções feitas
- O arquivo original havia perdido toda a indentação dos blocos (`def`, `while`, `for`, `if`), impedindo a execução — mesmo tipo de corrupção de cópia visto nas Aulas 4 e 5.
- Duas atribuições múltiplas (reset do `R`) e a f-string de instruções estavam quebradas no meio da expressão por quebras de linha inválidas; foram reescritas em linhas válidas.
- Adicionado `import sys` e `sys.exit()` ao final, para encerrar o processo de forma limpa ao fechar a janela (mesmo padrão da Aula 5).

#### Implementação
- `aula6-hierarquia-pai-filho.py` — cena interativa em **Pygame** com dois cubos em relação hierárquica pai-filho, seleção via `TAB`, transformações independentes por objeto e câmera móvel.
