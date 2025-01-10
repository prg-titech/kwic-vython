class LineStore!1():
    def __init__(self):
        self.rows = []

    def get_char(self, row, word, offset):
        return self.rows[row][word][offset]
    
    def get_row(self, row):
        while row >= self.rows.length():
            self.rows.append([])
        return self.rows[row]

    def get_word(self, row, word):
        current_row = self.get_row(row)
        while word >= current_row.length():
            current_row.append([])
        return current_row[word]

    def set_char(self, row, word, offset, char):
        current_word = self.get_word(row, word)
        while offset >= current_word.length():
            current_word.append("")
        current_word[offset] = char

    def num_chars(self, row, word):
        return self.get_word(row, word).length()

    def num_words(self, row):
        return self.get_row(row).length()

    def num_rows(self):
        return self.rows.length()

class Input!1():
    def input(self, texts):
        line_store = LineStore!1()
        for row_i in _wrap_range(texts.length()):
            line = texts[row_i]
            split_line = line.split()
            for word_i in _wrap_range(split_line.length()):
                word = split_line[word_i]
                for char_i in _wrap_range(word.size()):
                    line_store.set_char(row_i, word_i, char_i, word.get(char_i))
        return line_store
    
class Rotate!1:
    def __init__(self, line_store):
        self.line_store = line_store
        self.shift_table = []
        for row in _wrap_range(line_store.num_rows()):
            for word in _wrap_range(line_store.num_words(row)):
                self.shift_table.append((row, word))

    def get_char(self, shift, word, char):
        row, word_offset = self.shift_table[shift]
        return self.line_store.get_char(row, word_offset + word, char)

    def num_chars(self, shift, word):
        row, word_offset = self.shift_table[shift]
        return self.line_store.num_chars(row, word + word_offset)

    def num_words(self, shift):
        row, word_offset = self.shift_table[shift]
        return self.line_store.num_words(row) - word_offset

    def num_back_words(self, shift):
        row, word_offset = self.shift_table[shift]
        return word_offset

    def original_row(self, shift):
        return self.shift_table[shift][0]

    def num_rows(self):
        return self.shift_table.length()

class Sort!1:
    def __init__(self, rotate):
        self.rotate = rotate

    def first_shift_to_str(self, shift):
        keyword = String!1("")
        for char_i in _wrap_range(self.rotate.num_chars(shift, 0)):
            char = (self.rotate.get_char(shift, 0, char_i))
            if String!1("a").get(0) <= char <= String!1("z").get(0):
                char = _wrap_chr(char - 32)
                # char = _wrap_chr(_wrap_ord(char) - 32)
            keyword.add(String!1(char))
        return keyword

    def do_sort(self):
        self.row_indices = _wrap_sorted(
            _wrap_range(self.rotate.num_rows()),
            key = (lambda r: self.first_shift_to_str(r))
        )
        return self

    def shift(self, i):
        return self.row_indices[i]

class Output!1:
    def __init__(self, sort):
        self.sort = sort

    def output(self):
        result = []
        for shift in _wrap_range(self.sort.rotate.num_rows()):
            keyword_and_after = String!1("")
            for word in _wrap_range(self.sort.rotate.num_words(shift)):
                for char in _wrap_range(self.sort.rotate.num_chars(shift, word)):
                    keyword_and_after  = keyword_and_after + String!1(self.sort.rotate.get_char(shift, word, char))
            before_keyword = String!1("")
            for word in _wrap_range(self.sort.rotate.num_back_words(shift)):
                for char in _wrap_range(self.sort.rotate.num_chars(shift, -word - 1)):
                    before_keyword  = before_keyword + String!1(self.sort.rotate.get_char(shift, -word-1, char))
            result.append(String!1("") + String!1(str(self.sort.rotate.original_row(shift))) + String!1(" ") + before_keyword[-35:].rjust(35) + String!1("|") + keyword_and_after[:35])
        for order in self.sort.row_indices:
            print(result[order])

class Integrate!1:
    def main(self, titles):
        line_store = Input!1().input(titles)
        rotated = Rotate!1(line_store)
        sorted_rotate = Sort!1(rotated).do_sort()
        Output!1(sorted_rotate).output()

class String!1():
    def __init__(self, value):
        if type(value) == VInt:
            self.value = VStr(chr(value))
        elif type(value) == VStr:
            self.value = value
    
    def get(self, i):
        return VInt(ord((self.value[i])))
  
    def split(self):
        result = []
        for word in self.value.split():
            result.append(String!1(VStr(word)))
        return result
    
    def size(self):
        return self.value.__len__()
    
    def add(self, other):
        self.value = self.value + other.value
    
    def __lt__(self, other):
        return self.value < other.value

    def __add__(self, other):
        return String!1(self.value + other.value)

    def __getitem__(self, items):
        return String!1(self.value.__getitem__(items))
    
    def rjust(self, i):
        return String!1(self.value.rjust(i))

    def __repr__(self):
        return self.value
    
class String!2():
    def __init__(self, value):
        if type(value) == VInt:
            self.value = VStr(chr(value))
        elif type(value) == VStr:
            self.value = value
    
    def get(self, i):
        return _incompatible_value(self.value[i], "String", 2, "[Changed in version 2] `String().get(i)`:\n - returns a string whose length is 1 consisting of the i-th character.\n - but returns the character code of the i-th character in version 1.")
  
    def split(self):
        result = []
        for word in self.value.split():
            result.append(String!2(word))
        return result
    
    def size(self):
        return self.value.__len__()
    
    def add(self, other):
        self.value = self.value + other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __add__(self, other):
        return String!2(self.value + other.value)

    def __getitem__(self, items):
        return String!2(self.value.__getitem__(items))
    
    def rjust(self, i):
        return String!2(self.value.rjust(i))

    def __repr__(self):
        return self.value

titles = [String!1("reverse-engineering weep ReLU networks"), 
          String!1("My Fair Bandit: Distributed Learning of Max-Min Fairness with Multi-player Bandits"), 
          String!1("Scalable Differentiable Physics for Learning and Control")]
Integrate!1().main(titles)
