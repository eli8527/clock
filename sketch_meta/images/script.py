from PIL import Image
import PIL
# numFrames = 118
frameDims = (256, 256)
canvasDims = (16, 20)

outImg = Image.new("RGBA", ((canvasDims[0]-1) * frameDims[0], (canvasDims[1]-1) * frameDims[1]))

# numFramesUsed = canvasDims[0] * canvasDims[1]

i = 0
for x in xrange(0, canvasDims[0]-1):
  for y in xrange(0, canvasDims[1]-1):
    i = i + 1
    fn = "clock " + str(i) + ".svg.png"
    try:
      img = Image.open(fn)
      img.load()
    except:
      print("FAIL LOADING IMAGE: " + fn)
    print("loaded: " + fn)
    img = img.resize((256, 256), PIL.Image.ANTIALIAS)
    outImg.paste(img, box=(x * frameDims[0], y * frameDims[1]))

outImg.save("comp.png")
