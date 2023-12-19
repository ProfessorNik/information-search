<?php
$conn = pg_connect("host=localhost port=5432 dbname=study user=postgres password=admin")
or die("Нет соеденения с postgresql");
