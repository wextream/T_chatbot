import os

def Previous_Message():
    f = open('memory.txt','r',encoding='utf-8')
    m = ''
    for line in f:
        m+=line
    f.close()
    os.remove('memory.txt')
    return m

def New_Message(message):
    f = open('memory.txt','w',encoding='utf-8')
    f.write(message)
    f.close()

def Reset_memory():
    os.remove('memory.txt')
    f = open('memory.txt','w')
    f.write('')
    f.close()
