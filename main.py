import pygame , sys

pygame.init()

screen = pygame.display.set_mode((800,500))

clock = pygame.time.Clock()

pygame.mixer.init()


bigfont = pygame.font.Font(None , 80)
smallfont = pygame.font.Font(None , 30)

class Button:
    def __init__(self , text , width , height , x , y ):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.color = (255,100,100)
        self.rect = pygame.Rect(self.x , self.y , self.width , self.height)
    
    def spawn(self):
        pass

class LoadingScreen:

    def __init__(self):
        self.ready = False
    
    def home(self):
        screen.blit(pygame.image.load("loadingscreen2.png").convert(), (0,0))

        welcome = bigfont.render("WELCOME TO PYGAME TD", True , (127,107,252))

        pressto = smallfont.render("PRESS 'A' TO START " , True , (127 , 107 , 252))

        screen.blit(welcome , (20,100))

        screen.blit(pressto , (300,200))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.ready = True


loadingscreen = LoadingScreen()

class Firetower:
    def __init__(self , x , y ):
        self.time = 5*60
        self.damage = 10
        self.reloadtime = 3
        self.range = 100
        self.x = x
        self.y = y
    
    def draw(self):
        myrect = pygame.Rect(self.x , self.y , self.range , self.range)
        screen.blit(pygame.image.load("firetower_a.png").convert_alpha(), myrect)



class MainGame:
    
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()




            screen.blit(pygame.image.load("maingamebg.png").convert(),(0,0))


            screen.blit(pygame.image.load("firetower_a.png").convert_alpha(),(45 , 420))
            fireprice = smallfont.render("$20" , True , (0, 0 , 0))
            screen.blit(fireprice , (100 , 430))

            pygame.display.flip()
            clock.tick(60)





while True:

    if loadingscreen.ready:
        maingame = MainGame()
        maingame.run()
    else:
        loadingscreen.home()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
    


    pygame.display.flip()

    



sys.exit()