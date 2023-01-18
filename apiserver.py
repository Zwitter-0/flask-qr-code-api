from flask import Flask, request, make_response
from qrcode import make
from io import BytesIO

app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def generate_qr():
    url = request.args.get('url')
    img = make(url, box_size=70)

    # Save QR code to a BytesIO object
    bio = BytesIO()
    img.save(bio, format='png')
    bio.seek(0)

    # Send QR code as response
    response = make_response(bio.read())
    response.headers.set(
        'Content-Disposition', 'attachment', filename='qr.png')
    return response

if __name__ == '__main__':
    app.run()
