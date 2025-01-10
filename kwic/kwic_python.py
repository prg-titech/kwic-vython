class LineStore():
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

class Input():
    def input(texts):
        line_store = LineStore()
        for row_i in range(len(texts)):
            line = texts[row_i]
            split_line = line.split()
            for word_i in range(len(split_line)):
                word = split_line[word_i]
                for char_i in range(word.size()):
                    line_store.set_char(row_i, word_i, char_i, word.get(char_i))
        return line_store
    
class Rotate:
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

class Sort:
    def __init__(self, rotate):
        self.rotate = rotate

    def first_shift_to_str(self, shift):
        keyword = String_1("")
        for char_i in range(self.rotate.num_chars(shift, 0)):
            char = (self.rotate.get_char(shift, 0, char_i))
            if String_1("a").get(0) <= char <= String_1("z").get(0):
                char = (char) - (32)
            keyword.add(String_1(char))
        return keyword

    def do_sort(self):
        self.row_indices = sorted(
            range(self.rotate.num_rows()),
        key = (lambda r: self.first_shift_to_str(r))
        )
        print(self.row_indices)
        return self

    def shift(self, i):
        return self.row_indices[i]

class Output:
    def __init__(self, sort):
        self.sort = sort

    def output(self):
        result = []
        for shift in range(self.sort.rotate.num_rows()):
            keyword_and_after = "".join(
                "".join(chr(self.sort.rotate.get_char(shift, word, char))
                        for char in range(self.sort.rotate.num_chars(shift, word)))
                for word in range(self.sort.rotate.num_words(shift))
            )
            print(keyword_and_after)
            before_keyword = "".join(
                "".join(chr(self.sort.rotate.get_char(shift, -word - 1, char))
                        for char in range(self.sort.rotate.num_chars(shift, -word - 1)))
                for word in range(self.sort.rotate.num_back_words(shift))
            )
            result.append(f"{self.sort.rotate.original_row(shift):5} {before_keyword[-35:].rjust(35)}|{keyword_and_after[:35]}")
        for order in self.sort.row_indices:
            print(result[order])

class Integrate:
    def main(self, titles):
        line_store = Input.input(titles)
        rotated = Rotate(line_store)
        sorted_rotate = Sort(rotated).do_sort()
        Output(sorted_rotate).output()

class String_1():
    def __init__(self, value):
        if type(value) == int:
            self.value = chr(value)
        elif type(value) == str:
            self.value = value
    
    def get(self, i):
        if(i < 0):
            return 0
        if(len(self.value) <= i):
            return 0
        return ord((self.value[i]))
  
    def split(self):
        result = []
        for word in self.value.split():
            result.append(String_1(word))
        return result
    
    def size(self):
        return len(self.value)
    
    def add(self, other):
        self.value += other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
class String_2():
    def __init__(self, value):
        if type(value) == int:
            self.value = chr(value)
        elif type(value) == str:
            self.value = value
    
    def get(self, i):
        if(i < 0):
            return 0
        if(len(self.value) <= i):
            return 0
        return (self.value[i])
  
    def split(self):
        result = []
        for word in self.value.split():
            result.append(String_2(word))
        return result
    
    def size(self):
        return len(self.value)
    
    def add(self, other):
        self.value += other.value
    
    def __lt__(self, other):
        return self.value < other.value 

if __name__ == "__main__":
    titles = [String_1("reverse-engineering weep ReLU networks"), String_1("My Fair Bandit: Distributed Learning of Max-Min Fairness with Multi-player Bandits"), String_1("Scalable Differentiable Physics for Learning and Control")]
    # titles_books = [String_1("Reverse-engineering deep ReLU networks"), String_1("Hi")]
    # titles = titles_papers + titles_books
    # titles = [String_2("Reverse-engineering deep ReLU networks")]
    Integrate().main(titles)
