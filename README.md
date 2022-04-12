### Start Gunicorn
```
gunicorn -c config.py --bind=0.0.0.0:5500 --worker-tmp-dir /tmp app:app
```

## Test 
```
python client.py <request num>
```