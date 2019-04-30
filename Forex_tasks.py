
#Task1

import glob

import pandas as pd

pd.set_option('expand_frame_Repr',False)

path = r'C:\Users\Mat\Desktop\Forex_7' #Location of Forex_1 folder

allfiles = glob.glob(path + "/*.txt")  #Loads all the text files onto my dataframe.

frame = pd.DataFrame()  #Frame of dataframe

list_=[]

for file_ in allfiles:
    df = pd.read_csv(file_,index_col=None,sep='~',header=0)
    list_.append(df) #Tells python how to read my files in the dataframe
    
frame = pd.concat(list_)

frame

#Task2

path_1 =r'C:\\Users\Mat\Desktop\Learning_Python' #Location to send outputfile.
frame.to_csv(path_1+"/forextest1.txt",index=None,sep='~')#Output's the dataframe(frame) to a txt file to file location.

#Task3


file_ = r'C:\Users\Mat\Desktop\Learning_Python\forextest1.txt' #Location of Forex_1 file
 

frame = pd.read_csv(file_,index_col=None,sep='~',header=0)#Reads the file_ and displays file in python


frame
    
#Task4
    
frame=frame[['Rate_Symbol','Rate_Bid','timerun']]#keeping only 3 columns from dataframe(frame).

frame

#Task5

frame_1 = frame.drop_duplicates(subset=['Rate_Symbol'])#removes all duplicates from the dataframe and creates new dataframe from original dataframe. 

frame_1

    

    