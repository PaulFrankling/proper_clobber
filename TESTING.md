# Testing

## Validation

### HTML

#### W3C Markup Validation Service 

* [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the project. Each page was validated by its URI and produced no errors or warnings. When each HTML page was validated by direct input, all errors produced were due to templating.

![HTML Validation](readme/testing/validation/html-validation.png)

### CSS

#### W3C CSS Validation Service

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the project. As well as showing no errors when validating the projects CSS through its URI, there was also no errors when each CSS file was validated through direct input.

![CSS Validation](readme/testing/validation/css-validation.png)

### JavaScript

#### JSHint

* All JavaScript files or snippets of JavaScript at the bottom of HTML files were validated successfully through [JSHint](https://jshint.com/).

![JavaScript Validation](readme/testing/validation/jshint.png)

### Python

* All Python files were validated through the use of [PEP8 online](http://pep8online.com/) and all passed successfully.

![Python Validation](readme/testing/validation/python-validation.png)

* A Gitpod built-in linter called pylint was also used to fix bugs within the python code and provided many suggestions on how to improve the code. For instance it advised to place a docstring at the top of all the python files.

![Pylint Example](readme/testing/validation/pylint-example.png)

### Lighthouse

* Lighthouse was also used to test the project on both desktop and mobile.

#### Desktop

![Lighthouse Desktop Result](readme/testing/lighthouse-results/lighthouse-desktop-result.png)

#### Mobile

![Lighthouse Mobile Result](readme/testing/lighthouse-results/lighthouse-mobile-result.png)

## Testing of User stories from UX section of README.md

* As an unregistered customer...

    #### General

    1. *I want to be able to understand the purpose of the website.*
    1. *I want to be able to easily navigate around the website.*
    1. *I want to be able to easily locate and create a new account.*
    1. *I want to be notified when making specific actions on the website.*

    #### Products

    1. *I would like to view all the products the website is selling.*
    1. *I want to be able to search in the header for a specific product I am looking for.*
    1. *I want to be able to filter the products by specific details such as price or alphabetical order.*
    1. *I would like to be able to view separate categories of clothing for convenience.*
    1. *I would like to be able to view individual products on another page.*
    1. *I would like to interact with that product, by changing quantity, choosing size or adding it to the basket.*
    1. *I want a toast message to appear every time I add a product to see the current contents of my basket.*

    #### Basket

    1. *I want to be able to view my selected products in the basket.*
    1. *I would like to update quantity amount of a certain product or remove it from the basket.*
    1. *I want to be able to see the total of my basket and see it regularly updated by any changes.*
    
    #### Checkout

    1. *I want to be able to securely checkout and purchase the products.*
    1. *I want to receive an order confirmation once the items are purchased and for it to possess all the details of the order.*

    #### Blog

    1. *I want to view the website blog and see what useful insights there might be.*

    #### Contact

    1. *I would like to be able to contact the store owners with any query I have.*
    1. *I want to receive a confirmation email notifying me they know of my query.*

* As a registered customer:

    1. *I want to be able to login and out of the website comfortably.*
    1. *I want to be able to reset my password.*
    1. *I want to be able to view my personal profile.*
    1. *I want to be able to save default delivery details to skip the process of adding them in on a second order.*
    1. *I want to be able to update my default delivery details.*
    1. *I want to be able to view previous orders in the order history.*

* As the store owner:

    1. *I want customers to be able to select and purchase products comfortably.*
    1. *I want customers to enjoy reading the blogs and insights the website has to offer.*
    1. *I want to the user to be able to contact us with any queries or problems.*
    1. *I want to be able to add/edit/update products.*
    1. *I want to be able to delete products.*
    1. *I want to be able to add/edit/update blog posts.*
    1. *I want to be able to delete blog posts.*
    1. *I want to be able to maintain the use of the website information with the use of the admin panel.*

## Testing process