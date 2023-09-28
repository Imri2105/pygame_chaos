import pygame
import random
import time

pygame.init()
ScreenSize = (1600,900)
Screen = Screen = pygame.display.set_mode(ScreenSize)
WHITE = (255, 255, 255)



def drawLine(screen, color:tuple, start_point:tuple, end_point:tuple, flip = True): #drawing a line
    pygame.draw.line(screen,color,start_point,end_point)
    if flip:
        pygame.display.flip()

def drawPoint(screen, color:tuple, xpos:int, ypos:int, flip = True): #drawing a point 
    pygame.draw.rect(screen, color, pygame.Rect(xpos , ypos, 1, 1))
    if flip:
        pygame.display.flip()

def DrawMiddlePoint(screen, color:tuple, point_a:tuple, point_b:tuple, flip = True): #drawing the middle point between two points
    xpos = (point_a[0]+point_b[0])/2
    ypos = (point_a[1]+point_b[1])/2
    drawPoint(screen, color, xpos, ypos, flip)
    return xpos,ypos

class Triangle: #triangle class
    def __init__(self, a:tuple, b:tuple, c:tuple) -> None:
        self.point_a:tuple = a
        self.point_b:tuple = b
        self.point_c:tuple = c
    
    def draw(self, screen,color:tuple,flip = True): #draws the triangle
        drawLine(screen, color, self.point_a, self.point_b, False)
        drawLine(screen, color, self.point_a, self.point_c, False)
        drawLine(screen, color, self.point_c, self.point_b, False)
        if flip:
            pygame.display.flip()
    
    def getRandomVertex(self): #returning random vertex of the triangle
        num = random.randint(1,3)
        if num == 1:
            return self.point_a
        
        if num == 2:
            return self.point_b
        
        return self.point_c





def main():
    t = Triangle((800,100), (400,300), (1200,300)) #creation of triangle object
    t.draw(Screen,WHITE) #drawing of triangle
    xpos = 800 #xpos of starting point 
    ypos = 250 #ypos of starting point 
    drawPoint(Screen,WHITE,xpos,ypos) # drawing the first point
    run = True #flag that lets the user control the stopping and resuming of the visualization

    #main loop
    while True: 
        for event in pygame.event.get(): #exit option
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYUP: #pausing the visualiztion
                if event.key == pygame.K_SPACE: 
                    run = not run
                    print(f"run = {run}")

        if run: #drawing the next point
            ver = t.getRandomVertex()
            xpos,ypos = DrawMiddlePoint(Screen,WHITE,(xpos,ypos),ver)
            time.sleep(0.001)




if __name__ == "__main__":
    main()