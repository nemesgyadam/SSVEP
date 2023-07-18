import os
import numpy as np
import time
import mne
import threading
from mne.time_frequency import psd_array_welch



from config.default import cfg

from src.Unicorn import UnicornWrapper, unicorn_channels
from utils.psd_ascii import draw_ascii_bar


if __name__ == "__main__":
    mne.set_log_level('WARNING')
    Unicorn = UnicornWrapper(cfg)
    info = mne.create_info(ch_names=cfg['EEG_CHANNELS'], sfreq=cfg['SAMPLING_RATE'], ch_types='eeg')
    Unicorn.start_session()
    time.sleep(2)


    while True:
        d = Unicorn.get_session_data()[2:,...] # Drop trigger and timestamp
        raw = mne.io.RawArray(d, info)
        low_freq = 1
        high_freq = 40
        raw = raw.filter(l_freq=low_freq, h_freq=high_freq, method = 'iir')


        print("1")
        raw.pick(OCCIPITL_CHANNELS)
        # Get the data from the Raw object
        data, times = raw[:, :]
        print("2")
        # Compute the PSD
        psd, freqs = psd_array_welch(data, raw.info['sfreq'], fmin=2, fmax=22)
        print("3")
        avg_psd = psd.mean(0)
        draw_ascii_bar(freqs, avg_psd, cfg)
        time.sleep(2)
        


    
  


