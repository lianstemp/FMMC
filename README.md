<img align="right" src="https://visitor-badge.laobi.icu/badge?page_id=MRXAZK.FMMC">
<h1 align="center" style="margin-top: 0px;"> FastAPI Mysql MongoDB CRUD (FMMC)</h1>
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=fastapi,mysql,mongodb" />
  </a>
</p>

## Get Started 🚀

## Run Locally

Clone the project

```bash
  https://github.com/MRXAZK/FMMC.git
```

or

Fork the project on GitHub
Click on the "Fork" button in the top right corner of the page.
Select the account where you want to fork the repository.
Clone the forked repository

### Environment Variabel

#### SQL

|     KEY     |          VALUE           |
| :---------: | :----------------------: |
| `DB_ENGINE` |  `Your Database Engine`  |
|  `DB_HOST`  |  `Your Database Host `   |
|  `DB_PORT`  |   `Your Database Port`   |
|  `DB_NAME`  |  `Your Database Name `   |
|  `DB_USER`  | `Your Database Username` |
|  `DB_PASS`  | `Your Database Password` |

#### NOSQL

|             KEY              |               VALUE               |
| :--------------------------: | :-------------------------------: |
|        `MONGODB_URL`         | `Your MongoDB Connection String ` |
| `MONGO_INITDB_ROOT_USERNAME` |      `Your MongoDB Username`      |
| `MONGO_INITDB_ROOT_PASSWORD` |      `Your MongoDB Password`      |

> **Note** : You can take **.env.example** as a template and rename to **.env** and fill all requirement

### Optional

You can create a Virtual Environment for this project

```bash
  python3 -m venv venv
```

And Activate the Virtual Environment

```bash
  source venv/bin/activate
```

### Install Dependencies

```bash
  pip install -r requirements.txt
```

### Start The Server

```bash
  uvicorn main:app --reload
```

## Play With Docker

1. Make sure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed on your machine.
2. Build and run the Docker containers

```bash
   docker-compose up --build
```

The server will be running at http://0.0.0.0:8000/

> **Note** : You can also use the command **docker-compose up -d** to run the containers in detached mode.

3. You can stop the containers by running

```bash
docker-compose down
```

Or
If you want to remove the volumes as well, you can add --volumes flag to docker-compose down command like this:

```bash
docker-compose down --volumes
```
