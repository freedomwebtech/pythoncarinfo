import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# Prompt user to enter the car company and model
car_company = input("Enter the car company: ")
car_model = input("Enter the car model: ")

# URL of the website with placeholders for company and model
url = f"https://www.cartrade.com/{car_company.lower()}-cars/{car_model.lower()}/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all <p> tags with a specific class
    p_elements = soup.find_all('p', class_='specTitle mt-0 mb-0 mr-0 font-weight-normal')
    
    # Find all <td> tags with a specific class
    td_elements = soup.find_all('td', class_='specData')
    
    # Extract the text from each <p> tag and <td> tag
    data = []
    for p_element, td_element in zip(p_elements, td_elements):
        p_text = p_element.text.strip()
        td_text = td_element.text.strip()
        data.append([p_text, td_text])
    
    # Print the table
    print(tabulate(data, headers=["Attribute", "Value"], tablefmt="grid"))
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
