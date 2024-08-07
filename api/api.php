<?php
header('Content-Type: application/json');

// Include database configuration
include 'config.php';

// SQL query to fetch data
$sql = "SELECT * FROM Display_Data";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $data = array();

    // Fetch data
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }

    // Send data as JSON
    echo json_encode($data);
} else {
    echo json_encode(array("message" => "No records found"));
}

// Close the database connection
$conn->close();
?>
