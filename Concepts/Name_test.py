def MyTestName():
    print("name is __name__",__name__)
print("This is name_test.py")


if __name__=="__main__":
    MyTestName()
    print("called from module")
else:
    print("Module imported in some other files")