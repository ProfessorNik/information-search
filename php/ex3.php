<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Notebook</title>
    <?php
    include 'z10-3.inc'
    ?>
</head>
<body>
<?php
include "connect.inc";
global $conn;


$result = pg_query($conn, "select * from notebook") or die('Ошибка запроса: ' . pg_last_error());
print "<h4>Содержимое таблицы notebook</h4>";
print "<table>";

$build_table_head = fn($line) => "<tr>" . array_reduce(array_keys($line), fn($table_head, $col_name) => $table_head . "<th>$col_name</th>", "") . "</tr>";
$build_table_row = fn($line) => "<tr>" . array_reduce(array_values($line), fn($table_head, $col_value) => $table_head . "<td>$col_value</td>", "") . "</tr>";
$build_table_rows = function ($result) use ($build_table_row): string {
    $rows = "";
    while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
        $rows .= $build_table_row($line);
    }
    return $rows;
};
$build_table = function ($result) use ($build_table_rows, $build_table_head, $build_table_row): string {
    if (!($line = pg_fetch_array($result, null, PGSQL_ASSOC))) {
        return "";
    }

    return "<table>"
        . "<thead>"
        . $build_table_head($line)
        . "</thead>"
        . "<tbody>"
        . $build_table_row($line)
        . $build_table_rows($result)
        . "</tbody>"
        . "</table>";
};
print $build_table($result);
pg_free_result($result);

include "disconnect.inc";
?>
</body>
</html>