import numpy as np
import matplotlib.pyplot as plt

pixelSize = 4.08e-6
focalLength = 8e-3
pixelWidth = 1288
pixelHeight = 728
alphaHorizontal = 2*np.arctan(pixelSize*pixelWidth/(2*focalLength))
alphaVertical = 2*np.arctan(pixelSize*pixelHeight/(2*focalLength))

print np.rad2deg(alphaHorizontal)
print np.rad2deg(alphaVertical)

monaLisaWidth = 0.77
monaLisaHeight = 0.53

font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }

x = np.linspace(1.0, 10.0, num=100)
hPixels = pixelWidth*monaLisaWidth/(2*x*np.tan(alphaHorizontal/2))
vPixels = pixelHeight*monaLisaHeight/(2*x*np.tan(alphaVertical/2))
y = hPixels*vPixels

plt.plot(x, y, 'k')
#plt.plot(x, z, 'k')
plt.title('Number of pixels that represent Mona Lisa', fontdict=font)
plt.xlabel('Distance (m)', fontdict=font)
plt.ylabel('Pixels of Mona Lisa (width x height)', fontdict=font)

# Tweak spacing to prevent clipping of ylabel
# as recommended by the Matplotlib library
plt.subplots_adjust(left=0.15)
plt.show()

print "%d horizontal pixels at 1m" % (pixelWidth*monaLisaWidth/(2*1*np.tan(alphaHorizontal/2)))
print "%d horizontal pixels at 2m" % (pixelWidth*monaLisaWidth/(2*2*np.tan(alphaHorizontal/2)))
print "%d horizontal pixels at 5m" % (pixelWidth*monaLisaWidth/(2*5*np.tan(alphaHorizontal/2)))
print "%d horizontal pixels at 10m" % (pixelWidth*monaLisaWidth/(2*10*np.tan(alphaHorizontal/2)))

print "%d vertical pixels at 1m" % (pixelHeight*monaLisaHeight/(2*1*np.tan(alphaVertical/2)))
print "%d vertical pixels at 2m" % (pixelHeight*monaLisaHeight/(2*2*np.tan(alphaVertical/2)))
print "%d vertical pixels at 5m" % (pixelHeight*monaLisaHeight/(2*5*np.tan(alphaVertical/2)))
print "%d vertical pixels at 10m" % (pixelHeight*monaLisaHeight/(2*10*np.tan(alphaVertical/2)))
