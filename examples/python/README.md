This is a simple python script capable of accessing the ScrumDo API via HTTP Basic authentication.

It is released under the MIT License and is suitable as either a reference or a starting point for your applications.

Usage
=====

1. Optional: First, get set up a python virtual environment

    virtualenv env

2. Set up the requirements

    pip install -r requirements.txt

3. Create a local settings file.

    cp local_settings.example local_settings.py

4. Edit local_settings.py to include your authentication information

5. Run the script

    python scrumdo_example.py


MIT License
===========

Copyright (c) 2012 ScrumDo LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.