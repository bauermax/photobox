<?php
/////////////////////////////////////////////////
//CONFIG & VARIABLES
//OPEN .INI FILE
$config = parse_ini_file("config.ini");

//VARIABLES
$raw_token = $config['token_passphrase'];
$uploaddir = $config['uploaddir'];

//HASH RAW TOKEN
$check = md5($raw_token);

/////////////////////////////////////////////////

//IF GOOD PARAMS ARE NOT PROVIDED
if(!isset($_POST['token']) || !isset($_FILES['file']['name']) ){
  //DISPLAY ERROR AND KILL THE APP
  echo "ERROR : Either you can't access to this page, or you are not providing the good parameters";
  http_response_code(400);
  die();
}
/////////////////////////////////////////////////
 $client_token = $_POST['token'];
 $file = $_FILES['file'];


//CHECK IF TOKEN IS VALID
if($client_token == $check){

  //PROCEED TO UPLOAD
  $uploadfile = $uploaddir . basename($file['name']);

  if (move_uploaded_file($file['tmp_name'], $uploadfile)) {
    echo "SERVER : UPLOAD SUCCESS";
    http_response_code(200);
  }
  else {
    echo "SERVER : UPLOAD FAILURE";
    http_response_code(424);
  }

}
else{
  echo "SERVER : You are not allowed to upload files on this website";
  http_response_code(401);
}
/////////////////////////////////////////////////
