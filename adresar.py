import os

def Folders(path,depth=0):
    for item in os.listdir(path):
        if os.path.isdir(path+"\\"+item) and item[0] not in ".$":
            if len(os.listdir(path+"\\"+item))!=0:
                print('-'*depth,item)
                Folders(path+"\\"+item,depth+1)

Folders("C:\\")


