import qrcode              #importing qrcode module
from PIL import Image
qr=qrcode.Qrcode(vesrion=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)    #setting the qrcode conditions
qr.add_data("https://www.youtube.com/results?search_query=president+of+india")                          #adding a link to convert into QR
qr.make(fit=Ture)               #if a link is provided,convert it into QRcode using 'make' function
img=qr.make_image(fill_color="red",back_color='white')
img.save("president_youtube.png")

