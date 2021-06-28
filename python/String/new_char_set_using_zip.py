"""
Given a 26 letter character set, which is equivalent to character set of English alphabet i.e. (abcd….xyz) and act as
a relation. We are also given several sentences and we have to translate them with the help of given new character set.

Example:
    New character set : qwertyuiopasdfghjklzxcvbnm
    Input : "utta"
    Output : geek

    Input : "egrt"
    Output : code
"""


def get_new_str(new_ch_set, input):
    al_set = 'abcdefghijklmnopqrstuvwxyz'
    char_mapping_dict = dict(zip(new_ch_set, al_set))
    return "".join([char_mapping_dict[c] for c in input])


if __name__ == '__main__':
    new_ch_set = 'qwertyuiopasdfghjklzxcvbnm'
    input = 'utta'
    print(get_new_str(new_ch_set, input))
