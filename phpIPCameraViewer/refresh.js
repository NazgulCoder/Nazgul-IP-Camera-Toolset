document.addEventListener("DOMContentLoaded", function () {
  // Function to refresh images
  function refreshImages() {
    var images = document.getElementsByTagName("img");
    for (var i = 0; i < images.length; i++) {
      var imageUrl = images[i].src;
      images[i].src = imageUrl + '?' + new Date().getTime(); // Add a timestamp to bypass caching
    }
  }

  // Refresh images every 1 second
  setInterval(refreshImages, 1000);
});
