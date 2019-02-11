from PIL import Image
import numpy as np
def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    allNumbers = range(0,10)
    numbersWeHave = range(1,10)
    for eachNum in allNumbers:
        #print eachNum
        for furtherNum in numbersWeHave:
            
            print(str(eachNum)+'.'+str(furtherNum))


            
            imgFilePath = 'numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)
            
createExamples()