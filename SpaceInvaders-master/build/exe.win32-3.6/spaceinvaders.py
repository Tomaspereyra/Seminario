import pygame,time
from pygame.locals import *
import sys
import os
import random

# Constantes
parar = False
ancho = 800
alto = 600
blanco = 255, 255, 255
negro = 0, 0, 0
rojo = 200, 0, 0
rojo_brillante = 255, 0, 0
azul = 0, 0, 255 
pantalla = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()
pygame.mixer.pre_init(44100,16,2,4096)


pygame.init()
laser = pygame.mixer.Sound("laser.wav")
pygame.mixer.music.load("video game.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
def quitPausa():
    global parar
    parar=False
def pausa():
    fondo = cargar_imagen("618.jpg", "", alpha=False)
    pantalla.blit(fondo, (0, 0))
    pygame.display.flip()
    while parar:
        mensaje("Pausa", 0, 30, 400, 50, blanco)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        
        

        boton("Continuar",100,200,100,50,negro,rojo_brillante,"quitPausa")
        boton("Salir",50,400,100,50,negro,rojo_brillante,"Salir")

        pygame.display.update()
       
def cargar_imagen(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
     ruta = os.path.join(dir_imagen, nombre)
     try:
        image = pygame.image.load(ruta)
     except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
     # Comprobar si la imagen tiene "canal alpha" (como los png)
     if alpha is False:
        image = image.convert_alpha()
     else:
        image = image.convert()
     return image

def control():
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     fondo = cargar_imagen("controles.jpeg", "", alpha=False)
     pantalla.blit(fondo, (0, 0))
     
     pygame.display.flip()
     controles= True
     while controles:
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
             controles = False
             pygame.QUIT()
             
         mensaje("Controles", 0, 30, 400, 50)
         boton("Jugar", 150, 520, 120, 50, azul, rojo_brillante,"Jugar")    
         boton("Salir", 500, 520, 120, 50, azul, rojo_brillante,"Salir")  
         pygame.display.update()
            
    
def boton(msj, x, y, w, h, c_mate, c_brillo, accion): 
            
         mouse = pygame.mouse.get_pos()
         click = pygame.mouse.get_pressed()
         
         if x + w > mouse[0] > x and y + h > mouse[1] > y:                             
             mensaje(msj, 0, 30, (x + (w / 2)), (y + h / 2),rojo)
             
             
                 
             if click[0] == 1 and accion != None:
                 if accion == "Salir":
                     
                     pygame.quit()
                     sys.exit()
                 if accion == "Jugar":
                     Juego().run() 
                 if accion == "Controles":
                     control()                        
                 if accion =="quitPausa":
                     quitPausa()     
         else:
             mensaje(msj, 0, 30, (x + (w / 2)), (y + h / 2),blanco)
             pygame.display.flip()
             
def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect() 

def mensaje(text, desplazamientoy=0, tamano=80, ancho_=ancho, alto_=alto,color=blanco):
     largeText = pygame.font.SysFont("Space Invaders Regular", tamano,bold=False,italic=False)
     TextSurf, TextRect = text_objects(text, largeText,color)
     TextRect.center = ((ancho_), (alto_) - desplazamientoy)
     pantalla.blit(TextSurf, TextRect)    

class Juego:
    
    def introduccion(self):
           
     
     fondo = cargar_imagen("fondonuevo.jpeg", "", alpha=False)
     fondo = pygame.transform.scale(fondo, (800, 600)) 
     pantalla = pygame.display.set_mode((ancho, alto))
     pantalla.blit(fondo, (0, 0))
     pygame.display.flip()
     pygame.init()
     
         
     
 
     introJuego = True
     while introJuego:
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
             introJuego = False
             pygame.QUIT()
             sys.exit()
          
         
         mensaje("Anillos De Saturno", 0, 30, 500, 50)
         boton("Jugar", 100, 100, 120, 50, azul, rojo_brillante,"Jugar")
         boton("Controles",100, 300, 120, 50, rojo, rojo_brillante,"Controles")
         boton("Salir",100, 500, 120, 50,rojo,rojo_brillante,"Salir")
         
         mouse = pygame.mouse.get_pos()
         pygame.display.update()   
       
    def __init__(self):
        
        #definiciones de variables
        self.screen = pygame.display.set_mode((800, 600))
        pygame.font.init()
        self.font = pygame.font.SysFont("04b_25", 15)
        self.puntaje = 0
        self.vidas = 5
        self.killed = 0
        self.final= False
        #barrera de defensa
        disenioDeBarrera = [[],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
                               [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
                               [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
                               [0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
                               [1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1],
                               [1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1],
                               [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1]]

        self.enemigos_sprites = {
                0:[pygame.image.load("a1_0.png").convert_alpha(), pygame.image.load("a1_1.png").convert_alpha()],
                1:[pygame.image.load("a2_0.png").convert_alpha(), pygame.image.load("a2_1.png").convert_alpha()],
                2:[pygame.image.load("a3_0.png").convert_alpha(), pygame.image.load("a3_1.png").convert_alpha()],
                }
        self.player = pygame.image.load("shooter.png").convert()
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
        #Este fragmento determina que sprite de enemigo se utilizara y lo añade
        #a la lista
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

        #este fragmento genera las barreras
        for offset in range(1, 5):
            for b in disenioDeBarrera:
                for b in b:
                    if b != 0:
                        self.barrera_particulas.append(pygame.Rect(barreraX + espacio * offset, barreraY, 5,5))
                    barreraX += 5
                barreraX = 50 * offset
                barreraY += 3
            barreraY = 400

    def init2(self):
        self.vidas = 5
        self.killed = 0
        self.final= True
        #barrera de defensa

        self.enemigos_sprites = {
                0:[pygame.image.load("2a1_0.png").convert_alpha(), pygame.image.load("2a1_1.png").convert_alpha()],
                1:[pygame.image.load("2a2_0.png").convert_alpha(), pygame.image.load("2a2_1.png").convert_alpha()],
                2:[pygame.image.load("2a3_0.png").convert_alpha(), pygame.image.load("2a3_1.png").convert_alpha()],
                }
        #barrera de defensa
        disenioDeBarrera = [[],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
                               [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
                               [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
                               [0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
                               [1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1]]

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
        #Este fragmento determina que sprite de enemigo se utilizara y lo añade
        #a la lista
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
        self.chance = 940

        barreraX = 50
        barreraY = 400
        espacio = 100

        #este fragmento genera las barreras
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
        #enemyUpdate controla las colisiones con el jugador, y el movimiento de los enemigos.
        #tambien, controla la posibilidad de que un enemigo dispare
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
        #moveEnemiesDown se llama dentro de enemyUpdate para mover los enemigos
        #hacia abajo
        for enemigo in self.enemigos:
            for enemigo in enemigo:
                enemigo = enemigo[1]
                enemigo.y += 20

    def playerUpdate(self):
        #playerUpdate controla el movimieto y disparo del jugador
        tecla = pygame.key.get_pressed()
        if tecla[K_RIGHT] and self.playerX < 800 - self.player.get_width():
            self.playerX += 5
        elif tecla[K_LEFT] and self.playerX > 0:
            self.playerX -= 5
        if tecla[K_SPACE] and not self.bala:
            self.bala = pygame.Rect(self.playerX + self.player.get_width() / 2- 2, self.playerY - 15, 5, 10)

    def bulletUpdate(self):
        #bulletUpdate controla las colisiones de balas
        #colisiones entre enemigos y balas
        for i, enemigo in enumerate(self.enemigos):
            for j, enemigo in enumerate(enemigo):
                enemigo = enemigo[1]
                if self.bala and enemigo.colliderect(self.bala):
                    self.enemigos[i].pop(j)
                    self.killed+=1
                    self.bala = None
                    self.chance -= 1
                    self.puntaje += 100
                    pygame.mixer.Sound.play(laser)
                
        
        if self.bala:
            self.bala.y -= 20
            if self.bala.y < 0:
                self.bala = None

        #colisiones entre balas enemigas y el jugador
        for x in self.balas:
            x.y += 20
            if x.y > 600:
                self.balas.remove(x)
            if x.colliderect(pygame.Rect(self.playerX, self.playerY, self.player.get_width(), self.player.get_height())):
                self.vidas -= 1
                self.balas.remove(x)
                self.resetPlayer()
        #colisiones entre balas y barreras defensoras
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
        #coloca al jugador en  mitad de la pantalla si recibe un disparo
        self.playerX = 400

    def run(self):
         global parar 
         clock = pygame.time.Clock()
         for x in range(3):
            self.moveEnemiesDown()
         while True:
            
            clock.tick(60)
            
            self.screen.blit((pygame.image.load("star.jpg").convert()),(0,0))
           
            for event in pygame.event.get():
                tecla = pygame.key.get_pressed()
                if event.type == QUIT:
                    sys.exit()
                if tecla[K_p]:
                    parar=True
                    pausa() 
                    
            #Este fragmento dibuja los enemigos y el jugador     
            for enemigo in self.enemigos:
                for enemigo in enemigo:
                    self.screen.blit(pygame.transform.scale(self.enemigos_sprites[enemigo[0]][self.animacion_On], (35,35)), (enemigo[1].x, enemigo[1].y))
                    self.screen.blit(self.player, (self.playerX, self.playerY))
            
            #Este fragmento dibuja las balas y la barrera
            if self.bala:
                pygame.draw.rect(self.screen, (200, 0, 0), self.bala)
            for bullet in self.balas:
                pygame.draw.rect(self.screen, (200, 0, 0), bullet)
            for b in self.barrera_particulas:
                pygame.draw.rect(self.screen, (230, 135, 70), b)
            
            #Este fragmento determina si se gano o se perdio, o debe continuarse la ejecucion      
            if self.killed==60:
                if not self.final:
                    self.screen.blit(pygame.font.SysFont("fuente", 50).render("Ganaste!", -1, (52,255,0)), (100, 200))
                    self.screen.blit(pygame.font.SysFont("fuente", 50).render("Flecha ARRIBA para continuar", -1, (0, 0, 180)), (100, 300))
                    tecla = pygame.key.get_pressed()
                    if tecla[K_UP]:
                        Juego.init2(self)
                if self.final:
                    self.screen.blit(pygame.font.SysFont("fuente", 70).render("¡¡¡SALVASTE AL MUNDO!!!", -1, (0,255,0)), (8, 200)) 
            elif self.vidas > 0:
                self.bulletUpdate()
                self.enemyUpdate()
                self.playerUpdate()
                tecla = pygame.key.get_pressed()
                if tecla[K_q]:
                    sys.exit()
            elif self.vidas == 0:
                self.screen.blit(pygame.font.SysFont("fuente", 50).render("Perdiste!", -1, (190, 0, 0)), (100, 200))
                self.screen.blit(pygame.font.SysFont("fuente", 50).render("Flecha ARRIBA para reiniciar", -1, (0, 0, 180)), (100, 300))
                tecla = pygame.key.get_pressed()
                if tecla[K_UP]:
                    Juego.__init__(self)
            self.screen.blit(self.font.render("Vidas: {}".format(self.vidas), -1, (255,255,255)), (20, 10))
            self.screen.blit(self.font.render("Puntaje: {}".format(self.puntaje), -1, (255,255,255)), (400, 10))
            self.screen.blit(self.font.render("Quitar ' Q '".format(self.puntaje), -1, (255,255,255)), (717, 10))
            pygame.display.flip()


if __name__ == "__main__":
    pygame.display.set_caption("Anillos de Saturno")  
    pygame.init()
    Juego().introduccion()
