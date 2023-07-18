import os
import numpy as np
from datetime import datetime
import time
from scipy.signal import butter, lfilter, welch
import threading
from mne.time_frequency import psd_array_welch
from utils.signal_processing import butter_bandpass_filter, welch



from config.default import cfg

from src.Unicorn import UnicornWrapper, unicorn_channels
from utils.psd_ascii import draw_ascii_bar


if __name__ == "__main__":
    occipital_indices = [cfg['EEG_CHANNELS'].index(ch) for ch in cfg['OCCIPITL_CHANNELS']]


    Unicorn = UnicornWrapper(cfg)
    Unicorn.start_session()
    
    last_timestamp = datetime.now()
    while True:
        if (datetime.now() - last_timestamp).seconds < 1: continue
        last_timestamp = datetime.now()

        try:
            data = Unicorn.get_session_data()[2:,...] # Drop trigger and timestamp
            
            data = butter_bandpass_filter(data, cfg['FILTER'][0], cfg['FILTER'][1], cfg['SAMPLING_RATE'], order=6)
                    
            filtered_data = data[occipital_indices, :]

            frequencies, psd = welch(filtered_data, cfg)
           
            draw_ascii_bar(frequencies, avg_psd, cfg)

        except Exception as e:
            print(e)
            continue
   
  


