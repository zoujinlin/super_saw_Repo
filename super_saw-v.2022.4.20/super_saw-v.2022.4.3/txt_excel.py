import xlwt
import xlrd
import os
txtname = '2022-05-10-09-53-02.txt'
#txtname = savedFile
#excelname = '2022-05-10-09-53-02.xlsx'


excelname = txtname.split('.txt')
excelname=excelname[0]+'.xls'
try:
    with xlrd.open_workbook(excelname) as wb:
        print('excel exist')

except FileNotFoundError:
    # 创建工作簿
    wb = xlwt.Workbook(excelname)
    sh1 = wb.add_sheet('sheet')

fopen = open(txtname, 'r')
lines = fopen.readlines()

file = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 新建一个sheet
sheet = file.add_sheet('data')

i = 0
for line in lines:
    line = line.strip('\n')
    line = line.split('\t')
    a = line[0]
    b = line[1]
    c = line[2]
    d = line[3]
    e = line[4]
    f = line[5]

    sheet.write(i, 0, a)
    sheet.write(i, 1, b)
    sheet.write(i, 2, c)
    sheet.write(i, 3, d)
    sheet.write(i, 4, e)
    sheet.write(i, 5, f)
    i = i + 1

file.save(excelname)
