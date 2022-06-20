import random
from datetime import timedelta, datetime
from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago


APPLES = ["pink lady", "jazz", "orange pippin", "granny smith",
          "red delicious", "gala", "honeycrisp", "mcintosh", "fuji"]


def say_my_name():
    """A 'echo_to_file' task that uses a Bash operator."""
    """a simple function to yell my name into the abyss and have it saved it to a file"""

def print_greeting():
    """A 'greeting' task that reads our echo and gives it back to us with a bonus string"""
    # open up our saved echo and save it to a variable called echo_file
    with open('opt/airflow/dags/ch6_code_review.txt', 'r') as echo_file:
        # release our echo from the file and say it back to us as a greeting
        print(
            f'Hey, {echo_file: read()}. Here is your echo back. make sure you keep better track of it next time')

def print_string(apple_on_string):
    """function that takes a string as an argument and prints that string"""
    print(f'{apple_on_string}')


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(2),
    'schedule_interval': timedelta(days=1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


"""dag instantiation, no breathing"""
with DAG(
    # name dis dag
    'dag_yo',
    description='A simple DAG to return our echo with a bonus random apple',
    # passing the arg as the defaults args
    default_args=default_args,
) as dag:


t1 = BashOperator(
    """echo to file task"""
    task_id='say_my_name',
    # task to take my echo and save it in a file for later
    bash_command='echo "bri" > /opt/airflow/dags/ch6_code_review.txt')

t2 = PythonOperator(
    """Python function to greet me"""
    # name our greeting function
    task_id="print_hello"
    # call on our greeting function
    python_callable=print_greeting)

t3 = BashOperator(
    """using a Bash operator, echo "picking three random apples"""
    # name our echo apples operator
    task_id='rando_apples'
    # give our task the chore of yellin our echo back at us
    bash_command='echo "pick three apples at random from the apple basket"')

for n in range(3):
    """Use a 'for' loop with 'range' to create three Python operator tasks that will run simultaneously"""
    task = PythonOperator(
        # Have a unique task ID that includes the number generated by 'range'
        task_id=f't' + n,
        # Use a python_callable that calls a function that takes a string as an argument and prints that string
        python_callable=print_string,
        # Pass a random apple from the 'APPLES' list as the argument to that function. Note: if you prefer, you can use a decorator instead of a Python operator.
        apple_on_string=random.APPLE)


big_boy_task = DummyOperator(
    """just cause he dumb, dont mean he cant still help us out by telling us if this works or not"""
    # give him a job title so he feels important
    task_id="super_smart_guy")


    
