# flask-qr-code-api
Flask api server to generate high resolution with automatic downloading.
## Description
This is a Python Flask API server that generates and serves QR code images in response to GET requests. It takes a URL as a string from the query string of the GET request, generates a QR code image of the URL using the qrcode package, and sends the image back in the response. The response is automatically set to be downloadable with a filename 'qr.png' and the resolution of the image can be set by adjusting the box_size parameter of the qrcode package.
