for i in range(2,40):
    with open(f"tables_Multiplication_table_of_{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}")
            if j!=10:
                f.write('\n')