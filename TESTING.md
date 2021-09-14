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

    * *I want to be able to understand the purpose of the website.*

        * On arrival of the website, the user is able to understand the purpose of the website. This is due to the use of imagery, logo, the homepage CTA and the navigation links available to the user to visit.

        ![Homepage background](readme/testing/ux-testing/ux-homepage.png)

    * *I want to be able to easily navigate around the website.*

        * The user is able to navigate around the site easily by the use of the Fixed top navigation bar on every page of the website. The user can change page very quickly with close access to the navigation bar at all times. All links in the navigation bar are easily identifiable and dropdown menus are located on some links to help the user find something more specific for their needs.

    * *I want to be able to easily locate and create a new account.*
    * *I want to be notified when making specific actions on the website.*

    #### Products

    * *I would like to view all the products the website is selling.*
    * *I want to be able to search in the header for a specific product I am looking for.*
    * *I want to be able to filter the products by specific details such as price or alphabetical order.*
    * *I would like to be able to view separate categories of clothing for convenience.*
    * *I would like to be able to view individual products on another page.*
    * *I would like to interact with that product, by changing quantity, choosing size or adding it to the basket.*
    * *I want a toast message to appear every time I add a product to see the current contents of my basket.*

    #### Basket

    * *I want to be able to view my selected products in the basket.*
    * *I would like to update quantity amount of a certain product or remove it from the basket.*
    * *I want to be able to see the total of my basket and see it regularly updated by any changes.*
    
    #### Checkout

    * *I want to be able to securely checkout and purchase the products.*
    * *I want to receive an order confirmation once the items are purchased and for it to possess all the details of the order.*

    #### Blog

    * *I want to view the website blog and see what useful insights there might be.*

    #### Contact

    * *I would like to be able to contact the store owners with any query I have.*
    * *I want to receive a confirmation email notifying me they know of my query.*

* As a registered customer:

    * *I want to be able to login and out of the website comfortably.*
    * *I want to be able to reset my password.*
    * *I want to be able to view my personal profile.*
    * *I want to be able to save default delivery details to skip the process of adding them in on a second order.*
    * *I want to be able to update my default delivery details.*
    * *I want to be able to view previous orders in the order history.*

* As the store owner:

    * *I want customers to be able to select and purchase products comfortably.*
    * *I want customers to enjoy reading the blogs and insights the website has to offer.*
    * *I want to the user to be able to contact us with any queries or problems.*
    * *I want to be able to add/edit/update products.*
    * *I want to be able to delete products.*
    * *I want to be able to add/edit/update blog posts.*
    * *I want to be able to delete blog posts.*
    * *I want to be able to maintain the use of the website information with the use of the admin panel.*

## Testing process