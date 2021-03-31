import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename = "sample.xlsx")
wb.active = 0
sheet = wb.active
i = 1
print(sheet['A'+ str(i)].value)
while(str(sheet['A'+ str(i)].value) != 'None'):
    i=i+1
    print(sheet['A'+ str(i)].value)
print(str(i))
number = i-2 #кількість учасників
test = 'sample82'
c = 2 #counter
while ((str(sheet['B'+ str(c)].value) != test) and c<15):
    c=c+1
print(str(c))
if(c==15):
    print('ви не рееструвалися на обмін')
else:
    print(sheet['E'+ str(c)].value)
