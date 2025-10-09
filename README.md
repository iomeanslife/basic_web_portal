# basic_web_portal

A basic website using Python3 and sqlite with no external packages.

## ❗ Warning

This is just an excersize for educational purposes, and in no way meant to be used in a production setting without serious rework for modern cyber security considerations. Please read the [License](#license) before use.

## Requirements

This project needs both `python3` and `sqlite` installed and accesable in CLI and python code.

## Usage

After cloning the repo, run `main.py` with python in the command line of your choosing. The exact command depends on your operating system and development settings.

``` python3 main.py ```

This will generate a file called `small_database.db` with a table called `user` in which it will store the users the web portal creates.

You may need to adjust `config.ini` for it to work, i.e. use a different port if 8000 is already in use.

## Testing

The file `test_backend_functions.py` contains python unit tests that check if the code for accessing the database is working properly. Running the tests will create a database file called `test_database.db`.

to run all tests from the commandline, run:

``` python3 -m unittest ```

Read [Python documentation: unittest](https://docs.python.org/3/library/unittest.html) for further information.

## Files

Explanation what each of the files does.

### `main.py`

Loads the configuration and starts the server. Also contains the Handler for web requests and basic html to show in the browser.

### `backend_functions.py`

Contains code for accessing the database.

### `test_backend_functions.py`

Python unit tests for `backend_functions.py`

### `config.ini`

Contains configuration required for the server to run. Be considerate of changes upstream when local changes have been made.

## License (The MIT License) {#license}
Copyright 2025 Omar Ajerray

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

