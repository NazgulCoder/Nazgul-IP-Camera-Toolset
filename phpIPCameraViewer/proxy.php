<?php
if (!isset($_GET['url'])) {
    die("Missing 'url' parameter.");
}

$url = $_GET['url'];
$headers = get_headers($url);

foreach ($headers as $header) {
    if (strpos($header, 'Content-Type') !== false) {
        header($header);
    }
}

$response = file_get_contents($url);
echo $response;
?>
