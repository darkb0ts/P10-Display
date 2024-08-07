<?php

// Set content type to JSON
header('Content-Type: application/json');

// Include database configuration
include 'config.php';

// Get input data
$data = json_decode(file_get_contents('php://input'), true);

// Check if data is not empty
if (!empty($data)) {
    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO Display_Data (id, text, audio, scrolling, blink) VALUES (?, ?, ?, ?, ?) ON DUPLICATE KEY UPDATE text = VALUES(text), audio = VALUES(audio), scrolling = VALUES(scrolling), blink = VALUES(blink)");
    $stmt->bind_param("issii", $id, $text, $audio, $scrolling, $blink);

    // Iterate through the array and execute the query
    foreach ($data as $item) {
        $id = $item['id'];
        $text = $item['text'];
        $audio = $item['audio'];
        $scrolling = $item['scrolling'];
        $blink = $item['blink'];
        $stmt->execute();
    }

    // Close the statement
    $stmt->close();

    // Response
    echo json_encode(["status" => "success", "message" => "Data updated successfully"]);
} else {
    echo json_encode(["status" => "error", "message" => "No data provided"]);
}

// Close the connection
$conn->close();
?>
