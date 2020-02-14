database_exists=$(psql -ltq | cut -d \| -f 1 | grep -w 'airflow')

if ${database_exists}
then
  echo "It exists"
else
  echo "Nope..."
fi