import os
import pandas as pd
from rich.progress import track

FOLDER_PATH = "data/auto"
OUTPUT_NAME = "auto_202401to07.csv"

if __name__ == "__main__":
    
    # Initialize an empty DataFrame
    auto_df = pd.DataFrame()
    
    # Iterate over all files in the folder
    for file in track(os.listdir(FOLDER_PATH)):
        df = pd.read_csv(f"{FOLDER_PATH}/{file}")
        auto_df = pd.concat([auto_df, df], axis=0, ignore_index=True)  # Assign the result back to auto_df

    # Write the concatenated DataFrame to a new CSV file
    auto_df.to_csv(f"data/{OUTPUT_NAME}", index=False)