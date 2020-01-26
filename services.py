import http.client

class Services():
    def pause_song(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("POST", "/pause")
        response = conn.getresponse()
        text = response.read()
        return text.decode('ascii')

    def play_song(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("POST", "/play")
        response = conn.getresponse()
        text = response.read()
        return text.decode('ascii')

    def unpause_song(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("POST", "/unpause")
        response = conn.getresponse()
        text = response.read()
        return text.decode('ascii')

    def stop_song(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("POST", "/stop")
        response = conn.getresponse()
        text = response.read()
        return text.decode('ascii')

    def status_song(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("GET", "/status")
        response = conn.getresponse()
        text = response.read()
        return text.decode('ascii')


