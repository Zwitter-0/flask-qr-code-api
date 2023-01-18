# Usage
[1]. Run the serverapi file.\
[2]. There are two ways to get image of desired url.
###  - CURL command
    curl -X GET "http://localhost:5000/qr?url=example.com" -o qr.png
###  - Browser search
    You can also use a browser to access the API endpoint and retrieve the QR code image.
    Simply enter the URL http://localhost:5000/qr?url=example.com in the address bar of your browser,and it will automatically download the QR code image as "qr.png"
  
## note:
  You can use any url you want to convert into qr code, just replace example.com with desired url.
 
