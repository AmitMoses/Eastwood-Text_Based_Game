import Sentences


def input_check(user_input, valid_vec, text, text_check=True):
    # print(valid_vec)
    # print(user_input)
    if text_check:      # string to string input
        valid_vec = [str(item).lower() for item in valid_vec]
        user_input = user_input.lower()
        while user_input not in valid_vec:
            Sentences.instruction('please enter valid input')
            user_input = input(text).lower()
    else:               # string to int input
        while user_input not in [str(x) for x in range(1, len(valid_vec)+1)]:
            Sentences.instruction('please enter valid input')
            user_input = input(text)
        user_input = int(user_input)
    return user_input


def input_commend(valid_vec, text, show_options=True, text_check=True, getback=True):
    text = text + "\n>"
    if getback:
        valid_vec.append('Return to the town square')
    if show_options:
        options_list(valid_vec)
    answer = input(text)
    answer = input_check(answer, valid_vec, text, text_check)
    return answer


def options_list(names):
    for i in range(0, len(names)):
        print("{}.  {}".format(i+1, names[i]))
