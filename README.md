# Credit Simulator (By Aditya Putra)

## About the Application

1. This is a project intended for BCA Digital Technical Assessment
2. Written in Python especially built on version 3.11.5
3. It will run based on config located on `config,py` which currently only store API url
4. Functionalities:
    1. Calculate credit interactively using command line interface
    2. Alternatively, you can pass a text file to the program, and it will take the input from the file
    3. Load calculation from the API defined on the config
5. This program can be run in several ways (Of course you can run it with a direct python run but it won't be
   highlighted here)
    1. Running the executable
    2. Using make command
    3. Run it using Docker

## How it works

1. The program will calculate and run based on your input
    1. If you choose to run in `interactive` mode, your CLI will give you this prompt
    ```
    Credit Simulator
    Enter Vehicle Type (Motor/Mobil): mobil
    Is the vehicle New or Bekas (Baru/Bekas): baru
    Enter Vehicle Year (4 digits): 2023
    Enter Total Credit Amount (in Rupiah): 80000000
    Enter Loan Tenure (1-6 years): 3
    Enter Down Payment (in Rupiah): 65000000
    ```
    2. If you provide `(any_text).txt` as input. It will run based on what written there. Please follow this format (
       alternatively I've provided example file, see `example.txt`)
    ```
    mobil
    baru
    2022
    75000000
    2
    35000000
    ```
2. Run the input and it will give a result like this
    ```
    tahun 1 : Rp. 1,950,000.00/bulan, Suku Bunga : 8%
    tahun 2 : Rp. 2,107,950.00/bulan, Suku Bunga : 8.1%
    tahun 3 : Rp. 2,289,233.70/bulan, Suku Bunga : 8.6%
    ```
3. After it finished the calculation of your input. This program also will load an existing calculation provided by the
   API url in the config. If by default using this mock example `"http://www.mocky.io/v2/5d11a58d310000b23508cd62"`, it
   will give error like this cause it violates the new vehicle definition
    ```
    ==========
    Load Existing Calculations from API
    Error: For New vehicle, the year must be in the current year or the previous one
    ```

## How to Run

### Preparations

1. Make sure you have **python** installed on your machine. Since this built with version **3.11.5**, it's recommended
   using the same version or higher
2. Since we're using python, please also make sure you have **pip** installed
   3Make sure you have **Docker** installed on your machine, only if you want to run it with Docker
3. If you want to change the API Url redirection, please change `config.py`

### Setting Up and Run

1. Install required package using `pip`
    ```sh
    $ make prepare
    ```
2. Running the test
    ```sh
    $ make test
    ```
3. Running test with coverage
    ```sh
    $ make test-with-coverage
    ```
4. Run the program. You can run the program using all these variations
    1. Executable script
        1. Default or Interactive mode
        ```sh
        $ ./credit-simulator
       ```
        2. With File Input
       ```sh
        $ python main.py example.txt
       ```
    2. Make command
        1. Default or Interactive mode
         ```sh
         $ make run
        ```
        2. With File Input
        ```sh
         $ make run --input_file=example.txt
       ```
    3. Docker (This is for default only as to provide)
        1. Build the image first
         ```sh
         $ make build-docker
       ```
        2. Run the app
       ```sh
         $ make run-docker
       ```