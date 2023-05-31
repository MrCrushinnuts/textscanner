import argparse
import re

def normalize_line(line):
    
    line = re.sub(r'[^\w\s]', '', line).lower()
    
    line = re.sub(r'\s+', '', line)
    return line

def scan_text_document(input_line, text_document):
    with open(text_document, 'r') as file:
        lines = file.readlines()

    
        normalized_input_line = normalize_line(input_line)

        for line in lines:
            
            normalized_line = normalize_line(line)

            if normalized_input_line in normalized_line:
                print(f"Match found: {line.strip()}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Line Scanner Tool')
    parser.add_argument('line', help='line to search for')
    parser.add_argument('text_document', help='path to the text document')

    args = parser.parse_args()

    
    scan_text_document(args.line, args.text_document)
