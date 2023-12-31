# Our Spot Photo Sharing Platform
![homepage](readme/images/rm-homepage.webp)

## Testing Page

Live Site is [available HERE](https://ourspot-d2a3c52401dc.herokuapp.com/)

[Project Repository](https://github.com/todiane/our-spot)

[GitHub Project Table](https://github.com/users/todiane/projects/8/views/1?layout=board)

Flake8 is installed and being used to ensure [PEP8 python standard](https://peps.python.org/pep-0008/#introduction)

Developer: Diane Corriette - [GitHub](https://github.com/todiane) & [LinkedIn](https://www.linkedin.com/in/todianedev/)


## Browser Testing

<details>
Layout: The layout and appearance of the site has been tested for consistency throughout browsers. Browers tested include the main four:

- Chrome
- Firefox
- Safari
- Microsoft Edge

Website looks and functions as intended on all browsers.

| Test | Screenshot View | 
|:---|:---: |
| 1700 px Desktop |  ![Desktop](readme/tests/rm-desktop.png)  |
| Laptop  |  ![Laptop](readme/tests/rm-laptop.png)  |
| iPad Air - Tablet |  ![iPad](readme/tests/rm-ipad-air.png)  |
| Mobile - Pixel 7  |  ![Mobile](readme/tests/rm-pixel7.png)  |


</details>
<br>

## Functionality Testing

<details>

I tested the complete functionality of the site. This includes:

<img src="readme/tests/rm-manualtests.png">
<img src="readme/tests/rm-manualtests1.png">
<img src="readme/tests/rm-manualtests2.png"><br><br>

***Search functionality***

Search bar in navagation has been tested. Searched using countries e.g. Scotland, local areas e.g. Staffordshire. Searches using words such as "swim" or "walk" also show results. More specific search targetting is needed to improve this facility. If no locations are found when using the search facility nothing is shown. To improve user experience a message stating that nothing has been found needs to be included. This is will added in Stage Two.

<br>

</details>

 ## Python, CSS, JavaScript and HTML Tests

 <details> 

<br>

***python***

 Reformatting was performed on the python files using the code formatter [Black](https://github.com/psf/black)
 and the Code Institute [Python Linter](https://pep8ci.herokuapp.com/) was used to highlight coding errors.

 <img src="readme/tests/rm-ci-linter.png" width="90%">

<br>

***CSS and JavaScript Tests***

 [CSS validation service](https://jigsaw.w3.org/css-validator/) - css code validated

 ![css](readme/tests/rm-css-validation.png)<br><br>

 [Black](https://github.com/psf/black) was used to remodel format in Django

 [JSHint](https://jshint.com/) - no errors shown

 ![js test](readme/tests/rm-jshint.png)<br><br>


 ***HTML Testing***

 There is a line of code that has been left over the 79 characters usually expected because errors happened when it was changed.
 
 List.html page - line 16 - linter highlights 6 problems. When attempts were made to make changes to this line, including making it shorter, the images disappeared so it was left in place. CSS was included to avoid conflict with images on the location page using the same Bootstrap class.

 All html pages were tested using the [W3C Markup Validation](https://validator.w3.org/ ) Service.

 To ensure all code was validated accurately, the 'view page source' command in Google Chrome was used as follows:

- On each page of the deployed application right-click anywhere on the page and select View Page Source.
- Copy the entire code 
- Go to the validator.w3.org service and select the "validate by direct input" tab
- Paste the code into the box provided and click the CHECK button

<br>

 <img src="readme/tests/rm-validator-noerrors.png" width="90%"><br>
 
 <br>

I also tested each individual link (examples below)



Testing dashboard area with link (also added code into direct input)<br>

 <img src="readme/tests/rm-test-dashboard.png" width="90%"><br>

 Testing locations area with link (also added code into direct input)<br>

 <img src="readme/tests/fm-test-locations.png" width="90%"><br>

 Testing display location area with link (also added code into direct input)<br>

 <img src="readme/tests/rm-test-displaylocation.png" width="90%"><br>

 Testing add new location area with link (also added code into direct input)<br>

 <img src="readme/tests/fm-test-addlocation.png" width="90%"><br>

 Testing members area with link (also added code into direct input)<br>

 <img src="readme/tests/rm-test-editlocation.png" width="90%"><br>

 </details>

<br>

## Bugs

<details>

***Known Bugs***

- Users sometimes taken to the top of the page when they like, edit or delete a comment rather than staying in the location of the like/comment area.

- The 'report photo' and 'report profile' modal has stopped working but is not an essential component of project 4 or Stage One so will be fixed during Stage Two.

- When a user edits their location the date and time are also edited to the current date and time, rather than staying at the original date and time.

- In the profile area an email is required to save any profile updates. Members can register without email but cannot update their profile without one so initially made up emails have been used.

- After final deployment of the site to Heroku I asked for peer feedback and was told that a 500 error came up when the "add new spot" feature was used. As I was on my mobile at the time I logged in and tried to add a new spot and received a 500 error. I logged on to my pc and noticed my post was in the admin area even after the error, plus the post appeared in the "new locations" section. I added two more test location photos on my PC and they both worked ok. I then went back to my mobile, registered as a new member (Sally Smith) and added a new spot, that worked okay as well. I removed all the test posts but left the member profile. The site has been okay since but I wanted to document this in case it happens again.

</details>

## Performance and accessibility

 <details> 

<br>

The Lighthouse Chrome DevTools Performance test showed a 92% performance and 100% accessibility score. 

<img src="readme/tests/rm-lighthouse.png" width="70%"><br><br>


 ***Favicon***

A favicon has been added and shows up in the browser

![favicon](readme/tests/rm-favicon.png)<br><br>

 ***Robots.txt***

 A robots.txt file has been added to allow search engines to crawl the network.
 
 </details>

## Restrospective

Overall, I am happy with the number of tests I performed to ensure the first stage of this project - which as stated is a minimum viable product - is user-centered and working well. Being a user has helped me see what is needed from a members perspective and having a few actual members looking at the platform and gaining their feedback when it comes to testing has also been invaluable.

I need to improve my knowledge of testing aspect of projects outside of manual testing and in my next project I hope to include more test driven data from the start. I also need to improve my knowledge of creating tests using the Django test.py files along with my debugging skills.
