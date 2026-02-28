import pandas as pd
import matplotlib.pyplot as plt

def generate_insights(file_path):
    try:
        df = pd.read_csv(file_path)

        print("\nDataset Info:")
        print(df.info())

        print("\nSummary Statistics:")
        print(df.describe())

        print("\nMissing Values:")
        print(df.isnull().sum())

        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

        if len(numeric_cols) > 0:
            df[numeric_cols].hist(figsize=(8, 6))
            plt.tight_layout()
            plt.show()
        else:
            print("No numeric columns for visualization.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    file = input("Enter cleaned CSV file name: ")
    generate_insights(file)
