
from view import View

class Controller:

    input_text = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '(', ')', '+', '-', '*', '/']
    
    def __init__(self):
        self.view = View()

        self.is_new_expression = True
        self.is_result = False
        self.expression = ''
        self.result = ''

        self.setup_button()
        
        
    def setup_button(self):
        '''
        Assign command to all buttons 
        '''
        for btn in self.view.buttons:
            btn['command'] = (lambda txt = btn['text'] : self.button_action(txt))



    def button_action(self, button_name):
        '''
        Perform function accordingly whenever a button is clicked
        '''
        # print(text)
        if button_name in self.input_text:
           self.input(button_name)

        if button_name == '=':
            self.equal()
        
        if button_name == 'C':
            self.clear_calculator()
            


    def input(self, button):
        '''
        Function performed when an input button is clicked
        '''
        if button not in ['+', '-', '*', '/']:
            self.save_expression(button)
        else:
            self.operator()
            self.save_expression(button)
        self.view.insert_expression(self.expression)


    def save_expression(self, text):
        '''
        Save input expression
        '''
        # print(self.new_expression)
        if self.is_new_expression:
            self.expression = text
            self.is_new_expression = False
        else:
            self.expression += text


    def operator(self):
        if self.is_result:
            self.expression = self.result
            self.is_new_expression = False
            self.is_result = False
        else:
            self.is_new_expression = False



    def equal(self):
        '''
        Function performed when equal button is clicked
        '''
        self.evaluate(self.expression)
        # self.view.insert_result(self.result)
        self.is_new_expression = True
        self.is_result = True


    def evaluate(self, expression):
        '''
        Calculate the result of entered expression
        '''
        try:
            self.result = str(eval(expression))
            self.view.insert_result(self.result)
        except SyntaxError:
            self.view.insert_result('Syntax Error')
            self.is_new_expression = True
            self.is_result = False




    def clear_calculator(self):
        '''
        Function performed when Clear button is clicked
        '''
        self.is_new_expression = True
        self.result = ''
        self.expression = ''
        self.view.insert_result(self.result)
        self.view.insert_expression(self.expression)


    def start_app(self):
        self.view.init_display()


def main():
    controller = Controller()
    controller.start_app() 


if __name__ == '__main__':
    main()