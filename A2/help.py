def do_spambase():

    # Some chars aren't allowed in python
    blacklist_chars = {
        ';': "semicolon",
        '(': 'l_parenth',
        '[': 'l_bracket',
        '!': 'exclaim_point',
        '$': 'dollar_sign',
        '#': 'hashtag'
    }

    constant_defs = ''
    arr_def = 'columns = [\n'
    clean_name_translate_table = 'clean_names = {\n'
    with open('dummy.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:

            # Extract the var name
            var_name = line.split(':')[0]  # The variable in python code
            var_string = line.split(':')[0]  # the string representation
            for blist_char in blacklist_chars.keys():
                if blist_char in var_name:
                    var_name = var_name.replace(blist_char, blacklist_chars[blist_char])

            constant_defs += f"{var_name.upper()} = '{var_string}'\n"
            arr_def += f"\t{var_name.upper()},\n"

            split_words = var_string.split('_')
            # If freq is in it,
            if 'word_freq' in var_name or 'char_freq' in var_name:
                clean_name = f"Frequency of '{split_words[2]}'"
            # If run length is in it,
            elif 'run_length' in var_name:
                type = split_words[-1].title()
                clean_name = f"{type} Caps Running Length"
            else:
                raise Exception(f"Failed to parse string '{line}'")

            clean_name_translate_table += f"\t{var_name.upper()}: \"{clean_name}\",\n"

    arr_def += ']'
    clean_name_translate_table += '}'

    print(constant_defs)
    print(arr_def)
    print(clean_name_translate_table)


def do_nba():

    arr_def = 'NBA_COLUMNS = [\n'
    clean_names = 'NBA_CLEAN_NAMES = {\n'
    with open('dummy2.txt', 'r') as f:

        lines = f.readlines()

        for line in lines:
            var_name = line.split('=')[0].strip()

            arr_def += f'\t{var_name},\n'

            if 'DIFF' in var_name:
                clean = var_name.replace('_', ' ').replace('MADE', '').replace('DIFF', 'difference').title().strip()
            elif '_A' in var_name and var_name != 'TEAM_A':
                clean = var_name.replace('_', ' ').replace('MADE', '').replace(' A', '').title().strip()
                clean = 'A Team ' + clean
            else:
                clean = var_name.replace('_', ' ').title().strip()

            clean = clean.replace('  ', ' ')
            clean = clean.replace('Perc', '%')


            clean_names += f'\t{var_name}: "{clean}",\n'

    arr_def += ']'
    clean_names += '}'

    print(arr_def)
    print(clean_names)


do_nba()