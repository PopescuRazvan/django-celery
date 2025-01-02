#!/bin/ash

echo "Apply database migration"
python manage.py migrate

# Run the command
exec "$@"