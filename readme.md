Setup
-----

This assumes a minimalistic dev environment. You can also use Dev Studio's Python plugin if you like.

1. Install python 3.5
1. Create a virtual env 

        cd <project root directory>
        c:\python35-32\python.exe -m venv env

    This will create a virtual env in a directory called 'env'.

1. Activate that virtual env

        env\Scripts\activate.bat

    Your command prompt should now include (env) to indicate that that environment is active. You can also `python --version` to verify that Python 3.5 is in your path.

1. Install the packages required

        pip install -r requirements.txt

1. Run the app

        python runserver.py