class Singleton():
    """ 
    Singletonとは
    あるクラスのインスタンスがアプリケーション全体で”絶対”に一個しかない存在しないことを保証することができる。
    どんな時にこのパターンを使用するかというと、データベースの接続処理やロギング処理など共通のリソースを管理する場合に利用する。
    """     

    instance = None

    #オブジェクトを作成する前に実行される処理
    def __new__(cls):
        if cls.instance is None:
            #Singletonクラスはobjectクラスを継承しているため、super()はobjectを指す
            cls.instance = super().__new__(cls)
            print("インスタンスを作成")
        return cls.instance

def client():
    resultSingletonA = Singleton()
    resultSingletonB = Singleton()

    if(resultSingletonA is resultSingletonB):
        print("同じインスタンスです")
    else:
        print("同じインスタンスではありません")

if __name__ == "__main__":
    client()