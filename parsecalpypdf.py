# https://gist.github.com/nadya-p/373e1dc335293e490d89d00c895ea7b3
import pandas as pd
from pypdf import PdfReader
import os

pdfdir = r"/Users/pm/Documents/projects/calendar/files"

for root,dirs,files in os.walk(pdfdir):
    for file in files:
        path = os.path.join(root,file)
        # print(path)
        name,ext = os.path.splitext(path)
        if ext == '.pdf':
            reader = PdfReader(path)
            # print(len(reader.pages)) 
            number_of_pages = len(reader.pages)
            for pagenum in range(number_of_pages):
                page = reader.pages[pagenum]
                content = page.extract_text()

                exportname = name + ".txt"
                with open(exportname,'w') as exportfile:
                        exportfile.write(content)

            # exportname = name + ".txt"
            # with open(exportname,'w') as exportfile:
