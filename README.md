# BarberShop - the local barber for all.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/AwrelH/thebarber/main/static/barberlogo.png"?raw=true alt=""></p>

# <p href="#intro" id="intro"> - Intended Purpose of This Website:</p>

  - To greet customers.

  - To be a window of exposure.

  - Interact with the customer.

  - So customers can make appointments.


## Table of contents
- <a href="#ui">UI/UX</a>
- <a href="#thm">Themes</a>
- <a href="#epi">Epics</a>
- <a href="#us">User Stories</a>
- <a href="#des">Design</a>
- <a href="#wire">Wireframes</a>
- <a href="#erd">ERD Diagram</a>
- <a href="#tpy">Testing(Python)</a>
- <a href="#dep">Deployment</a>
- <a href="#b">Bugs During Development</a>
- <a href="#tu">Technologies Used</a>
- <a href="#cr">Credits</a>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="ui"></p>

# UI-UX

  ## Site Purpose

  - The Purpose of this website is get an exposure for the barbershop and in the same way let customers get fimiliar with the shop. It allows the registered users to book appointment and non-customers to get to know the place and if wanted to asks questions and get a respond via mail. Regarding the booking of appointments, they will have a full CRUD functionality for that.

  ## Site Goal and Intended Audience

  - Appeal to the community, share the shops work and add some personality to it. Intended audience is men and boys, customers in need of haircuts and beard grooming.


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="thm"></p>


# Epics

- The Unregistered User

- The Registered User


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="us"></p>

# User Stories

## User Story: Account registration

-   As a Site User
-   I can register an account
-   So that I can use the sites functionality

    ### Tasks

    - install allauth to give users the ability to register

## User Story: Manage Blogposts

-   As a Site Admin
-   I can create, read, update and delete blogposts
-   So that I can manage the blogcontent

    ### Tasks

    - create a superuser to be able to access the backend
    - create Model, View and Templates

  ### User Story: Open BLogposts
-   As a Site User
-   I can click on a post
-   So that I can read/look at that post
  
    ### Tasks

    - create model/view/template so that user can see post in detail
    
### User Story: Comment on post
-   As a Site Admin/Site User
-   I can leave a comment on a post
-   So that I can interact with users/site owner
  
    ### Tasks

    -  add comment possibility to blog_detail and wire it up


### User Story: Approve comments
-   As a Site Admin
-   I can approve or disapprove comment
-   So that the comment section is clean from bad language
  
    ### Tasks

    -  add a boolean to filter out what is approved or not

### User Story: Like and react
-   As a registered User
-   I can interact with posts by liking/or/other
-   So that I can interact with posts and site owner
  
    ### Tasks

    -  add icon that is clickable and counted
    -  in a form of scissors to make it more personal

### User Story: Create drafts
-   As a Site Admin
-   I can create drafts of posts
-   So that I can finish writing them later
  
    ### Tasks

    -  create a integerfield in the model to choose draft or published

### User Story: Booking of time
-   As a registered user
-   I can book an appointment of types
-   So that i can schedule my next appointment with ease
  
    ### Tasks

    - create new app
    - add new model/view/templates
    - decide what bits are necessary  
    
    ### Criteria
    - Create a booking
    - Read a booking
    - Update a booking
    - Delete a booking

### User Story: Datepicker
-   As a Site Admin
-   I can Show our availability
-   So that customers know when we are available
  
    ### Tasks

    - in template for booking click on datefield to make a calender appear
    - in template for booking make an integerfield with available slots

### User Story: View upvotes
-   As a Site Admin
-   I can view the liking of the users
-   So that I can see what the customers like
  
    ### Tasks

    - create a count of how people click the scissors 
    - implement that on the template

### User Story: About us
-   As a Site user
-   I can see where the barbershop is located
-   So that I can easy get there
  
    ### Tasks

    - create new app
    - add content to template with location, phone, email

### User Story: Offers/haircuts/shaving
-   As a registered user
-   I can see what kind of offers are presented
-   So that I can pick one of my choosing
  
    ### Tasks

    - Add type of appointment to booking model
    - add type of appointment to template
    - write about services in the about us section

### User Story: View blogposts
-   As a registered user
-   I can see all the posts
-   so that I get and understanding of the skills and works of the barber
  
    ### Tasks

    - present a blog page with all the post with a good overview

### User Story: Message us with ease
-   As any user
-   I want to be able to message the barber/site owner
-   In a easy fashion send my /question/feedback
  
    ### Tasks

    - add a form in the about section for users to use to send messages to site owner




<p align="right"><a href="#intro">Return to table of contents</a></p><p id="des"></p>

# Design

## Color Pallete
- HEX: 000000, 445261, 4B6B8C, 0D6EFD, F9EBDC
 <p align="center">
  <img width=500 src="https://raw.githubusercontent.com/AwrelH/thebarber/main/static/images/readme-images/palette.png"?raw=true alt=""></p>

## Fonts
- 'Belleza','Akaya Telivigala', Lato, sans-serif;


  

<p align="center">
  <img src=""?raw=true alt=""></p>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="wire"></p>

# Wireframes

  - Title of the wireframe

<p align="center">
  <img  src="https://raw.githubusercontent.com/AwrelH/thebarber/main/static/images/readme-images/index.png" alt=""> Index</p>

<p align="center">
  <img width=500 src="https://raw.githubusercontent.com/AwrelH/thebarber/main/static/images/readme-images/booking.png"?raw=true alt=""> Booking</p>

<p align="center">
  <img width=500 src="https://raw.githubusercontent.com/AwrelH/thebarber/main/static/images/readme-images/new_booking.png"?raw=true alt=""> New Booking</p>



<p align="center">
  <img width=500 src="https://raw.githubusercontent.com/AwrelH/thebarber/main/static/images/readme-images/blogpost.png"?raw=true alt=""> Blogpost</p>

<p align="center">
  <img width=500 src="https://raw.githubusercontent.com/AwrelH/thebarber/main/static/images/readme-images/about.png"?raw=true alt=""> About</p>

<p align="center">
  <img width=500 src="static/images/readme-images/Blog-Detail-PP.png"?raw=true alt=""></p>



<p align="right"><a href="#intro">Return to table of contents</a></p><p id="erd"></p>

# ERD Diagram

  - Title of ERD Diagram

<p align="center">
  <img src="static/images/readme-images/ERD diagram Project4.png"?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="lf"></p>

# Live Features

  - The live site is found

<p align="center">
  <img src=""?raw=true alt=""></p>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tpy"></p>

# Testing (Python)

  - a few Unittest was created to test out views and models


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="dep"></p>

# Deployment

## Steps to take prior to deployment on Heroku

1. creating a repository using code institutes template
1. install django and startproject and startapp
1. install required addons for the project
1. create a env.py file to store all the secret keys and credentials
1. replace secret key/databases in settings.py with variables from env.py
1. create a Procfile containing  `web: gunicorn barbershop.wsgi`
1. set up different variables, paths and templates directory
1. summernote editor was used so for this to work in Heroku add: `X_FRAME_OPTIONS = SAMEORIGIN `to
   settings.py
1. Use `python3 freeze --local > requirements.txt` so that Heroku install all the dependencies when deploying


  ### Early Deployment was an objective. Steps to take after creating a GitHub repository:
1. Sign in to [Heroku](https://id.heroku.com) 
1. Create New App
1. Select my region and click on create app button
1. Add resource in for of Heroku Postgres database
1. go to settings and  Reveal Config Vars and add a new record with SECRET_KEY, CLOUDINARY_URL, DISABLE_COLLECTSTATIC, PORT
1. Scroll to the top of the page and choose the Deploy tab
1. Select Github as the deployment method
1. Search for the repository thebarber and click the connect button
1. Scroll to the bottom of the deploy page and select the preferred deployment type
1. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

 ### Final Deployment

1. When final development is ready the debug setting needs to be changed to: `DEBUG = False` in settings.py, <br>
This also allows for the CSS-styling to get activated. 
1. In Heroku settings, `delete` the config var `DISABLE_COLLECTSTATIC = 1`

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="b"></p>

# Bugs (During Development)

  - During my development I stumbled on a few bugs regarding my database, and migrations. Even though I had been migrating things correctly, a change of a datafield in my booking model. That change created new instances of migrations files each time even though no new changes was made. Nothing that really impacted the project in any way but was annoying. 

  - In the late stage of my project I was met with another bug regarding my database and that created a lot of frustration, and I was unable to fix it, instead I clean out the database and started over. This ending up with uploading new content to the blog, users and so on. But in the end resulting into a bug free database. 

  - A smaller type of bug was when I had a `row` that was sitting in another, thus creating images and margins that were not in line when new blog posts were loaded. This was noticed by another student of code institute when I was asking for fresh eyes to help me spot the error.
 
## Bugs Further testing/Validating

As my project goes to the wire, and my time management not been on point meaning I haven't been able to go through the code, check for error and correct them properly within these areas below. 

### Lighthouse
As seen below there are a few things to do before one can be satisfied with the numbers. Compress image sizes, remove redundant code in head. Add alt='text' to images. Small contrast ratio regarding bits of the content. 



### CSS
This was error-free. 

### HTML
The first check of the site, the homepage. revealed 32 errors. Stray end tags, images without an alt-attribute, trailing slashs. Adding alt-text to the images will not be done. The about page had 12 error-messages.

### PEP8
Looking through the pep8 validator in the gitpod IDE, issues of code lines longer than 79, where a few before I broke them off in new lines. Some were not changeable because of django own namecalling, those were added with a # noqa tag. In my latest review this was error-free.





<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tu"></p>

# Technologies Used

  - HTML5
  - CSS
  - Django
  - Python
  - Javascript

  #### Django Packages

* [Gunicorn](https://gunicorn.org/)
   
* [Cloudinary](https://cloudinary.com/)
   
* [Dj_database_url](https://pypi.org/project/dj-database-url/)
   
* [Psycopg2](https://pypi.org/project/psycopg2/)
   
* [Summernote](https://summernote.org/)
  
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
  
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)


<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tu"></p>

# Credits

  - Images <br>
  Where googled from different barbershops and added to my page 

  - Walkthrough Code <br>
  Thanks to Code Institute for the walkthrough that set the path to start and finish of this project

  - Tutor Support <br>
  Recieved help from tutor when I was wondering why my CSS was not applied to the project, and got that solved quite easy. 

  - External Code <br>
  Used the following readme template as a good starting point for this project <br>
  https://github.com/gfpkelly1986/Punters-Pal 
  


