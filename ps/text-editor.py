

class TextEditor:

    document = None
    position = 0
    block_size = 0

    def __init__(self):
        self.document = ""
        self.position = 0

    def append(self, text):
        self.document = self.document[:self.position] + text + self.document[self.position+self.block_size:]
        self.position += len(text)
        return self.document

    def move(self, position):
        self.block_size = 0
        if self.position < 0:
            self.position = 0
            return self.document
        if self.position > len(self.document):
            self.position = len(self.document)
            return self.document

        self.position = position
        return self.document

    def delete(self, length=1):
        if self.position == len(self.document):
            return self.document
        self.document = self.document[:self.position] + self.document[self.position+self.block_size+length:]
        return self.document

    def select(self, left, right):
        self.position = left
        if right > len(self.document):
            right = len(self.document)
        self.block_size = right - left



editor = TextEditor()

print(editor.append("Hey you"))
print(editor.append(" all"))
print(editor.move(3))
print(editor.append(","))
print(editor.append(" miss"))
print(editor.delete())
print(editor.move(100))
print(editor.delete())
print(editor.select(5,11))
print(editor.append("REP"))
print(editor.select(10,150))
print(editor.append("yy"))