#!/usr/bin/python
import math
import sys
import random
from PIL import Image

def randRGB():
    rgb =[]
    rgb.append(random.randrange(0,255))
    rgb.append(random.randrange(0,255))
    rgb.append(random.randrange(0,255))
    return rgb

img = Image.open(sys.argv[1])
size = 420,420
img.thumbnail(size)
pixel = img.load()
x_max,y_max = img.size

#K Means Clustering Algorithm

#Number of Clusters

K = 5
iterations = 4

#Array for Centroids
centroids = [ randRGB() for i in range(K)]
clusters = [[] for i in range(K)]


for count in range(iterations):    
    print("Iterations " + str(count) + ": " + str(centroids))
    for x in range(x_max):
        for y in range(y_max):
            closestCentroid = 0
            closestCentroidDistance = 750
#            closestCentroidDistance = 250000
            for i in range(len(centroids)):
#                red = math.pow(centroids[i][0] - pixel[x,y][0],2)
#                blue = math.pow(centroids[i][1] - pixel[x,y][1],2)
#                green = math.pow(centroids[i][2] - pixel[x,y][2],2)
                red = abs(centroids[i][0] - pixel[x,y][0])
                blue = abs(centroids[i][1] - pixel[x,y][1])
                green = abs(centroids[i][2] - pixel[x,y][2])
                distance = red + blue + green
                if distance < closestCentroidDistance:
                    closestCentroidDistance = distance
                    closestCentroid = i
            clusters[closestCentroid].append(pixel[x,y])

    #Pixels are now seperated into clusters based on closest Centroid
    #print (clusters)
    #print(len(clusters[0]),len(clusters[1]),len(clusters[2]))

    #Now we take the average value of each cluster
    for i in range(len(centroids)):
        if len(clusters[i]) == 0:
            break
        redSum = 0
        greenSum = 0
        blueSum = 0

        for px in clusters[i]:
            redSum += px[0]
            blueSum += px[1]
            greenSum += px[2]

        redSum /= len(clusters[i])
        blueSum /= len(clusters[i])
        greenSum /= len(clusters[i])

        centroids[i][0] = int(redSum)
        centroids[i][1] = int(blueSum)
        centroids[i][2] = int(greenSum)

print (centroids)
