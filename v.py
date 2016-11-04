from libreria import *
from pygame.locals import *

#variables globales
global segundos #Duracion de la partida
global llaveEquipada #objeto interactivo
global trifuerzaEquipada #objeto interactivo
global pausado #auxiliar para pausar el juego
global segundosPausados # segundos guardados en la pausa
global introJuego #Activar la imagen de inicio
global pag
global lv
global vidaNivel1
global arcoItem
global arriba
global abajo
global izquierda
global derecha
global NumeroMuro

#iniciacion de variables globales

segundos=120 # tiempo = segundos - 1
llaveEquipada = False
trifuerzaEquipada = False
pausado=False
segundosPausados=0
introJuego=False
pag=1
lv = 1
vidaNivel1 = 0
arcoItem=False
arriba=False
abajo=False
izquierda=False
derecha=False
NumeroMuro=0




#funcion main
if __name__ == '__main__':
    pygame.init()
#cargando imagenes
    fondo=pygame.image.load("imagenes/fondo.png")
    bv=pygame.image.load('imagenes/barraVida.png')
    final=pygame.image.load("imagenes/Final.png")
    fondo2 = pygame.image.load("imagenes/fondo2.jpg")
    trifuerza = pygame.image.load("imagenes/trifuerza.png")
    corazon = pygame.image.load("imagenes/corazon.png")
    menosVida = pygame.image.load("imagenes/menosVida.jpg")
    #llavePantalla = pygame.image.load("imagenes/llave.png")
    linkT=pygame.image.load('imagenes/linkTrifuerza.png')
    linkC=pygame.image.load('imagenes/linkCorazon.png')
    linkA=pygame.image.load('imagenes/linkArco.png')
    linkV=pygame.image.load('imagenes/linkVeneno.png')
    escudo=pygame.image.load('imagenes/escudo.png')
    llama=pygame.image.load('imagenes/llama.png')
    alfombra=pygame.image.load('imagenes/alfombra.png')
#creando pantalla
    pantalla=pygame.display.set_mode([ancho,alto])
    pygame.display.set_caption("                                                                                           Lacopi        ")
#cuadrando el texto de la ventana
    fondoIntro=pygame.image.load("imagenes/fondoIntro.jpg")
#importando Font(fuente de letra)
    historia=pygame.font.Font("Triforce.ttf",40)
    tiempo=pygame.font.Font("Triforce.ttf",34)
    zeldaFuente=pygame.font.Font("Triforce.ttf",180)
    fakeZelda=pygame.font.Font("Triforce.ttf",70)
#intro
    presentando=historia.render("Parcial II ",True,NEGRO)
    presentando2=historia.render("The legend of Zelda - The Maze",True,ROJO)
    presentando3=historia.render("The legend of Zelda - The Maze",True,NEGRO)
    presentando4=historia.render("Alexander Villegas - Sebastian Sanchez",True,NEGRO)
    presentando5=historia.render("Ingenieria de Sistemas y Computacion",True,NEGRO)
    presentando6=historia.render("Computacion Grafica",True,NEGRO)
    presentando7=historia.render("Universidad Tecnologica de Pereira",True,NEGRO)
#final
    f1=zeldaFuente.render("Game Over ",True,BLANCO)
    f2=historia.render("Thanks For Playing",True,BLANCO)
    f22=historia.render("Thanks For Playing",True,NEGRO)

    s=historia.render("Press space to exit the game",True,AMARILLO)
    ss=historia.render("Press space to exit the game",True,NEGRO)
#primer nivel
    nivel1=historia.render("Level 1",True,BLANCO)
#textos de la narracion:
    narracion=historia.render("This is the story of a child who was born to become ",True,BLANCO)
    narracion2=historia.render("a hero, the evil in his world was hopeless, unless ",True,BLANCO)
    narracion3=historia.render("your courage to take him to overthrow the evil",True,BLANCO)
    narracion4=historia.render("that was imposed by the evil Ganondorf.",True,BLANCO)
    narracion5=historia.render("Long journeys led him to a morbid maze, where",True,BLANCO)
    narracion6=historia.render("Princess Zelda, last victim of the dreaded villain was.",True,BLANCO)
    #----------------------------------------------------------------------------------------------#
    narracion1=historia.render("This is the story of a child who was born to become ",True,NEGRO)
    narracion22=historia.render("a hero, the evil in his world was hopeless, unless ",True,NEGRO)
    narracion33=historia.render("your courage to take him to overthrow the evil",True,NEGRO)
    narracion44=historia.render("that was imposed by the evil Ganondorf.",True,NEGRO)
    narracion55=historia.render("Long journeys led him to a morbid maze, where",True,NEGRO)
    narracion66=historia.render("Princess Zelda, last victim of the dreaded villain was.",True,NEGRO)

    narracion7=historia.render("Press Space to Play...",True,ROJO)
    narracion77=historia.render("Press Space to Play...",True,BLANCO)
#textos de muerte y otras interacciones
    #texto = zeldaFuente.render("You Lose", True, ROJO)
    texto2 = zeldaFuente.render("You Win", True, BLANCO)
    texto3 = fakeZelda.render("You Drank Poison", True, ROJO)
    #texto6 = fakeZelda.render("You Died",True,ROJO)
    texto4 = fakeZelda.render("Time's Up", True, ROJO)
    texto5 = fakeZelda.render("You have rescued Zelda Princess", True, BLANCO)
    tiempo2= tiempo.render("TIEMPO: ",True,NEGRO)
    nombre= tiempo.render("Hyrule Castle Basement ",True,BLANCO)
    life = tiempo.render("Life: ", True, BLANCO)
    #llave=fakeZelda.render("Key Obtained",True,BLANCO)
    trifuerzaPower=fakeZelda.render("Triforce Obtained",True,BLANCO)
    contenedorPower=fakeZelda.render("Heart Container Obtained",True,BLANCO)
    arcoPower=fakeZelda.render("Bow Obtained",True,BLANCO)
    arcoInstruction=fakeZelda.render("Press space to shoot an arrow",True,AMARILLO)
    #noLlave = fakeZelda.render("You need a key",True,ROJO)
    #siLlave = fakeZelda.render("Door Unlocked",True,BLANCO)
    #puertaCerrada = fakeZelda.render("Door Locked",True,ROJO)
#texto de pausa y continuar
    pausar =zeldaFuente.render("Pause",True,BLANCO)
    continuar = fakeZelda.render("Continue: Y / N",True,BLANCO)
#reloj
    reloj=pygame.time.Clock()
#actualizacion
    pygame.display.flip()
#musica de inicio
    pygame.mixer.music.load("sonidos/musicaIntro.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.85)

    '''
    pantalla.fill(BLANCO)
    pantalla.blit(presentando,(ancho/2-70,alto/2-300))
    pantalla.blit(presentando3,(ancho/2-250,alto/2-150))
    pantalla.blit(presentando2,(ancho/2-252,alto/2-152))
    pantalla.blit(presentando4,(ancho/2-300,alto/2-10))
    pantalla.blit(presentando5,(ancho/2-260,alto/2+150))
    pantalla.blit(presentando6,(ancho/2-150,alto/2+200))
    pantalla.blit(presentando7,(ancho/2-255,alto/2+250))
    pygame.display.flip()
    pygame.time.delay(1000)
    '''

#creacion del intro y mantenerlo
    #introJuego=True

    while introJuego:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

#Posicionamiento todos los textos
        '''
        pantalla.blit(fondoIntro,(0,0))

        pantalla.blit(narracion1,(252,52))
        pantalla.blit(narracion22,(292,92))
        pantalla.blit(narracion33,(302,132))
        pantalla.blit(narracion44,(352,172))
        pantalla.blit(narracion55,(292,302))
        pantalla.blit(narracion66,(212,342))
        pantalla.blit(narracion77,(602,542))


        pantalla.blit(narracion,(250,50))
        pantalla.blit(narracion2,(290,90))
        pantalla.blit(narracion3,(300,130))
        pantalla.blit(narracion4,(350,170))
        pantalla.blit(narracion5,(290,300))
        pantalla.blit(narracion6,(210,340))
        pantalla.blit(narracion7,(600,540))
        '''
#actualizacion
        pygame.display.flip()
        reloj.tick(60)

        if event.type == pygame.KEYDOWN:

            if event.key==pygame.K_SPACE:
                pygame.mixer.music.stop()
                introJuego=False
                pantalla.fill(NEGRO)
                pantalla.blit(nivel1,(ancho/2-50,alto/2-50))
                pygame.display.flip()
                pygame.time.delay(3000)








#agregando sprites
    todos=pygame.sprite.Group()
    packMuros=pygame.sprite.Group()
    packAguaNorte=pygame.sprite.Group()
    packAguaOeste=pygame.sprite.Group()
    packAguaEste=pygame.sprite.Group()
    packAguaSur=pygame.sprite.Group()
    packRejas=pygame.sprite.Group()
#cuadrando texto de ventana
    pygame.display.set_caption("                                                                                   BILLY Y MANDY         ")
#cargando musica de laberinto
    pygame.mixer.music.load("sonidos/musica.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.85)
#cargando musica de pausa
    sonidoPausar=pygame.mixer.Sound("sonidos/pausar.wav")
    sonidoDespausar=pygame.mixer.Sound("sonidos/despausar.wav")

    #######Funciones#############
#Cronometro
    def crono():
        global segundos
        global pausado

        segundos = int (segundos)
        if segundos==-1:
            print "Game Over"
        else:
            segundos-=1
            time.sleep(1)
            return crono()
#Pausar
    def pausa():
        global pausado
        global segundos
        global segundosPausados

        pausado=True
        while pausado:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_y:
                        sonidoDespausar.play()
                        pygame.mixer.music.unpause()
                        pausado=False
                        segundos=segundosPausados
                        segundosPausados=0


                    elif event.key==pygame.K_n:
                        pygame.quit()
                        sys.exit()

            pantalla.blit(pausar,(ancho/2-180,alto/2-200))
            pantalla.blit(continuar,(ancho/2-200,alto/2))

            pygame.display.flip()
            reloj.tick(5)


    def get_line(start, end):


        """Bresenham's Line Algorithm
        Produces a list of tuples from start and end


        """
        # Setup initial conditions
        x1, y1 = start
        x2, y2 = end
        dx = x2 - x1
        dy = y2 - y1

        # Determine how steep the line is
        is_steep = abs(dy) > abs(dx)

        # Rotate line
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        # Swap start and end points if necessary and store swap state
        swapped = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            swapped = True

        # Recalculate differentials
        dx = x2 - x1
        dy = y2 - y1

        # Calculate error
        error = int(dx / 2.0)
        ystep = 1 if y1 < y2 else -1

        # Iterate over bounding box generating points between start and end
        y = y1
        points = []
        for x in range(x1, x2 + 1):
            coord = (y, x) if is_steep else (x, y)
            points.append(coord)
            error -= abs(dy)
            if error < 0:
                y += ystep
                error += dx

        # Reverse the list if the coordinates were swapped
        if swapped:
            points.reverse()
        return points









#CREACION DEL PRIMER NIVEL "usando un archivo de texto"

#implementacion de la funcion creacion de muros


    level1 = []
    level = open("nivel/laberinto.txt", "r")
    x = 0
    y = 0
    for l in level:
            level1.append(l)
    for row in level1:
            for col in row:
                    if col == "x":
                            muroB = MuroBloques("imagenes/obstaculoLaberinto.png",x,y)
                            packMuros.add(muroB)
                            todos.add(muroB)

                    if col == "a":
                            muroA = MuroBloques("imagenes/agua.png",x,y)
                            packAguaSur.add(muroA)
                            todos.add(muroA)


                    if col == "e":
                            muroA = MuroBloques("imagenes/agua.png",x,y)
                            packAguaEste.add(muroA)
                            todos.add(muroA)

                    if col == "i":
                            muroA = MuroBloques("imagenes/agua.png",x,y)
                            packAguaNorte.add(muroA)
                            todos.add(muroA)

                    if col == "o":
                            muroA = MuroBloques("imagenes/agua.png",x,y)
                            packAguaOeste.add(muroA)
                            todos.add(muroA)

                    if col == "t":
                            muroA = MuroBloques("imagenes/llama.png",x,y)
                            packMuros.add(muroA)
                            todos.add(muroA)

                    if col == "r":
                            muroA = MuroBloques("imagenes/reja.png",x,y)
                            packRejas.add(muroA)
                            todos.add(muroA)

                    if col == "m":
                            muroA = MuroBloques("imagenes/arbusto.png",x,y)
                            packMuros.add(muroA)
                            todos.add(muroA)

                    if col == "b":
                            muroA = MuroBloques("imagenes/pilar.png",x,y)
                            packMuros.add(muroA)
                            todos.add(muroA)

                    if col == "u":
                            muroA = MuroBloques("imagenes/agua.png",x,y)
                            packAguaSur.add(muroA)
                            todos.add(muroA)

                    if col == "P":
                            jp = Jugador("imagenes/personaje.png",x,y)
                            jp.muros = packMuros
                            todos.add(jp)
                    x += 15
            y += 15
            x = 0








#asignacion de clases
    #finales

    ll=llegada('imagenes/escalera.png')
    lln2=llegadaNivel2('imagenes/zelda.png')
    #ll2=llegadaFake('imagenes/cofreFalso.png')
    #enemigos
    e1=Enemigo('imagenes/enemigo.png',x,y)
    e2=Enemigo2('imagenes/enemigo.png',x,y)
    o= EnemigoOctorok('imagenes/octorok.png',x,y)
    k = EnemigoVolando('imagenes/EnemigoVolador.png',x,y)
    cu = Cuchilla1('imagenes/cuchilla.png',x,y)
    cu2 = Cuchilla2('imagenes/cuchilla.png',x,y)
    cb1=Caballero1('imagenes/caballero.png',x,y)
    cb2=Caballero2('imagenes/caballero.png',x,y)
    ganon=FinalBoss('imagenes/ganon.png',x,y)
    ganonVerde=FinalBoss('imagenes/ganonVerde.png',x,y)
    ganonAzul=FinalBoss('imagenes/ganonAzul.png',x,y)
    ganonRojo=FinalBoss('imagenes/ganonRojo.png',x,y)
    #objetos interactivos

    c = Cofre('imagenes/cofre.png',x,y)
    #b=Boton('imagenes/boton.png',x,y)
    #bP=Boton('imagenes/botonPresionado.png',x,y)
    cA =  Muro('imagenes/cofreAbierto.png',x,y)
    #t=Trifuerza('imagenes/trifuerza.png',x,y)
    #b1=Boton1('imagenes/boton1.png',x,y) # estas cuatro para botones de trifuerza
    #b2=Boton2('imagenes/boton2.png',x,y)
    #b3=Boton3('imagenes/boton3.png',x,y)
    #b4=Boton4('imagenes/boton4.png',x,y)
    #bp1=BotonPresionado1('imagenes/botonPresionado1.png',x,y) #lo mismo pero el sprite de apagado
    #bp2=BotonPresionado2('imagenes/botonPresionado2.png',x,y)
    #bp3=BotonPresionado3('imagenes/botonPresionado3.png',x,y)
    #bp4=BotonPresionado4('imagenes/botonPresionado4.png',x,y)
    contenedor=Contenedor('imagenes/contenedorCorazon.png',x,y)
    arco=Arco('imagenes/arco.png',x,y)
    #heredando la clase muro para posicionarlos en el barra de estado
    #llM = Muro('imagenes/llaveMenu.png',x,y)
    c1 = Muro('imagenes/cadena1.png',x,y)
    c2 = Muro('imagenes/cadena2.png',x,y)
    tM = Muro('imagenes/trifuerzaMenu.png',x,y)
    aM = Muro('imagenes/arcoMenu.png',x,y)
    p = Muro('imagenes/puerta.png',x,y)
    #p2 = Muro2('imagenes/puerta.png',x,y)
    g= Muro('imagenes/veneno.png',x,y)
    bO=Muro('imagenes/barreraOeste.png',x,y)
    bS=Muro('imagenes/barreraSur.png',x,y)
    bE=Muro('imagenes/barreraOeste.png',x,y)
    bN=Muro('imagenes/barreraNorte.png',x,y)
    #puertas
    #mp1=MuroPuerta1('imagenes/puertaTrifuerza.png',x,y)
    #mp2=MuroPuerta2('imagenes/puertaTrifuerza.png',x,y)
    #mp3=MuroPuerta3('imagenes/puertaTrifuerza.png',x,y)
    #mp4=MuroPuerta4('imagenes/puertaTrifuerza.png',x,y)

#posicionamiento de lo anterior
    ll.rect.x=760
    ll.rect.y=410
    lln2.rect.x=ancho/2
    lln2.rect.y=520
    #ll2.rect.x=1050
    #ll2.rect.y=345
    e2.rect.x=820
    e2.rect.y=250
    e1.rect.x=60
    e1.rect.y=400
    #cu.rect.x=350
    #cu.rect.y=414
    cu2.rect.x=670
    cu2.rect.y=260
    cb1.rect.x=80
    cb1.rect.y=200
    #cb2.rect.x=260
    #cb2.rect.y=265
    c.rect.x=200
    c.rect.y=220
    cA.rect.x=200
    cA.rect.y=220
    #llM.rect.x=210
    #llM.rect.y=620
    tM.rect.x=290
    tM.rect.y=620
    aM.rect.x=290
    aM.rect.y=620
    p.rect.x = 990
    p.rect.y = 105
    #p2.rect.x = 990
    #p2.rect.y = 345
    g.rect.x = 1050
    g.rect.y = 350
    #b.rect.x=1028
    #b.rect.y=18
    #bP.rect.x=1033
    #bP.rect.y=18
    o.rect.x =28
    o.rect.y=528
    k.rect.x=600
    k.rect.y=100
    #mp1.rect.x=539
    #mp1.rect.y=300
    #mp2.rect.x=600
    #mp2.rect.y=300
    #mp3.rect.x=660
    #mp3.rect.y=300
    #mp4.rect.x=721
    #mp4.rect.y=300
    #b1.rect.x=102
    #b1.rect.y=330
    #bp1.rect.x=102
    #bp1.rect.y=330
    #b2.rect.x=192
    #b2.rect.y=400
    #bp2.rect.x=192
    #bp2.rect.y=400
    #b3.rect.x=347
    #b3.rect.y=368
    #bp3.rect.x=347
    #bp3.rect.y=373
    #b4.rect.x=518
    #b4.rect.y=357
    #bp4.rect.x=523
    #bp4.rect.y=357
    #t.rect.x=1010
    #t.rect.y=228

#Asignamiento de grupos de sprites
    llegada=pygame.sprite.Group()
    llegadaFake=pygame.sprite.Group()
    Enemigo=pygame.sprite.Group()
    Enemigo2=pygame.sprite.Group()
    Cofre=pygame.sprite.Group()
    Muro=pygame.sprite.Group()
    Muro2=pygame.sprite.Group()
    #Boton=pygame.sprite.Group()
    #botonPresionado=pygame.sprite.Group()
    EnemigoOctorok=pygame.sprite.Group()
    EnemigoVolando=pygame.sprite.Group()
    #Cuchilla1=pygame.sprite.Group()
    Cuchilla2=pygame.sprite.Group()
    MuroPuerta1=pygame.sprite.Group()
    MuroPuerta2=pygame.sprite.Group()
    MuroPuerta3=pygame.sprite.Group()
    MuroPuerta4=pygame.sprite.Group()
    #Boton1=pygame.sprite.Group()
    #Boton2=pygame.sprite.Group()
    #Boton3=pygame.sprite.Group()
    #Boton4=pygame.sprite.Group()
    #BotonPresionado1=pygame.sprite.Group()
    #BotonPresionado2=pygame.sprite.Group()
    #BotonPresionado3=pygame.sprite.Group()
    #BotonPresionado4=pygame.sprite.Group()
    #Trifuerza=pygame.sprite.Group()
    Caballero1=pygame.sprite.Group()
    Caballero2=pygame.sprite.Group()
    bala=pygame.sprite.Group()
    bala2=pygame.sprite.Group()

    #------------------nivel2---------------------------#
    Contenedor=pygame.sprite.Group()
    llegadaNivel2=pygame.sprite.Group()
    FinalBoss=pygame.sprite.Group()
    Arco=pygame.sprite.Group()
#Agregando todo en los grupos
    llegada.add(ll)
    todos.add(ll)
    #llegadaFake.add(ll2)
    #todos.add(ll2)
    Enemigo.add(e1)
    todos.add(e1)
    Enemigo2.add(e2)
    todos.add(e2)
    Cofre.add(c)
    todos.add(c)
    Muro.add(p)
    todos.add(p)
    #Muro2.add(p2)
    #todos.add(p2)
    #Boton.add(b)
    #todos.add(b)
    EnemigoOctorok.add(o)
    todos.add(o)
    EnemigoVolando.add(k)
    todos.add(k)
    #Cuchilla1.add(cu)
    #todos.add(cu)
    Cuchilla2.add(cu2)
    todos.add(cu2)
    Caballero1.add(cb1)
    todos.add(cb1)
    #Caballero2.add(cb2)
    #todos.add(cb2)
    #MuroPuerta1.add(mp1)
    #todos.add(mp1)
    #MuroPuerta2.add(mp2)
    #todos.add(mp2)
    #MuroPuerta3.add(mp3)
    #todos.add(mp3)
    #MuroPuerta4.add(mp4)
    #todos.add(mp4)
    #Boton1.add(b1)
    #todos.add(b1)
    #Boton2.add(b2)
    #todos.add(b2)
    #Boton3.add(b3)
    #todos.add(b3)
    #Boton4.add(b4)
    #todos.add(b4)
    #Trifuerza.add(t)
    #todos.add(t)


#hilos de tiempo
    hilo=threading.Thread(target=crono,args=())
    hilo.start()

####### mantener el juego y ciclo del mismo ###############


    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                segundos=-1
                pygame.quit()
                sys.exit()

            telclasPulsadas=pygame.key.get_pressed() #telca pulsada

            if trifuerzaEquipada==True:
                telclasPulsadas=pygame.key.get_pressed() #telca pulsada

                if telclasPulsadas[pygame.K_p]: #tecla de pausa
                    sonidoPausar.play()
                    pygame.mixer.music.pause()
                    segundosPausados+=int(segundos)
                    pausa()

                if telclasPulsadas[pygame.K_UP]: #movimiento en sentido cardinal
                    jp.direccion(11)
                    arriba=True
                    abajo=False
                    izquierda=False
                    derecha=False
                if telclasPulsadas[pygame.K_LEFT]:
                    jp.direccion(33)
                    arriba=False
                    abajo=False
                    izquierda=True
                    derecha=False
                if telclasPulsadas[pygame.K_DOWN]:
                    jp.direccion(22)
                    arriba=False
                    abajo=True
                    izquierda=False
                    derecha=False
                if telclasPulsadas[pygame.K_RIGHT]:
                    jp.direccion(44)
                    arriba=False
                    abajo=False
                    izquierda=False
                    derecha=True


                if telclasPulsadas[pygame.K_UP]: #movimiento en sentido diagonal
                    if telclasPulsadas[pygame.K_RIGHT]:
                        jp.direccion(144)
                        arriba=True
                        abajo=False
                        izquierda=False
                        derecha=False
                if telclasPulsadas[pygame.K_UP]:
                    if telclasPulsadas[pygame.K_LEFT]:
                        jp.direccion(133)
                if telclasPulsadas[pygame.K_DOWN]:
                    if telclasPulsadas[pygame.K_RIGHT]:
                        jp.direccion(244)
                if telclasPulsadas[pygame.K_DOWN]:
                    if telclasPulsadas[pygame.K_LEFT]:
                        jp.direccion(233)

                if event.type == pygame.KEYUP and event.key == pygame.K_LEFT: #mantener posicion del personaje
                    jp.direccion(66)
                if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    jp.direccion(88)
                if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    jp.direccion(55)
                if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    jp.direccion(77)

            if arcoItem==True:
                if arriba==True:
                    if event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            jp.golpe10()
                            b=Bala('imagenes/flechaA.png',jp.rect.x+10,jp.rect.y-35)
                            b.dir=1
                            bala.add(b)
                            todos.add(b)

                if abajo==True:
                    if event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            jp.golpe10()
                            b=Bala('imagenes/flechaAb.png',jp.rect.x+10,jp.rect.y+35)
                            b.dir=3
                            bala.add(b)
                            todos.add(b)

                if izquierda==True:
                    if event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            jp.golpe10()
                            b=Bala('imagenes/flechaI.png',jp.rect.x-35,jp.rect.y+10)
                            b.dir=2
                            bala.add(b)
                            todos.add(b)

                if derecha==True:
                    if event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            jp.golpe10()
                            b=Bala('imagenes/flechaD.png',jp.rect.x+35,jp.rect.y+10)
                            b.dir=0
                            bala.add(b)
                            todos.add(b)


#movimiento del jugador

        if trifuerzaEquipada==False:
            telclasPulsadas=pygame.key.get_pressed() #telca pulsada
            if telclasPulsadas[pygame.K_p]: #tecla de pausa
                sonidoPausar.play()
                pygame.mixer.music.pause()
                segundosPausados+=int(segundos)
                pausa()

            if telclasPulsadas[pygame.K_UP]: #movimiento en sentido cardinal
                jp.direccion(1)
                arriba=True
                abajo=False
                izquierda=False
                derecha=False
            if telclasPulsadas[pygame.K_LEFT]:
                jp.direccion(3)
                arriba=False
                abajo=False
                izquierda=True
                derecha=False
            if telclasPulsadas[pygame.K_DOWN]:
                jp.direccion(2)
                arriba=False
                abajo=True
                izquierda=False
                derecha=False
            if telclasPulsadas[pygame.K_RIGHT]:
                jp.direccion(4)
                arriba=False
                abajo=False
                izquierda=False
                derecha=True

            if telclasPulsadas[pygame.K_UP]: #movimiento en sentido diagonal
                if telclasPulsadas[pygame.K_RIGHT]:
                    jp.direccion(14)
                    arriba=True
                    abajo=False
                    izquierda=False
                    derecha=False
            if telclasPulsadas[pygame.K_UP]:
                if telclasPulsadas[pygame.K_LEFT]:
                    jp.direccion(13)
            if telclasPulsadas[pygame.K_DOWN]:
                if telclasPulsadas[pygame.K_RIGHT]:
                    jp.direccion(24)
            if telclasPulsadas[pygame.K_DOWN]:
                if telclasPulsadas[pygame.K_LEFT]:
                    jp.direccion(23)

            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT: #mantener posicion del personaje
                jp.direccion(6)
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                jp.direccion(8)
            if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                jp.direccion(5)
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                jp.direccion(7)



#posicionamiento de items en barra de estado
        if lv == 1:
            pantalla.blit(fondo, (0, 0))
            pantalla.blit(fondo2,(0,610))
            segundos=str(segundos)
            cronometro = tiempo.render(segundos,0,NEGRO)
            pantalla.blit(cronometro,(200,30))
            pantalla.blit(tiempo2,(30,30))
            #pantalla.blit(nombre,(700,620))
            #pantalla.blit(escudo,(1020,620))
            #pantalla.blit(llama,(1005,75))
            #pantalla.blit(llama,(1080,75))
            #pantalla.blit(llama,(1005,160))
            #pantalla.blit(llama,(1080,160))
            #------------------------------#
            #pantalla.blit(llama,(1005,315))
            #pantalla.blit(llama,(1080,315))
            #pantalla.blit(llama,(1005,385))
            #pantalla.blit(llama,(1080,385))
            #pantalla.blit(alfombra,(15,570))
            #pantalla.blit(life,(380,620))
            #pantalla.blit(corazon,(450,620))
            #pantalla.blit(corazon,(490,620))
            #pantalla.blit(corazon,(530,620))
        if lv == 2:
            #life2 = tiempo.render("Life: "+str(ganon.vida), True, BLANCO)
            pantalla.blit(fondoNivel2,(0,0))
            pantalla.blit(fondo2,(0,610))
            segundos=str(segundos)
            cronometro = tiempo.render(segundos,0,BLANCO)
            pantalla.blit(cronometro,(100,620))
            pantalla.blit(tiempo2,(0,620))
            pantalla.blit(nombre2,(700,620))
            pantalla.blit(escudoGanon,(950,620))
            pantalla.blit(life,(380,620))

            if ganon.rect.x==ancho/2+30:
                FinalB=Bala2('imagenes/ganon.png',ganon.rect.x,ganon.rect.y)
                FinalB.linea=get_line((ganon.rect.x,ganon.rect.y),(jp.rect.x,jp.rect.y))
                bala2.add(FinalB)
                todos.add(FinalB)

            #pantalla.blit(life2,(380,320))



            if jp.vida >= 110.0 and jp.vida <= 120.0:
                pantalla.blit(corazon,(450,620))
                pantalla.blit(corazon,(490,620))
                pantalla.blit(corazon,(530,620))
                pantalla.blit(corazon,(570,620))

            if jp.vida >= 100.0 and jp.vida <=109.0:
                pantalla.blit(corazon,(450,620))
                pantalla.blit(corazon,(490,620))
                pantalla.blit(corazon,(530,620))

            if jp.vida >= 90.0 and jp.vida <=99.0:
                pantalla.blit(corazon,(450,620))
                pantalla.blit(corazon,(490,620))

            if jp.vida >= 76.0 and jp.vida <=89.0:
                pantalla.blit(corazon,(450,620))


        #Disparos de octorok
        if o.rect.x==50 or o.rect.x==80 or o.rect.x==110 or o.rect.x==140 or o.rect.x==170 or o.rect.x==200 or o.rect.x==230 or o.rect.x==260 or o.rect.x==290 or o.rect.x==320 or o.rect.x==350 or o.rect.x==380 or o.rect.x==410 or o.rect.x==440 or o.rect.x==470 or o.rect.x==500 :
            ba=Bala('imagenes/piedra.png',o.rect.x+62,o.rect.y)
            ba.dir=1
            bala.add(ba)
            todos.add(ba)

        for m in packMuros:
            l_choque=pygame.sprite.spritecollide(m,bala,True)

        l_choque=pygame.sprite.spritecollide(jp,packRejas,False)
        for ecol in l_choque:


            jp.menosVidaRejas()
            jp.golpe3()

        l_choque=pygame.sprite.spritecollide(jp,packAguaNorte,False)
        for ecol in l_choque:


            jp.menosVida()
            jp.golpe3()
            jp.rect.y-=2

        l_choque=pygame.sprite.spritecollide(jp,packAguaOeste,False)
        for ecol in l_choque:
            jp.menosVida()
            jp.golpe3()
            jp.rect.x-=2

        l_choque=pygame.sprite.spritecollide(jp,packAguaEste,False)
        for ecol in l_choque:


            jp.menosVida()
            jp.golpe3()
            jp.rect.x+=2

        l_choque=pygame.sprite.spritecollide(jp,packAguaSur,False)
        for ecol in l_choque:


            jp.menosVida()
            jp.golpe3()
            jp.rect.y+=2






        #Colision de item (Trifuerza)
        '''
        l_choque=pygame.sprite.spritecollide(jp,Trifuerza,False)
        for ecol in l_choque:

            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))



            if jp.vida>=80 and jp.vida<=87:


                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))




            trifuerzaEquipada = True
            jp.golpe1()
            pygame.mixer.music.stop()

            todos.draw(pantalla)
            pantalla.blit(trifuerzaPower,(ancho/2-350,alto/2-100))
            pantalla.blit(linkT,(ancho/2+150,alto/2-300))
            Trifuerza.remove(t)
            todos.remove(t)
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.mixer.music.load("sonidos/musicaTrifuerza.ogg")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.85)
            todos.add(tM)
            segundos+=3
        '''

        #Trifuerza no equipada
        if trifuerzaEquipada==False:
            for b in bala:
                #Colision de bala
                l_gb=pygame.sprite.spritecollide(jp,bala,True)
                for impacto in l_gb:
                    if jp.vida>=79 and jp.vida<=99:
                        pantalla.blit(menosVida,(530,620))
                    if jp.vida>=70 and jp.vida<=78:
                        pantalla.blit(menosVida,(490,620))
                    if jp.vida<=69:
                        jp.golpe2()
                        pygame.mixer.music.stop()
                        pantalla.blit(menosVida,(490,620))
                        pantalla.blit(menosVida,(530,620))
                        pantalla.blit(menosVida,(450,620))
                        todos.draw(pantalla)
                        #pantalla.blit(texto6,(ancho/2-120,alto/2-200))
                        #pantalla.blit(texto,(ancho/2-300,alto/2-100))
                        pygame.display.flip()
                        pygame.time.delay(6000)
                        segundos=-1
                        pygame.quit()
                        sys.exit()

                    jp.menosVidaBala()
                    jp.golpe3()

        #Trifuerza equipada
        elif trifuerzaEquipada==True:
            #Colision de bala
            l_gb=pygame.sprite.spritecollide(jp,bala,True)
            for impacto in l_gb:
                if jp.vida>=79 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))
                if jp.vida>=70 and jp.vida<=78:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))

                if jp.vida<=69:
                    jp.golpe2()
                    pygame.mixer.music.stop()
                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))
                    pantalla.blit(menosVida,(450,620))
                    #pantalla.blit(texto6,(ancho/2-120,alto/2-200))
                    #pantalla.blit(texto,(ancho/2-300,alto/2-100))
                    pygame.time.delay(6000)
                    segundos=-1
                    pygame.quit()
                    sys.exit()

                jp.menosVidaBala()
                jp.golpe3()
        

        #Colision de llegada a la escalera
        l_choque=pygame.sprite.spritecollide(jp,llegada,False)
        for ecol in l_choque:

            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))

            if jp.vida>=80 and jp.vida<=87:

                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))


            pygame.mixer.music.stop()


            #------------------------------------------------------------LEVEL 2----------------------------------------------------------------------------------------------------#


            lv = 2
            pygame.display.set_caption("                                                                                           The legend of Zelda ~ The Maze         ")

            pygame.mixer.music.load("sonidos/musicaIntro2.ogg")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.85)

            i2=pygame.image.load('imagenes/fondoIntro2.jpg')
            fondoNivel2=pygame.image.load('imagenes/fondoNivel2.jpg')
            escudoGanon=pygame.image.load('imagenes/escudoGanon.png')

            v1=pygame.image.load('imagenes/vidaGanon.png')

            gp=pygame.image.load('imagenes/ganonPantalla.png')

            nivel2=historia.render("Level 2",True,BLANCO)

            ti2=historia.render("The young hero was able to ",True,BLANCO)
            t2i2=historia.render("continue its mission, descending  ",True,BLANCO)
            t3i2=historia.render("even more in the terrible dungeon,",True,BLANCO)
            t4i2=historia.render("but did not know what awaited him ...",True,BLANCO)

            ati2=historia.render("The young hero was able to ",True,NEGRO)
            bt2i2=historia.render("continue its mission, descending  ",True,NEGRO)
            ct3i2=historia.render("even more in the terrible dungeon,",True,NEGRO)
            dt4i2=historia.render("but did not know what awaited him ...",True,NEGRO)

            n=historia.render("Press Space to Continue...",True,ROJO)
            n2=historia.render("Press Space to Continue...",True,BLANCO)

            nombre2= tiempo.render("Ganon Settlement ",True,BLANCO)


            contenedor.rect.x=325
            contenedor.rect.y=alto/2+10

            ganon.rect.x=ancho/2
            ganon.rect.y=alto/2-50

            ganonVerde.rect.x=ganon.rect.x
            ganonVerde.rect.y=ganon.rect.y

            ganonAzul.rect.x=ganonVerde.rect.x
            ganonAzul.rect.y=ganonVerde.rect.y

            ganonRojo.rect.x=ganonAzul.rect.x
            ganonRojo.rect.y=ganonAzul.rect.y

            arco.rect.x=ancho/2-40
            arco.rect.y=115

            c1.rect.x = ancho/2-50
            c1.rect.y = 500

            c2.rect.x = ancho/2+50
            c2.rect.y = 550

            bO.rect.x = ancho/2-145
            bO.rect.y = alto/2-45

            bE.rect.x = ancho/2+142
            bE.rect.y = alto/2-60

            bS.rect.x = ancho/2-80
            bS.rect.y = alto/2+78

            bN.rect.x = ancho/2-85
            bN.rect.y = 225



            introJuego=True

            while introJuego:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                pantalla.blit(i2,(0,0))

                pantalla.blit(ati2,(72,402))
                pantalla.blit(bt2i2,(52,452))
                pantalla.blit(ct3i2,(42,502))
                pantalla.blit(dt4i2,(32,552))

                pantalla.blit(ti2,(70,400))
                pantalla.blit(t2i2,(50,450))
                pantalla.blit(t3i2,(40,500))
                pantalla.blit(t4i2,(30,550))

                pantalla.blit(n2,(654,604))
                pantalla.blit(n,(652,602))

                pygame.display.flip()
                reloj.tick(60)

                if event.type == pygame.KEYDOWN:

                    if event.key==pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        introJuego=False
                        pantalla.fill(NEGRO)
                        pantalla.blit(nivel2,(ancho/2-50,alto/2-50))
                        pygame.display.flip()
                        pygame.time.delay(3000)




            pygame.mixer.music.load("sonidos/musica2.ogg")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.85)



            segundos=200


            #implementacion de la funcion creacion de muros

            packMuros.empty()
            todos.empty()

            llegada.empty()
            llegadaFake.empty()
            Enemigo.empty()
            Enemigo2.empty()
            Cofre.empty()
            Muro.empty()
            Muro2.empty()
            #Boton.empty()
            #botonPresionado.empty()
            EnemigoOctorok.empty()
            EnemigoVolando.empty()
            Cuchilla1.empty()
            Cuchilla2.empty()
            MuroPuerta1.empty()
            MuroPuerta2.empty()
            MuroPuerta3.empty()
            MuroPuerta4.empty()
            #Boton1.empty()
            #Boton2.empty()
            #Boton3.empty()
            #Boton4.empty()
            #BotonPresionado1.empty()
            #BotonPresionado2.empty()
            #BotonPresionado3.empty()
            #BotonPresionado4.empty()
            #Trifuerza.empty()
            Caballero1.empty()
            Caballero2.empty()
            bala.empty()



            vidaNivel1+=jp.vida

            level2 = []
            level = open("nivel/laberinto2.txt", "r")
            x = 0
            y = 0
            for l in level:
                    level2.append(l)
            for row in level2:
                    for col in row:


                            if col == "x":
                                    muroB = MuroBloques("imagenes/obstaculoLaberinto2.png",x,y)
                                    packMuros.add(muroB)
                                    todos.add(muroB)

                            if col == "a":
                                    muroA = MuroBloques("imagenes/agua.png",x,y)
                                    packAguaSur.add(muroA)
                                    todos.add(muroA)


                            if col == "e":
                                    muroA = MuroBloques("imagenes/agua.png",x,y)
                                    packAguaEste.add(muroA)
                                    todos.add(muroA)

                            if col == "i":
                                    muroA = MuroBloques("imagenes/agua.png",x,y)
                                    packAguaNorte.add(muroA)
                                    todos.add(muroA)

                            if col == "o":
                                    muroA = MuroBloques("imagenes/agua.png",x,y)
                                    packAguaOeste.add(muroA)
                                    todos.add(muroA)

                            if col == "t":
                                    muroA = MuroBloques("imagenes/llama.png",x,y)
                                    packMuros.add(muroA)
                                    todos.add(muroA)

                            if col == "r":
                                    muroA = MuroBloques("imagenes/reja.png",x,y)
                                    packRejas.add(muroA)
                                    todos.add(muroA)
                            if col == "m":
                                    muroA = MuroBloques("imagenes/arbusto.png",x,y)
                                    packMuros.add(muroA)
                                    todos.add(muroA)

                            if col == "b":
                                    muroA = MuroBloques("imagenes/pilar.png",x,y)
                                    packMuros.add(muroA)
                                    todos.add(muroA)

                            if col == "u":
                                    muroA = MuroBloques("imagenes/agua.png",x,y)
                                    packAguaSur.add(muroA)
                                    todos.add(muroA)

                            if col == "P":
                                    if trifuerzaEquipada==True:
                                        jp = Jugador("imagenes/linkAbajo.png",x,y)
                                        jp.muros = packMuros
                                        todos.add(jp)

                                    if trifuerzaEquipada==False:
                                        jp = Jugador("imagenes/personaje.png",x,y)
                                        jp.muros = packMuros
                                        todos.add(jp)






                            x += 15
                    y += 15
                    x = 0



            Contenedor.add(contenedor)
            todos.add(contenedor)



            FinalBoss.add(ganon)
            todos.add(ganon)


            packMuros.add(bO)
            todos.add(bO)
            packMuros.add(bS)
            todos.add(bS)
            packMuros.add(bE)
            todos.add(bE)


            Arco.add(arco)
            todos.add(arco)

            jp.vida=vidaNivel1




            # Condicionales de vida
            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))
            if jp.vida>=76 and jp.vida<=87:
                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))
            if jp.vida<=75:
                jp.golpe2()
                pygame.mixer.music.stop()
                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))
                pantalla.blit(menosVida,(450,620))
                #pantalla.blit(texto6,(ancho/2-120,alto/2-200))
                #pantalla.blit(texto,(ancho/2-300,alto/2-100))
                pygame.time.delay(3000)
                segundos=-1
                pygame.quit()
                sys.exit()

            #Limite de tiempo

            if segundos=='0':

                jp.golpe2()
                #ll2.golpe2=True
                pygame.mixer.music.stop()
                pantalla.blit(texto4,(ancho/2-150,alto/2-200))
                #pantalla.blit(texto,(ancho/2-300,alto/2-100))
                pygame.display.flip()
                pygame.time.delay(6000)
                pygame.quit()
                sys.exit()

        l_choque=pygame.sprite.spritecollide(jp,FinalBoss,False)
        for ecol in l_choque:
            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))


            if jp.vida>=76 and jp.vida<=87:


                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))


            jp.menosVida()
            jp.golpe3()


        l_choque=pygame.sprite.spritecollide(jp,Contenedor,False)
        for ecol in l_choque:

            pygame.mixer.music.pause()
            jp.golpe9()
            todos.draw(pantalla)
            pantalla.blit(linkC,(ancho/2+150,alto/2-300))
            pantalla.blit(contenedorPower,(ancho/2-450,alto/2-100))
            Contenedor.remove(contenedor)
            todos.remove(contenedor)
            pygame.display.flip()
            pygame.time.delay(3000)
            jp.vida=120
            jp.golpe11()
            pygame.display.flip()
            pygame.mixer.music.unpause()
            segundos+=3

        l_choque=pygame.sprite.spritecollide(jp,Arco,False)
        for ecol in l_choque:

            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))
            if jp.vida>=80 and jp.vida<=87:
                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))

            arcoItem=True
            pygame.mixer.music.pause()
            jp.golpe9()
            todos.draw(pantalla)
            pantalla.blit(linkA,(ancho/2+100,alto/2-300))
            pantalla.blit(arcoPower,(ancho/2-250,alto/2-100))
            pantalla.blit(arcoInstruction,(ancho/2-400,alto/2+100))
            Arco.remove(arco)
            todos.remove(arco)
            pygame.display.flip()
            pygame.time.delay(4500)
            Muro.add(aM)
            todos.add(aM)
            pygame.mixer.music.unpause()
            segundos+=4


            #Colision de bala
        l_gb=pygame.sprite.spritecollide(jp,bala2,True)
        for impacto in l_gb:

                jp.golpe1()

        for b in FinalBoss:
            #Colision de bala
            l_gb=pygame.sprite.spritecollide(b,bala,True)
            for impacto in l_gb:
                ganon.menosVidaBala()
                ganon.golpe1()
                if ganon.vida >=50 and ganon.vida <=75:
                    FinalBoss.remove(ganon)
                    todos.remove(ganon)
                    FinalBoss.add(ganonVerde)
                    todos.add(ganonVerde)

                    if ganon.vida==75:

                        packMuros.add(bN)
                        todos.add(bN)
                        NumeroMuro=random.randint(1,3)

                        if NumeroMuro==1:
                            packMuros.remove(bO)
                            todos.remove(bO)
                        if NumeroMuro==2:
                            packMuros.remove(bS)
                            todos.remove(bS)
                        if NumeroMuro==3:
                            packMuros.remove(bE)
                            todos.remove(bE)


                if ganon.vida >=25 and ganon.vida <=49:
                    FinalBoss.remove(ganonVerde)
                    todos.remove(ganonVerde)
                    FinalBoss.add(ganonAzul)
                    todos.add(ganonAzul)

                    if ganon.vida==49:

                        if NumeroMuro==1:
                            packMuros.add(bO)
                            todos.add(bO)
                        if NumeroMuro==2:
                            packMuros.add(bS)
                            todos.add(bS)
                        if NumeroMuro==3:
                            packMuros.add(bE)
                            todos.add(bE)

                        NumeroMuro=random.randint(1,4)

                        if NumeroMuro==1:
                            packMuros.remove(bO)
                            todos.remove(bO)
                        if NumeroMuro==2:
                            packMuros.remove(bS)
                            todos.remove(bS)
                        if NumeroMuro==3:
                            packMuros.remove(bE)
                            todos.remove(bE)

                        if NumeroMuro==4:
                            packMuros.remove(bN)
                            todos.remove(bN)


                if ganon.vida >=1 and ganon.vida <=24:
                    FinalBoss.remove(ganonAzul)
                    todos.remove(ganonAzul)
                    FinalBoss.add(ganonRojo)
                    todos.add(ganonRojo)

                    if ganon.vida==24:


                        packMuros.add(bO)
                        todos.add(bO)

                        packMuros.add(bS)
                        todos.add(bS)

                        packMuros.add(bE)
                        todos.add(bE)

                        packMuros.add(bN)
                        todos.add(bN)

                if ganon.vida<=0:
                    FinalBoss.remove(ganonRojo)
                    todos.remove(ganonRojo)
                    pygame.mixer.music.stop()
                    ganon.golpe2()
                    ganon.vida=1
                    llegadaNivel2.add(lln2)
                    todos.add(lln2)
                    todos.add(c1)
                    todos.add(c2)



        l_choque=pygame.sprite.spritecollide(jp,llegadaNivel2,False)
        for ecol in l_choque:
            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))
            if jp.vida>=80 and jp.vida<=87:
                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))

            jp.golpe1()
            pygame.mixer.music.stop()
            todos.draw(pantalla)
            pantalla.blit(texto5,(ancho/2-420,alto/2-200))
            pantalla.blit(texto2,(ancho/2-300,alto/2-100))
            pygame.display.flip()
            pygame.time.delay(6000)
            segundos=-1

            pygame.mixer.music.load("sonidos/final.ogg")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.85)
            pygame.display.flip()

            finaJuegol=True
            while final:

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                pantalla.blit(final,(0,0))
                pantalla.blit(f1,(ancho/2-400,alto/2-200))
                pantalla.blit(f22,(ancho/2-148,alto/2+102))
                pantalla.blit(f2,(ancho/2-150,alto/2+100))
                pantalla.blit(ss,(ancho/2-198,alto/2+202))
                pantalla.blit(s,(ancho/2-200,alto/2+200))
                pygame.display.flip()
                reloj.tick(60)
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        finalJuego=False
                        pygame.quit()
                        sys.exit()


        '''
        #Colision de llegada al cofre Falso "Veneno"
        l_choque=pygame.sprite.spritecollide(jp,llegadaFake,True)
        for ecol in l_choque:

            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))
            if jp.vida>=80 and jp.vida<=87:


                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))



            jp.golpe2()
            ll2.golpe2=True
            pygame.mixer.music.stop()
            llegadaFake.remove(ll2)
            todos.remove(ll2)
            Muro.add(g)
            todos.add(g)
            todos.draw(pantalla)
            pantalla.blit(linkV,(ancho/2+100,alto/2-200))
            pantalla.blit(texto3,(ancho/2-350,alto/2-200))
            pantalla.blit(texto,(ancho/2-400,alto/2-100))
            pantalla.blit(menosVida,(450,620))
            pantalla.blit(menosVida,(490,620))
            pantalla.blit(menosVida,(530,620))
            pygame.display.flip()
            pygame.time.delay(6000)
            segundos=-1
            pygame.quit()
            sys.exit()
        '''
        #Trifuerza no equipada
        if trifuerzaEquipada==False:
            #Colision de enemigo Caballero1
            l_choque=pygame.sprite.spritecollide(jp,Caballero1,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))


                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.menosVida()
                jp.golpe3()

        #Trifuerza equipada
        elif trifuerzaEquipada==True:
            #Colision de enemigo Caballero1
            l_choque=pygame.sprite.spritecollide(jp,Caballero1,True)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.golpe8()

        #Trifuerza no equipada
        if trifuerzaEquipada==False:
            #Colision de enemigo Caballero2
            l_choque=pygame.sprite.spritecollide(jp,Caballero2,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.menosVida()
                jp.golpe3()

        #Trifuerza equipada
        elif trifuerzaEquipada==True:
            #Colision de enemigo Caballero2
            l_choque=pygame.sprite.spritecollide(jp,Caballero2,True)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.golpe8()
        '''
        #Trifuerza no equipada
        if trifuerzaEquipada==False:
            #Colision enemigo Cuchilla1
            l_choque=pygame.sprite.spritecollide(jp,Cuchilla1,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.menosVida()
                jp.golpe3()

        #Trifuerza equipada
        elif trifuerzaEquipada==True:
            #Colision enemigo Cuchilla1
            l_choque=pygame.sprite.spritecollide(jp,Cuchilla1,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.menosVidaBala()
                jp.golpe3()
        '''
        #Trifuerza no equipada
        if trifuerzaEquipada==False:
            #Colision enemigo Cuchilla2
            l_choque=pygame.sprite.spritecollide(jp,Cuchilla2,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.menosVida()
                jp.golpe3()

        #Trifuerza equipada
        elif trifuerzaEquipada==True:
            #Colision enemigo Cuchilla2
            l_choque=pygame.sprite.spritecollide(jp,Cuchilla2,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.menosVidaBala()
                jp.golpe3()

        #Trifuerza no equipada
        if trifuerzaEquipada==False:
            #Colision enemigo1
            l_choque=pygame.sprite.spritecollide(jp,Enemigo,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.menosVida()
                jp.golpe3()

        #Trifuerza equipada
        elif trifuerzaEquipada==True:
            #Colision enemigo1
            l_choque=pygame.sprite.spritecollide(jp,Enemigo,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.menosVidaBala()
                jp.golpe3()



        #Trifuerza no equipada
        if trifuerzaEquipada==False:
            #Colision enemigo2
            l_choque=pygame.sprite.spritecollide(jp,Enemigo2,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.menosVida()
                jp.golpe3()

        #Trifuerza equipada
        elif trifuerzaEquipada==True:
            #Colision enemigo2
            l_choque=pygame.sprite.spritecollide(jp,Enemigo2,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=76 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.menosVidaBala()
                jp.golpe3()

        #Trifuerza no equipada
        if trifuerzaEquipada==False:
            #Colision EnemigoOctorok
            l_choque=pygame.sprite.spritecollide(jp,EnemigoOctorok,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=80 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))

                jp.menosVida()
                jp.golpe3()

        #Trifuerza equipada
        elif trifuerzaEquipada==True:
            #Colision EnemigoOctorok
            l_choque=pygame.sprite.spritecollide(jp,EnemigoOctorok,True)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=80 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.golpe8()

        #Trifuerza no equipada
        if trifuerzaEquipada==False:
            #Colision EnemigoVolando
            l_choque=pygame.sprite.spritecollide(jp,EnemigoVolando,False)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=80 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))

                jp.menosVida()
                jp.golpe3()

        #Trifuerza equipada
        elif trifuerzaEquipada==True:
            #Colision EnemigoVolando
            l_choque=pygame.sprite.spritecollide(jp,EnemigoVolando,True)
            for ecol in l_choque:
                if jp.vida>=88 and jp.vida<=99:
                    pantalla.blit(menosVida,(530,620))



                if jp.vida>=80 and jp.vida<=87:


                    pantalla.blit(menosVida,(490,620))
                    pantalla.blit(menosVida,(530,620))


                jp.golpe8()
        

        #Colision item "Cofre"
        l_choque=pygame.sprite.spritecollide(jp,Cofre,False)
        for ecol in l_choque:

            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))



            if jp.vida>=80 and jp.vida<=87:


                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))



            jp.golpe5()
            ll.golpe5=True
            todos.draw(pantalla)

            #pantalla.blit(llave,(ancho/2-300,alto/2-100))
            #pantalla.blit(llavePantalla,(ancho/2,alto/2-200))
            pygame.display.flip()
            pygame.time.delay(3000)
            Cofre.remove(c)
            todos.remove(c)
            packMuros.add(cA)
            todos.add(cA)
            #todos.add(llM)
            segundos+=3
            llaveEquipada = True

        #Colision puertas princesas
        l_choque=pygame.sprite.spritecollide(jp,Muro,False)
        for ecol in l_choque:

            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))



            if jp.vida>=80 and jp.vida<=87:


                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))



            todos.draw(pantalla)

            #Llave no equipada
            if llaveEquipada==False:
                jp.golpe7()
                #pantalla.blit(noLlave,(ancho/2-200,alto/2-100))
                jp.rect.x=p.rect.x-50
                pygame.display.flip()
                pygame.time.delay(1000)

            #Llave equipada
            elif llaveEquipada==True:
                jp.golpe4()
                ll.golpe4=True
                #pantalla.blit(siLlave,(ancho/2-200,alto/2-100))
                pygame.display.flip()
                pygame.time.delay(2000)
                Muro.remove(p)
                todos.remove(p)
                #todos.remove(llM)
                segundos+=3
                llaveEquipada=False


        #Colision puertas princesas
        l_choque=pygame.sprite.spritecollide(jp,Muro2,False)
        for ecol in l_choque:

            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))



            if jp.vida>=80 and jp.vida<=87:


                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))



            todos.draw(pantalla)
        '''
            #Llave no equipada
            if llaveEquipada==False:
                jp.golpe7()
                pantalla.blit(noLlave,(ancho/2-200,alto/2-100))
                jp.rect.x=p2.rect.x-50
                pygame.display.flip()
                pygame.time.delay(1000)

            #Llave equipada
            elif llaveEquipada==True:
                jp.golpe4()
                ll.golpe4=True
                pantalla.blit(siLlave,(ancho/2-200,alto/2-100))
                pygame.display.flip()
                pygame.time.delay(2000)
                Muro2.remove(p2)
                todos.remove(p2)
                todos.remove(llM)
                segundos+=3
                llaveEquipada=False

        
        #Colision puertas item Trifuerza
        l_choque=pygame.sprite.spritecollide(jp,MuroPuerta1,False)
        for ecol in l_choque:

            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))



            if jp.vida>=80 and jp.vida<=87:


                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))



            todos.draw(pantalla)


            jp.golpe7()
            pantalla.blit(puertaCerrada,(ancho/2-200,alto/2-100))
            jp.rect.x=mp1.rect.x-35
            pygame.display.flip()
            pygame.time.delay(1000)

        #Colision puertas item Trifuerza
        l_choque=pygame.sprite.spritecollide(jp,MuroPuerta2,False)
        for ecol in l_choque:

            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))



            if jp.vida>=80 and jp.vida<=87:


                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))



            todos.draw(pantalla)


            jp.golpe7()
            pantalla.blit(puertaCerrada,(ancho/2-200,alto/2-100))
            jp.rect.x=mp2.rect.x-35
            pygame.display.flip()
            pygame.time.delay(1000)

        #Colision puertas item Trifuerza
        l_choque=pygame.sprite.spritecollide(jp,MuroPuerta3,False)
        for ecol in l_choque:

            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))



            if jp.vida>=80 and jp.vida<=87:


                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))



            todos.draw(pantalla)


            jp.golpe7()
            pantalla.blit(puertaCerrada,(ancho/2-200,alto/2-100))
            jp.rect.x=mp3.rect.x-35
            pygame.display.flip()
            pygame.time.delay(1000)

        #Colision puertas item Trifuerza
        l_choque=pygame.sprite.spritecollide(jp,MuroPuerta4,False)
        for ecol in l_choque:

            if jp.vida>=88 and jp.vida<=99:
                pantalla.blit(menosVida,(530,620))



            if jp.vida>=80 and jp.vida<=87:


                pantalla.blit(menosVida,(490,620))
                pantalla.blit(menosVida,(530,620))



            todos.draw(pantalla)


            jp.golpe7()
            pantalla.blit(puertaCerrada,(ancho/2-200,alto/2-100))
            jp.rect.x=mp4.rect.x-35
            pygame.display.flip()
            pygame.time.delay(1000)
        '''

        # Condicionales de vida
        if jp.vida>=90.0 and jp.vida<=99.0:
            pantalla.blit(menosVida,(530,620))



        if jp.vida>=76.0 and jp.vida<=89.0:


            pantalla.blit(menosVida,(490,620))
            pantalla.blit(menosVida,(530,620))



        if jp.vida<=75.0:
            jp.golpe2()
            pygame.mixer.music.stop()
            pantalla.blit(menosVida,(490,620))
            pantalla.blit(menosVida,(530,620))
            pantalla.blit(menosVida,(450,620))
            todos.draw(pantalla)
            #pantalla.blit(texto6,(ancho/2-120,alto/2-200))
            #pantalla.blit(texto,(ancho/2-300,alto/2-100))
            pygame.display.flip()
            pygame.time.delay(3000)
            segundos=-1
            pygame.quit()
            sys.exit()





        #Limite de tiempo

        if segundos=='0':

            jp.golpe2()
            ll2.golpe2=True
            pygame.mixer.music.stop()

            todos.draw(pantalla)
            pantalla.blit(texto4,(ancho/2-150,alto/2-200))
            #pantalla.blit(texto,(ancho/2-300,alto/2-100))
            pygame.display.flip()
            pygame.time.delay(6000)
            pygame.quit()
            sys.exit()









        #Reloj,actualizacion y llenar la pantalla

        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
