from openpyxl import load_workbook
wb=load_workbook('p1.xlsx')

sheet=wb.worksheets[0]

# find the cell and change the value
cell_1=sheet.cell(1,1)
cell_1.value='new start'

# save the change to p2
wb.save("day10/p2.xlsx")