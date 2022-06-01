# ledger

step 1:  create version control table in database
  python migration/manage.py version_control postgresql://<username>:<password>@<host>:<port>/<db_name> <repository name>

  python migration/manage.py version_control postgresql://postgres:root@localhost:5432/ledger migrations

step 2: create manage.py file at src label to manage migration, not to be used in production
  migrate manage manage.py  --repository=migration  --url=postgresql://postgres:root@localhost:5432/ledger 

step 3: create script file
  python manage.py script "table name"

step 4: use this to upgrade version(table etc)
  python manage.py upgrade

step 5: to know the current version
  python manage.py db_version