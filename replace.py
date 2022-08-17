# pip install python-docx 
import docx
import os
from distutils.dir_util import copy_tree


def replace(old_docx, old_info, new_info):
    for para in old_docx.paragraphs:
        for run in para.runs:
            run.text = run.text.replace(old_info, new_info)

    for table in old_docx.tables:
        for row in table.rows:
            for cell in row.cells:
                cell.text = cell.text.replace(old_info, new_info)
