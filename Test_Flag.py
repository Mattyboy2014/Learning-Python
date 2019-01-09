

import glob

import pandas as pd

import numpy as np

pd.set_option('expand_frame_Repr',False)

path = r'C:\Users\Mat\Desktop\Forex_1' #Location of Forex_1 folder

allfiles = glob.glob(path + "/*.txt")  #Loads all the text files onto my dataframe.

frame = pd.DataFrame()  #Frame of dataframe

list_=[]

for file_ in allfiles:
    df = pd.read_csv(file_,index_col=None,sep='~',header=0)
    list_.append(df) #Tells python how to read my files in the dataframe
    
frame = pd.concat(list_)

frame 

frame_a = frame[['Rate_Symbol']] #Using original dataframe(frame) to create a new dataframe(frame_a)
frame_a['First_Char']= frame['Rate_Symbol'].str.slice(0,1)
frame_a['Test_Flag'] = np.where(frame['Rate_Symbol'].str.contains('E|A',regex=True),1,0)

frame_a
                             
    