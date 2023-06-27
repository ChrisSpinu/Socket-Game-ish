import socket
import _thread
import pickle

print('Enter ip:')
ip = input()

print('Enter port:')
port = input()

print('Enter maxplayers:')
maxplayers = input()

print('Starting server...')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,int(port)))
server.listen(5)
print('Server started successfully!')

players = []
positions = [0]

def threaded(connection, address):
    reply = ''
    while True:
        try:
            data = connection.recv(5120)
            reply = data.decode('utf-8')
            decodeReply1 = reply.strip('[')
            decodeReply2 = decodeReply1.strip(']')
            decodeReply = decodeReply2.split(',')

            if not data:
                print(f'Disconnected from {address}.')
                positions[playerInt] = positions[playerInt] = 0
                players.remove(connection)
                break
            else:
                print(f'Received from {address}, {reply}.')
                #print('0:',decodeReply[0])
                #print('1:',decodeReply[1])
                #print('2:',decodeReply[2])
                #print('3:',decodeReply[3])
                playerInt = int(decodeReply[3])
                playerZ = int(decodeReply[2])
                playerY = int(decodeReply[1])
                playerX = int(decodeReply[0])
                #print(playerInt)
                positions[playerInt] = f';{(playerX,playerY,playerZ,playerZ)};'
                #print('work1')
            connection.send(bytes(str(positions),'utf-8'))
        except:
            print(f'Error from: {address}, disconnected.')
            positions[playerInt] = positions[playerInt] = 0
            players.remove(connection)
            break
    print(f'Disconnected from {address}.')
    connection.close()
    
while True:
    if len(players) < int(maxplayers):
        Connection, Address = server.accept()
        print(f'Connection has been established from {Address}.')
        players.append(Connection)
        positions.append(0)
        Connection.send(bytes(str(len(players)),'utf-8'))
        _thread.start_new_thread(threaded,(Connection,Address))