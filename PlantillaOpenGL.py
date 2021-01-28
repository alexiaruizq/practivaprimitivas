from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *


def dibujarPasto():
    glColor3f(0.66666666666666666666666666666667,0.72549019607843137254901960784314,0.67843137254901960784313725490196)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.5,0.0)
    glVertex3f(1.0,-0.5,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()

def dibujarSol():
    glColor3f(0.91764705882352941176470588235294,0.90980392156862745098039215686275,0.70980392156862745098039215686275)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.6 , sin(angulo) * 0.2 + 0.6 ,0.0)
    glEnd()

def dibujarNube1():
    glColor3f(0.7,0.7,0.7)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.3 + 0.3 , sin(angulo) * 0.05 + 0.75 ,0.0)
    glEnd()

def dibujarNube2():
    glColor3f(0.7,0.7,0.7)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.3 + 0.6 , sin(angulo) * 0.06 + 0.4 ,0.0)
    glEnd()

def dibujarNube3():
    glColor3f(0.7,0.7,0.7)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.3 - 0.3 , sin(angulo) * 0.07 + 0.1 ,0.0)
    glEnd()

def dibujarRayos():
    glColor3f(0.91764705882352941176470588235294,0.77254901960784313725490196078431,0.70980392156862745098039215686275)
    glBegin(GL_TRIANGLE_STRIP)
    for x in range(90):
        angulo = x
        glVertex3f(cos(angulo) * 0.25 - 0.6, sin(angulo) * 0.25 + 0.6, 0.0)
    glEnd()

def dibujarArbol():
    glColor3f(0.98431372549019607843137254901961,0.86274509803921568627450980392157,0.86274509803921568627450980392157)
    glBegin(GL_QUADS)
    glVertex2f(0.8,-0.3)
    glVertex2f(0.75,-0.3)
    glVertex2f(0.75,-0.6)
    glVertex2f(0.8,-0.6)
    glEnd()

def dibujarHojas():
    glColor3f(0.91764705882352941176470588235294,0.90980392156862745098039215686275,0.70980392156862745098039215686275)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.12 + 0.775 , sin(angulo) * 0.135 - 0.275 ,0.0)
    glEnd()

def dibujarCasa():
    glColor3f(0.87450980392156862745098039215686, 0.88627450980392156862745098039216, 0.85882352941176470588235294117647)
    glBegin(GL_QUADS)
    glVertex2f(-0.6,-0.3)
    glVertex2f(0.2,-0.3)
    glVertex2f(0.2,-0.75)
    glVertex2f(-0.6,-0.75)
    glEnd()

def dibujarTecho():
    glColor3f(0.94509803921568627450980392156863, 0.70980392156862745098039215686275, 0.70980392156862745098039215686275)
    glBegin(GL_QUADS)
    glVertex2f(-0.7,-0.3)
    glVertex2f(0.3,-0.3)
    glVertex2f(0.15,-0.2)
    glVertex2f(-0.55,-0.2)
    glEnd()

def dibujarPuerta():
    glColor3f(0.93725490196078431372549019607843, 0.84705882352941176470588235294118, 0.71372549019607843137254901960784)
    glBegin(GL_QUADS)
    glVertex2f(-0.25,-0.55)
    glVertex2f(-0.15,-0.55)
    glVertex2f(-0.15,-0.75)
    glVertex2f(-0.25,-0.75)
    glEnd()

def dibujarPerilla():
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.008 - 0.17 , sin(angulo) * 0.008 - 0.65 ,0.0)
    glEnd()


def dibujarVentana1():
    glColor3f(0.57254901960784313725490196078431,0.57254901960784313725490196078431,0.61568627450980392156862745098039)
    glBegin(GL_QUADS)
    glVertex2f(-0.5,-0.4)
    glVertex2f(-0.4,-0.4)
    glVertex2f(-0.4,-0.5)
    glVertex2f(-0.5,-0.5)
    glEnd()

def dibujarVentana2():
    glColor3f(0.57254901960784313725490196078431,0.57254901960784313725490196078431,0.61568627450980392156862745098039)
    glBegin(GL_QUADS)
    glVertex2f(0,-0.4)
    glVertex2f(0.1,-0.4)
    glVertex2f(0.1,-0.5)
    glVertex2f(0,-0.5)
    glEnd()



def dibujar():
    #rutinas de dibujo
    dibujarPasto()
    dibujarRayos()
    dibujarSol()
    dibujarNube1()
    dibujarNube2()
    dibujarNube3()
    dibujarArbol()
    dibujarHojas()
    dibujarCasa()
    dibujarTecho()
    dibujarPuerta()
    dibujarVentana1()
    dibujarVentana2()
    dibujarPerilla()

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(600,600,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,600,600)
        #Establece color de borrado
        glClearColor(0.57254901960784313725490196078431,0.57254901960784313725490196078431,0.61568627450980392156862745098039,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()