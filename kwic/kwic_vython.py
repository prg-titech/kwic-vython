class LineStore!1():
    def __init__(self):
        self.rows = []

    def get_char(self, row, word, offset):
        return self.rows[row][word][offset]
    
    def get_row(self, row):
        while row >= len(self.rows):
            self.rows.append([])
        return self.rows[row]

    def get_word(self, row, word):
        current_row = self.get_row(row)
        while word >= len(current_row):
            current_row.append([])
        return current_row[word]

    def set_char(self, row, word, offset, char):
        current_word = self.get_word(row, word)
        while offset >= len(current_word):
            current_word.append("")
        current_word[offset] = char

    def num_chars(self, row, word):
        return len(self.get_word(row, word))

    def num_words(self, row):
        return len(self.get_row(row))

    def num_rows(self):
        return len(self.rows)

class Input!1():
    def input(self, texts):
        line_store = LineStore!1()
        for row_i in range(len(texts)):
            line = texts[row_i]
            split_line = line.split()
            for word_i in range(len(split_line)):
                word = split_line[word_i]
                for char_i in range(word.size()):
                    line_store.set_char(row_i, word_i, char_i, word.get(char_i))
        return line_store
    
class Rotate!1:
    def __init__(self, line_store):
        self.line_store = line_store
        self.shift_table = []
        for row in range(line_store.num_rows()):
            for word in range(line_store.num_words(row)):
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
        return len(self.shift_table)

class Sort!1:
    def __init__(self, rotate):
        self.rotate = rotate

    def first_shift_to_str(self, shift):
        keyword = String!1("")
        for char_i in range(self.rotate.num_chars(shift, 0)):
            char = (self.rotate.get_char(shift, 0, char_i))
            if String!1("a").get(0) <= char <= String!1("z").get(0):
                char = char - 32
            keyword.add(String!1(char))
        return keyword

    def do_sort(self):
        self.row_indices = sorted(
            range(self.rotate.num_rows()),
            key = (lambda r: self.first_shift_to_str(r))
        )
        return self

    def shift(self, i):
        return self.row_indices[i]

class Output!1:
    def __init__(self, sort):
        self.sort = sort

    def output(self):
        print(self.sort.row_indices)

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
    
class String!2():
    def __init__(self, value):
        if type(value) == VInt:
            self.value = VStr(chr(value))
        elif type(value) == VStr:
            self.value = value
    
    def get(self, i):
        return _incompatible_value(VStr(self.value[i]), "String", 2, "[Changed in version 2] `String().get(i)`:\n - returns a string whose length is 1 consisting of the i-th character.\n - but returns the character code of the i-th character in version 1.")
  
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

titles_papers = [String!2("reverse-engineering weep ReLU networks"), String!1("Hi"), String!1("Reverse-engineering deep ReLU networks")]
titles_books = [String!1("Reverse-engineering deep ReLU networks"), String!1("Hi")]
titles = titles_papers + titles_books
Integrate!1().main(titles)
