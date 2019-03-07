from openpyxl import load_workbook

def write_to_excel(col="D",row=1,result="Skip"):
    # 写Excel2007文件
    wb=load_workbook("../report/test_case.xlsx")
    # 打开login sheet页
    sheet=wb["login"]

    # 测试结果写入Excel文件
    sheet[col+str(row)]=result
        
    # 保存退出
    wb.save("../report/test_case.xlsx")
    wb.close()

