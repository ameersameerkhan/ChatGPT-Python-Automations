##################################################################################
# Generated on April 12 2023 by ChatGPT Mar 23 Version (GPT 4)
# 
# Prompt: 
#    I have a folder with subfolders containing two pdfs.
#    The first pdf ending in "_details.pdf"
#    The second pdf ending in "_letter.pdf".
#    Create a python program to merge the pdfs ending in "_details.pdf" into a single PDF and to merge the pdfs ending in "_letter.pdf". into another single PDF.
#    The program should able to iterate through all of the subdirectories.
# 
##################################################################################

import os
import PyPDF2

# Function to merge a list of PDFs into a single PDF file
def merge_pdfs(pdf_list, output_name):
    # Create a PdfMerger object
    merger = PyPDF2.PdfMerger()

    # Iterate through the PDF files in the list and append them to the merger object
    for pdf in pdf_list:
        merger.append(pdf)

    # Write the merged PDFs to the output file
    with open(output_name, "wb") as f:
        merger.write(f)

    # Close the merger object
    merger.close()

def main():
    # TODO: Specify the path to the root folder containing the subfolders
    root_folder = './path/to/your/folder'

    # Lists to store the PDF file paths
    details_pdfs = []
    letter_pdfs = []

    # Iterate through the root folder, subfolders, and files
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            # If the file ends with "_details.pdf", add its path to the details_pdfs list
            if file.endswith('_details.pdf'):
                file_path = os.path.join(root, file)
                details_pdfs.append(file_path)
            # If the file ends with "_letter.pdf", add its path to the letter_pdfs list
            elif file.endswith('_letter.pdf'):
                file_path = os.path.join(root, file)
                letter_pdfs.append(file_path)

    # Merge the PDFs in the details_pdfs list and save the result as "merged_details.pdf"
    merge_pdfs(details_pdfs, 'merged_details.pdf')
    # Merge the PDFs in the letter_pdfs list and save the result as "merged_letter.pdf"
    merge_pdfs(letter_pdfs, 'merged_letter.pdf')

if __name__ == '__main__':
    main()
