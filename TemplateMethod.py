from abc import ABC, abstractmethod

def client():
    """ 
    TemplateMethodとは
    テンプレートとなるスーパークラスと、そのクラスを実際に実装するサブクラスで形成されるデザインパターン。
    処理の枠組みと具体的な処理内容を分担させることで、スーパークラスを各サブクラスで継承した時に一貫性が保つことができる。
    また、詳細な処理をサブクラスに任せているため拡張性が高い。


    登場人物 
    ・AbstractClass
    ・ConcreteClass
    """
    charDisplay = CharDisplay("A")
    stringDisplay = StringDisplay("AAAA")

    charDisplay.display()
    stringDisplay.display()

#スーパークラス
#pythonではABCをインポートすることで抽象クラスを使用できる
class AbstractDisplay(ABC):
    #クラスメソッドを書く場合必ず引数にselfを入れる
    @abstractmethod
    def open(self):
        #何もしない
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(5):
            self.print()
        self.close()

#サブクラス
class CharDisplay(AbstractDisplay):
    charWord = None
    def __init__(self, ch):
        self.charWord = ch

    def open(self):
        print("<<")

    def print(self):
        print(self.charWord)

    def close(self):
        print(">>")
 
#サブクラス
class StringDisplay(AbstractDisplay):
    stringWord = None
    width = None
    def __init__(self, str):
        self.stringWord = str
        self.width = len(str)

    def open(self):
        self.printLine()

    def print(self):
        print(self.stringWord)

    def close(self):
        self.printLine()

    def printLine(self):
        print("+", end="")
        for i in range(self.width):
            print("-",end="")
        print("+")


if __name__ == "__main__":
    client()