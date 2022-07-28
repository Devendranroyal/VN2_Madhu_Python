# Program extracting all columns
# name in Python
import xlrd
from heapq import nlargest

loc = "matches.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

col_names = []
season_data = {}
# For row 0 and column 0
sheet.cell_value(0, 0)

for i in range(sheet.ncols):
    col_names.append(sheet.cell_value(0, i))
# print(col_names)

sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
season_data = {}
for row_no in range(1, sheet.nrows):
    # print(sheet.row_values(row_no))
    li = sheet.row_values(row_no)
    for each in range(0, len(li)):
        if each in [0, 1, 9, 11, 12]:
            li[each] = int(li[each])
    if li[1] not in season_data.keys():
        season_data[li[1]] = [li]
    else:
        season_data[li[1]].append(li)

for k, v in season_data.items():
    print(k, v)
print("==========")

# Q1 : Top 4 Winners for each season
# Q2 : Man of the match in each season
