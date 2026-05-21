from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# ---------------- INPUT ----------------
n = int(input("Number of processes: "))

process = []
burst = []

for i in range(n):
    process.append(input("Process name: "))
    burst.append(int(input("Burst time: ")))

# ---------------- FCFS TIMELINE ----------------
timeline = []
time = 0

for i in range(n):
    start = time
    time += burst[i]
    end = time
    timeline.append((process[i], start, end))

# ---------------- COLORS ----------------
colors = [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1)]

# ---------------- DRAW ----------------
def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    for i, (name, start, end) in enumerate(timeline):
        glColor3f(*colors[i % len(colors)])

        x1 = start / time
        x2 = end / time
        y = 0.5

        glBegin(GL_QUADS)
        glVertex2f(x1, y)
        glVertex2f(x2, y)
        glVertex2f(x2, y - 0.3)
        glVertex2f(x1, y - 0.3)
        glEnd()

    glFlush()

# ---------------- MAIN ----------------
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 200)
    glutCreateWindow(b"FCFS Visualizer")

    glClearColor(1, 1, 1, 1)
    gluOrtho2D(0, 1, 0, 1)

    glutDisplayFunc(draw)
    glutMainLoop()

main()
