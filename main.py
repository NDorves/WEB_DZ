# # This is a sample Python script.
#
# # Press Umschalt+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask!"



@app.route('/user/<name>')
def show_user_profile(name):
    return f'User {name}'


if __name__ == '__main__':
    app.run(debug=True)
