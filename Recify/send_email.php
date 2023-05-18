<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST['name'];
  $email = $_POST['email'];
  $subject = $_POST['subject'];
  $message = $_POST['message'];

  // Set the recipient email address
  $to = 'sergytrenych@gmail.com';

  // Set the email headers
  $headers = "From: $name <$email>" . "\r\n";
  $headers .= "Reply-To: $email" . "\r\n";
  
  // Send the email
  if (mail($to, $subject, $message, $headers)) {
    // Email sent successfully
    echo "Thank you! Your message has been sent.";
  } else {
    // Failed to send email
    echo "Sorry, there was a problem sending your message. Please try again later.";
  }
}
?>