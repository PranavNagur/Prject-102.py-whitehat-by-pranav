import os
originalfilename=input('Enter file pathwith file name ')
newfilename=input('Enter new file name ')
os.rename(originalfilename,newfilename)
print('File renamed successfully')