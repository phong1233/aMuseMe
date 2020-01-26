import http.client

class Services():
    def pause_song(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("POST", "/pause")
        response = conn.getresponse()
        text = response.read()
        return text.decode('ascii')

