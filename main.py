import pandas as pd
from data_quality_visualizer import DataQualityVisualizer

def main():
    # Sample data with some null values
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', None],
        'Age': [25, None, 30, 22],
        'City': ['New York', 'Los Angeles', None, 'Chicago']
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)

    # Create an instance of DataQualityVisualizer with the sample DataFrame
    dqv = DataQualityVisualizer(df)

    # Dictionary to map function names to class methods
    function_map = {
        'check_nulls': dqv.check_null_values,
        # Add other functions here as you expand the class
        # 'another_function': dqv.another_function,
        # 'more_functions': dqv.more_functions
    }

    while True:
        # Ask the user which function to run from DataQualityVisualizer
        print("Available functions: check_nulls")
        # Add other available functions to the prompt as you expand the class
        function_input = input("Enter the function you want to run: ")

        # Check if the entered function is available
        if function_input in function_map:
            # Call the corresponding function
            function_map[function_input]()
        else:
            print(f"Function '{function_input}' not recognized.")

        # Ask if the user wants to perform another check
        more_checks = input("Do you want to perform another data quality check? (yes/no): ")

        if more_checks.lower() != 'yes':
            break

if __name__ == '__main__':
    main()
