import numpy as np
import cv2

print("Enter your file name : ")
file_name = input()

image = cv2.imread(file_name,1)

artifacts = image.copy()
artifacts = np.asarray(artifacts)

artifacts2 = image.copy()
artifacts2 = np.asarray(artifacts2)

demosaic = image.copy()
demosaic = np.asarray(demosaic)

improved = image.copy()
improved = np.asarray(improved)

gc = image.copy()
gc = np.asarray(gc)

bc = image.copy()
bc = np.asarray(bc)

rc = image.copy()
rc = np.asarray(rc)


# GREEN PATTERN

for i in range(len(gc)):
    for j in range(len(gc[i])):
        if i%2 == 1 and j%2 == 1: # Even row + even collumn
            # Applying Bayer Patern
            gc[i][j][0] = 0
            gc[i][j][2] = 0    
        elif i%2 == 0:
            gc[i][j][0] = 0
            gc[i][j][2] = 0  
            if i == 0:
                if j == 0:
                    # Corner top left
                    gc[i][j][1] = gc[i+1][j+1][1]
                elif j == len(gc[i]) - 1:
                    # Corner top rigcht
                    if j%2 == 0:
                        gc[i][j][1] = gc[i+1][j-1][1]
                    else:
                        gc[i][j][1] = gc[i+1][j][1]
                else:
                    # Top middle
                    if j%2 == 0:
                        gc[i][j][1] =  ( int(gc[i+1][j-1][1]) + int(gc[i+1][j+1][1]) )/2
                    else:
                        gc[i][j][1] = gc[i+1][j][1]
            elif i == len(gc) - 1:
                if j == 0:    
                    # Bottom left
                    gc[i][j][1] = gc[i-1][j+1][1]
                elif j == len(gc[i]) - 1:
                    # Bottom rigcht
                    if j%2 == 0:
                        gc[i][j][1] = gc[i-1][j-1][1]
                    else:
                        gc[i][j][1] = gc[i-1][j][1]
                else:
                    # Bottom middle
                    if j%2 == 0:
                        gc[i][j][1] = gc[i-1][j-1][1]
                    else:
                        gc[i][j][1] = gc[i-1][j][1]
            else:
                if j == 0:
                    # Middle left 
                    gc[i][j][1] = ( int( gc[i-1][j+1][1]) + int( gc[i+1][j+1][1]))/2
                elif j == len(gc[i]) - 1:
                    # Middle right
                    if j%2 == 0:
                        gc[i][j][1] = ( int( gc[i-1][j-1][1]) + int( gc[i+1][j-1][1]))/2
                    else:
                        gc[i][j][1] = ( int( gc[i-1][j][1]) + int( gc[i+1][j][1]))/2
                else:
                    # Middle middle 
                    if j%2 == 0:
                        gc[i][j][1] = ( int( gc[i-1][j-1][1]) + int( gc[i-1][j+1][1]) + int( gc[i+1][j-1][1]) + int( gc[i+1][j+1][1]))/4
                    else:
                        gc[i][j][1] = ( int( gc[i-1][j][1]) + int( gc[i+1][j][1]))/2
        else:
            gc[i][j][0] = 0
            gc[i][j][2] = 0 
            if j == 0:
                gc[i][j][1] = gc[i][j+1][1]
            elif j == len(gc[i]) - 1:
                gc[i][j][1] = gc[i][j-1][1]
            else:
                gc[i][j][1] = (int( gc[i][j+1][1]) + int( gc[i][j-1][1]))/2


#RED PATTERN


for i in range(len(rc)):
    if i%2 == 0:
        for j in range(len(rc[i])):
            if j%2 == 1:
                rc[i][j][0] = 0
                rc[i][j][1] = 0
    else:
        for j in range(len(rc[i])):
            if j%2 == 0:
                rc[i][j][0] = 0
                rc[i][j][1] = 0

for i in range(len(rc)):
    if i%2 == 0:
        for j in range(len(rc[i])):
            if j%2 == 0:
                rc[i][j][0] = 0
                rc[i][j][1] = 0
                rc[i][j][2] = 0
                if i == 0:
                    if j == 0:
                        # Corner top left
                        rc[i][j][2] = (int( rc[i+1][j][2]) + int( rc[i][j+1][2]))/2
                    elif j == len(rc[i]) - 1:
                        # Corner top right
                        rc[i][j][2] = (int( rc[i+1][j][2]) + int( rc[i][j-1][2]))/2
                    else:
                        # top middle
                        rc[i][j][2] = (int( rc[i][j-1][2]) + int( rc[i][j+1][2]) + int( rc[i+1][j][2]) )/3
                elif i == len(rc) - 1:
                    if j == 0:
                        # Corner bottom left
                        rc[i][j][2] = (int( rc[i-1][j][2]) + int( rc[i][j+1][2]))/2
                    elif j == len(rc[i]) - 1:
                        # Corner bottom right
                        rc[i][j][2] = (int( rc[i-1][j][2]) + int( rc[i][j-1][2]))/2
                    else:
                        # bottom middle
                        rc[i][j][2] = (int( rc[i][j-1][2]) + int( rc[i][j+1][2])+ int( rc[i-1][j][2]) )/3
                else:
                    if j == 0:
                        # middle left
                        rc[i][j][2] = (int( rc[i-1][j][2]) + int( rc[i+1][j][2]) + int( rc[i][j+1][2]) )/3
                    elif j == len(rc[i]) - 1:
                        # middle right
                        rc[i][j][2] = (int( rc[i-1][j][2]) + int( rc[i+1][j][2]) + int( rc[i][j-1][2]) )/3
                    else:
                        # middle middle
                        rc[i][j][2] = (int( rc[i-1][j][2]) + int( rc[i+1][j][2]) + int( rc[i][j-1][2]) + int( rc[i][j+1][2]))/4               
                
    else:
        for j in range(len(rc[i])):
            if j%2 == 1:
                rc[i][j][0] = 0
                rc[i][j][1] = 0
                rc[i][j][2] = 0      
                
                if i == 0:
                    if j == 0:
                        # Corner top left
                        rc[i][j][2] = (int( rc[i+1][j][2]) + int( rc[i][j+1][2]))/2
                    elif j == len(rc[i]) - 1:
                        # Corner top right
                        rc[i][j][2] = (int( rc[i+1][j][2] )+ int( rc[i][j-1][2]))/2
                    else:
                        # top middle
                        rc[i][j][2] = (int( rc[i][j-1][2]) + int( rc[i][j+1][2]) + int( rc[i+1][j][2]) )/3
                elif i == len(rc) - 1:
                    if j == 0:
                        # Corner bottom left
                        rc[i][j][2] = (int( rc[i-1][j][2]) + int( rc[i][j+1][2]))/2
                    elif j == len(rc[i]) - 1:
                        # Corner bottom right
                        rc[i][j][2] = (int( rc[i-1][j][2]) + int( rc[i][j-1][2]))/2
                    else:
                        # bottom middle
                        rc[i][j][2] = (int( rc[i][j-1][2]) + int( rc[i][j+1][2]) + int( rc[i-1][j][2]) )/3
                else:
                    if j == 0:
                        # middle left
                        rc[i][j][2] = (int( rc[i-1][j][2]) + int( rc[i+1][j][2]) + int( rc[i][j+1][2]) )/3
                    elif j == len(rc[i]) - 1:
                        # middle right
                        rc[i][j][2] = (int( rc[i-1][j][2]) + int( rc[i+1][j][2]) + int( rc[i][j-1][2]) )/3
                    else:
                        # middle middle
                        rc[i][j][2] = (int( rc[i-1][j][2]) + int( rc[i+1][j][2]) + int( rc[i][j-1][2]) + int( rc[i][j+1][2]))/4 


#BLUE PATTERN


for i in range(len(bc)):
    if i%2 == 0:
        for j in range(len(bc[i])):
            if j%2 == 0:
                bc[i][j][1] = 0
                bc[i][j][2] = 0
                
for i in range(len(bc)):
    if i%2 == 0:
        for j in range(len(bc[i])):
            if j%2 == 1:
                bc[i][j][0] = 0
                bc[i][j][1] = 0
                bc[i][j][2] = 0
                if j == len(bc[i])-1:
                    # Very right
                    bc[i][j][0] = bc[i][j-1][0]
                else:
                    # Middle
                    bc[i][j][0] = ( int( bc[i][j-1][0]) + int( bc[i][j+1][0]) )/2
                    
    else:
        for j in range(len(bc[i])):
            bc[i][j][0] = 0
            bc[i][j][1] = 0
            bc[i][j][2] = 0
            if i == len(bc) - 1:
                if j == len(bc[i]) - 1:
                    # Corner bot left
                    bc[i][j][0] = bc[i-1][j-1][0]
                else:
                    # bcot middle
                    if j%2 == 0:
                        bc[i][j][0] = bc[i-1][j][0]
                    else:
                        bc[i][j][0] = ( int( bc[i-1][j-1][0]) + int( bc[i-1][j+1][0]) )/2
            else:
                if j == len(bc[i]) - 1:
                    # Middle left
                    if j%2 == 0:
                        bc[i][j][0] = ( int( bc[i+1][j][0]) + int( bc[i-1][j][0]) )/2
                    else:
                        bc[i][j][0] = ( int( bc[i-1][j-1][0]) + int( bc[i+1][j-1][0]) )/2
                else:
                    # Middle middle
                    if j%2 == 0:
                        bc[i][j][0] = ( int( bc[i+1][j][0]) + int( bc[i-1][j][0]) )/2
                    else:
                        bc[i][j][0] = ( int( bc[i-1][j-1][0]) + int( bc[i+1][j+1][0]) + int( bc[i-1][j+1][0]) + int( bc[i+1][j-1][0]) )/4



for i in range(len(demosaic)):
    for j in range(len(demosaic[i])):
        demosaic[i][j][0] = bc[i][j][0]
        demosaic[i][j][1] = gc[i][j][1]
        demosaic[i][j][2] = rc[i][j][2]

for i in range(len(artifacts)):
    for j in range(len(artifacts[i])):
        if ( int(artifacts[i][j][0]) - int(demosaic[i][j][0]) )**2 > 255:
            artifacts[i][j][0] = 255
        else:
            artifacts[i][j][0] = ( int(artifacts[i][j][0]) - int(demosaic[i][j][0]) )**2
        if ( int(artifacts[i][j][1]) - int(demosaic[i][j][1]) )**2 > 255:
            artifacts[i][j][1] = 255
        else:
            artifacts[i][j][1] = ( int(artifacts[i][j][1]) - int(demosaic[i][j][1]) )**2
        if ( int(artifacts[i][j][2]) - int(demosaic[i][j][2]) )**2 > 255:
            artifacts[i][j][2] = 255
        else:
            artifacts[i][j][2] = ( int(artifacts[i][j][2]) - int(demosaic[i][j][2]) )**2

# PART 2

newbc = bc.copy()

for i in range(len(newbc)):
    for j in range(len(newbc[i])):
        newbc[i][j][0] -= rc[i][j][2]

medianbc = newbc.copy()
medianbc = cv2.medianBlur(medianbc,3)

for i in range(len(medianbc)):
    for j in range(len(medianbc[i])):
        medianbc[i][j][0] += rc[i][j][2]
        
newgc = gc.copy()

for i in range(len(newgc)):
    for j in range(len(newgc[i])):
        newgc[i][j][1] -= rc[i][j][2]

mediangc = newgc.copy()
mediangc = cv2.medianBlur(mediangc,3)

for i in range(len(mediangc)):
    for j in range(len(mediangc[i])):
        mediangc[i][j][1] += rc[i][j][2]
        
for i in range(len(improved)):
    for j in range(len(improved[i])):
        improved[i][j][0] = medianbc[i][j][0]
        improved[i][j][1] = mediangc[i][j][1]
        improved[i][j][2] = rc[i][j][2]

for i in range(len(artifacts2)):
    for j in range(len(artifacts2[i])):
        if ( int(artifacts2[i][j][0]) - int(improved[i][j][0]) )**2 > 255:
            artifacts2[i][j][0] = 255
        else:
            artifacts2[i][j][0] = ( int(artifacts2[i][j][0]) - int(improved[i][j][0]) )**2
        if ( int(artifacts2[i][j][1]) - int(improved[i][j][1]) )**2 > 255:
            artifacts2[i][j][1] = 255
        else:
            artifacts2[i][j][1] = ( int(artifacts2[i][j][1]) - int(improved[i][j][1]) )**2
        if ( int(artifacts2[i][j][2]) - int(improved[i][j][2]) )**2 > 255:
            artifacts2[i][j][2] = 255
        else:
            artifacts2[i][j][2] = ( int(artifacts2[i][j][2]) - int(improved[i][j][2]) )**2

cv2.imshow('GREEN CHANNEL', gc)
cv2.imshow('RED CHANNEL', rc)
cv2.imshow('BLUE CHANNEL', bc)
cv2.imshow('DEMOSAIC', demosaic)
cv2.imshow('ARTIFACTS PART 1', artifacts)
cv2.imshow('IMPROVED', improved)
cv2.imshow('ARTIFACTS PART 2', artifacts2)

cv2.waitKey(0)
cv2.destroyAllWindows()








