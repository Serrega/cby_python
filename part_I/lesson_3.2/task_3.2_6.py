digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
address = [digits[-1]*2, digits[0]+symbols[4], digits[7]+symbols[2],
           digits[1]+digits[5], symbols[0]+digits[0], symbols[2]+digits[7]]
print(':'.join(address))
