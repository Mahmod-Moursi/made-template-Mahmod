import os
import pandas as pd

def test_output_file_exists():
    # Define the expected output file path
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    output_file = os.path.join(data_dir, 'merged_data.csv')
    
    # Check if the output file exists
    assert os.path.exists(output_file), f"Output file {output_file} does not exist."

def test_output_file_not_empty():
    # Define the expected output file path
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    output_file = os.path.join(data_dir, 'merged_data.csv')
    
    # Check if the output file is not empty
    assert os.path.getsize(output_file) > 0, f"Output file {output_file} is empty."

def test_output_file_format():
    # Define the expected output file path
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    output_file = os.path.join(data_dir, 'merged_data.csv')
    
    # Load the CSV file and check its structure
    df = pd.read_csv(output_file)
    required_columns = ['country', 'year', 'iso_code']  
    
    for column in required_columns:
        assert column in df.columns, f"Missing required column: {column}"

if __name__ == "__main__":
    test_output_file_exists()
    test_output_file_not_empty()
    test_output_file_format()
    print("All tests passed.")

