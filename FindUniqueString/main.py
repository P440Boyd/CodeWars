from typing import List


def find_uniq(strings: List):
    strings_sorted = [''.join(sorted(string.lower())) for string in strings]
    strings_sorted = [string for string in strings_sorted]
    char_distribution = {}
    for string in strings_sorted: 
        for char in string:
            if char not in char_distribution:
                char_distribution[char] = 0
                char_distribution[char] += 1
            char_distribution[char] += 1
    min_value = min(char_distribution.values())
    letters_with_min_value = [letter for letter, value in char_distribution.items() if value == min_value]
    filtered_strings = [string for string in strings if any(letter in string for letter in letters_with_min_value)]
    return filtered_strings[0]


def main():
    string_lists =[
    [ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ],
    [ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ],
    [ 'Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter' ],
    [ 'foobar', 'barfo', 'fobara', '   ', 'fobra', 'oooofrab' ],
    ]

    for string_list in string_lists:
        print(f"Unique string: '{find_uniq(string_list)}'")

if __name__ == "__main__":
    main()