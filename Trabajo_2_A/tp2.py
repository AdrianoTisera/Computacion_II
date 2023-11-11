import argparse
import http.server
import socket
from PIL import Image
from io import BytesIO
import multiprocessing
import sys

def grayscale_image(image_data):
    with Image.open(BytesIO(image_data)) as img:
        gray = img.convert('L')
        buf = BytesIO()
        gray.save(buf, format='JPEG')
        return buf.getvalue()

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            pool = multiprocessing.Pool(processes=1)
            result = pool.apply_async(grayscale_image, [post_data])
            gray_img_data = result.get()
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()
            self.wfile.write(gray_img_data)
        except:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Error: El archivo no es una imagen.')
        finally:
            sys.exit(0)

def run(server_class=http.server.HTTPServer, handler_class=CustomHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TP2 - procesa imágenes")
    parser.add_argument('-p', '--port', type=int, default=8000, help='Puerto de escucha')
    parser.add_argument('-i', '--ip', default=socket.gethostname(), help='Dirección de escucha')
    args = parser.parse_args()
    run(port=args.port)
