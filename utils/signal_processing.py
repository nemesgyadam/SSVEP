from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs  # Nyquist frequency, which is half of fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def welch(data, cfg):
    # Apply welch
    frequencies, psd = welch(filtered_data, cfg['SAMPLING_RATE'], nperseg=256, noverlap=128)

    # Filter frequencies
    freq_mask = (frequencies >= cfg['FILTER'][0]) & (frequencies <= cfg['FILTER'][1])
    frequencies = frequencies[freq_mask]
    psd = psd[:, freq_mask]

    # Average PSD across channels
    avg_psd = psd.mean(0)

    return frequencies, avg_psd