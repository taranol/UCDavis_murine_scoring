
# InteractiveShell.cache_size=0
# 10, n=2, ftype='iir',axis=0,zero_phase=True
# PC_name = socket.gethostname()
from scipy import signal

#Recording Data

recording_length_hours=12
sampling_freq=2000
epoch_length=20

recording_length_seconds=int(recording_length_hours*3600)
target_epoch_count=int(recording_length_seconds/epoch_length)
sampling_freq_dec=int(sampling_freq/10)    
epoch_samples_dec=sampling_freq_dec*epoch_length 

#File procressing parameters



#Decimation parameters:
channels=['ECog', 'EMG', 'HPC_L', 'HPC_R']
b,a=signal.butter(1,[1],'high', fs=sampling_freq)
zScoreAtDecimation=True

decimated_folder_path="/Users/Olga/CS_projects/Brandon_project/Data"
metadata_folder_path="/Users/Olga/CS_projects/Brandon_project/Meta"
processed_data_folder_path='/Users/Olga/CS_projects/Brandon_project/Processed'

#Feauture Generation:

full_features_length=100

#Data Saving Path:

basepath = f'D:/npy_no_z_/'
types = ['/NoNo/', '/NoSz/', '/SlNo/', '/SlSl/' ]

norm_flag=0




basepath = f'D:/npy_no_z_{epoch_length}/'
# b,a=(1,[1],'high', fs==sampling_freq)






