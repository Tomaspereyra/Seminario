import pygame
from pygame.locals import *
import sys
import random

class Juego:
    def __init__(self):
        self.puntaje = 0
        self.vidas = 2
        pygame.font.init()
        self.font = pygame.font.Font("assets/fuente.ttf", 15)
        disenioDeBarrera = [[],[0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
                         [0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                         [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                         [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                         [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
                         [1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
                         [1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1],
                         [1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1],
                         [1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1]]

        self.screen = pygame.display.set_mode((800, 600))
        self.enemigos_sprites = {
                0:[pygame.image.load("assets/a1_0.png").convert(), pygame.image.load("assets/a1_1.png").convert()],
                1:[pygame.image.load("assets/a2_0.png").convert(), pygame.image.load("assets/a2_1.png").convert()],
                2:[pygame.image.load("assets/a3_0.png").convert(), pygame.image.load("assets/a3_1.png").convert()],
                }
        self.player = pygame.image.load("assets/shooter.png").convert()
        self.animacion_On = 0
        self.direccion = 1
        self.enemigos_velocidad = 20
        self.enemigos_ultMov = 0
        self.playerX = 400
        self.playerY = 550
        self.bala = None
        self.balas = []
        self.enemigos = []
        self.barrera_particulas = []
        startY = 50
        startX = 50
        for filas in range(6):
            out = []
            if filas < 2:
                enemigo = 0
            elif filas < 4:
                enemigo = 1
            else:
                enemigo = 2
            for columns in range(10):
                out.append((enemigo,pygame.Rect(startX * columns, startY * filas, 35, 35)))
            self.enemigos.append(out)
        self.chance = 990

        barreraX = 50
        barreraY = 400
        espacio = 100

        for offset in range(1, 5):
            for b in disenioDeBarrera:
                for b in b:
                    if b != 0:
                        self.barrera_particulas.append(pygame.Rect(barreraX + espacio * offset, barreraY, 5,5))
                    barreraX += 5
                barreraX = 50 * offset
                barreraY += 3
            barreraY = 400

    def enemyUpdate(self):
        if not self.enemigos_ultMov:
            for enemigo in self.enemigos:
                for enemigo in enemigo:
                    enemigo = enemigo[1]
                    if enemigo.colliderect(pygame.Rect(self.playerX, self.playerY, self.player.get_width(), self.player.get_height())):
                        self.vidas -= 1
                        self.resetPlayer()
                    enemigo.x += self.enemigos_velocidad * self.direccion
                    self.enemigos_ultMov = 25
                    if enemigo.x >= 750 or enemigo.x <= 0:
                        self.moveEnemiesDown()
                        self.direccion *= -1
                    
                    chance = random.randint(0, 1000)
                    if chance > self.chance:
                        self.balas.append(pygame.Rect(enemigo.x, enemigo.y, 5, 10))
                        self.puntaje += 5
            if self.animacion_On:
                self.animacion_On -= 1                                                                                                                                                        
            else:
                self.animacion_On += 1
        else:
            self.enemigos_ultMov -= 1
    
        
    def moveEnemiesDown(self):
        for enemigo in self.enemigos:
            for enemigo in enemigo:
                enemigo = enemigo[1]
                enemigo.y += 20

    def playerUpdate(self):
        tecla = pygame.key.get_pressed()
        if tecla[K_RIGHT] and self.playerX < 800 - self.player.get_width():
            self.playerX += 5
        elif tecla[K_LEFT] and self.playerX > 0:
            self.playerX -= 5
        if tecla[K_SPACE] and not self.bala:
            self.bala = pygame.Rect(self.playerX + self.player.get_width() / 2- 2, self.playerY - 15, 5, 10)

    def bulletUpdate(self):
        for i, enemigo in enumerate(self.enemigos):
            for j, enemigo in enumerate(enemigo):
                enemigo = enemigo[1]
                if self.bala and enemigo.colliderect(self.bala):
                    self.enemigos[i].pop(j)
                    self.bala = None
                    self.chance -= 1
                    self.puntaje += 100
                
        if self.bala:
            self.bala.y -= 20
            if self.bala.y < 0:
                self.bala = None


        for x in self.balas:
            x.y += 20
            if x.y > 600:
                self.balas.remove(x)
            if x.colliderect(pygame.Rect(self.playerX, self.playerY, self.player.get_width(), self.player.get_height())):
                self.vidas -= 1
                self.balas.remove(x)
                self.resetPlayer()

        for b in self.barrera_particulas:
            check = b.collidelist(self.balas)
            if check != -1:
                self.barrera_particulas.remove(b)
                self.balas.pop(check)
                self.puntaje += 10
            elif self.bala and b.colliderect(self.bala):
                self.barrera_particulas.remove(b)
                self.bala = None
                self.puntaje += 10
    def resetPlayer(self):
        self.playerX = 400

    def run(self):
        clock = pygame.time.Clock()
        for x in range(3):
            self.moveEnemiesDown()
        while True:
            
            clock.tick(60)
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            for enemigo in self.enemigos:
                for enemigo in enemigo:
                    self.screen.blit(pygame.transform.scale(self.enemigos_sprites[enemigo[0]][self.animacion_On], (35,35)), (enemigo[1].x, enemigo[1].y))
            self.screen.blit(self.player, (self.playerX, self.playerY))
            if self.bala:
                pygame.draw.rect(self.screen, (52, 255, 0), self.bala)
            for bullet in self.balas:
                pygame.draw.rect(self.screen, (255,255,255), bullet)
            for b in self.barrera_particulas:
                pygame.draw.rect(self.screen, (52, 255, 0), b)
            
            if not self.enemigos:
                self.screen.blit(pygame.font.Font("assets/fuente.ttf", 100).render("Ganaste!", -1, (52,255,0)), (100, 200))
            elif self.vidas > 0:
                self.bulletUpdate()
                self.enemyUpdate()
                self.playerUpdate()
            elif self.vidas == 0:
                self.screen.blit(pygame.font.Font("assets/fuente.ttf", 100).render("Perdiste!", -1, (52,255,0)), (100, 200))
            self.screen.blit(self.font.render("Vidas: {}".format(self.vidas), -1, (255,255,255)), (20, 10))
            self.screen.blit(self.font.render("Puntaje: {}".format(self.puntaje), -1, (255,255,255)), (400, 10))
            pygame.display.flip()


if __name__ == "__main__":
    Juego().run()
