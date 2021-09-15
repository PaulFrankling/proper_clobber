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

        * The user is able to create an account by selecting 'Sign up' from the 'Account' dropdown menu.

        ![Sign up location](readme/testing/ux-testing/ux-signup-location.png)

        * The user is then taken to the sign up page where the form prompts the user what to input in each input field with the help of placeholder text.

        ![Sign up form](readme/testing/ux-testing/ux-signup-form.png)

        * The user is then informed their account needs verifying. An email is then sent to the user with a link taking them to a page on the website allowing them to confirm their email. Once confirmed, they are redirected to the login page in which they can now sign in with their new account credentials.

    * *I want to be notified when making specific actions on the website.*

        * The user is presented with a toast message on the top right of the screen when a specific action is taken. When adding products the user is shown their current basket. They are also notified when registering, signing in, logging out or when a user purchases their order. Below is an example of a toast message notifying the user of a specific action:

        ![Toast message example](readme/testing/ux-testing/ux-toast-example.png)

    #### Products

    * *I would like to view all the products the website is selling.*

        * The user is able to view all the products the website is selling by clicking on the home page 'Shop now' CTA button. The user can also access all the products by clicking on the navigation link 'All Products'. This is so the user can easily view all the variety of products the site has to offer.
    
    * *I want to be able to search in the header for a specific product I am looking for.*

        * The user is able to search for specific products in the search bar of the website header.

        ![Search bar](readme/testing/ux-testing/ux-searchbar.png)

        * The user can search for a product by inputting a query into the search bar and pressing enter or clicking on the magnifying glass. Below is an example of a search query result:

        ![Search result example](readme/testing/ux-testing/ux-search-results.png)

        * If the user searches for a product that doesn't exist, they are met with the following page:

        ![Nothing found search result](readme/testing/ux-testing/ux-search-nothingfound.png)

        * The user is also informed if they failed to input anything in the searchbar with a toast presenting an error message:

        ![Empty search query](readme/testing/ux-testing/ux-search-error.png)


    * *I want to be able to filter the products by specific details such as price or alphabetical order.*

        * The user is able to view products by a specific order with the use of a 'Sort by' select box. It is placed at the top left of the products page and the user can view the products by their price for instance, as they may have budget limitations or might want buy something slightly more expensive.

        ![Product sorting example](readme/testing/ux-testing/ux-sorting-example.png)

    * *I would like to be able to view separate categories of clothing for convenience.*

        * The user is able to view specific categories by using the 'Tailoring', 'Footwear' and 'Accessories' navigation bar dropdown menus:

        ![Category page example](readme/testing/ux-testing/ux-categories.png)

        * This way the user is able to view a category they are specifically looking for. They can also view a product by category by using the link on each product card when they are viewing 'All Products'.

    * *I would like to be able to view individual products on another page.*

        * The user can click on each individual product in order to view the products specific details.

    * *I would like to interact with that product, by changing quantity, choosing size or adding it to the basket.*

        * When the user has clicked on an individual product, they are able to change the quantity and choose a size required. When happy with their selection they can add their product to the basket by clicking on the 'Add to Basket' button.

        ![Product detail example](readme/testing/ux-testing/ux-product-detail.png)

    * *I want a toast message to appear every time I add a product to see the current contents of my basket.*

        * When the user adds a product to the basket, a toast pops up showing the user what the contents of the basket are. It shows the products, the products description, size and quantity selected. The user is also able to visit the basket page by clicking on the 'Secure Checkout' button.

        ![Basket toast](readme/testing/ux-testing/ux-basket-toast.png)

    #### Basket

    * *I want to be able to view my selected products in the basket.*

        * The user is able to view the contents of the basket by navigating to the basket page. The user can see the all the relevant information belonging to the item selected, i.e. description, size and quantity.

        ![Basket page example](readme/testing/ux-testing/ux-basket-example.png)

    * *I would like to update quantity amount of a certain product or remove it from the basket.*

        * The user can update the quantity of the chosen product by clicking on the plus and minus icons at either side of the select box field. Once altered to the amount the user wants, they need to click on 'Update' and it will update to the correct quantity selected. They can also remove the item altogether by selecting 'Remove'.

        ![Basket quantity field](readme/testing/ux-testing/ux-basket-quantity.png)

    * *I want to be able to see the total of my basket and see it regularly updated by any changes.*

        * Any alteration made by the user such as updating the quantity of product or removing it will adjust the basket total accordingly. Below shows an image of one item and the second image, shows the updated basket total when there is two products:

        ![Basket total price before](readme/testing/ux-testing/ux-total-price-before.png)
        
        ![Basket total price before](readme/testing/ux-testing/ux-total-price-after.png)
    
    #### Checkout

    * *I want to be able to securely checkout and purchase the products.*

        * Once the user is happy with their basket and click on the 'Secure Checkout' button on the Basket page, they will be taken to the checkout page. On the right of the screen, the user is able to clarify the items in the basket are what they want. The user can change any of them by clicking on the 'Adjust Basket' button below the form on the left and go back to the Basket page.

        * The user can checkout their order by filling out the form and inputting their card details. Once the form is valid, the checkout process can be completed successfully.

        ![Checkout page example](readme/testing/ux-testing/ux-checkout-example.png)

    * *I want to receive an order confirmation once the items are purchased and for it to possess all the details of the order.*

    #### Blog

    * *I want to view the website blog and see what useful insights there might be.*

        * The user can visit the blog by clicking on the 'Blog' link in the navigation bar. They can view all the blogs added on this page.

        ![Blog page example](readme/testing/ux-testing/ux-blog-example.png)

        * The user can click on the 'Read More' button to read that specific blogs full article. On a specific blog detail page, the user can see the origin of the blog by clicking on the credit link near the top of the page or on the 'Read Full Artcile Here' button at the bottom of the page.

        ![Blog detail page example](readme/testing/ux-testing/ux-blog-detail-example.png)

    #### Contact

    * *I would like to be able to contact the store owners with any query I have.*

        * The user can access the contact page by clicking on the 'Contact' page link on the navigation bar. The user is able to provide their name, email, subject and message before submitting it to the site owner.

        ![Contact page example](readme/testing/ux-testing/ux-contact-example.png) 

    * *I want to receive a confirmation email notifying me they know of my query.*

        * Once the form is valid and the user clicks on the 'Send Message' button, the site owner receives an email with the users information and query.

        ![Contact confirmation email](readme/testing/ux-testing/ux-contact-conf-email.png)

        * A toast also appears advising the user, the site owner has received the email and will respond shortly.

        ![Contact page toast](readme/testing/ux-testing/ux-contact-toast.png)

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
    * *I want the user to be able to contact us with any queries or problems.*
    * *I want to be able to add/edit/update products.*
    * *I want to be able to delete products.*
    * *I want to be able to add/edit/update blog posts.*
    * *I want to be able to delete blog posts.*
    * *I want to be able to maintain the use of the website information with the use of the admin panel.*

## Testing process