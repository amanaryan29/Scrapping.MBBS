<?php
extract($_POST);
if(isset($send))
{
    $message ="Disease ".$name." \n Symptoms ".$sym." \n Complications ".$com;
    $fp = fopen('people.txt', 'w');
// Open the file to get existing content
// Append a new person to the file
// Write the contents back to the file
    fwrite($fp, $message);
    $res = preg_replace('/[ ,]+/', '-', trim($name)); 
	//preg_replace function searches for string specified by pattern and replaces pattern with replacement if found
	//'/[ ,]+/' replaces all spaces and commas by '-'
    $conn="";
extract($_POST);
$dsn="mysql:dbname=mydb";
$user="root";
$password="codeblocks";
try {
    global $conn;
    $conn=new PDO($dsn,$user,$password);#PDO=> PHP Data Object
    $conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);

} catch (PDOException $e) {
    echo "Connection failed:",$e->getMessage();
} 
$flag=0;
try {

    $sq="select * from data ";
$r=$conn->query($sq);
    
    foreach ($r as $row) {
        echo $row['disease'];//row is the complete row of the table with disease => (as the combination of disease,symptom and complication ) and name is the link
        if ($row['disease']==$res) {// res is the  combination of disease,symptom and complication seperated by '-'
            $flag=1;
            # code...
        }
    }
	/* if flag is 1 indicates that the particular combination of disease,complications and symptoms have previously arrived 
	and we can directly pick the links from the database(Type of Dynamic Programming) */
    echo $flag;
        if ($flag==1) {
            $sql="select name from data where disease = $row[disease] ";
            $row1=$conn->query($sql);
            echo "Links are: <br />";
            foreach ($row1 as $row) {

                ?>
                <a href="<?php echo $row['name'] ?> "><?php echo $row['name'] ?></a>
                <?php
                }
            }
        else
        {
            //runs covert.py and returns the links corresponding to the combination of symptom,disease and complications
			$result = exec("C:\\Users\\Subham\\Anaconda3\\python.exe C:\\wamp\\www\\hackathon_PROB3\\convert.py");
			
			
			/*Exec() method emulate the command line, meaning exec("example.php") 
			works the same as php -f example.php on the command line. 
			This means you can pass arguments to by putting a space between 
			the file name and all the arguements (exactly like you would do in the command line). 
			So, exec("example.php $var1 $var2") is the same as php -f example.php $var1 $var2 on the command line. 
			Now the $argv variable come into pay in the executed script.
			Inside of example.php if you var_dump $argv you will see an array, 
			where the zero index is the name of the script being executed and all the other indexes are the variables passed to the scrip*/
$string = trim($result, ".");
// Split a string by a specified string into pieces
$split = explode(",", $string);
$count=1;
?>
<h1 style="color:white">Links are:</h1>
<?php

foreach($split as $value) //loop over values
{
    if ($count==1) {
        
    }
    else
    {
    ?>
    <a href="<?php echo $value ?> "><?php echo $value ?></a> 

    <?php
     $sql3="insert into `data`( `name`, `disease`) VALUES ( $res,$value) ";//insert into table for future reference (Dynamic)
            $row2=$conn->query($sql3);
    
      echo "<br />"; //print value
    }
    $count=$count + 1;
}


        }

    

            # code...
        }

        
 catch (Exception $e) {
    echo $e;
    

    
}
//runs covert.py and returns the links corresponding to the recommendation

$result1 = exec("C:\\Users\\Subham\\Anaconda3\\python.exe C:\\wamp\\www\\hackathon_PROB3\\ml.py");
$string1 = trim($result1, ".");
$split1 = explode(",", $string1);
$count=1;
?>
<h1 style="color:white">Recommended links are:</h1>
<?php 
foreach($split1 as $value1) //loop over values
{
    if ($count==1) {
        
    }
    else
    {
    ?>
    <a href="<?php echo $value1 ?> "><?php echo $value1 ?></a> 
    <?php
           

    
      echo "<br />"; //print value
    }
    $count=$count + 1;
}
  
}
  ?>

<html>
<head>
    <title>Results</title>
</head>
<body background="http://previews.123rf.com/images/studiom1/studiom11306/studiom1130600805/22545014-HEALTH-Background-concept-wordcloud-illustration-Print-concept--Stock-Photo.jpg"> 
<a href="forms.php" style="color:white">BACK</a>

</body>
</html>

