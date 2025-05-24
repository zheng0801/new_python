
class AnonymousSurvey:
    '''收集匿名调查问卷答案'''

    def __init__(self, question):
        '''存储一个问题，并未存储答案做准备'''
        self.question = question
        self.responses = []

    def show_question(self):
        #显示调查问卷
        print(self.question)

    def store_response(self, new_response):
        '''存储单份调查答卷'''
        self.responses.append(new_response)

    def show_result(self):
        '''显示手机到的所有答卷'''
        print('Survey result: ')
        for response in self.responses:
            print(f'- {response}')












