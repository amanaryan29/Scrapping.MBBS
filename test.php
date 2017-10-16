
<html>
<head>
    <title>Results</title>
</head>
<body background="http://previews.123rf.com/images/studiom1/studiom11306/studiom1130600805/22545014-HEALTH-Background-concept-wordcloud-illustration-Print-concept--Stock-Photo.jpg"> 

</body>
</html>

<?php
extract($_POST);
if(isset($senda))
{
    
    $message ="Disease ".$name." \n Symptoms ".$sym." \n Complications ".$com;
    $fp = fopen('people.txt', 'w');
// Open the file to get existing content
// Append a new person to the file
// Write the contents back to the file
    fwrite($fp, $message);
    $res = preg_replace('/[ ,]+/', '-', trim($name));
    
    $conn="";
extract($_POST);
$dsn="mysql:dbname=mydb";
$user="root";
$password="raaghav1508";
try {
    global $conn;
    $conn=new PDO($dsn,$user,$password);
    $conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);

} catch (PDOException $e) {
    echo "Connection failed:",$e->getMessage();
} 
$flag=0;
try {

    $sq="select * from data ";
$r=$conn->query($sq);
    
    foreach ($r as $row) {
        echo $row['disease'];
        if ($row['disease']==$res) {
            $flag=1;
            # code...
        }
    }
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
            $result = exec("C:\\Users\\ragha\\Anaconda2\\python.exe C:\\wamp\\www\\hackathon\\convert.py");
$string = trim($result, ".");
$split = explode(",", $string);
$count=1;
echo "Links are: <br />";
foreach($split as $value) //loop over values
{
    if ($count==1) {
        
    }
    else
    {
    ?>
    <a href="<?php echo $value ?> "><?php echo $value ?></a> 

    <?php
     $sql3="insert into `data`( `name`, `disease`) VALUES ( $res,$value) ";
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
$result1 = exec("C:\\Users\\ragha\\Anaconda2\\python.exe C:\\wamp\\www\\hackathon\\ml.py");
$string1 = trim($result1, ".");
$split1 = explode(",", $string1);
$count=1;
echo "<br /> <br />Recommended links: <br />";
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
$result1 = exec("C:\\Users\\ragha\\Anaconda2\\python.exe C:\\wamp\\www\\hackathon\\convert.py"); 
echo $result1;
  
}
  ?>



