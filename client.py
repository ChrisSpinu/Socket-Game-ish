import pygame
import socket
import pickle

pygame.init()

print('Enter ip:')
ip = input()

print('Enter port:')
port = input()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip,int(port)))
player = int(server.recv(5120).decode('utf-8'))


x = 50
y = 50
z = 50
speed = 10
5
window = pygame.display.set_mode((1000,500))
windowColor = (255,255,255)

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    
    window.fill(windowColor)
    pygame.draw.rect(window,(0,255,0),[x,y,z,z])
    try:
        myPos = [x,y,z,player]
        server.send(bytes(str(myPos),'utf-8'))
        recvMsg = server.recv(5120)
        #rint(recvMsg.decode('utf-8'))
        a = recvMsg.decode('utf-8').strip('[()]')
        b = a.split(';')
        for i in range(0, len(b)):
            #print(b[i])
            c = b[i].strip('()')
            d = c.split(',')
            #print(d[0])
            try:
                pygame.draw.rect(window,(0,255,0),[int(d[0]),int(d[1]),int(d[2]),int(d[3])])
            except:
                pass
    except:
        pass

    pygame.display.update()

pygame.quit()
