# 

text = "X-DSPAM-Confidence:    0.8475"

find_dot = text.find('.')

srt_number = text[find_dot-1:find_dot+5]
float_number = float(srt_number)
print(float_number)