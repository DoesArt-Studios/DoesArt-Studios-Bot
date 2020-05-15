<?php

if (isset($_POST['SUBMIT'])) {
  $name = $_POST['name'];
  $subject = $_POST['subjejct'];
  $mailFrom = $_POST['mail'];
  $message = $_POST['message'];
  
  $mailTo = "brodygabbusch@gmail.com";
  $headers = "from:".$mailFrom;
  $txt = "You have recieved an email from ".$name.".\n.\n".$message;  
  
  mail($mailTo, $subject, $txt, $headers);
  header("Location: jobs.html?mailsend");
}
