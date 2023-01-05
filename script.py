#Take a folder of image with one recto, one verso with text. Add the one with the text below the one with no text.
#save a new image with xxxx texte.png
#recognition of recto / verso is done by file name finishing by R or V

from PIL import Image
import os

#set the working directory
lien = r'C:\test'
os.chdir(lien)

#name should be the same for R and V file - eg. 0_R.jpg / 0_V.jpg
for f in os.listdir('.'):
    if f.endswith('R.png'):
        i = Image.open(f)
        f1 = f.replace('R.png','V.png')
        i1 = Image.open(f1)
        imgnew = Image.new('RGB',(i.width,i.height+i1.height))
        imgnew.paste(i,(0,0))
        imgnew.paste(i1,(0,i.height))
        imgnew.save(f.replace('R.png','avec texte.png'))

        

        
