import re
import os

class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def process_file(self):
        try:

            file_path = os.path.join('linux-commands', self.filename)

            # Fetch the file content
            with open(file_path, 'r') as file:
                content = file.read()
                print(f"Original Content: {content}")

            # Used re to find the value 'deepika'
            if 'deepika' not in content:
                print("The word 'deepika' was not found in the file.")
            else:
                print("Grep Result: deepika")

                # Used re to delete vowels in 'deepika'
                tr_result = re.sub(r'[eiou]', '', 'deepika')
                print(f"Tr Result: {tr_result}")

                # Used re to format the output (similar to awk)
                awk_result = re.sub(r'deepika', f'deepika {tr_result}', content)
                print(f"Awk Result: {awk_result}")

                # Used re to append 'senior devsecops engineer' to the same line (similar to sed)
                sed_result = re.sub(r'deepika.*', r'\g<0> senior devsecops engineer', awk_result)
                print(f"Final Content: {sed_result}")

        except FileNotFoundError:
            print(f"The file '{self.filename}' was not found. Please make sure the file exists in the 'linux-commands' directory.")

processor = FileProcessor('test-content.txt')

# Process the file
processor.process_file()