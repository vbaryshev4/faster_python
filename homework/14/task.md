## Задание: 
#### создать REST веб-сервис, который распознает язык текста.

#####*Пример запроса*:
POST / HTTP/1.1
  Accept: application/json
  Content-Type: application/x-www-form-urlencoded
  text=Hello+world.+Has+the+sun+risen+on+you+today%3F

#####*Пример ответа*:
HTTP/1.1 200 OK
  Content-Type: application/json
  {"language": "en"}

#####Для сервера можно использовать, например, библиотеку WsgiService:
- http://github.com/pneff/wsgiservice
- http://packages.python.org/WsgiService/

#####Пакет для распознавания языка:
- https://pypi.org/project/langdetect/
- https://www.slideshare.net/shuyo/language-detection-library-for-java