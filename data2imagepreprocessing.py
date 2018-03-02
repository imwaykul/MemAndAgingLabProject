import numpy as np
import tensorflow as tf



def removeCharacters(charArray, array):
    
    for character in charArray:
        while(character in array):
            array.remove(character)
    return array
        
    


def generateImages(fileName):
    imageDict = []
    trialsDict = {}
    eegFile = open(fileName, "r")
    eegLines = eegFile.readlines()
    lineNum = 0
    channelNum = 1
    tCount = 0
    pixelCount = 0
    trialImage = []
    imgInfo = []
    accuraciesPerTrial = []
    for line in eegLines:
        if (lineNum != 0):
            grandTotal = 32 * 10000.00
            splitting = line.split(" ")
            removeCharacters(["\n", ""], splitting)
            trial = splitting[0]
            accuracy = splitting[1]
            channel = splitting[2]
            time = splitting[3]
            voltage = splitting[4]
            accuracy = accuracy.replace(",", "")
            voltage = voltage.replace(",", "")
            time = time.replace(",", "")
            channel = channel.replace(",", "")
            trial = trial.replace(",", "")
            currTrial = int(trial)
            red = 255 * (float(time)/10000)
            green = 255 * (float(voltage) / 500)
            blue = 255 * (float(channel)/32)
            if (pixelCount >= 3200):
                imgInfo.append(trialImage)
                imageDict.append(imgInfo)
                accuraciesPerTrial.append(accuracy)
                imgInfo = []
                trialImage = []
                trialImage.append([red, green, blue])
                pixelCount = 0
                tCount = 0
                channelNum = 1
            elif (tCount >= 100):
                imgInfo.append(trialImage)
                trialImage = []
                trialImage.append([red, green, blue])
                tCount = 0
                channelNum += 1
            else:
                trialImage.append([red, green, blue])
        lineNum += 1
        tCount += 1
        pixelCount += 1
        
    return imageDict, accuraciesPerTrial


imgDict = generateImages("pseudo_eeg_data.txt")
imgList = imgDict[0]
imgAcc = imgDict[1]
print(len(imgAcc))
print(len(imgList))


