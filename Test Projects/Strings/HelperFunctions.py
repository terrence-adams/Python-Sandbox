class HelperFunctions:
    """Empty Constructor"""
    def __init__(self):
        pass

    """Declared static, no class parameters set """
    @staticmethod
    def input_and_validation():

        term = input("Please enter a string: ")
        if term is not None:
            return term

    @staticmethod
    def write_to_file(self, string_to_write='', file_name=''):
        my_file = open(file_name, "w")
        my_file.write(string_to_write)
        my_file.close()
    @staticmethod
    def append_to_file(self, string_to_write='', file_name=''):
        my_file = open(file_name, "a")
        my_file.write(string_to_write)
        my_file.close()

    @staticmethod
    def create_new_file(self, file_name=''):
        my_file = open(file_name, "x")
        my_file.close()



if __name__ == "__main__":
    hp = HelperFunctions()
    w = hp.input_and_validation()
    print(w)