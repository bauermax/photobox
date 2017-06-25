<?php
//feel free to add a .htpasswd for this folder
//<a data-fancybox="gallery" href="big_1.jpg"><img src="small_1.jpg"></a>
foreach(glob($imagepath.'*') as $filename){

    echo "<div class='gallery_col_image col-md-4 col-md-6 col-sm-6 col-xs-12' style='margin-top:30px;'>";
    echo '<img class=" thumbnail gallery_image img-responsive" src="../images/'.basename($filename).'">';
    echo '<a href="delete.php?name='.basename($filename).'"><button class="btn btn-danger">Delete</button></a>';
    //echo "<img class='gallery_image img-responsive' src='images/".basename($filename)."' alt=''/>";
    echo "</div>";
    //basename($filename) . "\n";
}
