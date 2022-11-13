<h1 align="center" style="margin-top: 0px;"> CodeName - Neural 🧠 </h1>

## Get Started 🚀  
## Run Locally  

Clone the project  

~~~bash  
  git clone https://github.com/MRXAZK/CodeName-Neural.git
~~~

### Environment Variabel


#### SQL
| KEY     | VALUE     |
| :---:         |   :---:       | 
| `DB_ENGINE`   |      `Your Database Engine`         |
| `DB_HOST`     |      `Your Database Host `       |
| `DB_PORT`     |      `Your Database Port`         |
| `DB_NAME`     |      `Your Database Name `        |
| `DB_USER`     |      `Your Database Username`         |
| `DB_PASS`     |      `Your Database Password`        |

#### NOSQL
| KEY     | VALUE     |   
| :---:         |   :---:       | 
| `MONGODB_URL` |      `Your MongoDB Connection String `          |         

> **Note** : You can take **.env.example** as a template and rename to  **.env** and fill all requirement

### Optional 

You can create a Virtual Environment for this project 

~~~bash  
  python3 -m venv venv
~~~

And Activate the Virtual Environment

~~~bash  
  source venv/bin/activate
~~~



### Install Dependencies

~~~bash  
  pip install -r requirements.txt
~~~

### Start The Server

~~~bash  
  uvicorn main:app --reload
~~~

## Run With Docker 

### Coming Soon