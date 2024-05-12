<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Backend Application README</h1>
    <p>This document serves as a comprehensive guide for utilizing and understanding the backend of our solar energy calculation application.</p>
    <h2>Overview</h2>
    <p>The backend application is engineered to fetch and compute solar energy data for a 7-day forecast period. It interacts with an external API to obtain relevant data based on geographical coordinates received from the frontend. This data is then processed to estimate the potential energy that can be generated from solar exposure.</p>
    <h2>Key Features</h2>
    <ul>
        <li><strong>Data Retrieval:</strong> Fetches solar data using an external API, based on geographical coordinates.</li>
        <li><strong>Energy Calculation:</strong> Calculates the energy that can be harvested from solar exposure, providing daily estimates over a seven-day period.</li>
        <li><strong>Coordinate Validation:</strong> Ensures the coordinates provided are within acceptable geographical boundaries.</li>
        <li><strong>JSON Endpoint:</strong> Outputs the processed data in JSON format accessible through a RESTful API endpoint.</li>
        <li><strong>Unit Testing:</strong> Features comprehensive unit tests to ensure the reliability and accuracy of the application.</li>
    </ul>
    <h2>API Usage</h2>
    <h3>Endpoints</h3>
    <p>The main endpoint of the application is:</p>
    <ul>
        <li><strong>GET /solar-data</strong> - Receives geographical coordinates as query parameters and returns the solar energy data in JSON format.</li>
    </ul>
    <h2>Example Request</h2>
    <p>To request data from the backend, use the following curl command:</p>
    <pre>
        curl -X GET "http://yourbackendurl.com/solar-data?lat=52.5200&lon=13.4050"
    </pre>
    <h2>Unit Tests</h2>
    <p>The backend includes unit tests for validating the functionality of each component. These tests are executed using a Python testing framework, such as pytest.</p>
    <h2>Getting Started</h2>
    <p>Follow these steps to set up the backend:</p>
    <ol>
        <li>Clone the repository.</li>
        <li>Install the necessary dependencies as listed below.</li>
        <li>Configure your environment variables appropriately.</li>
        <li>Run the application using the command <code>python app.py</code>.</li>
    </ol>
    <h2>Dependencies</h2>
    <p>Ensure all necessary project dependencies are listed below. Include libraries, frameworks, and any APIs the project relies on.</p>
</body>
</html>
