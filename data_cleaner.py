import pandas as pd

def clean_data(file_path, output_path="cleaned_data.csv"):
    try:
        df = pd.read_csv(file_path)
        print("Original Data Shape:", df.shape)

        df.drop_duplicates(inplace=True)
        df.fillna(method='ffill', inplace=True)
        df.dropna(how='all', inplace=True)

        print("Cleaned Data Shape:", df.shape)

        df.to_csv(output_path, index=False)
        print("Cleaned file saved as", output_path)

        return df

    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    file = input("Enter CSV file name: ")
    clean_data(file)
