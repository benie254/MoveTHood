# MoveTHood
Your neighborhood companion app for news, updates, contact information, and searches, among more

# MoveTHood
#### This repo creates a neighborhood app for people to interact, share ideas, and keep up to date with their neighborhoods. 

Generated with [Python](https://www.python.org/) version 3.8.13 for [Django](https://www.djangoproject.com/) version 4.0.5 
## Author
[Benson Langat](https://github.com/benie254)

## Description

MoveTHood enables users to add their locations and/or neighborhoods to a profile, besides read articles shared in the community. 
Users can also share their posts or add businesses to the platform. 
The app also consumes a quotes api and serves its custom api. 
The custom api queries the app's database for neighborhood businesses and contact details of nearby police & health departments. 

>The app supports `CRUD` functionalities to Create, Read, Update, and Delete images and their content/details. 


## Screenshot--Landing Page

<img src="https://user-images.githubusercontent.com/99865051/173784989-bc5eea15-5e20-43f6-a27e-c0e43170e21f.png" >

## Screenshot--Project Page

<img src="https://user-images.githubusercontent.com/99865051/173785021-a7e49942-2251-4110-af87-82b9c9daf3c4.png">

## Screenshot--Project Form

<img src="https://user-images.githubusercontent.com/99865051/173787738-9a2bf85d-7794-4e7c-8258-47eafc7e6e2b.png">

## Screenshot--Profile Page 

<img src="https://user-images.githubusercontent.com/99865051/173787857-45865fd3-1a91-4a7a-a5a4-2358724f24cd.png">


## Behavior Driven Development--BDD

**1. Home Page**
   - OUTPUT: 'Navbar', 'Home page content'
   
**2. User Action:** 
   - INPUT:  Click : Navbar : 'MoveTHood', 'Home'
   - OUTPUT: Home page
   - OUTPUT: All neighborhood posts

**3. User Action:**
   - INPUT:  Input : Navbar : Search form: 'Enter your hood name',
   - OUTPUT: business results--business results page

**4. User Action:**
   - INPUT:  Click : Navbar : 'Profile'
   - OUTPUT: User profile page: Profile photo, user details, bio, user posts, random quotes 

**5. User Action:** 
   - INPUT:  Click : Navbar : 'Create post',
   - OUTPUT: Post upload page 
   - OUTPUT: Post form

**6. User Action:** 
   - INPUT:  Click : Navbar : 'Add business',
   - OUTPUT: business upload page 
   - OUTPUT: Business form

**7. User Action:**
   - INPUT:  Click : Navbar : Logout
   - OUTPUT: Redirect: Login page. 


## Setup/Installation Requirements

* To use this open-source repo, clone it; to contribute, fork it. 
* Open your Terminal (CTRL + ALT + T on Ubuntu/Linux). 
* Make a destination directory in your preferred path (where you would like to clone the repo into.)
* Run the command ``` cd yourDestinationDirectory ```
* Run the command ``` git clone https://github.com/benie254/MoveTHood.git ``` to clone the repo into your destination directory. 
* Run the command ``` cd MoveTHood ``` to move you into this repo's directory.
* Run the command ``` atom . ``` for Atom or ``` code . ``` for VSCode --opens the directory in your preferred code editor. (it is okay if you use something different.)
* Happy coding!

## Known Bugs

No known bugs. Please report any issues or encountered bugs! 

## Technologies Used

* [Python](https://www.python.org/) 
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)

## Other Resources 

* [Bootstrap](https://getbootstrap.com/) 
* [Adobe Color Wheel](https://color.adobe.com/) 
* [Coolors](https://coolors.co/) 
* [Google Fonts](https://fonts.google.com)


## Support and contact details

Reach out with any issues, concerns, or contributions to [Benie-throughMail](davinci.monalissa@gmail.com)

### License

*Copyright (c) 2022* ***Benson Langat***

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*

###
Copyright (c) 2022 **Benson Langat**

[Python](https://www.python.org/) version 3.8.13
