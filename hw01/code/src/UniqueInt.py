import os
import glob
import datetime
import sys

class IntegerProcessor:
    @staticmethod
    def handle_files(input_file_path, output_file_path):
        unique_numbers = set()

        try:
            with open(input_file_path, 'r') as file:
                for line in file:
                    numbers = line.strip().split()
                    if len(numbers) != 1:
                        continue
                    num_str = numbers[0]
                    try:
                        num = int(num_str)
                        if -1023 <= num <= 1023:
                            unique_numbers.add(num)
                    except ValueError:
                        pass
        except FileNotFoundError:
            print(f"Error: {input_file_path} not found.")
            return

        with open(output_file_path, 'w') as file:
            for number in sorted(unique_numbers):
                file.write(f"{number}\n")

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Processed {input_file_path} at {current_time}. Output written to {output_file_path}.")

if __name__ == "__main__":
    input_folder = os.path.join(os.path.dirname(__file__), '../../sample_inputs/')
    output_folder = os.path.join(os.path.dirname(__file__), '../../sample_results/')

    input_files = glob.glob(os.path.join(input_folder, '*.txt'))

    for file_path in input_files:
        file_name = os.path.basename(file_path)
        output_file_path = os.path.join(output_folder, f'{file_name}_results.txt')
        IntegerProcessor.handle_files(file_path, output_file_path)

    memory_used = sys.getsizeof(IntegerProcessor)
    print(f"Total memory used by the script: {memory_used} bytes.")
