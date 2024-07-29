import pygame

# Inicializa Pygame
pygame.init()

# Clase Boton
class Boton:
    def __init__(self, x, y, ancho, alto, color_base, color_hover, texto='', fuente=None, color_texto=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color_base = color_base
        self.color_hover = color_hover
        self.color_actual = color_base
        self.texto = texto
        self.fuente = fuente if fuente else pygame.font.SysFont(None, 40)
        self.color_texto = color_texto

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color_actual, self.rect)
        if self.texto:
            texto_render = self.fuente.render(self.texto, True, self.color_texto)
            pantalla.blit(texto_render, texto_render.get_rect(center=self.rect.center))

    def es_presionado(self, posicion):
        return self.rect.collidepoint(posicion)

    def actualizar(self, posicion):
        if self.rect.collidepoint(posicion):
            self.color_actual = self.color_hover
        else:
            self.color_actual = self.color_base

# Configuraciones de pantalla
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Ejemplo de Botón')

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Crear un botón
boton = Boton(300, 250, 200, 100, ROJO, VERDE, 'Click Me')

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton.es_presionado(evento.pos):
                print('Botón presionado')

    pantalla.fill(BLANCO)

    # Actualizar y dibujar el botón
    boton.actualizar(pygame.mouse.get_pos())
    boton.dibujar(pantalla)

    pygame.display.flip()

pygame.quit()
