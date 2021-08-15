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
1. [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) is used to form the layout of the website and make it responsive. It is also used to add components to the project.
1. [Google Fonts](https://fonts.google.com/specimen/Archivo?query=archivo#standard-styles) is used to implement the primary font of **Archivo** and the secondary font of **Montserrat**.
1. [Font Awesome](https://fontawesome.com/) is used to add icons to the website.
1. [Coolor](https://coolors.co/ffffff-000000-7e7f83-ceff1a) is used to develop a colour scheme for the project.
1. [Flaticon](https://www.flaticon.com/) is used to create and style a shortcut icon/favicon for the project.
1. [TinyPNG](https://tinypng.com/) is used to compress the imagery memory size of the repository to help improve the speed of the website.
1. [Hover.css](https://ianlunn.github.io/Hover/) is used to apply a colour change to certain elements on the page when hovered over with the mouse.
1. [Git](https://git-scm.com/) is used for version control. Code produced in the Gitpod terminal is committed and then pushed to GitHub.
1. [GitHub](https://github.com/) is used to store the project code pushed from Git.

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

* Login to your Heroku account and you next need to input in the terminal:

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
    heroku git:remote -a <heroku app name>
    ```

* Heroku will now start building the app.

## Credits:

### Content

### Media Used

* Home page background image is by Cody Nottingham from [Unsplash](https://unsplash.com/photos/BAd_f3owqNc)
* All allauth pages background image is by Free-Photos from [Pixabay](https://pixabay.com/photos/guy-man-suit-railway-railroad-690483/)
* The images for each product on the website are available to view [here](IMG_CREDITS.md)