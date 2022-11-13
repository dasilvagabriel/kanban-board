# CS162_Kanban_Board
A kanban board web app built on Flask

# How to run (MAC):
All set up should be run from the directory '.../kanban-board/'

## Set up virtual environment (use terminal):
` python3 -m venv .venv` 
` source .venv/bin/activate` 
` pip3 install -r requirements.txt` 


## Set up Flask Application
`export FLASK_APP=kanban.app`
` export FLASK_ENV=development`
`flask run`
To run the application, run:
`python3 app.py`

## Visit local host to check live application
` http://localhost:5000/` 

## Windows
` python3 -m venv venv` 
` venv\Scripts\activate.bat` 
` pip3 install -r requirements.txt` 
` python3 app.py` 

## Run tests
With the virtual environment running, and on the root folder (in this case my_kaban), run
` python -m unittest` 
