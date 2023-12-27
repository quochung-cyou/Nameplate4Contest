from PIL import Image, ImageDraw, ImageFont
 
# Using readlines()
file1 = open('input.txt', 'r', encoding="utf8")
Lines = file1.readlines()
  
count = 0
# Strips the newline character


for line in Lines:
    print("Running at " + str(count+1) + "/" + str(len(Lines)) + " " + line.strip())
    count += 1
    W = 728
    H = 1024
    img = Image.new('RGB', (W, H), color = 'white')
    
    d = ImageDraw.Draw(img)
    
    #Longer len, smaller font
    fontsize = 45
    font = ImageFont.truetype(r'OpenSans_Condensed-Bold.ttf', fontsize)

    words = line.split()
    line = ""
    offset = H/3
    for word in words:
        if (word == "||"):
            _, _, w, h = d.textbbox((0, 0), line, font=font)
            offset += (H-h)/12
            d.text(((W-w)/2, offset), str(line), font=font, fill="black")
            line = ""
        else:
            line += word + " "
    if (line != ""):
        _, _, w, h = d.textbbox((0, 0), line, font=font)
        offset += (H-h)/12
        d.text(((W-w)/2, offset), str(line), font=font, fill="black")
    #Draw some decoration in 1/3 in middle
     
    d.line((20, H/3, W - 20, 0 + H/3), fill=(0,0,0), width=5)
    d.line((20, H/3*2, W - 20, H/3*2), fill=(0,0,0), width=5)
    d.line((20, H/3, 20, H/3*2), fill=(0,0,0), width=5)
    d.line((W - 20, H/3, W - 20, H/3*2), fill=(0,0,0), width=5)

    #Watermark in 1/3 in middle bottom
    watermark = "ProPTIT EndContest © 2023"
    font = ImageFont.truetype(r'iCiel_Brush_Up.ttf', 20)
    _, _, w, h = d.textbbox((0, 0), watermark, font=font)
    color = (12, 18, 69)
    d.text(((W-w)/2, H/3 + 50), watermark, font=font, fill="blue")
    img.save('output/' + str(count) + '.png')