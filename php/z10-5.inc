<?php

global $conn;

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



function vid_structure($conn, $table_name): void
{
    $result = pg_query($conn, "select column_name, data_type from information_schema.columns where table_name = '$table_name';") or die('Ошибка запроса: ' . pg_last_error());

    print "<h4>Структура таблицы $table_name</h4>";

    $struct = "";
    while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
        $struct .= "<div>";
        foreach ($line as $col_value) {
            $struct .= "$col_value ";
        }
        $struct .= "</div>";
    }

    print $struct;

    pg_free_result($result);
}



$vid_content = function ($conn, $table_name) use($build_table): void {
    $result = pg_query($conn, "select * from $table_name") or die('Ошибка запроса: ' . pg_last_error());
    print "<h4>Содержимое таблицы $table_name</h4>";
    print $build_table($result);
    pg_free_result($result);
};


$structures = $_GET["structure"] ?? null;
$contents = $_GET["content"] ?? null;


if ($structures) {
    foreach ($structures as $structure) {
        vid_structure($conn, $structure);
    }
}
if ($contents) {
    foreach ($contents as $content) {
        $vid_content($conn, $content);
    }
}
