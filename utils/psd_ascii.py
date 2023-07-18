import os
import numpy as np

def draw_ascii_bar(numbers: np.array, values: np.array, cfg: dict) -> None:
    min_val = cfg['psd_visulation_limits'][0]
    max_val = cfg['psd_visulation_limits'][1]
    
    # If all values are the same, prevent division by zero.
    if np.max(values) == np.min(values):
        scaled_values = values
    else:
        scaled_values = ((values - np.min(values)) / (np.max(values) - np.min(values))) * (max_val - min_val) + min_val
    
    
   
    output = '\n'.join(f'{num}: {"*" * int(val)}' for num, val in zip(numbers, scaled_values))
    os.system('cls')
    print(output)
