class myclass:
    __privateVar=27
    def __privMeth(self):
        print("i'm inside class myclass")
    def hello(self):
        print("private variable value:",myclass.__privateVar)

foo=myclass()
foo.hello()
foo.__privMeth()