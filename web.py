from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>COMPANY REVENUE</title>
<caption><h2>TOP REVENUE TABLE </h2></caption>
</head>
<body>
<table border ="2" cellpadding="2" width="600" height="300" bgcolor=blue">
<tr bgcolor="pink">
<th>s.no</th>
<th>Company Name</th>
<th>RUPEES in Billon</th>
<th>Country</th>
</tr>
<tr >
<td>1</td>
<td>Animation Labs</td>
<td>895.3</td>
<td>korea</td>
</tr>
<tr>
<td>2</td>
<td>Studio MAPPA</td>
<td>950.5</td>
<td>japan</td>
</tr>
<tr>
<td>3</td>
<td>Sentai Filmworks Studios</td>
<td>776.1</td>
<td>USA</td>
</tr>
<tr>
<td>4</td>
<td>Toi animation</td>
<td>863.2</td>
<td>japan</td>
</tr>
<tr>
<td>5</td>
<td>unfotable animation</td>
<td>897.4</td>
<td>russia</td>
</tr>
<tr>
<td>6</td>
<td>Ace Animations</td>
<td>900.8</td>
<td>china</td>
</tr>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("Company Revenue  webserver is running...")
httpd.serve_forever()