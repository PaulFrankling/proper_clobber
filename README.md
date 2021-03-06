# Proper Clobber

## Code Institute - Milestone Project 4

![Proper Clobber Site Mockup](readme/mockup/site-mockup.png)

[Click here to view the website](https://proper-clobber-project.herokuapp.com/)

Proper Clobber is an e-commerce website that sells smart tailored clothing for men. The purpose of the website is for users to view different products, add their desired products to their shopping basket and securely purchase their order. The user is also able to view different blogs and contact the owners of the website via the contact app.

> **Please note:** This project is solely for educational purposes, so do not attempt to enter real Debit/Credit Card details whilst using the Stripe functionality in the Checkout app.
> To test the Stripe Functionality for yourself, enter the following details:
> * **Card Number** - 4242 4242 4242 4242
>* **Expiry Date** - Any date.
> * **CVV** - Any 3 digit number.

## Table of contents:

  * [UX (User Experience):](#ux--user-experience--)
    + [User Stories](#user-stories)
      - [General](#general)
      - [Products](#products)
      - [Basket](#basket)
      - [Checkout](#checkout)
      - [Blog](#blog)
      - [Contact](#contact)
  * [Design:](#design-)
    + [Colour Scheme](#colour-scheme)
    + [Typography](#typography)
    + [Imagery](#imagery)
  * [Wireframes:](#wireframes-)
  * [Development:](#development-)
    + [Database Schema](#database-schema)
      - [Models](#models)
  * [Features:](#features-)
    + [General](#general-1)
    + [Home page](#home-page)
    + [Products page](#products-page)
    + [Product Detail page](#product-detail-page)
    + [Basket page](#basket-page)
    + [Checkout page](#checkout-page)
    + [Checkout Success page](#checkout-success-page)
    + [Profile page](#profile-page)
    + [Product Management page](#product-management-page)
    + [Blog page](#blog-page)
    + [Blog Detail page](#blog-detail-page)
    + [Blog Management page](#blog-management-page)
    + [Contact page](#contact-page)
  * [Features left to implement](#features-left-to-implement)
    + [Pagination](#pagination)
  * [Technology used:](#technology-used-)
    + [Frameworks, Libraries and Programs](#frameworks--libraries-and-programs)
  * [Testing:](#testing-)
  * [Deployment:](#deployment-)
    + [Deployment to Heroku](#deployment-to-heroku)
      - [Creating the app on Heroku](#creating-the-app-on-heroku)
      - [Setting up Postgres Database](#setting-up-postgres-database)
      - [Gunicorn](#gunicorn)
      - [Connecting to Heroku](#connecting-to-heroku)
      - [Deploying on Heroku](#deploying-on-heroku)
      - [Amazon AWS](#amazon-aws)
        * [Creating a bucket](#creating-a-bucket)
        * [Bucket Settings](#bucket-settings)
          + [Properties](#properties)
          + [Permissions](#permissions)
          + [Policy](#policy)
          + [Access Control List](#access-control-list)
          + [Creating a User](#creating-a-user)
          + [Creating the User](#creating-the-user)
        * [Connecting to Django](#connecting-to-django)
        * [Adding Media to AWS](#adding-media-to-aws)
    + [Making a local clone](#making-a-local-clone)
  * [Credits:](#credits-)
    + [Code](#code)
    + [Content](#content)
    + [Media Used](#media-used)
    + [Acknowledgements](#acknowledgements)

## UX (User Experience):

### User Stories

* As an unregistered customer...

    #### General

    * I want to be able to understand the purpose of the website.
    * I want to be able to easily navigate around the website.
    * I want to be able to easily locate and create a new account.
    * I want to be notified when making specific actions on the website.

    #### Products

    * I would like to view all the products the website is selling.
    * I want to be able to search in the header for a specific product I am looking for.
    * I want to be able to filter the products by specific details such as price or alphabetical order.
    * I would like to be able to view separate categories of clothing for convenience.
    * I would like to be able to view individual products on another page.
    * I would like to interact with that product, by changing quantity, choosing size or adding it to the basket.
    * I want a toast message to appear every time I add a product to see the current contents of my basket.

    #### Basket

    * I want to be able to view my selected products in the basket.
    * I would like to update quantity amount of a certain product or remove it from the basket.
    * I want to be able to see the total of my basket and see it regularly updated by any changes.
    
    #### Checkout

    * I want to be able to securely checkout and purchase the products.
    * I want to receive an order confirmation once the items are purchased and for it to possess all the details of the order.

    #### Blog

    * I want to view the website blog and see what useful insights there might be.

    #### Contact

    * I would like to be able to contact the store owners with any query I have.
    * I want to receive a confirmation email notifying me they know of my query.

* As a registered customer:

    * I want to be able to login and out of the website comfortably.
    * I want to be able to reset my password.
    * I want to be able to view my personal profile.
    * I want to be able to save default delivery details to skip the process of adding them in on a second order.
    * I want to be able to update my default delivery details.
    * I want to be able to view previous orders in the order history.

* As the store owner:

    * I want customers to be able to select and purchase products comfortably.
    * I want customers to enjoy reading the blogs and insights the website has to offer.
    * I want the user to be able to contact us with any queries or problems.
    * I want to be able to add/edit/update products.
    * I want to be able to delete products.
    * I want to be able to add/edit/update blog posts.
    * I want to be able to delete blog posts.
    * I want to be able to maintain the use of the website information with the use of the admin panel.

## Design:

### Colour Scheme

![Colour Scheme](readme/design/colour-scheme.png)

[Coolor](https://coolors.co/ffffff-f5f5f5-7e7f83-000000-ceff1a) was used to create a colour scheme for the project:

* White `#FFFFFF`
* Cultured `#F5F5F5`
* Gray Web `#7E7F83`
* Black `#000000`
* Electric Lime `#CEFF1A`

### Typography

The primary font for the project is **Archivo** and the secondary font is **Montserrat**. 
Both fonts were taken from [Google Fonts](https://fonts.google.com/specimen/Archivo?query=archivo#standard-styles).

### Imagery

The Imagery for the project was taken from [Pixabay](https://pixabay.com/), [Pexels](https://www.pexels.com/) & [Unsplash](https://unsplash.com/).
The homepage background was used to present a sunny landscape of New York to give a warm feeling to the user.
The sign in/register pages background was a black and white image of a suited man to provide a stylish and sophisticated feel to the website.

## Wireframes:

* [Home Page Wireframe](readme/wireframes/home-page-wireframe.png)

* [Products Page Wireframe](readme/wireframes/product-page-wireframe.png)

* [Product Detail Page Wireframe](readme/wireframes/product-detail-wireframe.png)

* [Basket Page Wireframe](readme/wireframes/basket-page-wireframe.png)

* [Checkout Page Wireframe](readme/wireframes/checkout-page-wireframe.png)

* [Checkout Success Page Wireframe](readme/wireframes/checkout-success-wireframe.png)

* [Profile Page Wireframe](readme/wireframes/profile-page-wireframe.png)

* [Add & Edit Blog/Products Pages Wireframes](readme/wireframes/add-edit-forms-wireframe.png)

* [Blog Page Wireframe](readme/wireframes/blog-page-wireframe.png)

* [Blog Detail Page Wireframe](readme/wireframes/blog-detail-wireframe.png)

* [Contact Page Wireframe](readme/wireframes/contact-page-wireframe.png)

## Development:

### Database Schema

![Database Schema](readme/database_schema/database-schema.png)

The Database Schema was designed by using [Quick Database Diagrams](https://app.quickdatabasediagrams.com/#/).

#### Models

* **Category** - Contains the categories of each product.
* **Product** - Contains specific information for each product.
* **Order** - Contains details of the customers order, delivery information and products ordered.
* **OrderLineItem** - Contains information of the products, quantities and total for the customers order.
* **User** - Contains username, password and email from [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html).
* **UserProfile** - Contains the details for future orders as well as historical ones.
* **BlogPost** - Contains the blog posts and all the information regarding the author and its origins.
* **ContactMessages** - Contains the messages and queries sent by customers.

## Features:

### General

The base of the website implements a fixed top navigation bar that presents the Logo, Search bar and icons representing accounts and basket. The accounts tab is a dropdown menu for registering an account or signing in. When the user is signed in, those options don't appear any more and their profile page and the logging out function become available. When the superuser is signed in they can visit the Blog and Product Management pages to add new blog posts or products. Lastly at the top of the navigation bar is the icon that links to the basket app and below it shows the price of the users current basket. When an item is added to the basket, the price changes to match the basket total and changes colour.

On the next row of the fixed top header, is the navigation links, which are Home, All Products, Tailoring dropdown menu, Footwear dropdown menu, Accessories dropdown menu, Blog and Contact. Below that is a general notice telling the user it is free delivery for orders above ??50.00.

When appropriate actions are taken, Toast messages appear below the basket icon. For example, when someone signs in or logs out, one appears. A Toast message will appear when the user adds an item to the basket and will provide information of the current basket every time an item is added to it.

The footer of the project presents social media icons that open up the sites on another tab. There is also company information, as well as copyright information.

### Home page

The user is first met with the home page when visiting the website. The page presents a hero image of a man dressed stylishly, sat on a bench as they view New York.
The page presents a slogan, as well as a 'Shop Now' CTA button that takes the user to the products page.

### Products page

The user can view all products by selecting 'All Products' in the navigation bar, or they can view products by their specific category in the navigation dropdown menus; Tailoring, Footwear and Accessories.

When the user arrives on a particular product page, they can sort the products in a particular order such as 'Product name' (Alphabetically), 'Price' or 'Rating'.

The products are presented with the use of cards, showing its image, name, price, category and rating. Clicking on these cards takes the user to its specific Product Detail page.

If the superuser is on this page, they can edit the chosen product by clicking on the 'Edit' button and it'll take them to the Product Management page (Edit Product). They can also delete a product on the Product page. The 'Delete' button is next to the 'Edit' button and when the 'Delete' button is clicked on, it activates a modal which gives the superuser a chance to cancel or confirm deletion. 

### Product Detail page

Each product has its own Product Detail page and presents its image in a larger form. Clicking on the image creates a new tab with a full screen image of the product.

The page also presents the products name, price, description, category and rating. As well as a select box for the user to choose a size for the product and a quantity box for the user to potentially purchase more of the same item. There is an 'Add To Basket' button as well, which adds the item to the basket.

If the superuser is on this page, they can edit the chosen product by clicking on the 'Edit' button and it'll take them to the Product Management page (Edit Product). They can also delete a product on the Product Detail page. The 'Delete' button is next to the 'Edit' button and when the 'Delete' button is clicked on, it activates a modal which gives the superuser a chance to cancel or confirm deletion. 

> The quantity box only allows the user to add up to ten items at a time. I researched a few clothing websites and found this to be a common maximum amount.

### Basket page

If the user hasn't added an item to the basket, they are given the option of being guided back to the products page with a 'Continue Shopping' CTA button.

When the user has items in the basket, the user can view which items they have added. They can see the image, name, sku code, size of item, price, quantity and subtotal, which shows the quantity selected multiplied by price of individual item.
The total and delivery is shown below as well as the grand total. The grand total shows the price of the basket total and delivery fee added together (if delivery fee is applied). A message appears advising the user if they order x amount more they will qualify for free delivery. This message disappears if the user is spending over ??50 and puts the delivery fee to ??0.

To end with, there is a 'Secure Checkout' button that takes the user to the Checkout page for them to complete the order process.
The total price information and 'Secure Checkout' button are placed at the top of medium and small device screen as opposed to the bottom of large size screens.

### Checkout page

Once the user is satisfied with their basket, they are taken to the Checkout page. On arrival the user is met with a group of input fields for personal information, i.e name, phone number and email. Then below that is a group of input fields for delivery details, such as street address, town or city and postcode of where the delivery is being sent too. Below that is the payment input field that is linked to Stripe for the user to purchase their order. 

On the right hand side of the page (on large size screens) is the current basket of items that the user is going to buy and the grand total they are paying. This section is shown at the top on mobiles and medium sized devices as opposed to the forementioned right side of the page of large sized screens.

### Checkout Success page

Once the order has been completed successfully, the user is taken to this page where they are able to view the receipt of their order. It presents order date and order number, order items and their details and quantities. It shows where the order is to be delivered and the total of the order. An order confirmation email is sent to the buyer of their order details too.

### Profile page

On the Profile page is two sections; Default delivery information and order history. The default delivery information can be edited and saved by clicking the 'Update information' button. Next to that is the order history which shows the users previous orders and the details of them. The orders each have a link that takes the user to its specific order details.

### Product Management page

The Product management page is only available to the superuser. On this page, crispy forms have been used and the superuser can create a product to add to the website. The user is also taken to this page when they have selected to edit a product from the Product or Product Detail pages.

### Blog page

The Blog page shows a list of blogs the user can preview and the user can view the full blog post by clicking on the 'Read More' button. An image, title, author, blog preview and post date is available to the user for each post.

### Blog Detail page

This page shows the full article of the specific blog chosen by the user. It presents the same information on the blog post from the Blog page but also has a credit for the source and a 'Read Full Article Here' button. This button takes the user to the original source of the blog post.

### Blog Management page

The Blog management page is only available to the superuser. On this page, crispy forms have been used and the superuser can create a blog post to add to the website. The user is also taken to this page when they have selected to edit a blog from the Blog or Blog Detail pages.

### Contact page

This page is designed to allow the user to contact the owner of the website. The user can input their first name, last name, email, a subject and a message. When the message is submitted, the message is sent to the email of the superuser. A confirmation email is also sent to the user, advising them the message has been received by the superuser.

## Features left to implement

### Pagination

* Pagination would be ideal to add to the products and blog posts pages as it would be better for the user experience. The Back to top button helps the user quickly get back to the top but the site would benefit from pagination.

## Technology used:

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs

1. [Django](https://www.djangoproject.com/) is the main high level Python web framework used to speed up the process of building this application.
1. [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) is used to set up user authentication on the site.
1. [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) is used to initialise bootstrap form classes in all forms in the project.
1. [Django Countries](https://pypi.org/project/django-countries/) is installed for the countries select field on the order form.
1. [Gunicorn](https://gunicorn.org/) is used for deploying the project to Heroku.
1. [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) is used to form the layout of the website and make it responsive. It is also used to add components to the project.
1. [Stripe](https://stripe.com/gb) is used as a payment processing platform for the project.
1. [Amazon AWS](https://aws.amazon.com/) is used to store the static files and media files belonging to the project.
1. [Postgres](https://www.postgresql.org/) is the database used by the deployed project.
1. [Google Fonts](https://fonts.google.com/specimen/Archivo?query=archivo#standard-styles) is used to implement the primary font of **Archivo** and the secondary font of **Montserrat**.
1. [Font Awesome](https://fontawesome.com/) is used to add icons to the website.
1. [Coolor](https://coolors.co/ffffff-000000-7e7f83-ceff1a) is used to develop a colour scheme for the project.
1. [Flaticon](https://www.flaticon.com/) is used to create and style a shortcut icon/favicon for the project.
1. [TinyPNG](https://tinypng.com/) is used to compress the imagery memory size of the repository to help improve the speed of the website.
1. [Pinetools](https://pinetools.com/) was used to resize wireframes.
1. [Hover.css](https://ianlunn.github.io/Hover/) is used to apply a colour change to certain elements on the page when hovered over with the mouse.
1. [Balsamiq](https://balsamiq.com/) is used to create the wireframing for the project.
1. [Quick Database Diagrams](https://app.quickdatabasediagrams.com/#/) is used to create the database schema for the project.
1. [Autoprefixer](https://autoprefixer.github.io/) is used to add web prefixes to all the CSS files in the project so the styling renders properly on all browsers.
1. [Am I responsive?](http://ami.responsivedesign.is/) is used to create a mockup of the project.
1. [Markdown TOC](https://ecotrust-canada.github.io/markdown-toc/) has been used to create a table of contents for the README.md and TESTING.md files.
1. [Git](https://git-scm.com/) is used for version control. Code produced in the Gitpod terminal is committed and then pushed to GitHub.
1. [GitHub](https://github.com/) is used to store the project code pushed from Git.
1. [Heroku](https://signup.heroku.com/) has been used to deploy the project.

## Testing:

To view the testing process, view [here](TESTING.md)

## Deployment:

* This project repository was created on [GitHub](https://github.com/) using the Code Institute Gitpod Template.

* Once the repository was created, the process of building my project started by clicking the green 'Gitpod' button above the repositories folders and files.

* Once the workspace loaded, I used the CLI(Command Line Interface) to create the relevant folders and files to start applying code to the project.

* My changes were continually added, committed and pushed to [GitHub](https://github.com/) in the CLI. The commands inputted were as follows:

    ```
    git add <filename>
    ```
    ```
    git commit -m "descriptive commit message"
    ```
    ```
    git push
    ```

### Deployment to Heroku

#### Creating the app on Heroku

This [project](https://github.com/PaulFrankling/proper_clobber) may be deployed to [Heroku](https://www.heroku.com/) by taking the following steps:

* Firstly, click on the 'New' button at the top right of the screen in [Heroku](https://www.heroku.com/).
* Then select 'Create a new app' from the two options provided.
* From there, give your new app a name and choose the region closest to you.
* Then select 'Create app'.

#### Setting up Postgres Database

The next step is to link it to the [Postgres](https://en.wikipedia.org/wiki/PostgreSQL) Database by doing the following:

* Firstly, you need to navigate to the 'Resources' tab.
* Then you need to search Postgres in the 'Add-ons' section and select 'Heroku Postgres'.
* Select the Free plan and click 'Provision'.
* The next step is to install two required dependencies by inputting them in the terminal:

    ```
    pip3 install dj_database_url
    ```
    ```
    pip3 install psycopg2_binary
    ```

* Then these dependencies need adding to the requirements.txt file by using the following command:

    ```
    pip3 freeze > requirements.txt
    ```

* Next you need to make sure the following is added at the top of your settings.py file: `import dj_database_url`

* The current Database settings need commenting out and the following needs to be added to the settings.py file:

    ```
        DATABASES = {
            'default': dj_database_url.parse('DATABASE_URL')
        }
    ```

    > The 'DATABASE_URL' can be found in the 'Config Vars' which are in the 'Settings' section of your Heroku app.

* It is important to note 'DATABASE_URL' is an environmental variable and that you need to make sure it is **NOT** shown in version control.

* Once you set up the above, the models need migrating to the new database. This is done by inputting in the terminal:

    ```
    python3 manage.py migrate
    ```

* A superuser for the app is then needed to be created with the following command:

    ```
    python3 manage.py createsuperuser
    ```

* Commit and push your changes without including any environment variables in version control.

* Next, an if-else statement can be added to the settings.py file. This statement means Postgres will be used if the 'DATABASE_URL' variable is available. If not the default database will be used.

    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```

* Now the [Postgres](https://en.wikipedia.org/wiki/PostgreSQL) database should be ready for use.

#### Gunicorn

* In order for the app to work, [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn) needs to be installed.

    ```
    pip3 install Gunicorn
    ```

* Next, the Procfile needs to be created:

    ```
    touch Procfile
    ```

* The Procfile code should look like this:

    ```
    web: gunicorn <app name>.wsgi:application
    ```

#### Connecting to Heroku

* Now to connect to Heroku through the terminal, input the following command:

    ```
    heroku login -i
    ```

* Login to your Heroku account. Then to temporarily disable the static files until set up in Amazon AWS, you next need to input in the terminal:

    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app <appname>
    ```

    > `--app` needs adding if you have more than one Heroku app.

* In the settings.py file, add the following code:

    ```
    ALLOWED_HOSTS = ["<heroku app name>.herokuapp.com", "localhost"]
    ```

    > This add Heroku to the list of allowed hosts and also 'localhost' so the project can be run locally.

* Commit and push your changes to GitHub.

* Then start the process of pushing to Heroku by inputting:

    ```
    heroku git:remote -a <heroku app name>
    ```

* Push those changes to Heroku by then inputting in the terminal:

    ```
    git push heroku master
    ```

* Heroku will now start building the app.

#### Deploying on Heroku

* Navigate to the 'Deploy' section of Heroku.
* Then search for the repository.
* When it finds the repository, select 'connect'.
* Then navigate further down the page and click on 'Enable Automatic Deploys'.

    > Now any changes pushed to GitHub will also be pushed to Heroku too.

#### Amazon AWS

Amazon AWS is used to store static and media files belonging to the project.

* Firstly, create an AWS account and work through the sign up process. Once the account is set up, you are able to set the project up on AWS.

##### Creating a bucket

* In the main dashboard, search for 'S3' and then click to get started.
* Click on 'Create Bucket'.
* Provide the bucket with a name and select a region.
* Then uncheck the 'Block all public access' box and take note that the bucket is now public.
* Then click 'Create Bucket'.

##### Bucket Settings

###### Properties

* Now go to the 'Properties' section and turn on static website hosting.
* Input index.html and error.html in the boxes containing their namesakes and click 'Save'.

###### Permissions

* Next, navigate to 'Permissions'.
* Then you need to input the following into the CORS Config:

    ```
    [
      {
          "AllowedHeaders": [
              "Authorization"
          ],
          "AllowedMethods": [
              "GET"
          ],
          "AllowedOrigins": [
              "*"
          ],
          "ExposedHeaders": []
      }
    ]
    ```

###### Policy

* Next, you want to go to 'Bucket Policy'.
* Then go to 'Policy generator'.
* Select S3 bucket policy.
* Add * in the principal field to select all principals.
* Then set the action to 'GetObject'.
* Copy and paste your ARN which is available on the previous page.
* Then click, 'Add Statement'.
* Now click on 'Generate Policy'.
* Copy and paste the new policy into the bucket policy.
* Then, add /* onto the end of the resources key.
* Click 'Save'.

###### Access Control List

* Go to the 'Access Control List' section.
* Then under 'Public access', click on 'Everyone'.
* Then check the 'List objects' box and click 'Save'.

###### Creating a User

* To create a user for the bucket, search for 'IAM' and click on it.
* Navigate to 'Groups' and click on 'Create New Group'.
* Give it a name, follow the steps, and click 'Create Group'.
* Then go to 'Policies' and select 'Create policy'.
* Select the JSON tab and go to 'Import managed policy'.
* Then search 'S3' in the search engine and select 'AmazonS3FullAccess' and click 'Import'.
* In the resources section, paste in the ARN from before.
* Then click 'Review Policy'.
* Fill in name and description and click 'Create policy'.
* Go back to the group and select 'Permissions' and go to 'Attach Policy'.
* Find the policy you just created and attach it.

###### Creating the User

* Select 'Users' from the IAM Dashboard sidebar and click 'Add user'.
* Create a username, check the 'Programmatic access' box and click 'Next'.
* Then select the group to add your user too.
* Click through to the send then click on 'Create user'.
* **Then it is important to download the CSV File at the end as it contains the user keys needed to access the app.**

##### Connecting to Django

Once the AWS has been set up, it can now be connected to Django.

* Firstly, you need to install the following packages, `boto3` and `django-storages` by inputting the following in the terminal:

    ```
    pip3 install boto3
    ```
    ```
    pip3 install django-storages
    ```

* These dependencies then need adding to the requirements.txt file by adding the following into the terminal:

    ```
    pip3 freeze > requirements.txt
    ```

* 'Storages' then needs to be added to the INSTALLED_APPS section of settings.py.
* The following code then needs adding to the settings.py file:

    > USE_AWS is an environmental variable created to only run this code when on Heroku.

    ```
    if "USE_AWS" in os.environ:

        AWS_STORAGE_BUCKET_NAME = '<bucket name>'
        AWS_S3_REGION_NAME = '<bucket region>'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

    > The AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY can be found in the downloaded **CSV File**.

* Now, go back to 'Settings' in Heroku and click 'Reveal Config Vars'.
* Then set up the required environmental variables.
* A custom_storages.py file now needs creating to tell Django that in production, the S3 bucket contains the static and media files.
* In the custom_storages.py file, S3Boto3Storage needs importing.
* Then the following classes need setting up in that file:

    ```
    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ```

* Once all the above is completed, commit and push changes to GitHub and Heroku.

##### Adding Media to AWS

Lastly, the media file needs to be added to the bucket.

* In the bucket, create a new folder and name it 'media'.
* Select upload and add the relevant images.
* Then select the option to grant public access.
* Then upload the files.

### Making a local clone

To run this project locally, you need to follow these steps:

1. Go to the [Proper Clobber repository](https://github.com/PaulFrankling/proper_clobber).
1. Above the repositories folders and files, click the 'Code' button.
1. In the 'HTTP' section, copy the URL shown.
1. Next, open **Git Bash**.
1. By using the `cd` command, change to the current working directory you want the cloned repository to be made.
1. Input `git clone` into the terminal and add the URL copied from step 3, then press enter.
1. Your local clone is now created.

Once you have opened up the project in the source-code editor, you need to install the required packages to run it. You can do this by inputting the following in the terminal and pressing enter:

`pip install -r requirements.txt`

> You can also download the ZIP folder of the project by clicking the 'Code' button above the folders and files in the GitHub repository and selecting 'Download ZIP'.

Once that is done, you must set up the required environmental variables to access full functionality of the site:

* DJANGO_SECRET_KEY = Your Secret key
* STRIPE_PUBLIC_KEY = Your Stripe Public key
* STRIPE_SECRET_KEY = Your Stripe Secret key
* STRIPE_WH_KEY = Your Stripe Webhook key
* IN_DEVELOPMENT = True

> Your Stripe variables and keys can be found on your Stripe dashboard.

> You need to create a new Django secret key too which can be taken from the [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/).

Once you have the added the environmental variables and their relevant keys, you need to migrate the the models to set up your database.

* Firstly, input in the terminal:

    ```
    python3 manage.py makemigrations --dry-run
    ```

* You then need to make migrations:

    ```
    python3 manage.py makemigrations
    ```

* Then check the migration plan by inputting:

    ```
    python3 manage.py migrate --plan
    ```

* Now you can migrate the changes:

    ```
    python3 manage.py migrate
    ```

* You then need to create a superuser to access the admin section:

    ```
    python3 manage.py createsuperuser
    ```

* Enter a username and password to set up your superuser, then finally you can run the project by inputting:

    ```
    python3 manage.py runserver
    ```


## Credits:

### Code

* The project was helped established by the Code Institute Tutorial **Boutique Ado** created by Chris Zielinski.
* [Stack Overflow](https://stackoverflow.com/questions/226131/how-to-disable-phone-number-linking-in-mobile-safari/) was used to prevent the telephone number from hyperlinking on mobile devices.
* [Stack Overflow](https://stackoverflow.com/questions/61058107/remove-char-from-the-required-field-label-in-form) was used to remove asterisks from the contact page input field labels.
* [W3 Schools](https://www.w3schools.com/howto/howto_css_zoom_hover.asp) helped with zooming in to a product image card ever so slightly.
* [Stack Overflow](https://stackoverflow.com/questions/19296688/how-to-set-display-time-of-toastmessage) was used to help timeout toasts and fade them out automatically after a few seconds.

### Content

* The Blog credits:
    * Are bespoke shoes worth it? by Simon Crompton from [Permanent Style](https://www.permanentstyle.com/2021/08/are-bespoke-shoes-worth-it.html)
    * What watch should I wear with a suit? by Katy Eriks from [Suit Shop](https://suitshop.com/blogs/news/what-watch-should-i-wear-with-a-suit/)
    * How to take care of your suit and make it last, by Natalie Kenney from [Suit Shop](https://suitshop.com/blogs/news/how-to-take-care-of-your-suit-and-make-it-last/)

### Media Used

* Home page background image is by Cody Nottingham from [Unsplash](https://unsplash.com/photos/BAd_f3owqNc)
* All allauth pages background image is by Free-Photos from [Pixabay](https://pixabay.com/photos/guy-man-suit-railway-railroad-690483/)
* The images for each product on the website are available to view [here](IMG_CREDITS.md)

### Acknowledgements

* The Slack community for all their help and support.
* The Code Institute Tutor Support team for responding to any difficulty or query quickly and efficiently.
* My Mentor Gurjot Singh for his advice, guidance and incredible support.

> This project was created for educational purposes only.