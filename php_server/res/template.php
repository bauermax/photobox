<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>PHOTOBOX GALLERY - EXIA</title>
  <link href="https://fonts.googleapis.com/css?family=Kelly+Slab" rel="stylesheet">
  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">


  <!-- FANCYBOX -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.0.47/jquery.fancybox.min.css" />
  <script src="//code.jquery.com/jquery-3.2.1.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.0.47/jquery.fancybox.min.js"></script>
  <!-- FANCYBOX -->
  <link href="res/css/style.css" rel="stylesheet">
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</head>
<body>
  <div class="container main-container">
    <div class="col-md-12">
      <h1 class="menu_title"><span class="exia">EXIA</span> PHOTO GALLERY</h1>
    </div>
  </div>
  <div class="container gallery">
    <div class="col-md-12">
      <h1 class="gallery_title">GALLERY <span class="gallery_subtitle">// ALL PHOTOS TAKEN BY THE EXIA PHOTOBOOTH</span></h1>
      <hr style="border-top: 1px solid #999;">
    </div>

    <div class="gallery">
      <br>
      <div class="col-md-12">
        <div class="row"><?php include('images.php');?></div>
      </div>
  </div>

  </div>

</body>
</html>
