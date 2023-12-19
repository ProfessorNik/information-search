<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Изменение notebook</title>
    <?php
    include 'z10-3.inc'
    ?>
</head>
<body>
<?php
include "connect.inc";
global $conn;
?>


<?php
$id = $_POST['id'] ?? null;
$field_name = $_POST['field_name'] ?? null;
$field_value = $_POST['field_value'] ?? null;

if ($field_name != null) {
    pg_query($conn, "UPDATE notebook SET $field_name='$field_value' WHERE id=$id") or die('Ошибка запроса: ' . pg_last_error());
}
?>


<form method="GET">
    <table>
        <thead>
        <tr>
            <th>id</th>
            <th>name</th>
            <th>city</th>
            <th>address</th>
            <th>birthday</th>
            <th>mail</th>
            <th>исправить</th>
        </tr>
        </thead>
        <tbody>
        <?php
        $build_table_row = fn($line) => "<tr>"
            . "<td>" . $line['id'] . "</td>"
            . "<td>" . $line['name'] . "</td>"
            . "<td>" . $line['city'] . "</td>"
            . "<td>" . $line['address'] . "</td>"
            . "<td>" . $line['birthday'] . "</td>"
            . "<td>" . $line['mail'] . "</td>"
            . "<td><input type='radio' name='id' value='" . $line["id"] . "'></td>"
            . "</tr>";

        $build_table_rows = function ($result) use ($build_table_row) {
            $table_rows = "";
            while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
                $table_rows .= $build_table_row($line);
            }

            return $table_rows;
        };

        $result = pg_query($conn, "select * from notebook") or die('Ошибка запроса: ' . pg_last_error());
        print $build_table_rows($result);
        pg_free_result($result);
        ?>
        </tbody>
    </table>
    <button style="margin-top: 5px" type="submit">Выбрать</button>
</form>

<form method="POST">
    <?php
    $id = $_GET['id'] ?? null;
    if ($id) {
        $result = pg_query($conn, "select * from notebook where id=$id") or die('Ошибка запроса: ' . pg_last_error());
        $line = pg_fetch_array($result, null, PGSQL_ASSOC);

        print "<input name='id' value='$id' type='hidden'>"
            . "<select name='field_name'>"
            . "<option value='name'>" . $line['name'] . "</option>"
            . "<option value='city'>" . $line['city'] . "</option>"
            . "<option value='address'>" . $line['address'] . "</option>"
            . "<option value='birthday'>" . $line['birthday'] . "</option>"
            . "<option value='mail'>" . $line['mail'] . "</option>"
            . "</select>"
            . "<label>введите новое значение: <input name='field_value'></label>"
            . "<button type='submit'>Заменить</button>";
    }
    ?>
</form>

<?php
include "disconnect.inc";
?>
</body>
</html>