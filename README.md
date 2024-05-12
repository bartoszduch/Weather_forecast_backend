<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Backend Application README</title>
</head>
<body>
    <h1>Backend Application README</h1>
    <p>This document serves as a guide for using and understanding the backend part of our solar energy calculation application.</p>

    <h2>Overview</h2>
    <p>This backend application is designed to fetch and compute solar energy data over a 7-day period. It utilizes an external API to retrieve the necessary data based on coordinates supplied from the frontend. The data is then processed to calculate the potential energy generated from sunlight exposure.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Data Retrieval:</strong> Uses an external API to gather solar data based on specific geographical coordinates.</li>
        <li><strong>Energy Calculation:</strong> Computes the amount of energy that can be harvested from solar exposure over a seven-day period.</li>
        <li><strong>Coordinate Validation:</strong> Validates the coordinates provided to ensure they fall within acceptable limits.</li>
        <li><strong>JSON Endpoint:</strong> Returns the processed data in JSON format through a designated endpoint.</li>
        <li><strong>Unit Testing:</strong> Includes several unit tests to verify the functionality and accuracy of the application.</li>
    </ul>

    <h2>API Usage</h2>
    <h3>Endpoints</h3>
    <p>The main endpoint of the application is described below:</p>
    <ul>
        <li><strong>GET /solar-data</strong> - Accepts geographical coordinates as input and returns the calculated solar energy data in JSON format.</li>
    </ul>
    
    <h2>Example Request</h2>
    <p>Here is an example of how to request data from the backend:</p>
    <code>
        curl -X GET "http://yourbackendurl.com/solar-data?lat=52.5200&lon=13.4050"
    </code>

    <h2>Unit Tests</h2>
    <p>The backend includes unit tests to ensure that each component functions correctly. These tests can be run using a standard Python testing framework like pytest.</p>

    <h2>Getting Started</h2>
    <p>To get started with this backend, you need to:</p>
    <ol>
        <li>Clone the repository.</li>
        <li>Install the necessary dependencies.</li>
        <li>Set up your environment variables.</li>
        <li>Run the application using a command like <code>python app.py</code>.</li>
    </ol>

    <h2>Dependencies</h2>
    <p>List all project dependencies here, such as external libraries or APIs.</p>
</body>
</html>
