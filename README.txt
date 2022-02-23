That start this project you need install some library. Open terminal and enter next:
- sudo apt-get install docker
- sudo apt-get install docker-compose
- sudo apt -y install postgresql

When you download application in your computer - need rename file 'env.example' to '.env':
    - in terminal /Test_Atlas enter 'mv env.example .env'

Run project:
1.1 in ./Test_Atlas enter : sudo docker-compose up --build

Start selery:
1. Open new terminal window, go in project directory and enter next: sudo docker-compose exec web bash
2.  Then enter 'celery -A add_to_database.celery worker --loglevel=INFO'. This command starts celery worker.
3. Then you need open new terminal window, go in project directory and enter next: 'sudo docker-compose exec web bash'
4. End entry ' celery -A add_to_database.celery beat --loglevel=INFO'. This command starts celery beat.

Endpoint for testing application:

1. Get all list exchanges: '/api/exchanges'

2. Get filter exhanges from database : '/api/exchanges/history?valcode=<Enter valcode>&date=<enter data in format -'dd.mm.yyyy'>'
2.1 Also you need get gilter only one get-params.

3.Get current rate: '/api/exchanges/current_rate?valcode=<Enter valcode>'


If you want make new migrations - you need do next:
1. In wew terminal window enter: sudo docker-compose exec web bash
2. Enter : flask db migrate
3. Enter : flask db upgrade
