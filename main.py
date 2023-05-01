import requests
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


# Определение класса главного окна приложения
class MainApp(App):
    
    # Обработчик кнопки запуска отправки запросов
    def run_requests(self, button):
        self.lbl_output.text = 'Загрузка'
        # Получение ссылок из текстового поля
        urls = self.txt_input.text.split('\n')
        
        # Получение количества запусков из текстового поля
        num_launches = int(self.txt_num_launches.text)
        
        # Очистка поля вывода
        self.lbl_output.text = ''
        
        # Отправка запросов по каждой ссылке
        for url in urls:
            k = 0
            self.lbl_output.text += 'Отправка запросов по ссылке: {}\n'.format(url)
            while k < num_launches:
                response = requests.get(url)
                self.lbl_output.text += 'Ответ сервера: {} {}\n'.format(response.status_code, response.reason)
                if response.status_code == 404:
                    self.lbl_output.text += 'Страница не найдена.\n'
                    break
                time.sleep(1)
                k += 1
        
        # Вывод сообщения о завершении работы
        self.lbl_output.text += 'Готово. Код выполнен.\n'
    
    
    # Метод создания графического интерфейса
    def build(self):
        
        # Создание главного контейнера и установка его свойств
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Создание текстового поля для ввода ссылок
        self.txt_input = TextInput(multiline=True, hint_text='Введите ссылки для посещения', size_hint=(1, 0.7))
        root.add_widget(self.txt_input)
        
        # Создание текстового поля для ввода количества запусков
        self.txt_num_launches = TextInput(hint_text='Количество запусков сайта', size_hint=(1, 0.2))
        root.add_widget(self.txt_num_launches)
        
        # Создание кнопки запуска отправки запросов
        btn_run = Button(text='Запустить', size_hint=(1, 0.1))
        btn_run.bind(on_press=self.run_requests)
        root.add_widget(btn_run)
        
        # Создание поля вывода результатов
        self.lbl_output = Label(text='', size_hint=(1, 1))
        root.add_widget(self.lbl_output)
        
        return root

# Запуск главного окна приложения
if __name__ == '__main__':
    MainApp().run()
