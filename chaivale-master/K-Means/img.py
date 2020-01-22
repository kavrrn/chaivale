import numpy as np
from PIL import Image

img = Image.open('awifs_ndvi_201701_15_1_clipped.tif')
array = np.array(img)
print(array.shape)


file=open("crop1.txt","w")
file.write(str(len(array[0]))+"\n")
file.write(str(len(array))+"\n")

print(array[0][0])
# for i in range(len(array)):
# 	for j in range(len(array[0])):
# 		file.write(str(array[i][j][0])+","+str(array[i][j][1])+","+str(array[i][j][2])+","+str(j+1)+","+str(i+1)+"\n")
for i in range(len(array)):
	for j in range(len(array[0])):
		file.write(str(array[i][j])+","+str(j+1)+","+str(i+1)+"\n")
file.close()
