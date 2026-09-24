"""
╔═══════════════════════════════════════════════════════════════╗
║  EXERCÍCIO PRÁTICO — COMPUTAÇÃO GRÁFICA E RA/RV            ║
║  Ambiente 3D interativo com câmera e objetos 3D               ║
║  Feito para estudo em Python + Pygame                        ║
╟───────────────────────────────────────────────────────────────╢
║  Objetivo: demonstrar conceitos de pipeline gráfico,         ║
║  projeção, transformação 3D e navegação em cena virtual.     ║
╚═══════════════════════════════════════════════════════════════╝
"""

import math
import pygame

pygame.init()

LARGURA, ALTURA = 1000, 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Computação Gráfica - RA/RV - Exercício Prático")
clock = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 22)
fonte_pequena = pygame.font.SysFont("arial", 18)

# Cores
FUNDO = (18, 24, 38)
BRANCO = (235, 240, 248)
AZUL = (80, 190, 255)
LARANJA = (255, 170, 80)
VERDE = (100, 220, 160)
ROXO = (180, 140, 255)
SELECAO = (255, 235, 120)

# Modelos 3D em coordenadas locais
CUBO = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
]
ARESTAS_CUBO = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]

PIRAMIDE = [
    (-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (0, 2.2, 0)
]
ARESTAS_PIRAMIDE = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (0, 4), (1, 4), (2, 4), (3, 4),
]

PRISMA = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
    (0, 2.5, 0),
]
ARESTAS_PRISMA = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
    (0, 8), (1, 8), (2, 8), (3, 8),
    (4, 8), (5, 8), (6, 8), (7, 8),
]


def rotacionar(ponto, angulo_x, angulo_y, angulo_z):
    """Aplica rotação em X, Y e Z sobre um ponto 3D."""
    x, y, z = ponto

    cx, sx = math.cos(angulo_x), math.sin(angulo_x)
    y, z = y * cx - z * sx, y * sx + z * cx

    cy, sy = math.cos(angulo_y), math.sin(angulo_y)
    x, z = x * cy + z * sy, -x * sy + z * cy

    cz, sz = math.cos(angulo_z), math.sin(angulo_z)
    x, y = x * cz - y * sz, x * sz + y * cz

    return (x, y, z)


def transformar(ponto, posicao, rotacao, escala):
    """Escala -> rotação -> translação."""
    escalado = tuple(c * escala for c in ponto)
    rotacionado = rotacionar(escalado, *rotacao)
    return tuple(g + t for g, t in zip(rotacionado, posicao))


def projetar_perspectiva(ponto, camera, distancia_focal=420):
    """Projeto em perspectiva a partir da câmera."""
    x, y, z = (ponto[i] - camera[i] for i in range(3))
    z = max(z, 0.15)
    fator = distancia_focal / z
    return (
        int(LARGURA / 2 + x * fator),
        int(ALTURA / 2 - y * fator),
    )


def projetar_ortografica(ponto, camera):
    """Projeto em projeção ortográfica."""
    x, y, z = (ponto[i] - camera[i] for i in range(3))
    fator = 180
    return (
        int(LARGURA / 2 + x * fator),
        int(ALTURA / 2 - y * fator),
    )


def desenhar_objeto(obj, camera, perspectiva, selecionado=False):
    """Transforma, projeta e desenha um objeto 3D."""
    pontos_2d = []
    for vertice in obj["modelo"]:
        mundo = transformar(
            vertice,
            obj["posicao"],
            obj["rotacao"],
            obj["escala"],
        )
        if perspectiva:
            pontos_2d.append(projetar_perspectiva(mundo, camera))
        else:
            pontos_2d.append(projetar_ortografica(mundo, camera))

    for a, b in obj["arestas"]:
        pygame.draw.line(
            tela,
            obj["cor"],
            pontos_2d[a],
            pontos_2d[b],
            3 if not selecionado else 5,
        )

    if selecionado:
        centro = [0, 0, 0]
        for ponto in obj["modelo"]:
            mundo = transformar(ponto, obj["posicao"], obj["rotacao"], obj["escala"])
            centro = [centro[i] + mundo[i] for i in range(3)]
        centro = tuple(c / len(obj["modelo"]) for c in centro)
        proj = projetar_perspectiva(centro, camera) if perspectiva else projetar_ortografica(centro, camera)
        pygame.draw.circle(tela, SELECAO, proj, 8, 2)


# Lista de objetos da cena
objetos = [
    {"modelo": CUBO, "arestas": ARESTAS_CUBO, "posicao": (-3.5, -0.5, 8), "rotacao": (0.0, 0.5, 0.0), "escala": 1.5, "cor": AZUL},
    {"modelo": PIRAMIDE, "arestas": ARESTAS_PIRAMIDE, "posicao": (2.5, 0.0, 9), "rotacao": (0.0, 0.8, 0.5), "escala": 1.6, "cor": LARANJA},
    {"modelo": PRISMA, "arestas": ARESTAS_PRISMA, "posicao": (0.0, 1.5, 12), "rotacao": (0.2, 1.2, 0.4), "escala": 1.1, "cor": VERDE},
]

camera = [0.0, 0.0, 0.0]
objeto_selecionado = 0
perspectiva = True
executando = True

while executando:
    dt = clock.tick(60) / 1000.0

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                executando = False
            elif evento.key == pygame.K_p:
                perspectiva = not perspectiva
            elif evento.key == pygame.K_r:
                camera[:] = [0.0, 0.0, 0.0]
                for obj in objetos:
                    obj["rotacao"] = (0.0, 0.0, 0.0)
                    obj["posicao"] = list(obj["posicao"])
            elif evento.key == pygame.K_1:
                objeto_selecionado = 0
            elif evento.key == pygame.K_2:
                objeto_selecionado = 1
            elif evento.key == pygame.K_3:
                objeto_selecionado = 2

    teclas = pygame.key.get_pressed()
    velocidade = 3.0 * dt

    # Movimento da câmera
    if teclas[pygame.K_LEFT]:
        camera[0] -= velocidade
    if teclas[pygame.K_RIGHT]:
        camera[0] += velocidade
    if teclas[pygame.K_UP]:
        camera[1] += velocidade
    if teclas[pygame.K_DOWN]:
        camera[1] -= velocidade
    if teclas[pygame.K_w]:
        camera[2] += velocidade
    if teclas[pygame.K_s]:
        camera[2] -= velocidade

    # Transformação do objeto selecionado
    obj = objetos[objeto_selecionado]
    if teclas[pygame.K_a]:
        obj["rotacao"] = (obj["rotacao"][0], obj["rotacao"][1] - velocidade, obj["rotacao"][2])
    if teclas[pygame.K_d]:
        obj["rotacao"] = (obj["rotacao"][0], obj["rotacao"][1] + velocidade, obj["rotacao"][2])
    if teclas[pygame.K_q]:
        obj["rotacao"] = (obj["rotacao"][0] - velocidade, obj["rotacao"][1], obj["rotacao"][2])
    if teclas[pygame.K_e]:
        obj["rotacao"] = (obj["rotacao"][0] + velocidade, obj["rotacao"][1], obj["rotacao"][2])
    if teclas[pygame.K_z]:
        obj["escala"] = max(0.5, obj["escala"] - 0.8 * dt)
    if teclas[pygame.K_x]:
        obj["escala"] = min(3.0, obj["escala"] + 0.8 * dt)

    # Visualização
    tela.fill(FUNDO)

    for indice, obj in enumerate(objetos):
        desenhar_objeto(obj, camera, perspectiva, selecionado=(indice == objeto_selecionado))

    modo = "perspectiva" if perspectiva else "ortográfica"
    texto = fonte.render(f"Projeção: {modo} | Objeto: {objeto_selecionado + 1}", True, BRANCO)
    instrucoes = fonte.render(
        "Setas/W-S: câmera | 1/2/3: seleciona | A/D: rotação Y | Q/E: rotação X | Z/X: escala | P: alternar | ESC: sair",
        True,
        (190, 205, 220),
    )
    tela.blit(texto, (20, 18))
    tela.blit(instrucoes, (20, 52))

    aux = fonte_pequena.render("Exercício de Computação Gráfica e RA/RV", True, (220, 230, 235))
    tela.blit(aux, (20, 82))

    pygame.display.flip()

pygame.quit()
