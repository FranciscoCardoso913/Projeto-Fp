# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 10:59:51 2021

@author: Utilizador
"""

import pygame
import random 

SCREEN_SIZE = (1500, 750)#
player={
        "nome":"JCL",#15 max
        "agilidade":60,
        "nivel":3,
        "vida":1800,
        "vidaM":1800,
        "img":"vy_0 (2).png",
        "ataque":500,
        "velocidade":60,
        "elemento1":"vento",
        "elemento2":"eletro"
        }
MARIO_SIZE = 73#
BLOCK_SIZE = 32#

mundo=1
level=0
pygame.init()#
screen = pygame.display.set_mode(SCREEN_SIZE)#

mario_img = pygame.image.load('vy_0.png')#

mario_x = 500
mario_y = 630

inimigos=[ {
    
 
    "nivel":2,
    "agilidade":60,
    "vida":2800,
    "vidaM":2800,
    "img":"ini_ini.png",
    "ataque":382,
    "velocidade":50,
    "elemento1":"eletro",
    "nome":"Canas",
    
    "ativo":False,
    "x":3000,
    "y":3000
    
    
    },
    {
    
    "nivel":2,
    "agilidade":60,
    "vida":2800,
    "vidaM":2800,
    "img":"razor.jpg",
    "ataque":289,
    "velocidade":50,
    "elemento1":"fogo",
    "nome":"Micheal",
    "img":'razor.jpg',
    "ativo":False,
    "x":3000,
    "y":3000
    
    },
    {
    
    "nivel":2,
    "agilidade":60,
    "vida":2800,
    "vidaM":2800,
    "img":"razor.jpg",
    "ataque":380,
    "velocidade":50,
    "elemento1":"natureza",
    "nome":"CCA",
    "img":'razor.jpg',
    "ativo":False,
    "x":3000,
    "y":3000
    
    },
    {
    
    "nivel":2,
    "agilidade":60,
    "vida":2800,
    "vidaM":2800,
    "img":"razor.jpg",
    "ataque":400,
    "velocidade":50,
    "elemento1":"agua",
    "nome":"Helena",
    "img":'razor.jpg',
    "ativo":False,
    "x":3000,
    "y":3000
    
    },
    {
    
    "nivel":2,
    "agilidade":60,
    "vida":2800,
    "vidaM":2800,
    "img":"razor.jpg",
    "ataque":300,
    "velocidade":50,
    "elemento1":"gelo",
    "nome":"Renato",
    "img":'razor.jpg',
    "ativo":False,
    "x":3000,
    "y":3000
    
    },
    {
    
    "nivel":2,
    "agilidade":60,
    "vida":2800,
    "vidaM":2800,
    "img":"razor.jpg",
    "ataque":300,
    "velocidade":50,
    "elemento1":"pedra",
    "nome":"Edna",
    "img":'razor.jpg',
    "ativo":False,
    "x":3000,
    "y":3000
    
    },
    {
    
    "nivel":2,
    "agilidade":60,
    "vida":2800,
    "vidaM":2800,
    "img":"razor.jpg",
    "ataque":300,
    "velocidade":50,
    "elemento1":"metal",
    "nome":"Pedro",
    "img":'razor.jpg',
    "ativo":False,
    "x":3000,
    "y":3000
    
    },
    {
     
    "nivel":2,
    "agilidade":60,
    "vida":2800,
    "vidaM":2800,
    "img":"razor.jpg",
    "ataque":500,
    "velocidade":50,
    "elemento1":"vento",
    "nome":"Indiano vingativo",
    "img":'razor.jpg',
    "ativo":False,
    "x":3000,
    "y":3000
    
    },
    {
    
    "nivel":2,
    "agilidade":60,
    "vida":2800,
    "vidaM":2800,
    "img":"razor.jpg",
    "ataque":800,
    "velocidade":50,
    "elemento1":"eletro",
    "nome":"inimigo8",
    "img":'razor.jpg',
    "ativo":False,
    "x":3000,
    "y":3000
    
    },
    {
     
    "nivel":2,
    "agilidade":60,
    "vida":2800,
    "vidaM":2800,
    "img":"razor.jpg",
    "ataque":800,
    "velocidade":50,
    "elemento1":"eletro",
    "nome":"inimigo9",
    "img":'razor.jpg',
    "ativo":False,
    "x":3000,
    "y":3000
    
    },
    {
     
    "nivel":2,
    "agilidade":60,
    "vida":2800,
    "vidaM":2800,
    "img":"razor.jpg",
    "ataque":800,
    "velocidade":50,
    "elemento1":"eletro",
    "nome":"inimigo10",
    "img":'razor.jpg',
    "ativo":False,
    "x":3000,
    "y":3000
    
    },
    ]

running = True
world=False
menu=True
clock = pygame.time.Clock()

def maps(level,mundo,inimigos,inimigo):
    
    level_maps=[]
    if mundo==1:
        
               
                
        if level==0:
            for i in inimigos:
                i["vida"]=i["vidaM"]
            
            level_maps = [
                        "2222222223332222222222222",
                        "2222222220002222222222223",
                        "2022000000000000020000003",
                        "2022000000000000020000003",
                        "2022000000000000020000003",
                        "2022000000000000020000003",
                        "2022000000000000020000003",
                        "2022000000000000020000003",
                        "2022000000000000020000003",
                        "2022000000000000020000003",
                        "2022000000000000020000003",
                        "2222222222222222222222202",
                    ]
            for i in inimigos:
                i["x"]=750
                i["y"]=350
                i["ativo"]=False
            
        elif level==1:
                level_maps = [
                            "2222222223332222222222222",
                            "3002222220002222220000000",
                            "3002000000000000020000000",
                            "3002050000000008020000000",
                            "3002000000000000020000000",
                            "3002060000000007020000000",
                            "3002000000000000020000000",
                            "3002050000000008020000000",
                            "3002000000000000020000000",
                            "3002060000000007020000000",
                            "3002000000000000020000000",
                            "2222223333222222222222222",       
                        ]
                for i in inimigos:
                    i["x"]=750
                    i["y"]=350
                    i["ativo"]=False
                if inimigos[1]["vida"]>0:
                    inimigos[1]["x"]=360
                    inimigos[1]["y"]=500
                    inimigos[1]["ativo"]=True
                if inimigos[0]["vida"]>0:
                    inimigos[0]["x"]=360
                    inimigos[0]["y"]=250
                    inimigos[0]["ativo"]=True 
        elif level==2:
                level_maps = [
                            "2222222223332222222222222",
                            "3002222220002222220000000",
                            "3002050805080508020000000",
                            "3002000000000000020000000",
                            "3002000000000000020000000",
                            "3002000000000000020000000",
                            "3002000000000000020000000",
                            "3002000000000000020000000",
                            "3002000000000000020000000",
                            "3002060706070607020000000",
                            "3002000000000000020000000",
                            "2222223333222222222222222",       
                        ]
                for i in inimigos:
                    i["x"]=750
                    i["y"]=350
                    i["ativo"]=False
                if inimigos[2]["vida"]>0:
                    inimigos[2]["x"]=360
                    inimigos[2]["y"]=250
                    inimigos[2]["ativo"]=True
                if inimigos[3]["vida"]>0:
                    inimigos[3]["x"]=600
                    inimigos[3]["y"]=250
                    inimigos[3]["ativo"]=True 
                if inimigos[4]["vida"]>0:
                    inimigos[4]["x"]=840
                    inimigos[4]["y"]=250
                    inimigos[4]["ativo"]=True
        elif level==3:
                level_maps = [
                            "2222222223332222222222222",
                            "3002222220002222220000000",
                            "3002050080050080020000000",
                            "3002000000000000020000000",
                            "3002000000000000020000000",
                            "3002060070060070020000000",
                            "3002050080050080020000000",
                            "3002000000000000020000000",
                            "3002000000000000020000000",
                            "3002060070060070020000000",
                            "3002000000000000020000000",
                            "2222223333222222222222222",       
                        ]
                for i in inimigos:
                    i["x"]=750
                    i["y"]=350
                    i["ativo"]=False
                if inimigos[5]["vida"]>0:
                    inimigos[5]["x"]=360
                    inimigos[5]["y"]=187.5
                    inimigos[5]["ativo"]=True
                if inimigos[6]["vida"]>0:
                    inimigos[6]["x"]=720
                    inimigos[6]["y"]=187.5
                    inimigos[6]["ativo"]=True
                if inimigos[7]["vida"]>0:
                    inimigos[7]["x"]=360
                    inimigos[7]["y"]=437.5
                    inimigos[7]["ativo"]=True
                if inimigos[8]["vida"]>0:
                    inimigos[8]["x"]=720
                    inimigos[8]["y"]=437.5
                    inimigos[8]["ativo"]=True
        
    if inimigo !=0:
        conter=0
        for i in inimigos:
            if inimigo["nome"]==i["nome"]:
                inimigos[conter]=inimigo
            else:
                conter+=1
    return level_maps,inimigos
        
def levels(mario_x,mario_y,level):
    mario_x=mario_x
   
    if level==0:
        level=1
        mario_x = 500
        mario_y = 630
    elif level==1 and mario_y>630:
        level=0
        mario_x = 670
        mario_y = 130
    elif level==1 and mario_y<100.5:
        level=2
        mario_x = 500
        mario_y = 630
    elif level==2 and mario_y>630:
        level=1
        mario_x = 670
        mario_y = 130
    elif level==2 and mario_y<100.5:
        level=3
        mario_x = 500
        mario_y = 630
    elif level==3 and mario_y>630:
        level=2
        mario_x = 670
        mario_y = 130
    elif level==3 and mario_y<100.5:
        level=0
        mario_x = 500
        mario_y = 630
    return level,int(mario_x), int(mario_y)
            
def moving(mario_x,mario_y,running,level,inimigos):
    estado=0
    conter=360
    conter2=360
    combate=False
    inimigo=0
    mario_img = pygame.image.load('vy_0 (2).png')
    level_maps,inimigos=maps(level,mundo,inimigos,inimigo)
    bg = pygame.image.load("background.png")
    left_key = right_key = up_key=down_key= False
    mario_vx = 0
    mario_vy = 0
    vx=0
    vy=0.7
    while running and world:
            conter2=conter2-1
            screen.blit(bg, (0, 0))
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        running = False
                    elif ev.key == pygame.K_LEFT or ev.key == pygame.K_a:
                        left_key = True
                        up_key = False
                        down_key = False
                    elif ev.key == pygame.K_RIGHT or ev.key == pygame.K_d:
                        right_key = True
                        up_key = False
                        down_key = False
                    elif ev.key == pygame.K_UP or ev.key == pygame.K_w:
                        up_key = True
                        left_key = False
                        right_key = False
                    elif ev.key == pygame.K_DOWN or ev.key == pygame.K_s:
                        down_key = True
                        left_key = False
                        right_key = False
                elif ev.type == pygame.KEYUP:
                    if ev.key == pygame.K_LEFT or ev.key == pygame.K_a:
                        left_key = False
                    elif ev.key == pygame.K_RIGHT  or ev.key == pygame.K_d:
                        right_key = False
                    elif ev.key == pygame.K_UP  or ev.key == pygame.K_w:
                        up_key = False
                    elif ev.key == pygame.K_DOWN  or ev.key == pygame.K_s:
                        down_key = False
            dt = clock.tick()
            if left_key :
                mario_vx = -0.5  
                if level_maps[int(mario_y/62.5)][int((mario_x-0.5)/62.5)]=="2":
                    mario_vx=0
                    #mario_x=mario_x+0.4
                if level_maps[int(mario_y/62.5)][int(mario_x/62.5)]=="3":
                    return mario_x,mario_y,running,level,combate,inimigo
            elif right_key  :
                mario_vx = +0.5
                if level_maps[int(mario_y/62.5)][int((mario_x+44+0.5)/62.5)]=="2":
                    mario_vx=-0
                    #mario_x= mario_x-0.4
                if level_maps[int(mario_y/62.5)][int((mario_x+44)/62.5)]=="3":
                    return mario_x,mario_y,running,level,combate,inimigo
            else:
                mario_vx = 0
            if up_key  :
                mario_vy= -0.5
                if level_maps[int((mario_y-35-0.5)/62.5)][int(mario_x/62.5)]=="2":
                    mario_vy=0
                    #mario_y=mario_y +0.4
                if level_maps[int((mario_y-35)/62.5)][int(mario_x/62.5)]=="3":
                    return mario_x,mario_y,running,level,combate,inimigo      
            elif down_key :
                mario_vy=+0.5
                if level_maps[int((mario_y+35+0.5)/62.5)][int(mario_x/62.5)]=="2":
                   # mario_y=mario_y -0.4
                    mario_vy=0
                if level_maps[int((mario_y+35)/62.5)][int(mario_x/62.5)]=="3":
                    return mario_x,mario_y,running,level,combate,inimigo
            else:
                mario_vy=0  
            if mario_vy>0:
                estado=3
                if conter<=360 and conter>270:
                    mario_img = pygame.image.load('vy_1 (2).png')
                    conter=conter-1
                elif conter<=270 and conter >180:
                    mario_img = pygame.image.load('vy_2 (2).png')
                    conter=conter-1
                elif conter<=180 and conter>90:
                    mario_img = pygame.image.load('vy_3 (2).png')
                    conter=conter-1
                elif conter<=90 and conter>0:
                    mario_img = pygame.image.load('vy_4 (2).png')
                    conter=conter-1
                elif conter<=0:
                    conter=360         
            elif mario_vy<0:
                estado=2
                if conter<=360 and conter>270:
                    mario_img = pygame.image.load('vy_5(2).png')
                    conter=conter-1
                elif conter<=270 and conter >180:
                    mario_img = pygame.image.load('vy_6 (2).png')
                    conter=conter-1
                elif conter<=180 and conter>90:
                    mario_img = pygame.image.load('vy_7 (2).png')
                    conter=conter-1
                elif conter<=90 and conter>0:
                    mario_img = pygame.image.load('vy_8 (2).png')
                    conter=conter-1
                elif conter<=0:
                    conter=360
            elif mario_vx<0:
                estado=1
                if conter<=360 and conter>270:
                    mario_img = pygame.image.load('vx_5 (2).png')
                    conter=conter-1
                elif conter<=270 and conter >180:
                    mario_img = pygame.image.load('vx_6 (2).png')
                    conter=conter-1
                elif conter<=180 and conter>90:
                    mario_img = pygame.image.load('vx_5 (2).png')
                    conter=conter-1
                elif conter<=90 and conter>0:
                    mario_img = pygame.image.load('vx_7 (2).png')
                    conter=conter-1
                elif conter<=0:
                    conter=360
            elif mario_vx>0:
                estado=0
                if conter<=360 and conter>270:
                    mario_img = pygame.image.load('vx_1 (2).png')
                    conter=conter-1
                elif conter<=270 and conter >180:
                    mario_img = pygame.image.load('vx_2 (2).png')
                    conter=conter-1
                elif conter<=180 and conter>90:
                    mario_img = pygame.image.load('vx_1 (2).png')
                    conter=conter-1
                elif conter<=90 and conter>0:
                    mario_img = pygame.image.load('vx_3 (2).png')
                    conter=conter-1
                elif conter<=0:
                    conter=360
            if mario_vx==0 and mario_vy==0:
                if estado==0:
                    mario_img = pygame.image.load('vx_1 (2).png')
                elif estado==1:
                    mario_img = pygame.image.load('vx_5 (2).png')
                elif estado==2:
                    mario_img = pygame.image.load('vy_0 (2).png')
                else:
                    mario_img = pygame.image.load('vy_9 (2).png')
            mario_x += mario_vx
            mario_y += mario_vy
            mario_img.set_colorkey((48, 120, 128))
            # x=0
            # y=0
            # e=pygame.image.load("razor.jpg")
            # for a in level_maps:
            #     y=y+1
            #     x=1
            #     for b in a:
            #         if b=="5" or b=="6" or b=="7" or b=="8":
            #             screen.blit(e,(x*60,y*62.5))
            #         x=x+1
            for i in inimigos:
                if i["ativo"]==True:
                     if level_maps[int((i["y"])/62.5)-1][int(i["x"]/60)-1]=="5":
                         vx=0
                         vy=0.7
                     if level_maps[int((i["y"])/62.5)-1][int(i["x"]/60)-1]=="6":
                         vx=0.7
                         vy=0
                     if level_maps[int((i["y"])/62.5)-1][int(i["x"]/60)-1]=="7":
                         vy=-0.7
                         vx=0
                     if level_maps[int((i["y"])/62.5)-1][int(i["x"]/60)-1]=="8":
                         vy=0
                         vx=-0.7
                     if vy>0:
                   
                        if conter2<=360 and conter2>270:
                            i["img"] = "ini_vy_0.png"
                            
                        elif conter2<=270 and conter2 >180:
                            i["img"] = "ini_vy_1 (2).png"
                            
                        elif conter2<=180 and conter2>90:
                            i["img"] = "ini_vy_0.png"
                            
                        elif conter2<=90 and conter2>0:
                            i["img"] = "ini_vy_2.png"
                            
                        elif conter2<=0:
                            conter2=360         
                     elif vy<0:
                        
                        if conter2<=360 and conter2>270:
                            i["img"] = "ini_vy_3.png"
                            
                        elif conter2<=270 and conter2 >180:
                            i["img"] = "ini_vy_4.png"
                            
                        elif conter2<=180 and conter2>90:
                            i["img"] = "ini_vy_5.png"
                            
                        elif conter2<=90 and conter2>0:
                            i["img"] = "ini_vy_4.png"
                            
                        elif conter2<=0:
                            conter2=360
                     elif vx<0:
                        
                        if conter2<=360 and conter2>270:
                            i["img"] = "ini_vx_0.png"
                            
                        elif conter2<=270 and conter2 >180:
                            i["img"] = "ini_vx_1.png"
                            
                        elif conter2<=180 and conter2>90:
                            i["img"] = "ini_vx_0.png"
                            
                        elif conter2<=90 and conter2>0:
                            i["img"] = "ini_vx_2.png"
                            
                        elif conter2<=0:
                            conter2=360
                     elif vx>0:
                        
                        if conter2<=360 and conter2>270:
                            i["img"] = "ini_vx_3.png"
                            
                        elif conter2<=270 and conter2 >180:
                            i["img"] = "ini_vx_4.png"
                            
                        elif conter2<=180 and conter2>90:
                            i["img"] ="ini_vx_3.png"
                            
                        elif conter2<=90 and conter2>0:
                            i["img"] = "ini_vx_5.png"
                            
                        elif conter2<=0:
                            conter2=360
                     i["y"]+=vy
                     i["x"]+=vx
                     enemy=pygame.image.load(i["img"])
                     enemy.set_colorkey((255, 255, 255))
                     screen.blit(enemy, (i["x"],i["y"])) 
                     condi1=int(mario_y/62.5)==int(i["y"]/62.5)and int(mario_x/62.5)==int(i["x"]/62.5) and i["ativo"]==True
                     condi2=int((mario_y-35)/62.5)==int(i["y"]/62.5)and int(mario_x/62.5)==int(i["x"]/62.5) and i["ativo"]==True
                     condi3=int((mario_y)/62.5)==int((i["y"]-35)/62.5)and int(mario_x/62.5)==int(i["x"]/62.5) and i["ativo"]==True
                     if condi1 or condi2 or condi3:
                        combate=True
                        i["ativo"]==False
                        i["img"]="ini_ini.png"
                        return mario_x,mario_y,running,level,combate,i
            screen.blit(mario_img, (int(mario_x), int(mario_y)))
            pygame.display.flip()
    return mario_x,mario_y,running,level,combate,inimigo

def menu_inicial(menu,world,running):
    white = (255, 255, 255)
    black=(0,0,0)
    grey=(125,125,125)
    font = pygame.font.Font('freesansbold.ttf', 120)
    font2= pygame.font.Font('freesansbold.ttf', 60)
    text = font.render('Tales of Leic', True, white)
    text2=font2.render('   Play   ', True, white,grey)
    text3=font2.render('   Quit   ', True, white)
    text2Rect=text2.get_rect()
    text3Rect=text3.get_rect()
    textRect = text.get_rect()
    textRect.center = (750,175)
    text2Rect.center = (500,600)
    text3Rect.center = (1100,600)
    op=1
    while menu:
        screen.fill(black)
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
        screen.blit(text3, text3Rect)
        for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_LEFT:
                         text2=font2.render('    Play    ', True, white,grey)
                         text3=font2.render('    Quit    ', True, white)
                         op=1
                    elif ev.key == pygame.K_RIGHT:
                         text2=font2.render('    Play    ', True, white)
                         text3=font2.render('    Quit    ', True, white,grey)
                         op=0
                    elif ev.key == pygame.K_ESCAPE:
                        menu=False
                        world=True
                    elif ev.key == pygame.K_RETURN:
                        if op==0:
                            menu=False
                            running=False
                            world=False
                        elif op==1:
                            menu=False
                            world=True
        pygame.display.flip()
    return menu,world,running
   
def esquema(player,inimigo):
        op=1
        bg = pygame.image.load("bg.jpg")#
        screen.blit(bg, (0, 0))
        mario_img = pygame.image.load(player["img"])
        inimigo_img= pygame.image.load(inimigo["img"])
        screen.blit(mario_img, (740, 330))
        pygame.font
        screen.blit(inimigo_img, (740, 150))
        font= pygame.font.Font('freesansbold.ttf', 180)
        fontb=pygame.font.Font('freesansbold.ttf', 193)
        fontt=pygame.font.Font('freesansbold.ttf', 17)
        fontbutton=pygame.font.Font('freesansbold.ttf', 47)
        fontbuttonb=pygame.font.Font('freesansbold.ttf', 53)
        white=(255,255,255)
        black=(0,0,0)
        grey=(200,200,200)
        darkgrey=(125,125,125)
        red=(250,0,0)
        lighter_blue=(0,250,250)
        light_blue=(0,213,213)
        blue=(0,150,250)
        brown=(173,89,42)
        green=(0,250,113)
        yellow=(250,200,0)
        respetivas_cores={
            "fogo":red,
            "vento":light_blue,
            "gelo":lighter_blue,
            "natureza":green,
            "pedra":brown,
            "metal":darkgrey,
            "agua":blue,
            "eletro":yellow
            }
        el=f"  {inimigo['elemento1']}  "
        elemento=fontt.render(el,True,white,respetivas_cores[inimigo["elemento1"]])
        button=fontbutton.render("          ",True,white,grey)
        buttons=fontbutton.render("          ",True,white,white)
        buttonb=fontbuttonb.render("         ",True,white,black)
        texto=esqueleto = fontt.render('texto', True, black)
        esqueleto = font.render('                ', True, grey,grey)
        borda=fontb.render('               ', True, black,black)
        nome_player= fontt.render(player["nome"], True, black)
        nome_inimigo= fontt.render(inimigo["nome"], True, black)
        nome_playerRect=nome_player.get_rect()
        nome_inimigoRect=nome_inimigo.get_rect()
        bordaRect=borda.get_rect()
        esqueletoRect=esqueleto.get_rect()
        textoRect=texto.get_rect()
        buttonRect=button.get_rect()
        buttonsRect=buttons.get_rect()
        buttonbRect=buttonb.get_rect()
        elementoRect=elemento.get_rect()
        elementoRect.center=(860,150)
        nome_playerRect.center=(420+3.5*len(player["nome"]),713)
        nome_inimigoRect.center=(750,50)
        esqueletoRect.center = (747,648)
        bordaRect.center = (747,648)
        textoRect.center=(390,600)
        screen.blit(borda, bordaRect)
        screen.blit(esqueleto, esqueletoRect)
        screen.blit(nome_player,nome_playerRect)
        screen.blit(nome_inimigo,nome_inimigoRect)
        for i in range(4): 
            if i==0:
                button=fontbutton.render("         ",True,white,respetivas_cores[player["elemento1"]])
            if i==1:
                button=fontbutton.render("         ",True,white,respetivas_cores[player["elemento2"]])
            else:
                buttonb=fontbuttonb.render("         ",True,white,black)
            buttonbRect.center=(i*180+480,610)
            screen.blit(buttonb,buttonbRect)
            buttonRect.center=(i*180+480,610)
            screen.blit(button,buttonRect)   
        if op==1:
                buttonsRect.center=(0*180+480,610)
                screen.blit(buttons,buttonsRect)
        if op==2:
                buttonsRect.center=(1*180+480,610)
                screen.blit(buttons,buttonsRect)
        if op==3:
                buttonsRect.center=(2*180+480,610)
                screen.blit(buttons,buttonsRect)
        if op==4:
                buttonsRect.center=(3*180+480,610)
                screen.blit(buttons,buttonsRect)
        barra_de_vida(player,inimigo)
        screen.blit(elemento,elementoRect)
        
        pygame.display.flip()
        
def chossing(chossing):
        chossing=True
        fontbutton=pygame.font.Font('freesansbold.ttf', 47)
        fontbuttonb=pygame.font.Font('freesansbold.ttf', 53)
        fontbtext=pygame.font.Font('freesansbold.ttf', 13)
        white=(255,255,255)
        black=(0,0,0)
        grey=(200,200,200)
        darkgrey=(125,125,125)
        button=fontbutton.render("          ",True,white,grey)
        buttons=fontbutton.render("          ",True,white,white)
        buttonb=fontbuttonb.render("         ",True,white,black)
        btext=fontbtext.render(player["elemento1"],True,black)
        btextRect=btext.get_rect() 
        buttonRect=button.get_rect()
        buttonsRect=buttons.get_rect()
        buttonbRect=buttonb.get_rect()
        op=1
        white=(255,255,255)
        black=(0,0,0)
        grey=(200,200,200)
        darkgrey=(125,125,125)
        red=(250,0,0)
        lighter_blue=(0,250,250)
        light_blue=(0,213,213)
        blue=(0,150,250)
        brown=(173,89,42)
        green=(0,250,113)
        yellow=(250,200,0)
        respetivas_cores={
            "fogo":red,
            "vento":light_blue,
            "gelo":lighter_blue,
            "natureza":green,
            "pedra":brown,
            "metal":darkgrey,
            "agua":blue,
            "eletro":yellow
            }
        while chossing:  
            if op<1:
                op=1
            elif op>4 and op<10:
                op=4
            for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        running = False
                    elif ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_LEFT:    
                             op=op-1
                        elif ev.key == pygame.K_RIGHT:       
                             op=op+1
                        elif ev.key == pygame.K_DOWN:
                             op=10
                        elif ev.key == pygame.K_UP:
                             op=1
                        elif ev.key == pygame.K_RETURN:
                             chossing=False
                        elif ev.key == pygame.K_ESCAPE:
                             chossing=False               
            for i in range(4): 
                if i==0:
                    button=fontbutton.render("          ",True,white,respetivas_cores[player["elemento1"]])
                    btext=fontbtext.render(player["elemento1"],True,black)
                if i==1:
                    button=fontbutton.render("          ",True,white,respetivas_cores[player["elemento2"]])
                    btext=fontbtext.render(player["elemento2"],True,black)
                elif i==2:
                    button=fontbutton.render("          ",True,white,grey)
                    btext=fontbtext.render("Espadas",True,black)
                elif i==3:
                    button=fontbutton.render("          ",True,white,grey)
                    btext=fontbtext.render("Escudo",True,black) 
                buttonbRect.center=(i*180+480,610)
                screen.blit(buttonb,buttonbRect)
                buttonRect.center=(i*180+480,610)
                screen.blit(button,buttonRect)  
                btextRect.center=(i*180+470,610) 
                screen.blit(btext,btextRect)
            if op==1:
                buttonsRect.center=(0*180+480,610)
                screen.blit(buttons,buttonsRect)
                btext=fontbtext.render(player["elemento1"],True,black)
                btextRect.center=(0*180+480,610) 
                screen.blit(btext,btextRect)
            if op==2:
                button=fontbutton.render("          ",True,white,respetivas_cores[player["elemento1"]])
                buttonRect.center=(0*180+480,610)
                screen.blit(button,buttonRect)
                buttonsRect.center=(1*180+480,610)
                screen.blit(buttons,buttonsRect)
                btext=fontbtext.render(player["elemento1"],True,black)
                btextRect.center=(0*180+480,610) 
                screen.blit(btext,btextRect)
                btext=fontbtext.render(player["elemento2"],True,black)
                btextRect.center=(1*180+470,610) 
                screen.blit(btext,btextRect)
            if op==3:
                button=fontbutton.render("          ",True,white,respetivas_cores[player["elemento1"]])
                buttonRect.center=(0*180+480,610)
                screen.blit(button,buttonRect)
                buttonsRect.center=(2*180+480,610)
                screen.blit(buttons,buttonsRect)
                btext=fontbtext.render(player["elemento1"],True,black)
                btextRect.center=(0*180+480,610) 
                screen.blit(btext,btextRect)
                btext=fontbtext.render("Espadas",True,black)
                btextRect.center=(2*180+470,610) 
                screen.blit(btext,btextRect)
            if op==4:
                button=fontbutton.render("          ",True,white,respetivas_cores[player["elemento1"]])
                buttonRect.center=(0*180+480,610)
                screen.blit(button,buttonRect)
                buttonsRect.center=(3*180+480,610)
                screen.blit(buttons,buttonsRect)
                btext=fontbtext.render(player["elemento1"],True,black)
                btextRect.center=(0*180+480,610) 
                screen.blit(btext,btextRect)
                btext=fontbtext.render("Escudo",True,black)
                btextRect.center=(3*180+470,610) 
                screen.blit(btext,btextRect)
            pygame.display.flip()
        return op                    
        
def fcritico(player,inimigo,op):
    critico=1
    if op==1:
        if inimigo["elemento1"]=="eletro":
            critico=2
        elif inimigo["elemento1"]=="pedra":
            critico=0.5
        elif inimigo["elemento1"]=="vento":
            critico=0
    elif op==4:
        critico=0 
    elif op==2:
        if player["elemento2"]=="fogo":
            if inimigo["elemento1"]=="metal":
                critico=2
            elif inimigo["elemento1"]=="natureza":
                critico=2
            elif inimigo["elemento1"]=="gelo":
                critico=2
            elif inimigo["elemento1"]=="agua":
                critico=0.5
            elif inimigo["elemento1"]=="pedra":
                critico=0.5
            elif inimigo["elemento1"]=="fogo":
                critico=0   
        elif player["elemento2"]=="natureza":
            if inimigo["elemento1"]=="pedra":
                critico=2
            elif inimigo["elemento1"]=="agua":
                critico=2
            elif inimigo["elemento1"]=="fogo":
                critico=0.5
            elif inimigo["elemento1"]=="gelo":
                critico=0.5
            elif inimigo["elemento1"]=="natureza":
                critico=0
        elif player["elemento2"]=="pedra":
            if inimigo["elemento1"]=="gelo":
                critico=2
            elif inimigo["elemento1"]=="eletro":
                critico=2
            elif inimigo["elemento1"]=="metal":
                critico=0.5
            elif inimigo["elemento1"]=="agua":
                critico=0.5
            elif inimigo["elemento1"]=="pedra":
                critico=0  
        elif player["elemento2"]=="metal":
            if inimigo["elemento1"]=="pedra":
                critico=2
            elif inimigo["elemento1"]=="gelo":
                critico=2
            elif inimigo["elemento1"]=="fogo":
                critico=0.5
            elif inimigo["elemento1"]=="eletro":
                critico=0.5
            elif inimigo["elemento1"]=="metal":
                critico=0   
        elif player["elemento2"]=="gelo":
            if inimigo["elemento1"]=="natureza":
                critico=2
            elif inimigo["elemento1"]=="agua":
                critico=2
            elif inimigo["elemento1"]=="fogo":
                critico=0.5
            elif inimigo["elemento1"]=="pedra":
                critico=0.5
            elif inimigo["elemento1"]=="metal":
                critico=0.5
            elif inimigo["elemento1"]=="gelo":
                critico=0
        elif player["elemento2"]=="agua":
            if inimigo["elemento1"]=="fogo":
                critico=2
            elif inimigo["elemento1"]=="pedra":
                critico=2
            elif inimigo["elemento1"]=="natureza":
                critico=0.5
            elif inimigo["elemento1"]=="gelo":
                critico=0.5
            elif inimigo["elemento1"]=="eletro":
                critico=0.5
            elif inimigo["elemento1"]=="agua":
                critico=0  
        elif player["elemento2"]=="eletro":
            if inimigo["elemento1"]=="metal":
                critico=2
            elif inimigo["elemento1"]=="agua":
                critico=2
            elif inimigo["elemento1"]=="pedra":
                critico=0.5
            elif inimigo["elemento1"]=="vento":
                critico=0.5
            elif inimigo["elemento1"]=="eletro":
                critico=0
    return critico

def barra_de_vida(player,inimigo):
    green=(0,213,0)
    yellow=(250,213,50)
    red=(213,0,0)
    corp=green
    cori=green
    percentagem_player=int((player["vida"]*50)/player["vidaM"])
    percentagem_inimigo=int((inimigo["vida"]*50)/inimigo["vidaM"])
    if percentagem_player<25 and percentagem_player>10:
        corp=yellow
    elif percentagem_player<=10:
        corp=red
    if percentagem_inimigo<25 and percentagem_inimigo>10:
        cori=yellow
    elif percentagem_inimigo<=10:
        cori=red
    font= pygame.font.Font('freesansbold.ttf', 20)
    barra_player=font.render(" "*percentagem_player,True,(0,0,0),corp)
    barra_inimigo=font.render(" "*percentagem_inimigo,True,green,cori)
    barra_playerR=barra_player.get_rect()
    barra_inimigoR=barra_inimigo.get_rect()
    barra_playerR.center=((413+3*percentagem_player),685)
    barra_inimigoR.center=(750,100)
    screen.blit(barra_player, barra_playerR)
    screen.blit(barra_inimigo, barra_inimigoR)  
    
def texto_luta(player,inimigo,op,critico,v,acu):
        bg = pygame.image.load("bg.jpg")
        screen.blit(bg, (0, 0))
        mario_img = pygame.image.load(player["img"])
        inimigo_img= pygame.image.load(inimigo["img"])
        screen.blit(mario_img, (740, 330))
        pygame.font
        screen.blit(inimigo_img, (740, 150))
        font= pygame.font.Font('freesansbold.ttf', 180)
        fontb=pygame.font.Font('freesansbold.ttf', 193)
        fontt=pygame.font.Font('freesansbold.ttf', 17)
        texto=''
        black=(0,0,0)
        grey=(200,200,200)
        nome_player= fontt.render(player["nome"], True, black)
        nome_inimigo= fontt.render(inimigo["nome"], True, black)
        texto1=esqueleto = fontt.render(texto, True, black,grey)
        esqueleto = font.render('                ', True, grey,grey)
        borda=fontb.render('               ', True, black,black)
        nome_playerRect=nome_player.get_rect()
        nome_inimigoRect=nome_inimigo.get_rect()
        bordaRect=borda.get_rect()
        esqueletoRect=esqueleto.get_rect()
        textoRect=texto1.get_rect()
        nome_playerRect.center=(420+3.5*len(player["nome"]),713)
        nome_inimigoRect.center=(750,50)
        esqueletoRect.center = (747,648)
        bordaRect.center = (747,648)
        textoRect.center=(413,600)
        screen.blit(borda, bordaRect)
        screen.blit(esqueleto, esqueletoRect)
        barra_de_vida(player,inimigo)
        screen.blit(nome_player,nome_playerRect)
        screen.blit(nome_inimigo,nome_inimigoRect)
        if v==0:
            if op==1:
                texto=f"{player['nome']} usou {player['elemento1']}!"
            elif op==2:
                texto=f"{player['nome']} usou {player['elemento2']}!"
            elif op==3:
                texto=f"{player['nome']} usou Espadas!"
            elif op==4:
                texto=f"{player['nome']} usou Escudo!"
            texto1=esqueleto = fontt.render(texto, True, black)
            screen.blit(texto1, textoRect)
            pygame.display.flip()
            pygame.time.wait(800)
            if acu==1.5:
                texto="                                                       "
                texto1=esqueleto = fontt.render(texto, True, black,grey)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                texto=f"{player['nome']} acertou um critico!"
                texto1=fontt.render(texto, True, black)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                pygame.time.wait(800)
            elif acu==0.5:
                texto="                                                       "
                texto1=esqueleto = fontt.render(texto, True, black,grey)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                texto=f"{player['nome']} acertou de raspão!"
                texto1=esqueleto = fontt.render(texto, True, black)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                pygame.time.wait(800)
            elif acu==0:
                texto="                                                       "
                texto1=esqueleto = fontt.render(texto, True, black,grey)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                texto=f"{player['nome']} falhou!"
                texto1=esqueleto = fontt.render(texto, True, black)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                pygame.time.wait(800)
            if critico==2 and acu!=0:
                texto="                                                       "
                texto1=esqueleto = fontt.render(texto, True, black,grey)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                texto="O ataque é super eficaz!"
                texto1=esqueleto = fontt.render(texto, True, black)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                pygame.time.wait(800)
            elif critico==0.5 and acu!=0:
                texto="                                                       "
                texto1=esqueleto = fontt.render(texto, True, black,grey)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                texto="O ataque é pouco eficaz!"
                texto1=esqueleto = fontt.render(texto, True, black)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                pygame.time.wait(800)
            elif critico==0 and op!=4 and acu!=0:
                texto="                                                       "
                texto1=esqueleto = fontt.render(texto, True, black,grey)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                texto="O ataque não tem efeito!"
                texto1=esqueleto = fontt.render(texto, True, black)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                pygame.time.wait(800)
        elif v==1:
            texto=f"{inimigo['nome']} usou {inimigo['elemento1']}!"
            texto1=esqueleto = fontt.render(texto, True, black)
            screen.blit(texto1, textoRect)
            pygame.display.flip()
            pygame.time.wait(800)
        elif v==3:
            texto=f"{player['nome']} morreu!"
            texto1= fontt.render(texto, True, black)
            screen.blit(texto1, textoRect)
            pygame.display.flip()
            pygame.time.wait(800)
            
        elif v==2:
            texto=f"{inimigo['nome']} morreu!"
            texto1=esqueleto = fontt.render(texto, True, black)
            screen.blit(texto1, textoRect)
            pygame.display.flip()
            pygame.time.wait(800)
        pygame.display.flip()
        barra_de_vida(player,inimigo)
        pygame.display.flip()
            
def minigame1(player,inimigo):
        running=True
        font= pygame.font.Font('freesansbold.ttf', 180)
        fontb=pygame.font.Font('freesansbold.ttf', 180)
        fontt=pygame.font.Font('freesansbold.ttf', 17)
        ag=inimigo["agilidade"]/ player["agilidade"]
        if ag>2.4:
            ag=2.4
        elif ag<1:
            ag=1
        vx=5*ag
        x=747
        while running:
            font= pygame.font.Font('freesansbold.ttf', 180)
            fontb=pygame.font.Font('freesansbold.ttf', 180)
            fontt=pygame.font.Font('freesansbold.ttf', 17)
            white=(255,255,255)
            black=(0,0,0)
            grey=(200,200,200)
            red=(250,0,0)
            green=(0,250,113)
            yellow=(250,200,0)
            texto=esqueleto = fontt.render('texto', True, black)
            esqueleto = font.render('                ', True, grey,grey)
            borda=fontb.render('               ', True, black,black)
            camada=font.render('                ', True, grey,black)
            camadaR=camada.get_rect()
            camadaR.center=(747,648)
            bordaRect=borda.get_rect()
            esqueletoRect=esqueleto.get_rect()
            textoRect=texto.get_rect()
            esqueletoRect.center = (747,648)
            bordaRect.center = (747,648)
            textoRect.center=(390,600)
            screen.blit(borda, bordaRect)
            screen.blit(camada, camadaR)
            camada=font.render('            ', True, grey,red)
            camadaR.center=(847,648)
            screen.blit(camada, camadaR)
            camada=font.render('        ', True, grey,yellow)
            camadaR.center=(947,648)
            screen.blit(camada, camadaR)
            camada=font.render('  ', True, grey,green)
            camadaR.center=(1097,648)
            screen.blit(camada, camadaR)
            if x>=747 and x<=1497:
                vx=vx
            else:
                vx=-vx
            x=x+vx
            camada=font.render('|', True, white)
            camadaR.center=(x,648)
            screen.blit(camada, camadaR)
            pygame.display.flip()
            for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        running = False
                    elif ev.type == pygame.KEYDOWN:    
                        if ev.key == pygame.K_SPACE or ev.key == pygame.K_RETURN:
                             running=False
                        elif ev.key == pygame.K_ESCAPE:        
                             running=False
        if x>=1097 and x<=1197:
            return 1.5
        elif x>=947 and x<=1347:
            return 1
        elif x>= 847 and x<=1447:
            return 0.5
        else:
            return 0

def minigame2(player,inimigo):
        t=400
        running=True
        teclas=[]
        power=0
        white=(255,255,255)
        black=(0,0,0)
        grey=(200,200,200)
        red=(250,0,0)
        green=(0,250,113)
        yellow=(250,200,0)
        font= pygame.font.Font('freesansbold.ttf', 180)
        fontb=pygame.font.Font('freesansbold.ttf', 193)
        fontt=pygame.font.Font('freesansbold.ttf', 17)
        fontbutton=pygame.font.Font('freesansbold.ttf', 47)
        fontbuttonb=pygame.font.Font('freesansbold.ttf', 53)
        fontt=pygame.font.Font('freesansbold.ttf', 17)
        fontimer=pygame.font.Font('freesansbold.ttf', 7)
        button=fontbutton.render("       ",True,white,grey)
        buttonb=fontbuttonb.render("       ",True,white,black)
        texto= fontt.render('texto', True, black)
        timer=fontimer.render(' '*t, True, black,green)
        white=(255,255,255)
        black=(0,0,0)
        grey=(200,200,200)
        red=(250,0,0)
        green=(0,250,113)
        yellow=(250,200,0)
        esqueleto = font.render('                ', True, grey,grey)
        borda=fontb.render('               ', True, black,black)
        textoRect=texto.get_rect()
        timeRect=timer.get_rect()
        bordaRect=borda.get_rect()
        esqueletoRect=esqueleto.get_rect()
        esqueletoRect.center = (747,648)
        bordaRect.center = (747,648)
        textoRect.center=(390,600)
        timeRect.center=(747,562)
        screen.blit(borda, bordaRect)
        screen.blit(esqueleto, esqueletoRect)
        screen.blit(timer, timeRect)
        buttonRect=button.get_rect()
        buttonbRect=buttonb.get_rect()
        comandos={ "A":pygame.K_a,"B":pygame.K_b,"C":pygame.K_c,"D":pygame.K_d,"E":pygame.K_e,
                  "F":pygame.K_f,"G":pygame.K_g,"H":pygame.K_h,"I":pygame.K_i,"J":pygame.K_j,
                  "K":pygame.K_k,"L":pygame.K_l,"M":pygame.K_m,"N":pygame.K_n,"O":pygame.K_o,
                  "P":pygame.K_p,"Q":pygame.K_q,"R":pygame.K_r,"S":pygame.K_s,"T":pygame.K_t,
                  "U":pygame.K_u,"V":pygame.K_v,"W":pygame.K_w,"X":pygame.K_x,"Y":pygame.K_y,
                  "Z":pygame.K_z
            }
        letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for i in range(5):
            buttonbRect.center=(i*140+465,640)
            screen.blit(buttonb,buttonbRect)
            buttonRect.center=(i*140+465,640)
            screen.blit(button,buttonRect)
            n=int(random.random() *25)
            texto= fontt.render(letras[n], True, black)
            teclas.append(letras[n])
            textoRect.center=(i*139+480,640)
            screen.blit(texto,textoRect) 
        pygame.display.flip()
        x=inimigo["agilidade"]/ player["agilidade"]
        if x>2:
            x=2
        elif x<1:
            x=1
        while running:
            timer=fontimer.render(' '*400, True, black,grey)
            screen.blit(timer, timeRect)
            t=t-0.13*x
            if t<=0:
                running=False
            if t>200:
                timer=fontimer.render(' '*int(t), True, black,green)
            elif t>50:
                timer=fontimer.render(' '*int(t), True, black,yellow)
            else:
                timer=fontimer.render(' '*int(t), True, black,red)   
            screen.blit(timer, timeRect)       
            pygame.display.flip()
            for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        running = False
                    elif ev.type == pygame.KEYDOWN:   
                        if ev.key == comandos[teclas[0]] and power==0:
                              power=0.5
                              buttonRect.center=(0*140+465,640)
                              button=fontbutton.render("       ",True,white,green)
                              screen.blit(button,buttonRect)
                              texto= fontt.render(teclas[0], True, black)
                              textoRect.center=(0*139+480,640)
                              screen.blit(texto,textoRect)
                        elif ev.key == comandos[teclas[1]] and power==0.5:
                             power=0.75
                             buttonRect.center=(1*140+465,640)
                             button=fontbutton.render("       ",True,white,green)
                             screen.blit(button,buttonRect)
                             texto= fontt.render(teclas[1], True, black)
                             textoRect.center=(1*139+480,640)
                             screen.blit(texto,textoRect)
                        elif ev.key == comandos[teclas[2]] and power==0.75:
                              power=1
                              buttonRect.center=(2*140+465,640)
                              button=fontbutton.render("       ",True,white,green)
                              screen.blit(button,buttonRect)
                              texto= fontt.render(teclas[2], True, black)
                              textoRect.center=(2*139+480,640)
                              screen.blit(texto,textoRect)
                        elif ev.key == comandos[teclas[3]] and power==1:
                              power=1.25
                              buttonRect.center=(3*140+465,640)
                              button=fontbutton.render("       ",True,white,green)
                              screen.blit(button,buttonRect)
                              texto= fontt.render(teclas[3], True, black)
                              textoRect.center=(3*139+480,640)
                              screen.blit(texto,textoRect)
                        elif ev.key == comandos[teclas[4]] and power==1.25:
                              power=1.5
                              buttonRect.center=(4*140+465,640)
                              button=fontbutton.render("       ",True,white,green)
                              screen.blit(button,buttonRect)
                              texto= fontt.render(teclas[4], True, black)
                              textoRect.center=(4*139+480,640)
                              screen.blit(texto,textoRect)
                              running=False
        pygame.display.flip()   
        return power       
                
def combat(player,inimigo):
    running=True
    inimigo["img"]=="ini_ini.png"
    while player["vida"]>0 and inimigo["vida"]>0:
        defendido=False
        power=1
        esquema(player,inimigo)
        op=chossing(chossing)
        critico=fcritico(player, inimigo,op)
        if op==1 or op==2:
            power=minigame2(player,inimigo)
            acu=minigame1(player,inimigo)
        if op==3:
            acu=minigame1(player,inimigo)
        if op==4:
            acu=minigame1(player,inimigo)
            if acu==1.5:
                defendido=True
            else:
                acu=0   
        if op!=4:
            if player["velocidade"]>=inimigo["velocidade"]:
                inimigo["vida"]=inimigo["vida"]-int(player["ataque"]*critico*acu*power)    
                texto_luta(player,inimigo,op,critico,0,acu)
                pygame.time.wait(500)    
                if inimigo["vida"]>0:
                    player["vida"]=player["vida"]-int(inimigo["ataque"])
                    texto_luta(player,inimigo,op,critico,1,acu)
                    pygame.time.wait(500)
                    if player["vida"]<0:
                        texto_luta(player,inimigo,op,critico,3,acu)   
                        running=False
                else:
                    inimigo["vida"]=0
                    texto_luta(player,inimigo,op,critico,2,acu)
            else:
                player["vida"]=player["vida"]-int(inimigo["ataque"])
                texto_luta(player,inimigo,op,critico,1,acu)
                pygame.time.wait(500)  
                if player["vida"]>0:
                     inimigo["vida"]=inimigo["vida"]-int(player["ataque"]*critico*acu*power)
                     texto_luta(player,inimigo,op,critico,0,acu)
                     pygame.time.wait(500)  
                     barra_de_vida(player,inimigo)
                     if inimigo["vida"]<0:
                        texto_luta(player,inimigo,op,critico,2,acu)      
                else:    
                    player["vida"]=0
                    texto_luta(player,inimigo,op,critico,3,acu)   
        else:
            fontt=pygame.font.Font('freesansbold.ttf', 17)
            black=(0,0,0)
            grey=(200,200,200)
            texto="                                                       "
            texto1= fontt.render(texto, True, black,grey)
            textoRect=texto1.get_rect()
            textoRect.center=(550,600)
            if defendido:
                texto_luta(player,inimigo,op,critico,1,acu)
                pygame.time.wait(500)
                texto="                                                       "
                texto1= fontt.render(texto, True, black,grey)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                texto=f"O ataque foi defendido! "
                texto1=fontt.render(texto, True, black)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                pygame.time.wait(800)
                texto="                                                       "
                texto1= fontt.render(texto, True, black,grey)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                texto=f"{player['nome']} pode contra-atacar! "
                texto1=fontt.render(texto, True, black)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                pygame.time.wait(800)
                esquema(player,inimigo)
                while op==4:
                    op=chossing(chossing)
                critico=fcritico(player, inimigo,op)
                if op==1 or op==2:
                    power=minigame2(player,inimigo)
                    acu=minigame1(player,inimigo)
                if op==3:
                        acu=minigame1(player,inimigo)
                inimigo["vida"]=inimigo["vida"]-int(player["ataque"]*critico*acu*power)    
                texto_luta(player,inimigo,op,critico,0,acu)
                pygame.time.wait(500)
                if player["vida"]<0:
                        texto_luta(player,inimigo,op,critico,3,acu)
            else:
                texto_luta(player,inimigo,op,critico,1,acu)
                pygame.time.wait(500)
                texto="                                                       "
                texto1= fontt.render(texto, True, black,grey)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                texto=f"O ataque  não foi defendido! "
                texto1=fontt.render(texto, True, black)
                screen.blit(texto1, textoRect)
                pygame.display.flip()
                pygame.time.wait(800)
                player["vida"]=player["vida"]-int(inimigo["ataque"])
                texto_luta(player,inimigo,op,critico,1,acu)
                pygame.time.wait(500)
                if player["vida"]<=0:
                    player["vida"]=0
                    texto_luta(player,inimigo,op,critico,3,acu)            
    inimigo["ativo"]=False  
    inimigo["x"]=1560           
    return player,inimigo,running    

while running:  
    if world: 
       mario_x,mario_y,running,level,combate,inimigo= moving(mario_x,mario_y, running,level,inimigos)
       if running==True:
           if combate:
               player,inimigo,running=combat(player,inimigo)           
           else:
               level,mario_x,mario_y=levels(mario_x,mario_y,level)
               level_maps,inimigos=maps(level,mundo,inimigos,inimigo)
    if menu:
       menu,world,running=menu_inicial(menu,world,running)

pygame.quit()