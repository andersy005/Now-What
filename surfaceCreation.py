import math
import sys

f = open('sinusoids.dat','w')

# create a 10 by 10 matrix of two interfering sinusoids
# And saves it in the file opened above
# Each data point by default creates a 1 mm square base voxel

pi = 4. * math.atan(1.)
print('pi is ', pi)

numx = 100;
numy = 100;

for x_index in range(0, numx):
	for y_index in range(0, numy):
		xcenter1 = x_index
		xcenter2 = x_index - 50
		ycenter1 = y_index
		ycenter2 = y_index - 50

		radius1 = 0.2 * pi * math.sqrt((xcenter1 * xcenter1) + (ycenter1 * ycenter1))
		radius2 = 0.2 * pi * math.sqrt((xcenter2 * xcenter2) + (ycenter2 * ycenter2))
		fxy = 2.0 * math.cos(radius1) + 2 * math.cos(radius2) + 6
		f.write(str(fxy) + ' ')
	f.write('\n')
f.close()


