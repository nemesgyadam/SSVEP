import pygame
import time
import threading
import os
from config.default import cfg


from src.Stimulus import Stimulus


if __name__ == "__main__":
    visual_stimulus = Stimulus(cfg)
    visual_stimulus.loop()
  


