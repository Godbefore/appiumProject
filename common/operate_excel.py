from openpyxl import load_workbook
import json

wb=load_workbook("../report/test_case.xlsx")
sheet=wb["login"]
for i in range(1,4):
    sheet["D%s"%i]="PASS"

wb.save("../report/test_case.xlsx")
wb.close()

