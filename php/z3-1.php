<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<?php
$x = 1;
$y = 1;
$diagonalColor = "gray";
$borderStyle = "border: 1px solid;";
$table = "<table style='$borderStyle'>";

while ($y <= 10) {
    $table .= "<tr>";
    while ($x <= 10) {
        $number = $x*$y;
        $style = match ($x == $y) {
            true => "background-color: $diagonalColor; $borderStyle padding: 5px;",
            false => "$borderStyle padding: 5px;"
        };

        $table .= "<td style='$style'>$number</td>";
        $x++;
    }
    $table .= "</tr>";
    $x=1;
    $y++;
}

$table .= "</table>";
print $table;
?>

</body>
</html>