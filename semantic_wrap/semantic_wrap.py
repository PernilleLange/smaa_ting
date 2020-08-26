import re
import sys



def semantic_wrap(incoming):
    outgoing = re.sub(r'([.!?])(\"*) +', r'\1\2\n', incoming)
    return outgoing

def semantic_wrap_file(file_path):
    with open(file_path) as text_file:
        return semantic_wrap(text_file.read())

if __name__ == "__main__":
    sys.stdout.write(semantic_wrap_file(sys.argv[-1]))
    #print(semantic_wrap_file(sys.argv[-1]))
# test = 'No quotes. This sentence has "quoted text." This one does not.'
# print(semantic_wrap(test))
# print(type(open(input_file, 'r').read()))

