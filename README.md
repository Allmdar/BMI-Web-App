# BMI-Web-App
Created a website, using HTML + CSS and the Bottle framework, which takes input from the user (height and weight) and calculates their BMI. 

## Output ##


https://user-images.githubusercontent.com/76918821/209247917-f5ac73ae-e26d-4d8f-943c-4b046268f8cc.mov

## Algorithm ##

In my first python file **(bottle_app.py)**, which was used as a dispatcher for the rest of the two programs, I imported **default_app()** *(maintains a stack of Bottle instances and uses the top of the stack as a default
application for some of the module-level functions and decorators)*, **route** *(distinguishes between static and dynamic routes), post (to get data from the bmi_frontpage.html and make use of it)*, and **template.** 

In line 3 and 4 of the python file, **@route(’/’)** tells the program to run *bmi_frontpage.html* as soon as the webpage is run. Furthermore, on line 7, **@post(’result’)** is connected to line 40 of the second program *(bmi_frontpage.html)*, where it technically tells the program to run the result.html page when the user hits the submit button on the bmi_frontpage.html. In the last line (12) of the first program, it tells the program to run the application (default_app)

In the second file (bmi_frontpage.html), we start with arranging the HTML file and then style it in the <head> section as that part of the code is not being displayed on the page. The code that is being displayed on the page is put in the <body> section.
  

Between **line 40-54**, I set up the form. Moreover, I used an **action and method within the form element** to *redirect the user to the result when the form is submitted*. Lastly, when the input is asked from the user (weight/height), I set the following within the element: 
  
*type=”number” → To not allow the user to enter a string or produce an error if the user does* 
*step=”any” → allows the user to enter floating point numbers*
*value=0 → default value*
*name=”weight” or name=”height”→ As a reference or placeholder that is used later on in our python algorithm.*
  
The third file (result.html) connects all the dots together. The code between **<% %>** represents the python code. The python code gets the height and width and converts into a float for the BMI Calculation: 
  *output = (round((weight/height**2) * 703,2)) *
  
I then checked whether the output met a certain scenario for the BMI using an if statement and then closed the python code with **“end.”** Both the calculation of the BMI and the status of the BMI are printed on the web page using **{{}}** after they are converted from an integer to a string.
  



