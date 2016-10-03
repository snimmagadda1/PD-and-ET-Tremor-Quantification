from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name              = 'Adafruit_BluefruitLE',
      version           = '0.9.0',
      author            = 'Tony DiCola',
      author_email      = 'tdicola@adafruit.com',
      description       = 'Python library for interacting with Bluefruit LE (Bluetooth low energy) devices on Linux or OSX.',
      license           = 'MIT',
      url               = 'https://github.com/adafruit/Adafruit_Python_BluefruitLE/',
      packages          = find_packages())
