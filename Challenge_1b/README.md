# Prerequisites
* Docker must be installed and running.

## How to Run

1.  **Build the Docker image:**
    From the project's root directory, run the following command to build the image:
    ```bash
    docker build -t my-project .
    ```

2.  **Run the Docker container:**
    Use the following command to run the script. This will create a local `output` directory and save the `result.json` file there.
    ```bash
    docker run --rm -v "$(pwd)/output":/app/output my-project
    ```

3.  **Check the results:**
    The output file will be available at `./output/result.json`.
