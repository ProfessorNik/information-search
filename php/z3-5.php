<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<?php

$fill = function ($array, $valueGenerator) {
    for ($n = 1; $n <= 10; $n++) {
        $array [] = $valueGenerator($n);
    }

    return $array;
};

$print_array = function ($array) {
    $out = implode(", ", $array);
    print "<p>$out</p>";
};

$treug = $fill([], fn($n) => $n * ($n + 1) / 2);
$print_array($treug);

$square = $fill([], fn($n) => $n * $n);
$print_array($square);

$rez = array_merge($treug, $square);
$print_array($rez);

sort($rez);
$print_array($rez);

array_shift($rez);
$print_array($rez);

$unique_rez = array_unique($rez);
$print_array($unique_rez);
?>

</body>
</html>