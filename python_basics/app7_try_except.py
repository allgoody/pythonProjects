# eliminate or catch traceback
# surrount section of code with try and except
# if the try works - except is skipped
# if try fails  - it jumps to except section


astr = input('input something:')
try:
    istr = int(astr)    # traceback here
except:
    istr = -1
print('first', istr)

astr = input('input something again:')
try:
    istr = int(astr)
except:
    istr = -2
print('second', istr)