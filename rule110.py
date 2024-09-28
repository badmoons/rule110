#!/usr/bin/env python3
LINE_LENGTH = 80
first_line = ""
for i in range(LINE_LENGTH):
    if i != LINE_LENGTH-1:
        first_line = first_line + "."
    else:
        first_line = first_line + "*"

# uncomment to get 40 char long line or customize yourself.
# first_line = ".*....................................*."
patterns = {
    "...": ".",
    "..*": "*",
    ".*.": "*",
    ".**": "*",
    "*..": ".",
    "*.*": "*",
    "**.": "*",
    "***": ".",
}

def rule110_recursive(prev_line, max_depth=10, depth=0):
    if depth >= max_depth:
        return
    global patterns
    print(prev_line)
    new_line = prev_line
    for x in range(len(prev_line)-1):
        if x == 0:
            continue
        else:
            current_pattern = f"{prev_line[x-1]}{prev_line[x]}{prev_line[x+1]}"
            if current_pattern in patterns:
                # print(patterns[current_pattern])
                new_line = new_line[:x] + patterns[current_pattern] + new_line[x+1:]
    print(new_line)
    rule110_recursive(new_line, max_depth, depth + 1)

rule110_recursive(first_line, 80)
