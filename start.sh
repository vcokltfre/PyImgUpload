ln -s /data ./static
gunicorn --bind 0.0.0.0:5000 --workers 8 wsgi:app