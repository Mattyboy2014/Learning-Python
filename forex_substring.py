    
frame_a = frame[['Rate_Symbol']]
frame_a['Firstline_Rate_Symbol']= frame['Rate_Symbol'].str.slice(0,1)
frame_a