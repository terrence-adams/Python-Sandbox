__author__ = 'adam0954'


class Documentation:

    def write_dir(self, x):
        pyObj = x
        with open('{}.txt'.format(pyObj), 'w') as dir_functions:
            for i in dir(x):
                dir_functions.writelines(i)
                dir_functions.write('\n')


if __name__ == '__main__':
    d = Documentation()
    d.write_dir('type')