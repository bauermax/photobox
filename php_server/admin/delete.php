<?php
//feel free to add a .htpasswd for this folder
if(isset($_GET['name'])){

  $mainpath = '../images/';
  $id = $_GET['name'];

  $return = unlink($mainpath.$id);


}
header("Location: index.php");
