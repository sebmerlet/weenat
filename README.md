###### Environment: 
    linux, python 3, virtualenv
###### Install steps
    ```console
    git clone https://github.com/sebmerlet/weenat
    cd weenat
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py loaddata db_populate.json
    ./manage.py test
    ./manage.py runserver
    ```