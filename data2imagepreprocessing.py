import numpy as np
import tensorflow as tf

colors = ["red", "orange", "yellow", "green", "blue", "purple" ,"grey", "brown", "white", "black"]
scenes = ["office", "city", "forest", "house"]
objects = ["lizard", "toothbrush", "ribs", "piggy bank", "teddy bear", "car", "football", "salad"]
conditions = ["VAL", "INVAL", "REQ", "NEU"]

class Trial:
    def __init__(self, firstCue, secondCue, ti_one, ti_two):
        self.firstCue = firstCue
        self.secondCue = secondCue
        self.ti_one = ti_one
        self.ti_two = ti_two
        
    #trial 1,2,3: encoding, retrieval, etc
    def set_trial_type(trial_type):
        self.trial_type = trial_type

    def get_trial_type(trial_type):
        return self.trial_type

    def set_interval_times(cue, cue_stim, stim_pres, resp):
        self.cue = cue
        self.cue_stim = cue_stim
        self.stim_pres = stim_pres
        self.resp = resp

    def get_total_time():
        return self.cue + self.cue_stim + self.stim_pres + self.resp

    def get_interval_times():
        return [self.cue, self.cue_stim, self.stim_pres, self.resp]

    def match(answer, key):
        return answer == key

    #valid, invalid, required, or neutral
    def set_condition(condition):
        self.condition = condition

    def get_condition():
        return self.condition

    




def removeCharacters(charArray, array):
    
    for character in charArray:
        while(character in array):
            array.remove(character)
    return array

#o = object
#s = scene
#t = trial #
def scene_to_object(o, s, t):
    o_to_s_dict = {}
    o_to_s_dict[o] = (t, s)
    return o_to_s_dict



so_one = scene_to_object(objects[2], scenes[1], 45)
so_two = scene_to_object(objects[4], scenes[3], 116)

#print("s-o pair one: ", so_one)
#print("s-o pair two: ", so_two)


    
def attribute_to_index(att_list):
    counter = 1
    att_to_ix = {}
    for att in att_list:
        att_to_ix[att] = counter
        counter += 1
    return att_to_ix


        
        

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




def cueMatch(cue1, cue2):
    return cue1 == cue2

def validQ(cue1, cue2):
    if (cueMatch(cue1, cue2) == True):
        return "valid"
    return "invalid"

def que_to_context(truth_val):
    if (truth_val == "valid"):
        return 1
    return 0


#imgDict = generateImages("pseudo_eeg_data.txt")
#imgList = imgDict[0]
#imgAcc = imgDict[1]
#print(len(imgAcc))
#print(imgList[0])

noMatch = validQ("forest", "tree")
associatedValNoMatch = que_to_context(noMatch)
match = validQ("forest", "forest")
associatedValMatch = que_to_context(match)
#print(associatedValNoMatch)
#print(associatedValMatch)
        


color_to_ix = attribute_to_index(colors)
scene_to_ix = attribute_to_index(scenes)
object_to_ix = attribute_to_index(objects)
condition_to_ix = attribute_to_index(conditions)


#print("Color to Index Dict: ", color_to_ix)
#print("Scene to Index Dict: ", scene_to_ix)
#print("Object to Index Dict: ", object_to_ix)
#print("Condition to Index Dict: ", condition_to_ix)



