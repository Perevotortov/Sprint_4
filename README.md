# Sprint_4
## Настройка проекта
```pip install virtualenv``` установка virtualenv  
```virtualenv venv``` создание окружения  
```venv/Scripts/activate.bat``` активация окружения  
```pip install -r requirements.txt```  установка зависимостей из файла
## Структура проекта 
В файл ```conftest``` содержит фикстуры для тестов  
В файл ```pages``` поместил страницы для тестов
В файл ```locators``` поместил локаторы
В файл ```tests``` поместил тесты заказа и вопросов на главной странице, а также проверки кнопок Яндекс и Самокат  

## Запуск тестов
```python -m pytest tests -v```  - простой запуск  
```pytest tests --alluredir=allure_results``` - запуск с отчетом allure  
```allure serve allure_results``` - получение отчета

