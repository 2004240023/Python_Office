from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active

ws1 = wb.create_sheet("Mysheet")

ws1 = wb['Mysheet']

cells = ws1['A1':'J10']

i = 1

for row in cells:
    for cell in row:
        cell.value = i
        i += 1

ws['A1'] = 42
# Rows can also be appended
ws.append([1, 2, 3])
# Python types will automatically be converted
import datetime
ws['A2'] = datetime.datetime.now()

# --追加
#for x in range(1,101):
#    for y in range(1,101):
#        ws.cell(row=x,column=y)
#a ='A'
#d = 10
#c = a + str(d)
#ws[c] = 10
# Save the file
wb.save("sample.xlsx")
