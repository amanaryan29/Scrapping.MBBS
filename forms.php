
<?php 
extract($_POST);
if(isset($send))
{
	
	$message ="Disease ".$name." \n Symptoms ".$mobile." \n Complications ".$query;
    $fp = fopen('people.txt', 'w');
// Open the file to get existing content
// Append a new person to the file
// Write the contents back to the file
    fwrite($fp, $message);

 }
	
 
?>
<html>
<head>
	<title>Scrape.MBBS</title>
	<img src="CAPTURE.PNG" width="100%">

</head>
<body style="background-color:offwhite;">
<form method="post" action="index.php">
 <table align="center" border="1" background="a.jpg" width="100%" height="32%">
	<tr>
	<th>Enter Diseases</th>
	<td><input type="text" name="name"/></td>
	</tr>
	<tr>
		<th>Enter Symptoms</th>
		<td><input type="text" name="sym"></td>
	</tr>	
	
	
	<tr>
		<th>Enter Complications</th>
		<td><textarea name="com"></textarea></td>
	</tr>
		
	
	<tr>
        
		<td align="center" colspan="3">
		<a href="rare.php"><img src="b.jpg" align="right" height="40%" width="20%"></a>
		<input type="submit" value="Submit" name="send"/>
	</tr>
	</table>
</form>
</body>
</html>