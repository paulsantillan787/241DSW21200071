from dotenv import load_dotenv
import os

load_dotenv()


user = os.environ['USER']
pwd = os.environ['PASSWORD']
host = os.environ['HOST']
database = os.environ['DATABASE']
server = os.environ['SERVER']

DATABASE_CONNECTION=f'{server}://{user}:{pwd}@{host}/{database}'
