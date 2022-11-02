import turtle
import time
import random

posponer = 0.1   #importante los numero con coma ',' se escriben con punto '.'  Ademas esto esta relentizando a la serpiente una milecima de segundo

#Marcador
score = 0
high_score = 0

#canal de youtube YouDevs 

#Configuracion ventana
wn = turtle.Screen()
wn.title('Juego de snake')
wn.bgcolor('black')
wn.setup(width= 600, height= 600)
wn.tracer(0)  #mejora la vista supuestamente chequear luego

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.penup() # quita el rastro de la serpiente moviendose
cabeza.goto(0,0)
cabeza.color('white')
cabeza.direction = 'stop'

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.penup() 
comida.goto(0,100)
comida.color('red')

#Segmentos / cuerpo serpiente
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('Score: 0       High score: 0', align ='center', font = ('Courier', 24, 'normal'))


#Funciones
def arriba():
    cabeza.direction = 'up'
def abajo():
    cabeza.direction = 'down'
def izquierda():
    cabeza.direction = 'left'
def derecha():
    cabeza.direction = 'right'

def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Teclado
wn.listen()
wn.onkeypress(arriba, 'Up')
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')


while True:         #bucle infinito para que nosotros demos la instruccion de cuando queremos que termine
    wn.update()

    #Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = 'stop'

        #Esconder los segmentos; en realidad buscar como eliminarlos
        for segmento in segmentos:
            segmento.goto(2000,2000)


        #Limpiar lista de segmentos
        segmentos.clear()

        #Resetear marcador
        score = 0
        texto.clear()
        texto.write('Score: {}       High score: {}'.format(score, high_score), align ='center', font = ('Courier', 24, 'normal'))


    #Colisiones comida
    if cabeza.distance(comida) < 20:   #choque cabeza con comida; 20es porque tanto cabeza como comida miden 20 pixeles
        x = random.randint(-280,280) #no lo hacemos en 300 para que nose cree en los bordes
        y = random.randint(-280,280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.color('grey')
        nuevo_segmento.penup() 
        segmentos.append(nuevo_segmento)

        #Aumentar marcador
        score += 10

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write('Score: {}       High score: {}'.format(score, high_score), align ='center', font = ('Courier', 24, 'normal'))

            
    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)    #total de elementos dentro de la lista
    for index in range(totalSeg -1, 0, -1):   #iterando el ultimo elemento sigue al anterior
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    #Colisiones con el propio cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = 'stop'

            #Esconder segmentos
            for segmento in segmentos:
                segmento.goto(2000,2000)
            
            segmentos.clear()
            score = 0
            texto.clear()
            texto.write('Score: {}       High score: {}'.format(score, high_score), align ='center', font = ('Courier', 24, 'normal'))

    time.sleep(posponer)



