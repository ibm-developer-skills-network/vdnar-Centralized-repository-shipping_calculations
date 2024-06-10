<!DOCTYPE html>
<html>
<head>
    <title>Shipping Cost Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }
        .container {
            text-align: center;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type="number"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .result {
            margin-top: 20px;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Shipping Cost Calculator</h1>
        <form id="shippingForm">
            <label for="weight">Package Weight (kg):</label><br>
            <input type="number" id="weight" name="weight" step="0.01" required><br>
            <label for="rate">Shipping Rate (per kg):</label><br>
            <input type="number" id="rate" name="rate" step="0.01" required><br>
            <button type="submit">Calculate</button>
        </form>
        <div class="result" id="result"></div>
    </div>
    <script>
        document.getElementById('shippingForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const weight = parseFloat(document.getElementById('weight').value);
            const rate = parseFloat(document.getElementById('rate').value);
            const shippingCost = weight * rate;
            document.getElementById('result').textContent = `Shipping Cost: ${shippingCost.toFixed(2)} USD`;
        });
    </script>
</body>
</html>

