class Text:
    def __init__(self, pos, char):
        self.pos = pos
        self.char = char
    def get_pos(self):
        return self.pos
    def set_pos(self, new_pos):
        self.pos = new_pos
    def set_char(self, new_char):
        self.char = new_char
    def get_char(self):
        return self.char

def give_range_blocks(txts : list[Text]) -> list[tuple[int, int]]:
    "{{} {}}"
    res = []
    stack = []
    for txt in txts:
        if txt.get_char() == '}':
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                raise Exception
        stack.append(txt.get_pos())
    return res

def num_indents(text : str, cursor_pos : int) -> int:
