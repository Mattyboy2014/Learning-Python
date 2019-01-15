
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


frame = frame[['Rate_Symbol','Rate_Bid']] #Keeping 2 columns from original dataframe.

frame['First_Char']= frame['Rate_Symbol'].str.slice(0,1) #Using str.slice function to display first character of Rate_Symbol.

frame['Test_Flag'] = np.where(frame['Rate_Symbol'].str.contains('E|A',regex=True),1,0) #Flag to see if Value is Rate_Symbol contains A or E.

frame['Number_of_Characters'] = frame.Rate_Symbol.str.len() #Using str.len function to count number of characters in Rate_Symbol Values.

frame['Over_5']='Missing'
frame.loc[frame.Number_of_Characters > 5,'Over_5']=frame.Rate_Symbol # Using 2 output statements if condition is met or not.

frame['A_Or_E']=frame.Rate_Bid 
frame.loc[frame['Rate_Symbol'].str.contains('A|E'), 'A_Or_E']=frame.Rate_Symbol #Different output values if condition is met or not met

frame #frame used to run program/dataframe