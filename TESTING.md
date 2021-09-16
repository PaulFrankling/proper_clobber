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

        * Once the user has successfully checked out and ordered their items, the user is taken to the checkout success page. On this page the user can see their order information from the order just made.

        ![Checkout success page](readme/testing/ux-testing/ux-checkout-success.png)

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

        * Once the form is valid and the user clicks on the 'Send Message' button, the user receives an email advising them the site owner will be in touch shortly.

        ![Contact confirmation email](readme/testing/ux-testing/ux-contact-conf-email.png)

        * A toast also appears advising the user the site owner will be touch shortly.

        ![Contact page toast](readme/testing/ux-testing/ux-contact-toast.png)

* As a registered customer:

    * *I want to be able to login and out of the website comfortably.*

        * The user is able to successfully login to the website by going to to the 'Account' dropdown menu on the top right of the navigation bar. The login page requires an email or username and a password to access their account and the details can be remembered by an optional checkbox, making it quicker for the user logging into the website in the future.

        ![Login page example](readme/testing/ux-testing/ux-log-in.png)

        * The user can also log out by going to the 'Account' dropdown menu when signed in and selecting 'Log Out'. The user is then taken to the log out confirmation page allowing them to change their mind if necessary.

        ![Log out example](readme/testing/ux-testing/ux-log-out.png)

    * *I want to be able to reset my password.*

        * The user is able to reset their password by clicking on the 'Forgot Password?' link on the login page. When they click on it, they are taken to a page instructing them to input their email so an email can be sent with a link for the user to reset their password. When the user clicks on the link, they are then able to change their password and confirm it by inputting it a second time. Once the user has finished, they are advised it has been successfully reset and a toast message advises them too.

    * *I want to be able to view my personal profile.*

        * When the user is signed in, they can access their profile by going to the 'Account' dropdown menu and clicking on 'My Profile'. This page shows default delivery details and previous order history information belonging to the specific logged in profile.

    * *I want to be able to save default delivery details to skip the process of adding them in on a second order.*

        * The user can do this on the Checkout page when purchasing their order. Below the order form, is an optional checkbox for the user to interact with. If it is clicked when the order is submitted, the delivery information is saved to the profile page.

        ![Profile default delivery details](readme/testing/ux-testing/ux-profile-delivery-update.png)

    * *I want to be able to update my default delivery details.*

        * The user can do this by visiting their profile page and filling out the form and when finished they can save it by clicking on 'Update Information'. When they return to the Checkout page, they will then see the updated delivery address details.

    * *I want to be able to view previous orders in the order history.*

        * The order history can be viewed on the right hand side of the profile page. It shows a list of all orders made and the user can view the full details of an order by clicking on the order number link.

        ![Profile order history](readme/testing/ux-testing/ux-order-history.png)

* As the store owner:

    * *I want customers to be able to select and purchase products comfortably.*

        * Customers are able to easily view products, choose a size and quantity and add it to their basket before checking out securely. They are then provided with a order confirmation reciept on the checkout success page as well as an email confirming their order.

    * *I want customers to enjoy reading the blogs and insights the website has to offer.*

        * Users are able to visit the blog easily on the main navigation bar. They can view all the previews on the blog page, visit each page to view the full article and they can visit the origin of the blog too. The blogs have potential useful information relevant to the user with regards to clothing.

    * *I want the user to be able to contact us with any queries or problems.*

        * The user can easily contact the site owner through the Contact page. They are notified of their message has been successfully sent through the use of a toast and a confirmation email.

    * *I want to be able to add/edit/update products.*

        * As the site owner, products are able to be added by going to the Product Management page which is located in the 'Accounts' dropdown menu.

        ![Add product page](readme/testing/ux-testing/ux-add-product.png)

        * Products can be edited and updated by clicking on the 'Edit' button on the Product page or Product Detail page. This takes the site owner to the Product Management (Edit Product) page where the input fields are prepopulated with existing product information so it can be easily edited and updated.

        ![Edit product page](readme/testing/ux-testing/ux-edit-product.png)

    * *I want to be able to delete products.*

        * Products can be deleted by the site owner when they are on the Product or Product Detail page. If they click on the 'Delete' button, a modal appears giving the user the option to confirm the deletion to better prevent accidental deletion of a product.

        ![Product modal](readme/testing/ux-testing/ux-product-modal.png)

    * *I want to be able to add/edit/update blog posts.*

        * As the site owner, blog posts are able to be added by going to the Blog Management page which is located in the 'Accounts' dropdown menu. 

        ![Add blog page](readme/testing/ux-testing/ux-add-blog.png)

        * Blog posts can be edited and updated by clicking on the 'Edit' button on the Blog page or Blog Detail page. This takes the site owner to the Blog Management (Edit Post) page where the input fields are prepopulated with existing blog post information so it can be easily edited and updated.

        ![Edit blog page](readme/testing/ux-testing/ux-edit-blog.png)

    * *I want to be able to delete blog posts.*

        * Blog posts can be deleted by the site owner when they are on the Blog or Blog Detail page. If they click on the 'Delete' button, a modal appears giving the user the option to confirm the deletion to better prevent accidental deletion of a blog post.

        ![Blog modal](readme/testing/ux-testing/ux-blog-modal.png)

    * *I want to be able to maintain the use of the website information with the use of the admin panel.*

        * As a site owner, the admin panel is very useful in managing things like products, blog posts, users,messages from users and orders.

## Testing process

### Manual Testing

#### Navigation bar

* All navigation bar links were tested and worked correctly. &check;
* All dropdown menus appear correctly when their link has been clicked and all dropdown menu links take the user to the right page. &check;
* The 'Proper Clobber' logo takes the user back to the home page as intended. &check;
* Below the basket icon, shows the total price of the current basket and correctly changes price every time an item is added or removed. &check;
* The search bar works as expected, it returns a page of products if the user correctly matches something in the product database. &check;
* If a search query doesn't match a product on the site, the user is informed that '0 Products found for "*Query*". &check;
* If nothing is inputted, the user receives a toast advising they haven't 'entered any search criteria!'. &check;

#### Footer

* All social media links take the user to the correct page and correctly open a new tab for the user to view them on. &check;

#### Home

* The 'Shop Now' CTA button takes the user to the 'All Products' page as intended. &check;

#### Products

##### Product page

* Each product takes the user to that specific products detail page. &check;
* Each product zooms in slightly when hovered over correctly &check;
* The sort by select box options were all tested and ordered all the products correctly. &check;
* The number of products on the page presented next to the sort by select box always shows the correct amount of products currently on the page. &check;

##### Product Detail page

* When the user hovers over the product image, it zooms in slightly as expected. &check;
* When the user clicks on the product image, it opens a new tab for the user to view a full page image of the product as intended. &check;
* The size select box shows the correct sizes for the product and works as intended. &check;
* If an item has clothing sizing it will shows sizes; XS to XXL as intended and for footwear sizing; UK 6 to UK 13 as intended. &check;
* The quantity select box minus and plus buttons work correctly. i.e they decrease or increase quantity by 1 each time they are pressed. &check;
* The quantity will not go below 1 as intended and above 10 as intended. If the user tries to manually input a number out of this range, they aren't able to add the product to basket and will be informed it must be 'less than or equal to 10'. &check;
* The 'Add to Basket' button works as expected and adds the item(s) to basket. &check;



