i = 32
cnt_in_line = 1
while i <= 127:
    if cnt_in_line % 10 != 0:
        print(f'"{i}-{chr(i)}"', end=' ')
    else:
        print(f'"{i}-{chr(i)}"', end='\n')
    i += 1
    cnt_in_line += 1
