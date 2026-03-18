## API Version Plan

### In-memory data shape

- `target`
- `numbers`

### Endpoint

- `GET /bridge-repair/solve`

### Query input

- `part` (required, `1` or `2`)
- `filename` (optional, default: `input.txt`)

### Flow

1. Read input file
2. Parse each line into:
   - `target`
   - `numbers`
3. Run the selected solver based on `part`
4. Count records
5. Measure execution time
6. Return result

### Success response

- `part`
- `filename`
- `recordCount`
- `totalCalibrationResult`
- `timeTakenSeconds`

### Alternate flow

- invalid `part` -> `400 Bad Request`
- file not found -> `404 Not Found`
- file read / processing error -> `500 Internal Server Error`
