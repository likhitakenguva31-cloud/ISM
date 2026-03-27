import os
import pandas as pd

# Load CSV files from the root directory and the data folder

# Root directory CSV files
root_csv_files = [f for f in os.listdir('.') if f.endswith('.csv') and os.path.isfile(f)]

# Data folder CSV files
data_folder = 'data'
data_csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv') and os.path.isfile(os.path.join(data_folder, f))]

# Function to load CSV files
def load_csv_files(csv_file_list):
    data_frames = []
    for csv_file in csv_file_list:
        df = pd.read_csv(csv_file)
        data_frames.append(df)
        # You can do additional processing here if needed
    return data_frames

# Load all CSV files from both locations
all_csv_files = root_csv_files + [os.path.join(data_folder, f) for f in data_csv_files]
data_frames = load_csv_files(all_csv_files)

# Now you can use 'data_frames' as needed in your application.