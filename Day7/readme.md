How to run the code:

1. Run Part 1 using the command `python .\BridgeRepair-Part1.py <input filename>`. If no filename is provided, it will default to `input.txt`.
2. Run Part 2 using the command `python .\BridgeRepair-Part2.py <input filename>`. If no filename is provided, it will default to `input.txt`.
3. The output will show the total calibration result, total entries and time taken to run the code.

How to run the API version:

Install requirements using `pip install -r requirements.txt`.

1. Start the API using the command `py -m uvicorn BridgeRepair-API_Version:app --reload`.
2. Open the Swagger UI at `http://127.0.0.1:8000/docs` to test the endpoint.
3. Use the `GET /bridge-repair/solve` endpoint with:
   - `part` (required: `1` or `2`)
   - `filename` (optional: defaults to `input.txt`)
4. The response will return the part number, filename, record count, total calibration result, and execution time.
