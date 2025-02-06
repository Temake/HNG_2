# Number Classification API

## Description
This project is a Flask API that classifies numbers based on various properties such as prime, perfect, armstrong, even, and odd. It also fetches fun facts about the number from an external API.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd PROJECT_2
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the Flask application, execute the following command:
```bash
python main.py
```
The application will start on `http://127.0.0.1:5000`.

## API Endpoints
- **GET /api/classify-number**: Classifies a number based on its properties.
  - **Query Parameters**:
    - `number`: The number to classify (required).
  - **Response**: Returns a JSON object with the classification results.

