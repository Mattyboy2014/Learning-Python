

import glob

import pandas as pd

import numpy as np

pd.set_option('expand_frame_Repr',False)

path = r'C:\Users\Mat\Desktop\Forex_1' #Location of Forex_1 folder.

allfiles = glob.glob(path + "/*.txt")  #Loads all the text files onto my dataframe.

frame = pd.DataFrame()  #Frame of dataframe.

list_=[]

for file_ in allfiles:
    df = pd.read_csv(file_,index_col=None,sep='~',header=0)
    list_.append(df) #Tells python how to read my files in the dataframe.
    
frame = pd.concat(list_)



frame = frame[['Rate_Symbol']] #Using original dataframe(frame) to create a new dataframe(frame_a).

frame['First_Char']= frame['Rate_Symbol'].str.slice(0,1)#Using str.slice function to display first character from Rate_Symbol.

frame['Test_Flag'] = np.where(frame['Rate_Symbol'].str.contains('E|A',regex=True),1,0)

frame['Number_of_Characters']=frame['Rate_Symbol'].str.len()


frame
                             
    