# MI filter for nppes data

This project takes npi data file found on the [cms gov](https://download.cms.gov/nppes/NPI_Files.html) site [(direct download link)](https://download.cms.gov/nppes/NPPES_Data_Dissemination_July_2025_V2.zip) and utilizes polars lazy load to optimally filter and generate a new csv based on a state filter. This new file should be much smaller, and can be loaded into excel

# python package manager - UV

This project is managed using uv. If you do not have uv, please go to [uv installation page](https://docs.astral.sh/uv/getting-started/installation/) and install uv based on your OS

Once complete, navigate to this folder in your cli and run ```uv sync``` to generate the venv that has all the requirements

You can activate this env in your cli by navigating to the .venv folder and running activate
- For linux/macos, you would run ```. .venv/bin/activate```
- For windows, you would run ```. .venv/bin/Scripts/activate```

# data download

```dl_data.sh``` has been provided if you'd like to programmatically download the zip file. Run the .sh file using ```. dl_data.sh```

# data_extraction.ipynb

This notebook walks through the data extraction method in a secton format and has code to visualize details regarding the dataset

# app.py

This file houses the tkinter code to create the gui for non-technical users. It's a very simple program loop that presents all the .csv files found in its working directory, and lets you select the right file and run extraction, generating a new csv with a Michigan filter

# Pyinstaller

Pyinstaller is being used to generate a standalone .exe. FYI, pyinstaller can only generate an executable that works with the current OS, and can not generate cross build to run on other OS's.

To generate the standalone app, run ```pyinstaller --onefile --windowed app.py```