# CLI App

This is a simple CLI app written in Python to use [REST APIs](https://www.odata.org/getting-started/) by giving different command line arguments.

## Installation

Install the dependency packages using pipfile.

```bash
pipenv install
```

## Usage

Run **`CLI.py`** file and give appropriate arguments to get the desired output.

1. To get details of an existing user from the REST API.

   ```bash
   python CLI.py user_detail <Id>
   ```

   example-

   ```bash
   python CLI.py user_detail russellwhyte
   ```

2. To get the data set from REST API using filter. At the moment only FirstName filter is available. So all the data where FirstName gets matched to passed argument will come in response data set.

   ```bash
   python CLI.py user_filter <firstname>
   ```

   example-

   ```bash
   python CLI.py user_filter Scott
   ```

3. To create a new data on the server we need to pass user's properties as body of the web request. We can save user's properties in the **`new_user.json`** file and run below command.

   ```bash
   python CLI.py create_user
   ```

## License

[MIT](https://opensource.org/licenses/MIT)
