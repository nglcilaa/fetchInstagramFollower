from http.server import BaseHTTPRequestHandler, HTTPServer
import instaloader
import json

class InstagramFollowerHandler(BaseHTTPRequestHandler):
    def get_instagram_followers(self, username):
        try:
            # Crea un'istanza di Instaloader
            loader = instaloader.Instaloader()

            # Ottieni il profilo dell'utente
            profile = instaloader.Profile.from_username(loader.context, username)

            # Ottieni il numero di follower
            followers_count = profile.followers

            return followers_count
        except Exception as e:
            print(f"Errore nel recupero dei follower di Instagram: {e}")
            return None

    def do_GET(self):
        if self.path == "/instagram/followers":
            username = "ngl_cila"
            followers = self.get_instagram_followers(username)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')  # Aggiungi questo header
            self.end_headers()
            
            if followers is not None:
                print(f"Numero di follower di {username}: {followers}")  # Aggiungi questo log
                self.wfile.write(json.dumps({'followers': followers}).encode())
            else:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')  # Aggiungi questo header
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Errore nel recupero dei follower di Instagram.'}).encode())

def run(server_class=HTTPServer, handler_class=InstagramFollowerHandler, port=7000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()






