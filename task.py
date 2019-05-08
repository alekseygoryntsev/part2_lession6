# 1. Создайте классы Noun и Verb.
# 2. Настройте наследование от Word.
# 3. Добавьте защищенное свойство «Грамматические характеристики».
# 4. Перестройте работу метода show класса Sentence.
# 5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.

class Word:
    def __init__(self, text='', part_of_speech='', grammar_parametrs=''):

        self.text = text
        self.part_of_speech = part_of_speech
        self.__grammar_parametrs = grammar_parametrs
    def get_params(self):
        return self.__grammar_parametrs

class Noun(Word):
    def __init__(self, text, grammar_parametrs='', part_of_speech='существительное'):
        super().__init__(text, part_of_speech, grammar_parametrs)

class Verb(Word):
    def __init__(self, text, grammar_parametrs='', part_of_speech='глагол'):
        super().__init__(text, part_of_speech, grammar_parametrs)

class Sentence:
    def __init__(self, content=[], words_list=[]):
        self.content = content
        self.words_list = words_list

    def show(self):
        result = [self.words_list[i].text for i in self.content]
        str_result = ' '.join(result).capitalize()
        return str_result
    def show_parts(self):
        res_list = []
        for i in self.content:
            mass_el = self.words_list[i].get_params().split(', ')
            for el in mass_el:
                res_list.append(el)

        result = set(res_list)
        str_result = 'Грамматические характеристики: %s.' % ', '.join(result)
        return str_result

obj_sentence = Sentence([2, 1, 0], [Noun('раму', 'род, число, падеж, склонение'), \
Verb('мыла', 'число, время, наклонение'), Noun ('мама', 'род, число, падеж, склонение')])
print(obj_sentence.show_parts())