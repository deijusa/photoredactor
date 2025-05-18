#создай тут фоторедактор Easy Edit
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PIL import Image,ImageOps,ImageEnhance
import os




app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Easy Editor')
# main_win.resize(1920,1015)
# main_win.setGeometry(100,100,100,100)


layoutMAIN = QHBoxLayout()
layout1 = QVBoxLayout()
layout2 = QVBoxLayout()
layout3 = QHBoxLayout()

photo = QLabel('фотка')
# photo.resize(1600,1000)
listseach = QListWidget()
btnseach = QPushButton('Папка')
btnleft = QPushButton('влево')
btnright = QPushButton('вправо')
btnMirror = QPushButton('Отpзеркалить')
btnsharpness = QPushButton('резкость')
btnBW = QPushButton('Ч/Б')
BTN = QPushButton('Контрастность')


layout1.addWidget(btnseach)
layout1.addWidget(listseach)
layout2.addWidget(photo)
layout3.addWidget(btnleft)
layout3.addWidget(btnright)
layout3.addWidget(btnBW)
layout3.addWidget(btnMirror)
layout3.addWidget(btnsharpness)
layout3.addWidget(BTN)



layout2.addLayout(layout3)
layoutMAIN.addLayout(layout2,stretch=7)
layoutMAIN.addLayout(layout1, stretch= 1)


main_win.setLayout(layoutMAIN)
seach = ''
def chooseWorkdir():
    global seach
    seach = QFileDialog.getExistingDirectory()
    files = os.listdir(seach)
    # print (files)
    result = []
    for namefile in files:
        for exp in ['.jpg','.png','.jpeg','.svg','.gif']:
            if namefile.endswith(exp):
                result.append(namefile)
    listseach.clear()
    listseach.addItems(result)
# def photo():
#     pixmapimage = QPixmap()

class ImageProccesor():
    def __init__(self):
        self.photo=None
        self.filename=None
        self.dirphoto='PhotoImage'
    def do_bw(self):
        self.photo = self.photo.convert('L')
        self.savephoto()
        image_path = os.path.join(seach,self.dirphoto,self.filename)
        self.showImage(image_path)
    def showImage(self,path):
        pixmapimage = QPixmap(path)
        label_w , label_y = photo.width(),photo.height()
        scale_pixmap = pixmapimage.scaled(label_w,label_y,Qt.KeepAspectRatio)
        photo.setPixmap(scale_pixmap)
        photo.setVisible(True)
    # def do_bw(self):
    #     self.photo = self.photo.convert('L')
    #     self.savephoto('mr')
    #     image_path = os.path.join(seach,self.dirphoto,self.filename)
    #     self.showImage(image_path)
    def savephoto(self):
        path = os.path.join(seach,self.dirphoto)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path,self.filename)
        self.photo.save(image_path)
    def sharpness(self):
        self.photo = ImageEnhance.Sharpness(self.photo).enhance(3)
        self.savephoto()
        image_path = os.path.join(seach,self.dirphoto,self.filename)
        self.showImage(image_path)  
    def Contrast(self):
        self.photo = ImageEnhance.Contrast(self.photo).enhance(1.1)
        self.savephoto()
        image_path = os.path.join(seach,self.dirphoto,self.filename)
        self.showImage(image_path)  
    def mirror (self):
        self.photo = self.photo.transpose(Image.FLIP_LEFT_RIGHT)
        self.savephoto()
        image_path = os.path.join(seach,self.dirphoto,self.filename)
        self.showImage(image_path) 
    def rotateleft(self):
        self.photo = self.photo.transpose(Image.ROTATE_270)
        
        self.savephoto()
        image_path = os.path.join(seach,self.dirphoto,self.filename)
        self.showImage(image_path)
    def rotateright(self):
        self.photo = self.photo.transpose(Image.ROTATE_90)
        self.savephoto()
        
        image_path = os.path.join(seach,self.dirphoto,self.filename)
        self.showImage(image_path)      
    def loadImage(self,filename):


        self.filename=filename
        seachImage = os.path.join(seach,filename)
        self.photo= Image.open(seachImage)



workimage = ImageProccesor()
def showChoseImage():
    if listseach.currentRow() >=0:
        filename = listseach.currentItem().text()
        workimage.loadImage(filename)
        listseachs = os.path.join(seach,workimage.filename)
        workimage.showImage(listseachs)




btnseach.clicked.connect(chooseWorkdir)
listseach.currentRowChanged.connect(showChoseImage)
btnBW.clicked.connect(workimage.do_bw)
btnsharpness.clicked.connect(workimage.sharpness)
BTN.clicked.connect(workimage.Contrast)
btnMirror.clicked.connect(workimage.mirror)
btnleft.clicked.connect(workimage.rotateleft)
btnright.clicked.connect(workimage.rotateright)
main_win.showMaximized()
main_win.show()
app.exec_()





