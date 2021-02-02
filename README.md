# Portfolio-Website-using-Flask-and-Python
1. Create a virtual-environment so that it'll be easier for you when you finally build thew website and you awant to deploy it.
2. Install all the necessary libraries for your website. In my case, the libraries I used are: * Flask, * Gunicorn, * csv(just for my convenience), * datetime(just for my convenience)
3. Set-up the virtual environment and change it to development mode using "set FLAS_ENV=development" because the changes need to reflect as you are working. It'll make our life easier.;)
4. In my case, I downloaded the template for my website from https://html5up.net/ which offers free open source templates for your website. Try it!
5. Create a templates folder in your project directory (**outside the virtualenv folder**) and place all the html files from your templates in this. This is because Flask looks for templates folder by default and if doesn't find it, you'll be thriwn with an error.
6. Also, you need a static folder(this is default too, just like templates) where all your css, js, images, and all other files need to be placed. If your template doesn't have it, create a static folder and places all the other files in static.
7. That's it! You are all set to write the code for flask application and make changes to the html, css files. In my case, the flask app is "app.py". Read the flask documentation before you start running it. 
8. Also, the images you see in static/images are mine, please replace them with yours, and deploy the application.
9. Finally, after developing the flask app and testing your website on local IP, use "pip  freeze > requirements.txt" on your venv to see all the libraries installed and use the .txt file on any hosting platform to install from the file instead of manually installing each library.
10. I used GCP to host my website. There are other sources like AWS, Heroku, pythonanywhere, to host your Flask web-app.
11. Check out my website at http://rahulsonti.tech/ (or) https://cobalt-compound-235621.uc.r.appspot.com/ . PEACE OUT!!!
