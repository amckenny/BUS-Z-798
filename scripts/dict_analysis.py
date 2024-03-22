import functools
from collections import Counter

# Dictionary/rule-based coding
def read_dictionary(filename: str) -> list:
    with open(filename, "r") as infile:
        dict_data = infile.readlines()

    i = 0
    for idx, line in enumerate(dict_data):
        dict_data[idx] = line.strip()
        if dict_data[idx] in ("#1-MEMO#", "#2-METADATA#", "#3-WORDLIST#", "###"):
            i += 1

    if i < 4:
        raise ValueError("CAT Scanner 1.0 .dict file is malformed (missing one or more sections). Cannot import.")

    segments_processed = {"#1-MEMO#": False, "#2-METADATA#": False, "#3-WORDLIST#": False}
    current_segment = None
    var_name = None
    title = None
    memo = ""
    word_list = {'words':[]}
    error_msgs = ""

    for line in dict_data:
        if "#1-MEMO#" in line:
            current_segment = "#1-MEMO#"
            segments_processed["#1-MEMO#"] = True
        elif "#2-METADATA#" in line:
            current_segment = "#2-METADATA#"
            segments_processed["#2-METADATA#"] = True
        elif "#3-WORDLIST#" in line:
            current_segment = "#3-WORDLIST#"
            segments_processed["#3-WORDLIST#"] = True
        elif "###" in line:
            break
        elif current_segment == "#1-MEMO#":
            memo = memo + line + "\n"
        elif current_segment == "#2-METADATA#":
            if "title=" in line:
                title = line[line.find('"') + 1:-1].strip()
            elif "variable_name=" in line:
                var_name = line[line.find('"') + 1:-1].strip()
        elif current_segment == "#3-WORDLIST#":
            try:
                if line.count('"') == 2:
                    word_list['words'].append(line.replace('"', '').strip().lower())
                else:
                    if len(line.strip()) > 0:
                        error_msgs += f"\nWordlist line {line} could not be processed - " \
                                      f"Improper number of quotation marks."
            except ValueError as e:
                error_msgs += f"\nWordlist line {line} could not be processed - {str(e)}"

    if False not in segments_processed.values() and title is not None and var_name is not None and len(word_list) > 0:
        word_list.update({"memo": memo.strip(), "filename": filename, "title": title, "var_name": var_name})
    else:
        if False in segments_processed.values():
            error_msgs += "\nOne or more segments could not be processed."
        if title is None:
            error_msgs += "\nTitle metadata could not be processed."
        if var_name is None:
            error_msgs += "\nVariable Name metadata could not be processed."
        if len(word_list) == 0:
            error_msgs += "\nWordlist segment was empty."

        raise ValueError(f"CAT Scanner 1.0 .dict file is malformed: {error_msgs}\nImport failed.")

    return word_list

# Counts the number of instances of 'wordlist' words in 'tokens'
def get_count(tokens, wordlist):
  text_counter = Counter(tokens)
  return functools.reduce(lambda a,b: a+b, [text_counter[word] for word in wordlist])