# Start Hypercorn Server
```
pip install -r requirements.txt
hypercorn app:app
```

# Run aiohttp Websockt Client with Concurrent Recv and Close
```
python client.py
```

# Results

```
Waiting for message
Closed code: None
```

The closed code is `None`.
