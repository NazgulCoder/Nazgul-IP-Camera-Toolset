<!DOCTYPE html>
<html>
<head>
  <title>IP Cameras Viewer</title>
  <style>
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    #image-grid {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      align-items: center;
      width: 70vw;
      height: 70vh;
    }
    .image-cell {
      flex: 1 0 calc(50% - 5px); /* Two images per row with 10px gap */
      max-width: 50%;
      padding: 5px;
      box-sizing: border-box;
    }
    img {
      width: 100%;
      height: auto;
      display: block;
      margin: 0 auto; /* Center the images */
    }
  </style>
</head>
<body>
  <div id="image-grid">
    <?php
    $imageUrls = file('image_urls.txt', FILE_IGNORE_NEW_LINES);
    foreach ($imageUrls as $url) {
      echo '<div class="image-cell"><img src="proxy.php?url=' . urlencode($url) . '" alt="IP Camera Image"></div>';
    }
    ?>
  </div>
  <script src="refresh.js"></script>
</body>
</html>
