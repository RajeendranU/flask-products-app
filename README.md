# Flask Products API

A RESTful Flask API for managing products across multiple categories (TV, Mobile, Laptop) with Docker support and comprehensive testing.

## Features

- RESTful API endpoints for product management
- Support for multiple product categories (TV, Mobile, Laptop)
- Docker containerization with Gunicorn
- Comprehensive pytest test suite
- CORS enabled for cross-origin requests
- Health check endpoint for monitoring

## API Endpoints

- `GET /` - API information and available endpoints
- `GET /health` - Health check endpoint
- `GET /products` - Get all products from all categories
- `GET /products/<category>` - Get products by category (tv, mobile, laptop)
- `GET /product/<category>/<id>` - Get a specific product by category and ID
- `GET /categories` - Get all available categories

## Product Categories

### TV
- Samsung 55-inch QLED TV
- LG 65-inch OLED TV
- Sony 43-inch LED TV

### Mobile
- iPhone 15 Pro
- Samsung Galaxy S24
- Google Pixel 8

### Laptop
- MacBook Pro 14-inch
- Dell XPS 15

## Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/RajeendranU/flask-products-app.git
cd flask-products-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## Docker Deployment

### Build the Docker image:
```bash
docker build -t flask-app .
```

### Run the container:
```bash
docker run -d -p 5000:5000 --name flask-app-container flask-app
```

The application will run with Gunicorn using 4 workers for better performance.

## Testing

Run the test suite using pytest:
```bash
pytest tests/test_app.py
```

The test suite includes:
- Home endpoint tests
- Health check tests
- Products endpoint tests
- Category filtering tests
- Specific product retrieval tests
- Error handling tests

## Project Structure

```
flask-products-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Process file for deployment
├── Dockerfile            # Docker configuration
├── .dockerignore         # Docker ignore file
├── .gitignore           # Git ignore file
├── tests/
│   └── test_app.py      # Test suite
└── README.md            # This file
```

## Technologies Used

- Flask 3.0.0 - Web framework
- Flask-CORS 4.0.0 - Cross-origin resource sharing
- Gunicorn 21.2.0 - WSGI HTTP Server
- Pytest 7.4.3 - Testing framework
- Docker - Containerization

## License

This project is open source and available for use.
