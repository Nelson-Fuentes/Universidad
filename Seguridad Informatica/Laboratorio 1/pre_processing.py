import string


def _get_file_content(filename: str):
    file = open(filename, 'r')
    file_content = file.read()
    return file_content


def _replacing(file_content: str, f: str, t: str):
    return file_content.replace(f, t)


def _replacing_various(file_content: str, changes: list):
    for change in changes:
        file_content = _replacing(file_content, change[0], change[1])
    return file_content


def _deleting_tildes(file_content):
    changes = [['á', 'a'], ['é', 'e'], ['í', 'i'], ['ó', 'o'], ['ú', 'u']]
    file_content = _replacing_various(file_content, changes)
    return file_content


def _delete_blank_spaces(file_content: str):
    changes = [[' ', ''], ['\n', '']]
    return _replacing_various(file_content, changes)


def _deleting_punctuation_marks(file_content):
    punctuation_marks = string.punctuation + "¿¡"
    for char in punctuation_marks:
        file_content = file_content.replace(char, '')
    return file_content


def _alphabet(file_content: str):
    alphabet = []
    for char in file_content:
        if not char in alphabet:
            alphabet.append(char)
    return alphabet


def _save_file(filemane, file_content):
    f = open(filemane, "w")
    f.write(file_content)
    f.close()


if __name__ == '__main__':
    filename = 'poem.txt'
    file_content = _get_file_content(filename)
    changes = [['j', 'i'], ['h', 'i'], ['ñ', 'n'], ['k', 'l'], ['u', 'v'], ['w', 'v'], ['y', 'z'], ['x', 'r']]
    file_content = _replacing_various(file_content, changes)
    file_content = _deleting_tildes(file_content)
    file_content = file_content.lower()
    file_content = _delete_blank_spaces(file_content)
    file_content = _deleting_punctuation_marks(file_content)
    alphabet = _alphabet(file_content)
    new_file_name = 'POEMA_PRE.TXT'
    _save_file(new_file_name, file_content)
    print('File saved')
    print('ALFABETO:', alphabet, 'Longitud' ,len(alphabet))
