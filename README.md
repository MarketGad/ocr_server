# OCR_Server

    apt-get install python3-venv    //if you don't have python3-venv

    export FLASK_ENV=development
    export FLASK_APP=application.py
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    python3 -m flask run 
    or
    python3 -m flask run --host=0.0.0.0
    
Open at http://0.0.0.0:5000/ and see the magic happen
