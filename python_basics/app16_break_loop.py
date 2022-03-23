# break statement ends current loop and jumps to the statement after the loop

while True :    # <-- infinite loop bc of True
    line = input('>')
    if line == 'done' :
        break
    print(line)
print('Done')