<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // collect value of inputted ingredients 
  $ingredients = $_REQUEST['ingredients'];
  if (empty($ingredients)) {
    echo "No ingredient selected";
  } else {
    echo $ingredients;
  }
}
?>
