# Proper Clobber

## Code Institute - Milestone Project 4

Proper Clobber is an e-commerce website that sells smart tailored clothing for men. The purpose of the website is for users to view different products, add their desired products to their shopping basket and securely purchase their order.

## UX (User Experience):

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

## Wireframes:

* [Home Page Wireframe](readme/wireframes/home-page-wireframe.png)

* [Products Page Wireframe](readme/wireframes/products-page-wireframe.png)

### Technology used:

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
1. [Google Fonts](https://fonts.google.com/specimen/Archivo?query=archivo#standard-styles) is used to implement the primary font of **Archivo** and the secondary font of **Montserrat**.
1. [Font Awesome](https://fontawesome.com/) is used to add icons to the website.
1. [Coolor](https://coolors.co/ffffff-000000-7e7f83-ceff1a) is used to develop a colour scheme for the project.
1. [Flaticon](https://www.flaticon.com/) is used to create and style a shortcut icon/favicon for the project.
1. [TinyPNG](https://tinypng.com/) is used to compress the imagery memory size of the repository to help improve the speed of the website.
1. [Hover.css](https://ianlunn.github.io/Hover/) is used to apply a colour change to certain elements on the page when hovered over with the mouse.
1. [Git](https://git-scm.com/) is used for version control. Code produced in the Gitpod terminal is committed and then pushed to GitHub.
1. [GitHub](https://github.com/) is used to store the project code pushed from Git.
1. [Heroku](https://signup.heroku.com/) has been used to deploy the project.

## Testing:

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

* [Stack Overflow](https://stackoverflow.com/questions/226131/how-to-disable-phone-number-linking-in-mobile-safari/) was used to prevent the telephone number from hyperlinking on mobile devices. 

### Content

### Media Used

* Home page background image is by Cody Nottingham from [Unsplash](https://unsplash.com/photos/BAd_f3owqNc)
* All allauth pages background image is by Free-Photos from [Pixabay](https://pixabay.com/photos/guy-man-suit-railway-railroad-690483/)
* The images for each product on the website are available to view [here](IMG_CREDITS.md)
* Blog credits:
    * Are bespoke shoes worth it? by Simon Crompton from [Permanent Style](https://www.permanentstyle.com/2021/08/are-bespoke-shoes-worth-it.html)
    * What watch should I wear with a suit? by Katy Eriks from [Suit Shop](https://suitshop.com/blogs/news/what-watch-should-i-wear-with-a-suit/)
    * How to take care of your suit and make it last, by Natalie Kenney from [Suit Shop](https://suitshop.com/blogs/news/how-to-take-care-of-your-suit-and-make-it-last/)