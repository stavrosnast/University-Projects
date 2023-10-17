<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Products</title>
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

<body>
  <div class="container mt-5">
    <form action="" method="post" class="mb-3">
      <select name="Prodcuts[]" multiple>
        <option value="101">Term Plan</option>
        <option value="102">Whole Life</option>
        <option value="103">Retirement Plan</option>
        <option value="201">Comprehensive</option>
        <option value="202">Third-Party</option>
        <option value="301">Individual</option>
        <option value="302">Family</option>
        <option value="303">Critical Illness</option>
        <option value="401">Natural Causes</option>
        <option value="402">Burglaries</option>
      </select>
      <input type="submit" name="submit" vlaue="Choose options">
    </form>
    <?php
    if (isset($_POST['submit'])) {
      if (!empty($_POST['Prodcuts'])) {
        foreach ($_POST['Prodcuts'] as $selected) {
          $mysqli = mysqli_connect("localhost", "root", "", "insurance");

          $sql =  "SELECT
                 customer.cname,
                 customer.afm,
                 customer.csurname,
                 customer.address,
                 customer.city,
                 customer.tk,
                 customer.phone,
                 customer.doy
                FROM customer
                JOIN contract
                ON contract.custcode = customer.custcode
                JOIN product
                ON product.prodcode = contract.prodcode
				WHERE PRODUCT.PRODCODE = " . $selected;

          $res = mysqli_query($mysqli, $sql);

          if ($res) {
            while ($newArray = mysqli_fetch_array($res, MYSQLI_BOTH)) {
              $cust_cname  = $newArray['cname'];
              $cust_afm = $newArray['afm'];
              $cust_csurname = $newArray['csurname'];
              $cust_address = $newArray['address'];
              $cust_city = $newArray['city'];
              $cust_tk = $newArray['tk'];
              $cust_phone = $newArray['phone'];
              $cust_doy = $newArray['doy'];
              echo "<p><b>Customer Name:</b> " . $cust_cname . "<br/>" .
                "<b>AFM:</b> " . $cust_afm . "<br/>" .
                "<b>Surname:</b> " . $cust_csurname . "<br/>" .
                "<b>Address:</b> " . $cust_address . "<br/>" .
                "<b>City:</b> " . $cust_city . "<br/>" .
                "<b>TK:</b> " . $cust_tk . "<br/>" .
                "<b>Phone:</b> " . $cust_phone . "<br/>" .
                "<b>Municipality:</b> " . $cust_doy . "<br/></p>";
            }
          }
          mysqli_free_result($res);
          mysqli_close($mysqli);
        }
      } else {
        echo 'Please select the value.';
      }
    }
    ?>
  </div>
  <center>
    <form name="goBack" method="post" action="index.html">
      <p><input type="submit" name="submit" value="Return to menu"></p>
    </form>
  </center>
</body>

</html>