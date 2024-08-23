
#%% Library 

import numpy as np

#%% Function

def data_gen(name1="NHA"):    
    """
    Imports the CSV file without its headers and first column, and transposes it into an np.array
    
    Parameters
    ----------
    name: str
    The name of the CSV file that will be used

    Returns
    -------
    the array
    """
    path="your file path here"
    
    data_1=np.genfromtxt(path+name1+".csv",delimiter=',',skip_header=3, skip_footer=0)
    #data_1=np.genfromtxt(path+name1+".csv",delimiter=';',skip_header=3, skip_footer=0)
    data_1=data_1[:,1:]
     
    return(data_1)


def data_gen_wave(crop_lower=0, crop_higher=3, name="waves"):
    """
    Gets the 2 wavelengths arrays
    Files need to be in csv format to be usable
    csv file must be: 1 sample per column and rows=observation for 1 wavelength, and 1st column=wavelengths
    
    Parameters
    ----------
    crop: int, default=0
    the number of lines at the bottom of the dataset (so the shorter wavelengths) that need to be excluded
    Default=1 in case the last line is empty 
    
    name: str, default 'waves'
    The name of the csv file to be used 
    
    
    Returns
    -------
    2 arrays with the 2 wavelengths
    """
    
    path="the waves file pathway here"
    

    data_1=np.genfromtxt(path+name+".csv",delimiter=';',skip_header=crop_higher, skip_footer=crop_lower)
    long_wvlgth=data_1[:,0]
    short_wvlgth=data_1[:1245,1]
    long_wavelength=long_wvlgth.tolist()
    short_wavelength=short_wvlgth.tolist()

    print(len(long_wavelength), len(short_wavelength))
    
    return(long_wavelength, short_wavelength)

def resample_index(long, short):
    """
    map each element in the short list to the closest element in the long list based on their numerical values
    
    Parameters
    ----------
    long: previously generated index for the original dataset with 2924 wavelength values
        
    short: previously generated index for the original dataset with 1245 wavelength values
    
    
    Returns
    -------
    Return a series of interest in the "long" that are closest to each element in "short".
    """
    
    
    resample=[]
    for i in short:
        index=0
        mini=10
        for j in range(len(long)):
            compare=abs(i-long[j])
            if compare<mini:
                mini=compare
                index=j
        resample.append(index)
    return(resample)


def resample(index, name_array, name):
    """
    Conducts the resampling by omitting the features in the original dataset 
    based on the defined "short" wavelength
    
    Parameters
    ----------
    index: 
    
    name_array: the original data array 
        
    name: name of the output file
    
    Returns
    -------
    resampled spectra file in .csv files
    """
    
    l_name=name_array.tolist()
    
    new_list=[]
    for i in index:
        new_list.append(l_name[i])
    
    final_array=np.array(new_list)
    np.savetxt(name +"_resampled.csv", final_array, delimiter=",")
    return(final_array)

#%% Read in the wavelength and generate corresponding index for resamling later

long, short= data_gen_wave(name="waves")
index=resample_index(long, short)

#%%  Read in the data files 

healthy1=data_gen("C1_f2")
healthy2=data_gen("C2_f2")
healthy4=data_gen("C4_f2")
healthy3=data_gen("C3_f")
healthy5=data_gen("C5__f2")
healthy6=data_gen("C6_f")
healthy7=data_gen("C7_reaL_f")
healthy8=data_gen("C8_f")
healthy9=data_gen("C9_f")
healthy10=data_gen("C10_f")


#%% Resample and generate the output files 

resample(index,healthy1, "C1")
resample(index,healthy2, "C2")
resample(index,healthy3, "C3")
resample(index,healthy4, "C4")
resample(index,healthy5, "C5")
resample(index,healthy6, "C6")
resample(index,healthy7, "C7")
resample(index,healthy8, "C8")
resample(index,healthy9, "C9")
resample(index,healthy10, "C10")




