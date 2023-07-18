# config.py

cfg = {
    'IMAGE_PATH': "resources/stim_B.jpg",
    'FLICKER_RATES': [12, 12],
    'IMAGE_POSITIONS': [(0.05, 1/4), (0.7, 1/4)],
    'EEG_CHANNELS': [ "FP1", "FFC1", "FFC2", "FCZ", "CPZ", "CPP1", "CPP2", "PZ"],
    'OCCIPITL_CHANNELS' : ["CPP1","CPP2", "PZ"],
    'SAMPLING_RATE': 250,
    'FILTER': (8.0,20),
    'psd_visulation_limits': (0, 100),

}
