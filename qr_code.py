import qrcode                         #importing qrcode module
img=qrcode.make("https://www.youtube.com/results?search_query=president+of+india")                                 #generating qrcode using make function as an image using img varaiable
img.save("president_youtube.png")
