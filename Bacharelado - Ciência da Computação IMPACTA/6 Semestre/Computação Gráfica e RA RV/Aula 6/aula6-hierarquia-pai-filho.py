"""
╔═══════════════════════════════════════════════════════════════╗
║  Aula 06 — EXERCÍCIO PRÁTICO — AULA 6         IMPACTA         ║
║  Computação Gráfica e RA/RV                                   ║
║  25 de Agosto de 2026                                         ║
╟───────────────────────────────────────────────────────────────╢
║  Anotações e comentários por Gabriel Muchon Pavanelli         ║
║  github: gblsunn                                              ║
╚═══════════════════════════════════════════════════════════════╝
"""

import math
import sys
import pygame

pygame.init()

LARGURA, ALTURA = 1000, 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Manipulação de objetos 3D")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 18)

# Vértices de um cubo unitário, centrado na origem.
CUBO = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
]
ARESTAS = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
           (0, 4), (1, 5), (2, 6), (3, 7)]


def rotacionar(ponto, rx, ry, rz):
    """Aplica rotações sucessivas nos eixos X, Y e Z."""
    x, y, z = ponto
    # Rotação em X
    c, s = math.cos(rx), math.sin(rx)
    y, z = y * c - z * s, y * s + z * c
    # Rotação em Y
    c, s = math.cos(ry), math.sin(ry)
    x, z = x * c + z * s, -x * s + z * c
    # Rotação em Z
    c, s = math.cos(rz), math.sin(rz)
    x, y = x * c - y * s, x * s + y * c
    return x, y, z


def transformar(ponto, pos, escala, rot):
    """Escala local, depois rotação e, por fim, translação."""
    x, y, z = ponto
    x, y, z = x * escala[0], y * escala[1], z * escala[2]
    x, y, z = rotacionar((x, y, z), *rot)
    return x + pos[0], y + pos[1], z + pos[2]


def projetar(ponto, camera, foco=520):
    """Câmera simples: deslocamento no mundo e projeção perspectiva."""
    x, y, z = ponto
    cx, cy, cz = camera
    x, y, z = x - cx, y - cy, z - cz
    z = max(z, 0.1)
    tela_x = LARGURA / 2 + foco * x / z
    tela_y = ALTURA / 2 - foco * y / z
    return int(tela_x), int(tela_y)


def desenhar_objeto(superficie, objeto, camera, cor):
    pontos = [projetar(transformar(v, objeto['pos'], objeto['escala'], objeto['rot']), camera)
              for v in CUBO]
    for a, b in ARESTAS:
        pygame.draw.line(superficie, cor, pontos[a], pontos[b], 3)


objeto = {'pos': [0, 0, 8], 'escala': [1.5, 1.5, 1.5], 'rot': [0, 0, 0]}
filho = {'pos': [0, 0, 2.8], 'escala': [0.55, 0.55, 0.55], 'rot': [0, 0, 0]}
camera = [0, 0, 0]
selecionado = 'pai'

rodando = True
while rodando:
    dt = relogio.tick(60) / 1000

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                selecionado = 'filho' if selecionado == 'pai' else 'pai'
            if evento.key == pygame.K_r:
                objeto['pos'], objeto['rot'], objeto['escala'] = [0, 0, 8], [0, 0, 0], [1.5, 1.5, 1.5]
                filho['pos'], filho['rot'], filho['escala'] = [0, 0, 2.8], [0, 0, 0], [0.55, 0.55, 0.55]

    teclas = pygame.key.get_pressed()
    alvo = objeto if selecionado == 'pai' else filho
    velocidade = 3 * dt

    # Translação do objeto selecionado no plano XZ.
    if teclas[pygame.K_LEFT]:
        alvo['pos'][0] -= velocidade
    if teclas[pygame.K_RIGHT]:
        alvo['pos'][0] += velocidade
    if teclas[pygame.K_UP]:
        alvo['pos'][2] -= velocidade
    if teclas[pygame.K_DOWN]:
        alvo['pos'][2] += velocidade

    # Rotação em torno dos eixos X e Y.
    if teclas[pygame.K_a]:
        alvo['rot'][1] -= 1.8 * dt
    if teclas[pygame.K_d]:
        alvo['rot'][1] += 1.8 * dt
    if teclas[pygame.K_w]:
        alvo['rot'][0] -= 1.8 * dt
    if teclas[pygame.K_s]:
        alvo['rot'][0] += 1.8 * dt

    # Escala uniforme.
    if teclas[pygame.K_q]:
        alvo['escala'] = [max(0.2, v - 1.2 * dt) for v in alvo['escala']]
    if teclas[pygame.K_e]:
        alvo['escala'] = [v + 1.2 * dt for v in alvo['escala']]

    # Manipulação da câmera: I/K sobe/desce, J/L desloca lateralmente.
    if teclas[pygame.K_j]:
        camera[0] -= 3 * dt
    if teclas[pygame.K_l]:
        camera[0] += 3 * dt
    if teclas[pygame.K_i]:
        camera[1] += 3 * dt
    if teclas[pygame.K_k]:
        camera[1] -= 3 * dt

    tela.fill((18, 25, 38))

    # O filho é desenhado em coordenadas do pai: relação hierárquica simples.
    desenhar_objeto(tela, objeto, camera, (60, 190, 255))
    filho_mundo = dict(filho)
    filho_mundo['pos'] = [objeto['pos'][i] + filho['pos'][i] for i in range(3)]
    filho_mundo['rot'] = [objeto['rot'][i] + filho['rot'][i] for i in range(3)]
    desenhar_objeto(tela, filho_mundo, camera, (255, 190, 70))

    texto = (f"Selecionado: {selecionado} | TAB alterna | Setas move | "
             f"A/D e W/S gira | Q/E escala")
    texto2 = "J/L e I/K movem a câmera | R restaura"
    tela.blit(fonte.render(texto, True, (235, 235, 235)), (20, 20))
    tela.blit(fonte.render(texto2, True, (190, 205, 220)), (20, 48))

    pygame.display.flip()

pygame.quit()
sys.exit()
