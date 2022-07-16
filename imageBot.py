from PIL import Image
from perlin_noise import PerlinNoise
import math
import random
from tqdm import tqdm

noise1 = PerlinNoise(octaves=3.33, seed=random.randint(0,10000000))
noise2 = PerlinNoise(octaves=3.33, seed=random.randint(0,10000000))
noise3 = PerlinNoise(octaves=3.33, seed=random.randint(0,10000000))

def newImg():
    width, height = 1080, 1080
    totalPixels = width*height
    img = Image.new('RGB', (width, height))
    print("Creating Image...")
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    for x in tqdm(range(height)):
        for y in range(width):
            #noiseVal1 = ((noise1([x/width, y/height])+1)/2)*100
            noiseVal1 = noise1([x/width, y/height])*100
            #noiseVal2 = ((noise2([x/width, y/height])+1)/2)*100
            noiseVal2 = noise2([x/width, y/height])*100
            #noiseVal3 = ((noise3([x/width, y/height])+1)/2)*100
            noiseVal3 = ((noise3([x/width, y/height])))*100
            img.putpixel((x,y), (
                r + math.floor(noiseVal1),
                g + math.floor(noiseVal2),
                b + math.floor(noiseVal3)
                ))

    img.save('sqr.png') 

    return img

wallpaper = newImg()
wallpaper.show()