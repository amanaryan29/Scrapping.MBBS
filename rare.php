
<html>
<head>
	<title>Rare disease</title>
</head>
<body style="background-color:yellow">
<?php
    $result = exec("C:\\Users\\Subham\\Anaconda3\\python.exe C:\\wamp\\www\\hackathon_PROB3\\disease.py");
$string = trim($result, ".");
$split = explode(",", $string); //The explode() function breaks a string into an array.
$count=1;
foreach($split as $value) //loop over values
{
	if ($count==1) {
		echo "The disease is: ".$value."<br />";
	}
	else
    {
	?>
	<a href="<?php echo $value ?> "><?php echo $value ?></a> 

	<?php
	  echo "<br />"; //print value
	}
	$count=$count + 1;
}  


?>
<a href="rare.php">Click here for another disease</a>
<br>
<a href="forms.php">Back</a> 

</body>
</html>