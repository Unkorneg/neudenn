`export FLASK_APP=app`
`export FLASK_ENV=development`
`flask run`

Create migration repository
`flask db init`

routes :

login page
create profile page
profile page
modify profile page

home page with search

search results page

pattern page

pattern creation page

about page


@Alamin: You will need to create a web form with a file field where the user can select a picture to upload. The server will then save the file to disk. You can finally add a route that returns the image, so that you can include it in a  element in your page. If you implement something like this, it is important to validate the uploads, you want to make sure they have the expected size (not a huge file that may fill your disk), and also that they are valid jpeg/png/etc files, not something else.
