import pyautogui as pg
def SaveinPaint():
    pg.moveTo(157,877,1)
    pg.click(157,877)
    pg.write('Paint')
    pg.press('enter',1,1)
    pg.keyDown('ctrl')
    pg.press('v')
    pg.keyUp('ctrl')
    pg.click(17,32,1)
    pg.moveTo(39,206,1)
    pg.click(39,206,1)
    pg.moveTo(858,224,1)
    pg.click(858,224,1)
    pg.write('C:\\Users\\USER\\Desktop\\chatbot')
    pg.press('enter',1,1)
    pg.moveTo(823,549,1)
    pg.click(823,549,1)
    pg.write('2')
    pg.moveTo(1095,621,1)
    pg.click(1095,621,1)
    pg.moveTo(848,438,1)
    pg.click(848,438,1)
    pg.moveTo(1567,14,1)
    pg.click(1567,14,1)


    
def screenshot():
    pg.press('prtscr')

def MapinfoOpen():
    pg.moveTo(157,877,0.5)
    pg.click(157,877)
    pg.write('Mapinfo')
    pg.press('enter',1,1)

def Mapclick():
    pg.click(221,38,1)

def findCoordinate(message):
    pg.click(344,112,1)
    pg.write(message)
    pg.press('enter',2,1)
    pg.moveTo(345,131,0.5)

def ZoomIN():
    Mapclick()
    pg.moveTo(448,68,0.5)
    pg.click(448,68,1)
    pg.moveTo(800,506,0.5)
    pg.click(800,506)
def ZoomOUT():
    Mapclick()
    pg.moveTo(491,71,0.5)
    pg.click(491,71,1)
    pg.moveTo(800,506,0.5)
    pg.click(800,506)

def Savecrop(file_name):
    pg.moveTo(157,877,0.5)
    pg.click(157,877)
    pg.write('Paint')
    pg.press('enter',1,1)  #important!!
    pg.keyDown('ctrl')
    pg.press('v')
    pg.keyUp('ctrl')
    pg.moveTo(1526,850,0.5)
    pg.click(1526,850,1)
    pg.press('left')
    pg.click(80,34,1)
    pg.moveTo(132,77,0.5)
    pg.click(132,77,1)
    pg.moveTo(8,126,0.5)
    pg.dragTo(804,482,0.5,button='left')
    pg.keyDown('ctrl')
    pg.press('c')
    pg.press('z')
    pg.press('v')
    pg.keyUp('ctrl')
    pg.moveTo(801,408)
    pg.dragTo(806,491,0.5,button='left')
    pg.click(17,32,1)
    pg.moveTo(39,206,0.5)
    pg.click(39,206,1)
    pg.moveTo(858,224,0.5)
    pg.click(858,224,1)
    pg.write('C:\\Users\\USER\\Desktop\\chatbot')
    pg.press('enter',1)
    pg.moveTo(823,549,0.5)
    pg.click(823,549,1)
    pg.write(file_name)
    pg.press('enter')
    pg.moveTo(848,438,0.5)
    pg.click(848,438,1)
    pg.moveTo(1567,14,0.5)
    pg.click(1567,14,1)

def Maptools():
    Mapclick()
    pg.click(814,77)

def GetSiteinfo(): 
    Maptools()
    pg.moveTo(246,161,1)
    pg.click(246,161)
    pg.moveTo(800,506,1) ##1215 FOR 4753 , 1216 FOR 0.4754KM   NOT A 100% ACCURACY!!
    pg.click(800,506)
    pg.moveTo(151,160,1)
    pg.click(151,160)

    

def initExplorer():
    pg.dragTo(312,236,2,button='left')
def initInfo():
    pg.dragTo(832,236,2,button='left')

def infoBegin():
    pg.moveTo(151,160,0.5)
    pg.click(151,160)
    pg.moveTo(125,184,0.5)
    pg.click(125,184,1)

def GetCellinfo(number):
    infoBegin()
    pg.moveTo(65,817)
    for i in range (0,number):
        pg.click(65,817)

def Savecellinfo1(file_name):
    screenshot()
    pg.moveTo(157,877,0.5)
    pg.click(157,877,1)
    pg.write('Paint')
    pg.press('enter',1,1)
    pg.keyDown('ctrl')
    pg.press('v')
    pg.keyUp('ctrl')
    pg.moveTo(1526,850,0.5)
    pg.click(1526,850,1)
    pg.press('left')
    pg.click(80,34,1)
    pg.moveTo(132,77,0.5)
    pg.click(132,77,1)
    pg.moveTo(9,141,0.5)
    pg.dragTo(328,482,1,button='left')
    pg.keyDown('ctrl')
    pg.press('c')
    pg.press('z')
    pg.press('v')
    pg.keyUp('ctrl')
    pg.moveTo(324,392,0.5)
    pg.dragTo(411,503,1,button='left')
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')
    pg.moveTo(1586,789,0.5)
    pg.click(1586,789,1)
    screenshot()
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')
    pg.keyDown('ctrl')
    pg.press('v')
    pg.keyUp('ctrl')
    pg.click(80,34,1)
    pg.moveTo(132,77,0.5)
    pg.click(132,77,1)
    pg.moveTo(9,141,0.5)
    pg.dragTo(328,482,1,button='left')
    pg.keyDown('ctrl')
    pg.press('c')
    pg.press('z')
    pg.press('v')
    pg.keyUp('ctrl')
    pg.moveTo(148,197,0.5)
    pg.dragTo(573,197,1,button='left')
    pg.moveTo(737,394,0.5)
    pg.dragTo(806,505,1,button='left')
    pg.click(17,32,1)
    pg.moveTo(39,206,0.5)
    pg.click(39,206,1)
    pg.moveTo(858,224,0.5)
    pg.click(858,224,1)
    pg.write('C:\\Users\\USER\\Desktop\\chatbot')
    pg.press('enter',1,1)
    pg.moveTo(823,549,0.5)
    pg.click(823,549,1)
    pg.write(file_name)
    pg.moveTo(1095,621,0.5)
    pg.click(1095,621,1)
    pg.moveTo(848,438,0.5)
    pg.click(848,438,1)
    pg.moveTo(1567,14,0.5)
    pg.click(1567,14,1)

    

def Savecellinfo():
    Savecellinfo1('info1')
    pg.moveTo(1586,789)
    pg.click(1586,789)
    Savecellinfo1('info2')
    endcellinfo()

def endcellinfo():
    pg.moveTo(103,816,0.5)
    pg.click(103,816)

def closeinfo():
    pg.moveTo(164,163,0.5)
    pg.click(164,163,button='right')
    pg.moveTo(200,378,0.5)
    pg.click(200,378)

def slide():
    pg.moveTo(412,80,0.5)
    pg.click(412,80)
    pg.moveTo(1588,484,0.5)
    pg.dragTo(15,484,2,button='left')

def initZoom():
    pg.moveTo(631,138)
    pg.click(631,138)
    pg.write('0.4754')
    pg.press('enter')

def Spatialclick():
    pg.moveTo(293,37)
    pg.click(293,37)

def Insertsymbol():
    pg.moveTo(914,110)
    pg.click(914,110)
    pg.moveTo(916,177,0.5)
    pg.click(916,177)
    pg.moveTo(800,506,0.5)
    pg.click(800,506)

def Selectsymbol():
    pg.moveTo(129,83)
    pg.click(129,83)
    pg.moveTo(800,506,0.5)
    pg.click(800,506,2)

def locateurself(longitude,latitude):
    pg.write(longitude)
    pg.press('tab')
    pg.write(latitude)
    pg.press('enter')

def Findsymbol():
    pg.moveTo(245,103)
    pg.click(245,103)
    pg.moveTo(219,138,0.5)
    pg.click(219,138)

def delsymbol():
    pg.press('del')

def Findmark():
    pg.moveTo(245,103,0.5)
    pg.click(245,103)
    pg.moveTo(211,294,0.5)
    pg.click(211,294)
    pg.moveTo(790,550)
    pg.click(790,550)

def Saveimage():
    pg.moveTo(366,34)
    pg.click(366,34)
    pg.moveTo(104,108,0.5)
    pg.click(104,108)
    pg.moveTo(106,307,0.5)
    pg.click(106,307) 

def Endinfo():
    closeinfo()
    ZoomOUT()
    ZoomOUT()
    slide()







##closeinfo()
##screenshot()
##SaveinPaint()
#closeinfo()
#initExplorer()
#initInfo()
##ZoomIN()
#Savecellinfo()
# ZoomIN()
#ZoomIN()
#GetSiteinfo()
#screenshot()
#Savecrop('map')









##Savecellinfo()
##Maptools()
##screenshot()
##Savecrop()

