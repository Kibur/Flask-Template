# Flask-Template
Minimal getting started Flask template with a basic Bootstrap.<br>
Template structure following http://flask.pocoo.org/docs/0.10/ and https://exploreflask.com/

<h1>Getting started</h1>
<h2>Fork the repository and clone</h2>
<b>Note:</b> You can change the repository name in `Settings` -> `Repository name`<br>
```
git clone https://github.com/<username>/<project>
```
After cloning you can rename the folder and make sure to replace the project name in `app.py`
<h2>Virtual environment (<b>recommended</b>)</h2>
```
# Go to your project folder
cd <project>

# Install if not already done virtualenv
pip install virtualenv

# Create a virtual environment folder called "venv"
virtualenv venv

# Activate the virtual environment
source ./venv/bin/activate
```
<h2>Install Flask dependencies</h2>
```
pip install -r requirements.txt
```

<h2>Test your Flask application</h2>
```
python app.py
```
<span>Open your web browser and surf to: </span>`http://localhost:5000`
