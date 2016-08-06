<?php
$qrdata= htmlspecialchars($_GET['c'] , ENT_QUOTES);

//Format the data and write the QR data to a local file
$qrdata= str_replace(" ", "+", $qrdata);
$file = "qr.data";
file_put_contents($file, $qrdata);

//Function to convert the base64 to image file
function base64_to_jpeg($base64_string, $output_file) {
    $ifp = fopen($output_file, "wb"); 
    $data = explode(',', $base64_string);
    fwrite($ifp, base64_decode($data[1])); 
    fclose($ifp); 
    return $output_file; 
}

//Call to the function
$image = base64_to_jpeg( $qrdata, 'tmp.jpg' );
?>
