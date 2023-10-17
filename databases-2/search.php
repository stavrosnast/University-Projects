<html>

<body>

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>View Products</title>
    <style>
      .container {
        max-width: 350px;
        margin: 50px auto;
        text-align: center;
      }

      select {
        width: 100%;
        min-height: 150px;
        margin-bottom: 20px;
      }

      input[type="submit"] {
        margin-bottom: 20px;
      }
    </style>
  </head>
  <center>
    <?php
    //Εκτέλεση σύνδεσης
    $mysqli = mysqli_connect("localhost", "root", "", "insurance");

    //Έλεγχος σύνδεσης
    if (mysqli_connect_errno()) {
      printf("Connect failed: %s\n", mysqli_connect_error());
      exit();
    } else {

      //Ορισμός charset  σύνδεσης
      mysqli_set_charset($mysqli, "utf8");

      $date_of_contr = $_POST["date_con"];
      $afm_customer = $_POST["afm"];
	  
	  if ( !gettype($afm_customer) == "integer" || empty($afm_customer) || empty($date_of_contr) ){
		  
		echo  "<p><b>Error: Empty field or wrong data type</b></p>";
	  } else{
				//Σύνταξη ερωτήματος
		$sql = "CALL monthly_cost_proc($afm_customer, '$date_of_contr', @active_contracts, @mcost)";

		//Εκτέλεση ερωτήματος στην βάση
		$res = mysqli_query($mysqli, $sql);
	
		$select = mysqli_query($mysqli, 'SELECT @active_contracts, @mcost');
		$result = mysqli_fetch_assoc($select);

		$procOutput_sum = $result['@active_contracts'];
		$procOutput_product = $result['@mcost'];
	
		echo  "<p><b>Total Contracts:</b> " . $procOutput_sum . "<br/>" .
        "<b>Cost:</b> " . $procOutput_product . "<br/></p>";

		mysqli_free_result($select);	
	}
      //Κλείσιμο σύνδεσης με βάση
      mysqli_close($mysqli);
    }
    ?>
	<form name="goBack" method="POST" action="instert_am.php">
	   <p><input type="submit" name="submit" value="Search again"></p>
	</form>
    <form name="goBack" method="post" action="index.html">
      <p><input type="submit" name="submit" value="Return to menu"></p>
	</form>
  </center>
</body>

</html>