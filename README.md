# Self-Assembly Mobility Mapping

Tools for ion mobility mass spectrometry acquisition, interpretation, and visualization.

Author: Dr. Eric Janusson
Python 3.7.4

## Introduction

This module is designed for processing data produced from Waters ion mobility mass spectrometer. It also contains functions for plotting ion mobility mass spectrometric data as well as data processing and analysis. This module was created to handle large sets of ion mobility mass spectrometry (IMS-MS) experiment files and data.

Instructions:
Install Waters DriftScope 2.9 to default directory: "C:\DriftScope\".
    # Note that this module will not run chromatographic-based IMS peak picking without this program installed as proprietary Waters DLL files are required to work with files acquired with Waters MS software.

- Move all IMS-MS experiment files (Waters .RAW folder format) to desired working directory and copy full data directory path.

- Run samm.py in terminal shell.

- When prompted, paste data directory and press Enter.
    #By default, all data is exported to a folder in the data directory named "Apex Output"
