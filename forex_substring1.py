
import glob

import pandas as pd


pd.set_option('expand_frame_Repr',False)

path = r'C:\Users\Mat\Desktop\Forex_1'

allfiles = glob.glob(path + "/*.txt")

frame = pd.DataFrame()

list_=[]

for file_ in allfiles:
    df = pd.read_csv(file_,index_col=None,sep='~',header=0)
    list_.append(df)
    
frame = pd.concat(list_)

frame

frame_a = frame[['Rate_Symbol']]
frame_a['First_Char']= frame['Rate_Symbol'].str.slice(0,1)
frame_a

                             