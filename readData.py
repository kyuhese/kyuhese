import openpyxl

wb = openpyxl.load_workbook("0805.xlsx")

ws = wb.worksheets[0]

data = ws.cell(row = 1, column = 1)

print(data)