# datafun-05-sql

#### I created a new repo in Github
#### I added the README.md file when creating the new repo
#### I opened the Documents folder in File Explorer since that is where I wanted this project to be stored
#### I cloned the new repo to the Documents folder with the following command
```shell

git clone site_URL

```
## Opening project and adding files in VS Code

#### I opened the new project in VS Code
#### I added a .py file to write my code in
#### I added a .gitignore file
#### I added a requirements.txt file

#### I created a virtual environment using the code below

```shell
py -m venv .venv
.venv\Scripts\Activate

```
## Install packages in Virtual Envvironment

#### The code below installs pandas and pyarrows in the requirements.txt file
```shell

pip install pandas pyarrow
python -m pip freeze > requirements.txt

```