import json

app_type = b'GeeksForGeeks'
a = json.dumps({'method': 'connectDevice', 'value': app_type})
print(a)
