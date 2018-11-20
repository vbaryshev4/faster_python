from flask import Flask
from langdetect import detect

app = Flask(__name__)


# Пример запроса:
'''
POST / HTTP/1.1
  Accept: application/json
  Content-Type: application/x-www-form-urlencoded
  text=Hello+world.+Has+the+sun+risen+on+you+today%3F
'''

# Пример ответа:
'''
HTTP/1.1 200 OK
  Content-Type: application/json
  {"language": "en"}
'''

@app.route('/<query>', methods=['POST'])
def recognize_language(query):
    result = query.split('+')
    result = ' '.join(result)
    language = detect(result)
    return str({'language': language})


if __name__ == "__main__":
    app.run(debug=True)