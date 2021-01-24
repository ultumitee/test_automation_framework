# About

This is an automation suite which tests below requirements for Trendyol web page
* Log in to system with a user
* Click on each boutique tabs and verify if all boutique images are loaded
* Navigate to a random boutique and verify if all product images are loaded
* Navigate to a product detail
* Add the product to basket and verify if added

This tool is developed with Python and uses pytest framework for testing execution

## Dependency

To be able to run this tool, Python 3.X is required

## Installation

* Clone the source code from [Github]("https://github.com/ultumitee/test_automation_framework")

* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements

```bash
git clone https://github.com/ultumitee/test_automation_framework.git
pip install requirements.txt
```

## Usage
* First of all, update the user_info.yaml file and enter email, password information for login scenario
```yaml
EMAIL: Enter Email Address Here
PASSWORD: Enter Password Here
```
* After updating the configuration, you can execute below command to run the UI tests

```bash
pytest tests/test_trendyol_ui.py --browser chrome --html=report/report.html
```
You can use Chrome, Firefox, Internet Explorer, Edge or Opera browsers in browser parameter

* To run the api tests, you can execute the command below
```bash
pytest tests/test_api.py --html=report/report.html
```

After the execution, it generates an HTML report and adds a screenshot of the last state in report folder