table_number = 0
while table_number <= 10:
    print(f"Table de {table_number}:", end=" ")
    
    multiplier = 0
    while multiplier <= 10:
        print(table_number * multiplier, end=" ")
        multiplier += 1

    print()  
    table_number += 1