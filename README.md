# BridgeUP-assignment
Home Assignment: Building an API in Python for Managing Weights (`w`)

**Objective:**

Create a RESTful API using Python (with Flask or FastAPI) to manage the weights (`w`) of a campaign, category, or source within a given JSON structure. The API should allow updating these weights with specific limitations and validation checks.

**Requirements:**

1. **API Endpoints**:
   - `GET /client/{clientId}/weights`: Retrieve the entire structure with all current weights.
   - `PUT /client/{clientId}/weights`: Update the weights (`w`) of a source / a category or of a campaign within a category.

2. **Validation Checks**:
   - The total weight of all campaigns within a category must sum to 100.
   - The total weight of all categories within a source must sum to 100.
   - The total weight of all sources must be a non-negative number, and individual updates should not cause the weight to go below zero.
   - The weight (`w`) for any entity should be between 0 and 100.

3. **Error Handling**:
   - Return appropriate HTTP status codes and error messages for invalid operations, such as attempting to set a weight outside the 0-100 range or causing an aggregate weight to exceed 100.

4. **Initial Data Structure**:
   - The API should start with a predefined JSON structure (like the one provided earlier).

**Implementation Details:**

- **Framework**: You can use either Flask or FastAPI or others.
- **Data Storage**: Use an in-memory data structure (e.g., a Python dictionary) to represent the JSON structure. Optionally, implement persistence using a file or database.
- **Testing**: Provide a set of unit tests or API tests to validate that the API functions correctly.




### Example Data Structure (for Reference)

```json
{
  "source-a": {
    "w": 0
  },
  "source-b": {
    "w": 100,
    "categories": {
      "kitchen-tools": {
        "w": 20,
        "campaigns": {
          "electric-garlic-chopper": {
            "w": 100
          }
        }
      },
      "gadgets": {
        "w": 50,
        "campaigns": {
          "smartphone-stand": {
            "w": 20
          },
          "wireless-charger": {
            "w": 50
          },
          "wireless-gadget-01": {
            "w": 50
          }
        }
      }
    }
  }
}
```

### Detailed Task Breakdown
1. **Setup the Environment**:
   - Install necessary dependencies (Flask or FastAPI).
   - Create a basic project structure.

2. **Define the Data Structure**:
   - Use a Python dictionary to represent the initial JSON structure.
3. **Implement the API Endpoints**:
   - `GET /weights`: Return the entire JSON structure.
   - `PUT /weights/source/{source_name}`: Update the `w` of a source.
     - Validate that the updated weight does not cause the total weight to exceed 100.
   - `PUT /weights/source/{source_name}/category/{category_name}`: Update the `w` of a category.
     - Validate that the updated weight does not cause the total weight of categories within the source to exceed 100.
   - `PUT /weights/source/{source_name}/category/{category_name}/campaign/{campaign_name}`: Update the `w` of a campaign.
     - Ensure that the total weight of campaigns within the category remains 100.

4. **Validation and Error Handling**:
   - Implement validation logic to ensure weights are within the allowed range and the totals meet the requirements.
   - Handle cases where the entity being updated does not exist.

5. **Testing**:
   - Write tests to cover successful updates, boundary cases, and invalid operations.

### Deliverables

1. **Source Code**: The complete source code of the API.
2. **Instructions**: A README file with instructions on how to run the API locally and how to test it.
3. **Tests**: Unit tests or API tests validating the functionality of the API.
4. **Sample Requests**: Example curl commands or Postman collection to demonstrate how to interact with the API.
5. A list of edge cases that are not covered by the code and you think should be on the next stage of this service development

### Evaluation Criteria

- **Correctness**: The API should correctly implement the requirements and handle validation properly.
- **Code Quality**: Code should be clean, well-organized, and follow best practices.
- **Error Handling**: The API should provide informative error messages and handle edge cases gracefully.
- **Testing**: Adequate test coverage should be provided to ensure the API functions as expected.

This assignment will assess your ability to create a robust API with validation logic and handle various edge cases while maintaining data integrity.
