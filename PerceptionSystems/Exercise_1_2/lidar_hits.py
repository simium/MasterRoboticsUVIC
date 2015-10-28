import numpy as np
import matplotlib.pyplot as plt

minLaserRange = 0.1
maxLaserRange = 30.0
laserAngle = 0.25
legWidth = 0.15

font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }

x = np.linspace(minLaserRange, maxLaserRange, num=100)
y = 1+np.rad2deg(np.arctan(legWidth/x))/laserAngle

plt.plot(x, y, 'k')
plt.title('Hits vs Distance with UTM-30LN', fontdict=font)
plt.xlabel('Distance (m)', fontdict=font)
plt.ylabel('Laser hits', fontdict=font)

# Tweak spacing to prevent clipping of ylabel
# as recommended by the Matplotlib library
plt.subplots_adjust(left=0.15)
plt.show()

print "%d laser hits at 1m" % (1+np.rad2deg(np.arctan(legWidth/1))/laserAngle)
print "%d laser hits at 3m" % (1+np.rad2deg(np.arctan(legWidth/3))/laserAngle)
print "%d laser hits at 5m" % (1+np.rad2deg(np.arctan(legWidth/5))/laserAngle)
