
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<body>
<?php

$hostname = "192.168.2.XXX";
$username = "XXX";
$password = "XXXXX";
$db = "IOT_PROTOTYP_TEMP";

$dbconnect=mysqli_connect($hostname,$username,$password,$db);
# Check the connection
if ($dbconnect->connect_error) {
  die("Database connection failed: " . $dbconnect->connect_error);
}
?>

<table border="1" align="center">
<tr>
  <td>Sensor</td>
  <td>Temperature</td>
  <td>Humidity</td>
</tr>

<?php
# prepare a query to the mySQL database
$query = mysqli_query($dbconnect, "SELECT * FROM sensor_raw_temp LIMIT 10 ")
   or die (mysqli_error($dbconnect));

while ($row = mysqli_fetch_array($query)) {
  echo
   "<tr>
    <td>{$row['sensor_id']}</td>
    <td>{$row['temperature']}</td>
    <td>{$row['humidity']}</td>
   </tr>\n";

}

?>
</table>
</body>
</html>
