# Mi filter for nppes data

This project simply takes npidata pfile found on the [cms gov](https://download.cms.gov/nppes/NPI_Files.html) site. - [direct download link](https://download.cms.gov/nppes/NPPES_Data_Dissemination_July_2025_V2.zip):, and utilizes polars lazy load to optimally filter and generate file based on a state filter

# python package manager - UV

This project is managed using uv. If you do not have uv, please go to [uv installation page](https://docs.astral.sh/uv/getting-started/installation/) and install uv based on your OS

Once complete, navigate to this folder in your cli and run ```uv sync``` to generate the venv that has all the requirements

You can activate this env in your cli by navigating to the .venv folder and running activate
- For linux/macos, you would run ```. .venv/bin/activate```
- For windows, you would run ```. .venv/bin/Scripts/activate```

# data download

```dl_data.sh``` has been provided if you'd like to programmatically download the zip file. Run the .sh file using ```. dl_data.sh```

# data_extraction.ipynb

This notebook just walks through extracting the data quickly, and some code blocks to visualize details about the dataset

# Pyinstaller

Pyinstaller is being used to generate a standalone .exe. Just as a reminder, pyinstaller only generate the file based the current running OS, and can not generate cross builds to run on other OS's.

To generate the standalone app, run ```pyinstaller --onefile --windowed app.py```