import random
class File:
    def __init__(self):
        self.type_list = []
        self.length_list = []
        self.file = ''

    def add(self, type_, amount):
        self.type_list.append(type_)
        self.length_list.append(amount)
        print(self.type_list, self.length_list)
    def generate(self):
        for i in range(len(self.type_list)):

            file_list = []

            for element in self.type_list[i]:

                type_ = element[0]
                amount = self.length_list[i]

                if type_ == int:
                    if type(element[1]) == int:
                        range_ = range(element[1])
                    else:
                        range_ = range(*element[1])
                    file_list.append([random.choice(range_) for _ in range(amount)])

                elif type_ == str:
                    str_len = element[1]
                    letter_list = list(map(chr, list(range(65, 91)) + list(range(97, 123))))
                    file_list.append([''.join([random.choice(letter_list) for _ in range(str_len)]) for _ in range(amount)])

            for a in range(len(file_list[0])):
                for b in range(len(file_list)):
                    self.file += f'{file_list[b][a]} '
                self.file += '\n'

        return self.file


if __name__ == '__main__':
    file = File()
    type_dict = {'int': int, 'str': str}
    message_dict = {int: 'Введите range(от 1 до 3-х чисел): ', str: 'Введите длину слова: '}
    type_list = []
    while True:
        s = input('Введите тип(пока что int/str): ').strip()

        if s in type_dict.keys():

            type_ = type_dict[s]
            s = input(message_dict[type_]).split()
            length = 0

            if len(s) == 1:
                length = int(s[0])
            else:
                length = list(map(int, s))

            type_list.append((type_, length))

            s = input('Будет ли еще что-то в строке(y/n)? ').strip()

            if s == 'y':
                pass
            elif s == 'n':
                s = input('Введите кол-во строк: ')
                amount = int(s)
                file.add(type_list, amount)
                type_list = []
                s = input('Делаем файл(введите stop для генерации)? ').strip()
                if s == 'stop':
                    break
            else:
                print('Ошибка ввода, будем считать, что да.')

        else:
            print('Ошибка ввода, попробуйте еще раз.')
    fout = open(input('Название файла(без .txt): ') + '.txt', 'w')
    fout.write(file.generate())
    fout.close()
