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
    line = str(count) + '. ' + line
    
    #If too long, go to next line
    line2 = ''
    #Split by word
    words = line.split(' ')
    line = ''
    for i in range(len(words)):
        if i <= len(words) / 2:
            line = line + words[i] + ' '
        else:
            line2 = line2 + words[i] + ' '
    
    #Longer len, smaller font
    fontsize = 60


    font = ImageFont.truetype(r'OpenSans_Condensed-Bold.ttf', fontsize)
    _, _, w, h = d.textbbox((0, 0), line, font=font)
    d.text(((W-w)/2, (H-h)/3 + (H-h)/6), line, font=font, fill="black")
    height1 = (H-h)/3 + (H-h)/6
    _, _, w, h = d.textbbox((0, 0), line2, font=font)
    d.text(((W-w)/2, height1 + (H-h)/12), line2, font=font, fill="black")


    #Draw some decoration in 1/3 in middle

    d.line((0, H/3, W, 0 + H/3), fill=(0,0,0), width=5)
    d.line((0, H/3*2, W, H/3*2), fill=(0,0,0), width=5)

    #Watermark in 1/3 in middle bottom
    watermark = "ProPTIT EndContest © 2023"
    font = ImageFont.truetype(r'iCiel_Brush_Up.ttf', 20)
    _, _, w, h = d.textbbox((0, 0), watermark, font=font)
    color = (12, 18, 69)
    d.text(((W-w)/2, H/3 + 50), watermark, font=font, fill=color)
    img.save('output/' + str(count) + '.png')