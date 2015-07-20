# Import necessary libraries
import socket

# Basic variables
server = "irc.freenode.net"
channel = "#Victorthewizard"
botnick = "Vics_Bot"
filename = "log.txt"
tolog = False

def ping():
    ircsock.send(bytes("PRIVMSG " + channel + " :GOT PINGED\n", "utf-8"))
    ircsock.send(bytes("PONG :Pong\n", "utf-8"))

def sendmsg(chan, message):
    ircsock.send(bytes("PRIVMSG " + chan + " :" + message + "\n", "utf-8"))

def joinchan(chan):
    ircsock.send(bytes("JOIN " + chan + "\n", "utf-8"))

def hello():
    ircsock.send(bytes("PRIVMSG " + channel + " :Testing out git!\n", "utf-8"))

if __name__ == '__main__':
    ircsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ircsock.connect((server, 6667))
    ircsock.send(bytes("USER " + botnick + " " + botnick + " " + botnick + " : Tut bot\n", "utf-8"))
    ircsock.send(bytes("NICK " + botnick + "\n", "utf-8"))
    joinchan(channel)

    while 1:
        ircmsg = ircsock.recv(2048)
        ircmsg = ircmsg.strip(bytes('\n\r', "utf-8"))
        print(ircmsg)
        
        if tolog:
            fo.write(ircmsg)
    
        if ircmsg.find(bytes(":Hello " + botnick, "utf-8")) != -1:
            hello()

        if ircmsg.find(bytes("PING :", "utf-8")) != -1:
            ping()

        if ircmsg.find(bytes(":!log", "utf-8")) != -1 and tolog == False:
            tolog = True
            fo = open(filename, "wb")

        if ircmsg.find(bytes(":!stoplog", "utf-8")) != -1 and tolog == True:
            fo.close()
            
