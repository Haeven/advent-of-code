def transpose(word_array):
    trie = {}
    for i in range(len(word_array)):
        current = trie
        for c in word_array[i]:
            current = current.setdefault(c, {})
        current["value"] = i + 1

    return trie


def parse_line(line, root):
    result = ""
    current_node = root
    last_char = ''

    for c in line:
        # Check character to be numeric, set accordingly
        if c.isnumeric():
            result += c
            current_node = root
            continue

        if c in current_node:
            # Current character is the follow up to the last character
            current_node = current_node[c]
        else:
            # Last character is not to follow up
            if last_char in root and c in root[last_char]:
                # ...however last char is a starting char, handles edge cases
                current_node = root[last_char][c]
            elif c in root:
                # ... current character is a starting character
                current_node = root[c]

        if 'value' in current_node:
            result += repr(current_node['value'])

        last_char = c

    return result


def get_calibration(line, root):
    numbers = parse_line(line, root)
    if len(numbers) == 1:
        num = int(numbers[0] + numbers[0])
    else:
        num = int(numbers[0] + numbers[-1])
    return num


def main():
    english_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    root = transpose(english_numbers)

    total = 0

    with open("input.txt", 'r') as inf:
        for line in inf:
            total += get_calibration(line, root)

    print(total)


if __name__ == "__main__":
    main()


