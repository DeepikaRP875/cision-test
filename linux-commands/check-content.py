import subprocess

class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def process_file(self):
        try:
            # Fetch the file content
            with open(self.filename, 'r') as file:
                content = file.read()
                print(f"Original Content: {content}")

            # Use grep to find the value 'deepika'
            grep_result = subprocess.run(['grep', '-o', 'deepika', self.filename], capture_output=True, text=True)
            if grep_result.returncode != 0:
                print("The word 'deepika' was not found in the file.")
            else:
                print(f"Grep Result: {grep_result.stdout.strip()}")

                # Use tr to delete vowels in 'deepika'
                tr_result = subprocess.run(f"echo {grep_result.stdout.strip()} | tr -d 'eiou'", capture_output=True, text=True, shell=True)
                print(f"Tr Result: {tr_result.stdout.strip()}")

                # Use awk to format the output
                awk_command = f"awk '{{gsub(\"deepika\", \"{grep_result.stdout.strip()} {tr_result.stdout.strip()}\"); print}}' {self.filename}"
                awk_result = subprocess.run(awk_command, capture_output=True, text=True, shell=True)
                print(f"Awk Result: {awk_result.stdout.strip()}")

                # Use sed to append 'senior devsecops engineer' to the same line
                sed_command = f"echo \"{awk_result.stdout.strip()}\" | sed 's/{grep_result.stdout.strip()}.*/& senior devsecops engineer/'"
                sed_result = subprocess.run(sed_command, capture_output=True, text=True, shell=True)
                print(f"Final Content: {sed_result.stdout.strip()}")

        except FileNotFoundError:
            print(f"The file '{self.filename}' was not found. Please make sure the file exists in the current directory.")

processor = FileProcessor('test-content.txt')

# Process the file
processor.process_file()