import pygame as pg
import numpy as np
import numba as nb
import time
import sys
import os

class Window:
    def __init__(self, title):
        self.screen = pg.display.set_mode((1600, 900), pg.DOUBLEBUF, pg.OPENGL)
        pg.display.set_caption("Game Engine: 0 FPS")
        pg.font.init()

        self.gameTitle = title

        self.clock = pg.time.Clock()
        self.running = True
        self.fps = 165

        self.objects = []
        self.objectColors = []

        self.objectsTree = pg.Rect(0, 0, 300, 900)
        self.objectsTreeColor = (30, 30, 30)
        self.objectsTreeBorder = 2
        self.objectsTreeBorderColor = (255, 255, 255)

        self.addObjButton = pg.Rect(0, 800, 300, 100)
        self.addObjButtonColor = (0, 200, 0)
        self.addObjButtonBorder = 2
        self.addObjButtonBorderColor = (255, 0, 0)
        self.addObjButtonText = "Add Object"
        self.addObjButtonFont = pg.font.SysFont("Arial", 50)


        self.viewport = pg.Rect(300, 0, 1300, 900)
        self.viewportColor = (0, 0, 0)
        self.viewportBorder = 2
        self.viewportBorderColor = (255, 255, 255)

    def run(self):
        while self.running:
            self.clock.tick(self.fps)
            self.events()
            self.update()
            self.draw()

    def packGame(self, debug=False):
        with open("game.py", "w") as f:
            f.write("import pygame as pg\n")
            f.write("import numpy as np\n")
            f.write("import numba as nb\n")
            f.write("import time\n")
            f.write("import sys\n")
            f.write("\n")
            f.write("screen = pg.display.set_mode((1300, 900), pg.DOUBLEBUF, pg.OPENGL)\n")
            f.write("pg.display.set_caption(\"" + self.gameTitle + "\")\n")
            f.write("\n")
            f.write("clock = pg.time.Clock()\n")
            f.write("running = True\n")
            f.write("fps = 165\n")
            f.write("objects = []\n")
            f.write("objColors = []\n")
            f.write("\n")

            for obj in self.objects:
                if debug: print("Adding object: " + str(self.objects.index(obj)) + " out of " + str(len(self.objects)))
                f.write("objects.append(pg.Rect(" + str(obj.x - 300) + ", " + str(obj.y) + ", " + str(obj.width) + ", " + str(obj.height) + "))\n")
                f.write("objColors.append((" + str(self.objectColors[self.objects.index(obj)][0]) + ", " + str(self.objectColors[self.objects.index(obj)][1]) + ", " + str(self.objectColors[self.objects.index(obj)][2]) + "))\n")

            f.write("\n")
            f.write("while running:\n")
            f.write("    clock.tick(fps)\n")
            f.write("    for event in pg.event.get():\n")
            f.write("        if event.type == pg.QUIT:\n")
            f.write("            running = False\n")
            f.write("\n")
            f.write("        keys = pg.key.get_pressed()\n")
            f.write("        if keys[pg.K_ESCAPE]:\n")
            f.write("            running = False\n")
            f.write("\n")
            f.write("    screen.fill((0, 0, 30))\n")
            f.write("    for i in range(len(objects)):\n")
            f.write("        pg.draw.rect(screen, objColors[i], objects[i])\n")
            f.write("    pg.display.flip()\n")
            f.write("\n")
            f.write("pg.quit()\n")
            f.write("sys.exit()\n")
        f.close()

        os.system("python game.py")

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            keys = pg.key.get_pressed()
            if keys[pg.K_ESCAPE]:
                self.running = False
            elif keys[pg.K_BACKQUOTE]:
                self.packGame(debug=True)

            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pos()[0] < 300 and pg.mouse.get_pos()[1] > 800:
                    self.objects.append(pg.Rect(300, 0, 100, 100))
                    self.objectColors.append((255, 255, 255))

    def update(self):
        pg.display.set_caption(f"Game Engine: {self.clock.get_fps():.2f} FPS")

    def draw(self):
        self.screen.fill((0, 0, 30))
        pg.draw.rect(self.screen, self.objectsTreeColor, self.objectsTree)
        pg.draw.rect(self.screen, self.objectsTreeBorderColor, self.objectsTree, self.objectsTreeBorder)
        pg.draw.rect(self.screen, self.viewportColor, self.viewport)
        pg.draw.rect(self.screen, self.viewportBorderColor, self.viewport, self.viewportBorder)
        pg.draw.rect(self.screen, self.addObjButtonColor, self.addObjButton)

        self.screen.blit(self.addObjButtonFont.render(self.addObjButtonText, True, (255, 255, 255)), (self.addObjButton.x + 20, self.addObjButton.y + 20))
        
        for obj in self.objects:
            pg.draw.rect(self.screen, self.objectColors[self.objects.index(obj)], obj)
        pg.display.flip()

class GameEngine:
    def __init__(self):
        self.running = False
        self.title = "My Game"

        self.window = Window(self.title)
        self.window.run()

if __name__ == "__main__":
    game = GameEngine()
    pg.quit()