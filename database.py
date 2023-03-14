from sqlalchemy import create_engine
from sqlalchemy import text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={        
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
my_secret = os.environ['DB_CONNECTION_STRING']
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from tutor_"))

    tutor_ = []
    for row in result.fetchall():
      tutor_.append(dict(row._mapping))
    return tutor_


      
   # print("type(result):", type(result))
   # result_all = result.fetchall()
   # print("type(result.fetchall()):", type(result_all))
   # first_result = result_all[0]
   # print("type(first_result):", type(first_result))
   # first_result_dict = dict(first_result._mapping)
   # print("type(first_result_dict):", type(first_result_dict))
   # print(first_result_dict)
