# Experimental linguistics with Python (I)
This is an example project developed for the wiki post [Experimental linguistics with Python (I)](https://wiki.mcasado.org/posts/20201016_Experimental-linguistics-with-Python-I/).

# Set up
You can download the workspace and run the experiment locally with some regards.

First of all, please note that no audios are included. You want to include your own. Secondly, please, remove the file ``static/.gitkeep``. It is there only for Git purposes. Should you run the experiment with ``.gitkeep`` there, Flask will interprete it as an audio file from the experiment.

# Dependencies
The project runs over [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/index.html). There's Pipfile with the dependencies to be run with [``pipenv``](https://pipenv-es.readthedocs.io/es/latest/index.html).

# Run
To start a server, just run ``$ flask run`` and you will be prompted with the port where the app is running.

# Further info
Visit the the [wiki](https://wiki.mcasado.org/posts/20201016_Experimental-linguistics-with-Python-I/). for full info on this project.