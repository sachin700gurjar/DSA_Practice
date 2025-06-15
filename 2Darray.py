rows = int(input("Enter row value:"))
cols = int(input("Enter col values:"))
arr = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input("Enter the element:"))
        row.append(val)
    arr.append(row)
print("\nfull array--")
for i in arr:
    print(i)
print("\nrow wise sum--")
for i in range(rows):
    print(f"sum of row {i}:{sum(arr[i])}")
print("\ncolumn wise sum--")
for j in range(cols):
    col_sum = 0
    for i  in range(rows):
        col_sum+=arr[i][j]
    print(f"sum of column {j}:{col_sum}")
print("\nTranspose array--")
Transpose = []
for j in range(cols):
    new_arr = []
    for i in range(rows):
        new_arr.append(arr[i][j])
    Transpose.append(new_arr)
for a in Transpose:
    print("\n Transpose matrix:",a)
