<?php
//<a data-fancybox="gallery" href="big_1.jpg"><img src="small_1.jpg"></a>
foreach(glob($imagepath.'*') as $filename){
    echo "<div class='gallery_col_image col-md-4 col-md-6 col-sm-6 col-xs-12'>";
    echo '<a data-fancybox="gallery" href="images/'.basename($filename).'"><img class="gallery_image img-responsive" src="images/'.basename($filename).'"></a>';
    //echo "<img class='gallery_image img-responsive' src='images/".basename($filename)."' alt=''/>";
    echo "</div>";
    //basename($filename) . "\n";
}
