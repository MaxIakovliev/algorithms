def excel_column_number_to_name(column_number):
    abx=list()
    index=column_number - 1
    res=""
    while index>=0:
        char=chr(int(index%26) +ord('A'))
        index=index/26-1
        res=char+res
    return res

for i in range(950):
    print(excel_column_number_to_name(i+1))