# IMPORTS DE LIBRERIAS
import sys, pygame
from pygame.locals import *
from tkinter.constants import FALSE


#DECLARACIONES DE VARIABLES Y CONSTANTES

#TAMAÑO DE PANTALLA
WIDTH = 900
HEIGHT = 500
#POSICION ACTUAL DEL PERSONAJE
MposX =300
MposY =318
#CONTADOR QUE INDICA CUAL ES EL SPRITE A MOSTRAR
cont=6
#BOOLEAN QUE INDICA HACIA DONDE MIRA EL PERSONAJE
direc=True
#INDICE DE LAS MATRICES QUE CONTROLAN EL SPRITE
i=0
#ARREGLOS PARA SEPARAR EL SPRITE
xixf={}
Rxixf={}
#DECLARACION DE PARABOLA PARA EL SALTO
parabola={}
#INDICAN SI EL PERSONAJE ESTA O NO EN EL AIRE
salto = False
salto_Par=False


#===============================================================================
#================================IMAGEN=========================================
#ESTA FUNCION SE LLAMA PARA SIMPLIFICAR LA CARGA DE TODAS LAS IMAGENES
def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error as message:
                raise SystemExit(message)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
#===============================================================================
 
#==================================TECLADO======================================
#===============================================================================
def teclado():
    
    #LLAMADA QUE INDICA QUE VAMOS A UTILIZAR LAS VARIABLES GLOBALES
    global MposX
    global cont, direc, salto, salto_Par
    
    #EL OBJETIVO DE ESTA VARIABLE ES REDUCIR EL ESPACIO Y LA COMPLEJIDAD DE
    #LAS PRUEBAS LOGICAS QUE CONTROLAN LOS EVENTOS
    teclado = pygame.key.get_pressed()
    
    #COMPROBACION DE SALTO PARABOLICO
    if teclado[K_UP] and teclado[K_RIGHT] and salto_Par==False:
        salto_Par=True
    elif teclado[K_UP] and teclado[K_LEFT] and salto_Par==False:
        salto_Par=True
         
    #COMPROBACION DE MOVIMIENTO DE IZQUIERDA A DERECHA O VISCEVERSA
    elif teclado[K_RIGHT]and salto==False and salto_Par==False:
        MposX+=2
        cont+=1
        direc=True
    elif teclado[K_LEFT]and salto==False and salto_Par==False:
        MposX-=2
        cont+=1
        direc=False
        
    #COOMPROBBACION DE SALTO EN LINEA RECTA
    elif teclado[K_UP] and salto==False and salto_Par==False:
        salto=True           
    else :
        cont=6
         
    return 
#===============================================================================

#==================================SPRITE=======================================
#===============================================================================
def sprite():

    global cont
 
    #ESTOS VALORES INDICAN COMO SE VA A SEPARAR EL SPRITE
    xixf[0]=(0,0,160,208)
    xixf[1]=(167,0,160,208)
    xixf[2]=(326,0,160,208)
    xixf[3]=(484,0,156,208)
    xixf[4]=(632,0,155,208)
    xixf[5]=(800,0,155,208)
    #ESTOS VALORES SON PARA EL SPRITE QUE CAMINA HACIA LA IZQUIERDA
    Rxixf[0]=(800,0,155,208)
    Rxixf[1]=(640,0,160,208)
    Rxixf[2]=(484,0,156,208)
    Rxixf[3]=(326,0,160,208)
    Rxixf[4]=(167,0,160,208)
    Rxixf[5]=(0,0,160,208)
    
    #ESTAS PRUEBAS CONTROLAN CUAL ES LA PARTE DEL SPRITE QUE SE DEBE MOSTRAR 
    p=6
    global i
        
    if cont==p:
        i=0
    if cont==p*2:
        i=1
    if cont==p*3:
        i=2
    if cont==p*4:
        i=3
    if cont==p*5:
        i=4
    if cont==p*6:
        i=5
        cont=0
    
    return
#===============================================================================

#===============================================================================
#=============================BUCLE===PRINCIPAL=================================
def main():
    
    pygame.init()    
    
    #DISPLAYAMOS LA VENTANA Y EL NOMBRE DE LA APLICACION
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dale dale, que vos podes!")
    
    #CARGAMOS LAS IMAGENES, LA ULTIMA ES LA VERSION ESPEJADA DEL SPRITE
    #LA IMAGEN DEL FONDO ES PROVISORIA, LUEGO SE GENERARA UN MAPA COMPLETO
    #MEDIANTE EL USO DE UNA APLICACION EXTERNA
    fondo = imagen("resources/fondo.png")
    mario = imagen("resources/sprites.png",True)   
    mario_inv=pygame.transform.flip(mario,True,False);
    #DECLARACION DE VARIABLES
    clock = pygame.time.Clock()
    global salto_Par,MposX,MposY,salto  
    bajada=False
    bajada_Par=False
    
    while True:
        #COFIGURACION Y LLAMADA A FUNCIONES
        time = clock.tick(90)
        sprite()
        teclado()
        fondo = pygame.transform.scale(fondo, (1000, 500))
        screen.blit(fondo, (0, 0))
        
        #COMPROBACION DE CAMINATA
        if direc==True and salto==False: 
            screen.blit(mario, ( MposX, MposY),(xixf[i]))
    
        if direc==False and salto==False: 
            screen.blit(mario_inv, ( MposX, MposY),(Rxixf[i]))
        
        
        #COMPROBACION DE SALTO
        if salto==True:            
            if direc==True:
                screen.blit(mario, ( MposX, MposY),(xixf[5]))
            if direc==False:
                screen.blit(mario_inv, ( MposX, MposY),(Rxixf[1]))   
            
            if bajada==False:
                MposY-=4               
                
            if bajada==True:
                MposY+=4               
            
            if MposY==186:
                bajada=True
            
            if MposY==318:
                bajada=False
                salto=False
        #======================================================================   
        pygame.display.flip()
        #COMPROBACION DE SALTO PARABOLICO
        if salto_Par==True and direc==True:            
            screen.blit(mario, ( MposX, MposY),(xixf[1]))
            if bajada_Par==False:
                MposY-=3
                MposX+=2
            if bajada_Par==True:
                MposY+=3
                MposX+=2
            if MposY==246:
                bajada_Par=True
            if MposY==318:
                bajada_Par=False
                salto_Par=False
        elif salto_Par==True and direc==FALSE:            
            
            screen.blit(mario_inv, ( MposX, MposY),(Rxixf[1]))
            
            if bajada_Par==False:
                MposY-=3
                MposX-=2
            if bajada_Par==True:
                MposY+=3
                MposX-=2
            if MposY==246:
                bajada_Par=True
            if MposY==318:
                bajada_Par=False
                salto_Par=False   
    
        #=========================CIERRE=DE=LA=VENTANA========================== 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    return 0

if __name__ == '__main__': 
    main()