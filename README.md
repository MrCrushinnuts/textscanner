Text Scanner
The text scanner tool is a Python script that allows you to search for a specific line within a text document. It provides a simple and efficient way to find matches and extract relevant information from large files.



Features
    
    • Searches for a specific line within a text document
    • Ignores punctuation and capitalization for more accurate matching
    • Provides the matched line(s) as output



Usage
   1. Ensure that you have Python 3 installed on your system.
   
   2. Clone this repository or download the scanner.py file.
   3. Open a terminal and navigate to the directory where the scanner.py file is located.
 
    4. Run the script using the following command:
       python3 scanner.py <line> <text_document>
       Replace <line> with the line you want to search for, and <text_document> with the path to the text document you want to scan. The script will search for the provided line in the text document and display any matching lines found.

If you encounter any errors related to missing dependencies, make sure to install them using the pip package manager:

pip3 install argparse

pip3 install regex

Please note that the script assumes the input text document is in plain text format.
Feel free to customize and modify the code as needed for your specific use case.
