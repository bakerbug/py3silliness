import tempfile


class TempFilePractice:

    def temp_file(self, data='My Little Pony'):
        # Mode 'w+' allows for read and write
        file = tempfile.TemporaryFile(mode='w+')
        file.write(data)
        file.seek(0)
        new_data = file.readlines()

        print('Data is: {}'.format(new_data))

    def temp_file_two(self, data="This is my file!"):
        with tempfile.TemporaryFile(mode='w+') as newfile:
            newfile.write(data)
            newfile.seek(0)
            new_data = newfile.read()

            print('Data is: {}'.format(new_data))


if __name__ == '__main__':
    test = TempFilePractice()
    test.temp_file('This is my temp file!')
    test.temp_file_two('There are many like it,')
