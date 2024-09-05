import PyPDF2 as pypdf

file1 = input("Enter the 1 pdf file name: ")
file2 = input("Enter the 2 pdf file name: ")
pdf_files = [file1, file2]
merger = pypdf.PdfMerger()
for filename in pdf_files:
    files = open(filename, 'rb')
    pdfReader = pypdf.PdfReader(files) 
    merger.append(pdfReader)
files.close()
merger.write('merged.pdf')