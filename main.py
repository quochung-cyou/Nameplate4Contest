from PIL import Image, ImageDraw, ImageFont
 
# Using readlines()
file1 = open('input.txt', 'r', encoding="utf8")
Lines = file1.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    print("Running at " + str(count))
    count += 1
    W = 728
    H = 1024
    img = Image.new('RGB', (W, H), color = 'white')
    
    d = ImageDraw.Draw(img)
    line = str(count) + '. ' + line
    font = ImageFont.truetype(r'arimo.ttf', 70) 
    _, _, w, h = d.textbbox((0, 0), line, font=font)
    d.text(((W-w)/2, (H-h)/2), line, font=font, fill="black")
    img.save('output/' + str(count) + '.png')