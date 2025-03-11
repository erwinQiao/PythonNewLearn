"""
KitName: mergePDF
Author: Qiao
Version: 0.1
Date: 2025/3/11
"""
import os
from pypdf import PdfWriter

def merge_pdfs(pdf_folder, output_path):
    # create a Pdfwriter 对象
    pdf_writer = PdfWriter()

    # get all pdf file
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    if pdf_files:
        # 遍历所有PDF文件，其添加到PdfWriter
        for pdf_file in pdf_files:
            pdf_path = os.path.join(pdf_folder,pdf_file)
            print(f'正在合并{pdf_file}')
            with open(pdf_path,'rb') as file:
                pdf_writer.append(file)

        with open(output_path,'wb') as output_file:
            pdf_writer.write(output_file)
        print(f'合并完成，文件保存在:{output_path}')
    else:
        print("请检查文件夹中是否有pdf文件!")

if __name__ == '__main__':
    pdf_folder = "D:\\pythonLearn\\pythonProject\\pdf"
    output_path="D:\\pythonLearn\\pythonProject\\pdf\\merge.pdf"
    merge_pdfs(pdf_folder, output_path)
