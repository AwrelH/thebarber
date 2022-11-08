# BarberShop - the local barber for all.
    IMAGE
  <p align="center">
  <img src=""?raw=true alt=""></p>

# <p href="#intro" id="intro"> - Intended Purpose of This Website:</p>

  - Fill in: To greet customers.

  - Fill in: To be a window of exposure.

  - Fill in: To interact with the customer.

  - Fill in: So customers can make appointments.


## Table of contents
- <a href="#ui">UI/UX</a>
- <a href="#thm">Themes</a>
- <a href="#epi">Epics</a>
- <a href="#us">User Stories</a>
- <a href="#de">Design</a>
- <a href="#wire">Wireframes</a>
- <a href="#erd">ERD Diagram</a>
- <a href="#lf">Live Features</a>
- <a href="#df">Desired Features</a>
- <a href="#tpy">Testing(Python)</a>
- <a href="#tjs">Testing(Javascript)</a>
- <a href="#dep">Deployment</a>
- <a href="#b">Bugs During Development</a>
- <a href="#ub">Unsolved Bugs</a>
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





# Design

## Color Pallete
- HEX: 000000, 445261, 4B6B8C, 0D6EFD, F9EBDC
 

## Fonts
- 'Belleza','Akaya Telivigala', Lato, sans-serif;


  

<p align="center">
  <img src=""?raw=true alt=""></p>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="wire"></p>

# Wireframes

  - Title of the wireframe

<p align="center">
  <img src="(https://raw.githubusercontent.com/AwrelH/thebarber/main/static/barberlogo.png?raw=true)" alt="">INDEX</p>

<p align="center">
  <img src="static/images/readme-images/Login-Page-PP.png"?raw=true alt=""></p>

<p align="center">
  <img src="static/images/readme-images/Sign-up-Page-PP.png"?raw=true alt=""></p>

<p align="center">
  <img src="static/images/readme-images/Note-Entry-PP.png"?raw=true alt=""></p>

<p align="center">
  <img src="static/images/readme-images/Note-Display-PP.png"?raw=true alt=""></p>

<p align="center">
  <img src="static/images/readme-images/Blog-Chat-PP.png"?raw=true alt=""></p>

<p align="center">
  <img src="static/images/readme-images/Blog-Detail-PP.png"?raw=true alt=""></p>



<p align="right"><a href="#intro">Return to table of contents</a></p><p id="erd"></p>

# ERD Diagram

  - Title of ERD Diagram

<p align="center">
  <img src="static/images/readme-images/ERD diagram Project4.png"?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="lf"></p>

# Live Features

  - Live Features

<p align="center">
  <img src=""?raw=true alt=""></p>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="df"></p>

# Desired Features

  - Desired Features

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tpy"></p>

# Testing (Python)

  - Unit-Testing-Python

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tjs"></p>

# Testing (JavaScript)

  - Unit-Testing-JavaScript

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="dep"></p>

# Deployment

  - Early Deployment

  - Final Deployment

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="b"></p>

# Bugs (During Development)

  - Bug One

  - Bug Two

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="ub"></p>

# Bugs (Unsolved)

  - Bug One

  - Bug Two

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tu"></p>

# Technologies Used

  - Tech One

  - Tech Two

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tu"></p>

# Credits

  - Images

  - Media

  - Walkthrough Code

  - Tutor Support

    - Help from Sean in Tutor support with the following code on the 16-10-2022:
            <p>
              instance = new_entry.save(commit=False)<br>
              instance.created_by = User.objects.get(username=request.user.username)<br>
              instance.save()
            </p>

    - The code above helped to solve a technical issue whereby I was rendering a form for the user to enter data and I did not want the created_by field to be seen by the user but it was a ForeignKey field and threw a violates not null exception when left blank. This code helped me to create an instance of the new_entry and set its ForeignKey to the users username before committing it to the database thus resolving the error.

  - External Code

<p align="center">
  <img src=""?raw=true alt=""></p>


