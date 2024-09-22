import pandas as pd

def load_data(file_path):
    """Load data from a CSV """
    return pd.read_csv(file_path)

def process_data(df):
    """filtering and adding a new column."""
    
    # Define a function to determine status
    def determine_status(age):
        if age > 30:
            return 'senior'
        else:
            return 'junior'

    df['status'] = df['age'].apply(determine_status)
    
    return df

def save_data(df, output_path):
    """Save the processed data to a new CSV file."""
    df.to_csv(output_path, index=False)

def main():
    # Load data
    data = load_data('data.csv')
    print("Original Data:")
    print(data)

    # Process data
    processed_data = process_data(data)
    print("Processed Data:")
    print(processed_data)

    # Save processed data
    save_data(processed_data, 'processed_data.csv')
    print("Processed data saved to 'processed_data.csv'")

if __name__ == '__main__':
    main()
