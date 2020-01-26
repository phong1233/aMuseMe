import http.client
import socket
socket.gethostbyname("")

def pause_song():
  conn = http.client.HTTPSConnection("conuhacks-2020.tsp.cld.touchtunes.com")
  header={
    "Authorization": "5dc2b08f09bbf5877eeb9209ce354a72"
  }
  conn.request("GET", "/v1/songs?query=robbery&size=30", body=None, headers=header)
  response = conn.getresponse()
  text = response.read()
  return text

print(pause_song())