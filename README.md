# Social Content Analysis Application

It is an application that instantly displays the discussions on social media about a topic (hashtag) and determines whether these discussions contain insults in various categories, and if it does, it shows which words of the text are evaluated in that insult category.

## Technologies

The main technologies are:

- [PostgreSQL](https://www.postgresql.org/) - RDBMS database
- [Python](https://docs.python.org/3.10/) - Python version: 3.10 
- [SQLAlchemy](https://docs.sqlalchemy.org/) - SQLAlchemy version: 2.0
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Bootstrap version: 5.0

## Prerequisites

### Environment

Please set up your Python version to `3.10`

```bash
python --version
```
- Install Virtualenviroment
```bash
pip install virtualenv
```
- Create the virtualenv
```bash
virtualenv venv
```
- Activate the venv
```bash
source venv/bin/activate
```
- Install libraries
```bash
pip install -r requirements.txt
```

### Configuration

Create your `.env` file.
```bash
cd <project-directory>

touch .env
```
- Add environment variables into `.env` file
```bash
* HASHTAG=#hashtag
* DATABASE=postgresql
* HOST=localhost
* USERNAME=postgres
* PASSWORD=postgres
* PORT=5432
```

## Run Job

```bash
python app.py
```

