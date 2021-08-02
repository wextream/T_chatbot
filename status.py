def Ok_status():
    f = open('status.txt','w',encoding='utf-8')
    f.write('Available')
    f.close()

def Not_ok_status():
    f = open('status.txt','w',encoding='utf-8')
    f.write('Unavailable')
    f.close()

def Read_status():
    f = open('status.txt','r',encoding='utf-8')
    m = ''
    for line in f:
        m+=line
    f.close()
    return m

