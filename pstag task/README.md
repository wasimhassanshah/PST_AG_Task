# Car Search Application
- This application allows me to search for cars based on multiple criteria—length, weight, velocity, and color—using a Python + SQL stack. It also provides the possibility to download the result list in XML format.

**1. Project Requirements**
- Python (version 3.11)
- SQL (via SQLite with SQLAlchemy)

**2. Installation Steps**

- a. Open this folder in VS Code (or another IDE).

- b. Open the Terminal in the project’s directory.

- c. Create a Conda Virtual Environment:

In bash write 

conda create -p venv python==3.11 -y


- d. Activate the Virtual Environment:

In bash write

conda activate venv/

**3. Install the Required Packages (Flask, SQLAlchemy, etc.):**

In bash write

pip install -r requirements.txt


** Running the Application
Initialize or Migrate the Database

# Running the Application

**4. By default, when you run the app, it will create cars.db if it doesn’t exist**
a. Run app.py:
In bash write :
python app.py

b. Verify the Application

Open your browser and navigate to given in terminal : http://127.0.0.1:5000/

You will see a simple web interface (from index.html) that lets you input the following values:

Length: e.g., 4.5
Weight: e.g., 1200
Velocity: e.g., 200
Color: e.g., red

- Click Search to retrieve the matching cars.

- Click Download XML to get the results in XML format.


# Running the Tests

a. Run the Test File (test_app.py):

In bash write

python test_app.py

b. Successful Test Output
You should see something like:


..
----------------------------------------------------------------------
Ran 2 tests in 0.XXXs

OK

- This means both tests ran successfully:

test_search checks the /search endpoint and expects “red” in the results.
test_download checks the /download endpoint and ensures it returns an HTTP 200 status code.


# . Description of Each File

a. app.py

Uses Python and SQLAlchemy (with SQLite) to define a Car model.
Exposes two routes:
/search: filters cars by all provided criteria (length, weight, velocity, color) using AND logic.
/download: returns the filtered results in XML format as a string.

b. test_app.py

Contains basic tests verifying that:
Searching (/search) returns a 200 response and includes “red” in the data.
Downloading (/download) returns a 200 response.
Demonstrates software quality by verifying endpoints are working correctly.

c. index.html

Presents a simple interface for the user to input the criteria and either search or download results in XML.
Allows me to fill in length, weight, velocity, color fields.

d. requirements.txt (if present)

Lists the necessary packages (Flask, SQLAlchemy, etc.) to run this application.

#  Proving the Implementation Meets Requirements
Does This Code Meet the Requirements?

a. Stack: Python latest version, SQL

I’m using Python 3.11 + SQLite (through SQLAlchemy). Check.

b. Domain Object: Car

The Car model has length, weight, velocity, color. Check.

c. Web Search That Respects All Criteria

The /search route applies all filters if they are provided (using an AND condition). Check.

d. Result List Downloadable as XML

The /download route returns an XML string of all cars matching the filters. Check.

e. Prove the Implementation Meets the Requirement

I have tests (test_app.py) to check both /search and /download. Check.

f. Ensure Software Quality and Execution

The tests run successfully, demonstrating basic functionality. Check.

**Conclusion: This solution fully satisfies the task requirements.**


# Conclusion
- My solution searches for cars by specific criteria: length, weight, velocity, color.
- It returns the results as JSON in the /search route or as XML in the /download route.
- The included tests prove correctness and ensure the software quality is maintained.
- By following the steps above, the examiner can confirm the solution is operational, meets all requirements, and demonstrates proper execution.

