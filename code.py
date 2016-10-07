import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import * 

class DrawImage(QMainWindow): 
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)

        self.setWindowTitle('Select Window')
        self.local_image = QImage('image_file_name.JPG')

        self.local_grview = QGraphicsView()
        self.setCentralWidget( self.local_grview )

        self.local_scene = QGraphicsScene()

        self.image_format = self.local_image.format()
        #self.pixMapItem = self.local_scene.addPixmap( QPixmap(self.local_image) )
        self.pixMapItem = QGraphicsPixmapItem(QPixmap(self.local_image), None, self.local_scene)

        self.local_grview.setScene( self.local_scene )

        self.pixMapItem.mousePressEvent = self.pixelSelect

    def pixelSelect( self, event ):
        print 'hello'
        position = QPoint( event.pos().x(),  event.pos().y())
        color = QColor.fromRgb(self.local_image.pixel( position ) )
        if color.isValid():
            rgbColor = '('+str(color.red())+','+str(color.green())+','+str(color.blue())+','+str(color.alpha())+')'
            self.setWindowTitle( 'Pixel position = (' + str( event.pos().x() ) + ' , ' + str( event.pos().y() )+ ') - Value (R,G,B,A)= ' + rgbColor)
        else:
            self.setWindowTitle( 'Pixel position = (' + str( event.pos().x() ) + ' , ' + str( event.pos().y() )+ ') - color not valid')


def main():
    app = QtGui.QApplication(sys.argv)
    form = DrawImage()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
    
    
*************************************************************
    
    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Formatter(object):
    def __init__(self, im):
        self.im = im
    def __call__(self, x, y):
        z = self.im.get_array()[int(y), int(x)][0]
        return 'x={:.01f}, y={:.01f}, z={:.01f}'.format(x, y, z)

data = np.random.random((10,10))

fig, ax = plt.subplots()
img = mpimg.imread('1001.jpg')
im = ax.imshow(img, interpolation='none')
ax.format_coord = Formatter(im)
plt.show()


*********************************************************


import Image
import glob


file_names = glob.glob("type2/*.jpg")

print len(file_names)

for x in file_names:
	image_file = Image.open(x)
	image_file = image_file.resize((160, 120), Image.ANTIALIAS)
	new_file_name = x.replace("type2", "resType2")
	image_file.save(new_file_name, optimize=True, quality=95)
	image_file = image_file.transpose(Image.FLIP_LEFT_RIGHT)
	new_file_name = new_file_name.replace(".jpg", "_flipped.jpg")
	image_file.save(new_file_name, optimize=True, quality=95)





