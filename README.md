Sure! Here's a ready-to-use `README.md` file formatted specifically for GitHub:

---

````markdown
# 🦋 Lepidex - Butterfly Species Classifier API

Lepidex is a machine learning-powered REST API that identifies butterfly species from uploaded images using a trained Keras model and FastAPI.

## 🚀 Quick Start

### 1. Clone the repository

```bash

git clone https://github.com/dhruvreddy/lepidex-backend.git
cd lepidex-backend
````

### 2. Create a virtual environment and install dependencies

```bash

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the API

```bash

python main.py
```

Visit `http://localhost:8000/docs` to access the Swagger UI for testing the API.

## 📤 API Endpoint

### `POST /scan`

Upload a butterfly image and get a predicted species.

**Request:**

* **Form field:** `image` (file)

**Response:**

```json
{
  "butterfly": {
    "Common Name": "An 88",
    "Binomial Name": "Diaethria anna",
    "Domain": "Eukarya",
    "Kingdom": "Animalia",
    "Phylum": "Arthropoda",
    "Class": "Insecta",
    "Order": "Lepidoptera",
    "Family": "Nymphalidae",
    "Genus": "Diaethria",
    "Species": "D. anna"
  }
}
```

## 🧠 Model Info

The API uses a trained TensorFlow/Keras model stored at `/butterfly_v1.keras`. It predicts the class index, which is mapped to a species label defined in `schemas.py`.

## 🛠 Project Structure

```
.
├── Dockerfile
├── LICENSE
├── README.md
├── __pycache__
│   └── main.cpython-39.pyc
├── butterfly_v1.keras
├── dependency_injection
│   ├── __init__.py
│   ├── __pycache__
│   └── lepidex_di.py
├── main.py
├── pyproject.toml
├── repositories
│   ├── __init__.py
│   ├── __pycache__
│   └── lepidex.py
├── routers
│   ├── __init__.py
│   ├── __pycache__
│   └── lepidex_router.py
├── schemas
│   ├── __init__.py
│   ├── __pycache__
│   └── butterfly_schema.py
└── uv.lock
```

## 📦 Tech Stack

* FastAPI
* TensorFlow / Keras
* Pillow
* NumPy
* Uvicorn

## 🧪 Example `curl` Request

```bash
curl -X POST "http://localhost:8000/scan" \
  -H "accept: application/json" \
  -F "image=@path/to/image.jpg"
```

## 📄 License

MIT License [[LICENSE](LICENSE)]

## 🤝 Contributions

Feel free to open issues or pull requests. Feedback and contributions are welcome!

Let me know if you'd like to customize the author name, add badges (like build status, license, etc.), or include instructions for Docker deployment or model training.

