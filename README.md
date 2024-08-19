# BridgeUP-assignment
Home Assignment: Building an API in Python for Managing Weights (`w`)

**Objective:**

Create a RESTful API using Python (with Flask or FastAPI) to manage the weights (`w`) of a campaign, category, or source within a given JSON structure. The API should allow updating these weights with specific limitations and validation checks.

- **Source weights**: Cannot exceed a total of 100.
- **Category weights**: Within a source, the total weight cannot exceed 100.
- **Campaign weights**: Within a category, the total weight must equal exactly 100.

## Requirements

- Python 3.8+
- FastAPI
- Pydantic
- Uvicorn (for running the server)
- Pytest (for testing)


## Running on AWS
The server is running on aws on `44.222.239.1:8000`
APIs:

  `GET: /client/{client_id}/weights`
  
  `PUT: /client/{client_id}/weights/source/{source_name}`
  
  `PUT: /client/{client_id}/weights/source/{source_name}/category/{category_name}`

  `​PUT: /client​/{client_id}​/weights​/source​/{source_name}​/category​/{category_name}​/campaign​/{campaign_name}`

  The update operation will require a simple payload: `{"w": 40}`


## Local installation
1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/weight-management-api.git
   cd weight-management-api

2. **Create and activate a virtual env:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install requirements:**
   `pip install -r requirements.txt`


4. **Running server:**
    `uvicorn app.main:app --reload`

2. **Running tests:**
    `pytests`

3. **Project structure:**
    ```sh
    ├── app
    │   ├── __init__.py           
    │   ├── main.py               
    │   ├── models.py            
    │   ├── services.py          
    │   ├── data.py               
    │   ├── custom_error.py       
    |   └── tests
    │       ├── __init__.py           
    │       └── test_main.py          
    ├── requirements.txt          
    └── README.md                 

## Next steps

1. Supporting Concurrent Updates
Simultaneous updates to the same source, category, or campaign could lead to data inconsistencies.
Need to implement a mechanisms to handle concurrent updates.

2. Implementation of Authorization and Authentication
The project lacks completely of authorization checks could expose sensitive data or allow unauthorized changes.

