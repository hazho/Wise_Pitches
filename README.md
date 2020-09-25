***

# Pitch Website

#### **Monday September 24 2020** ;

---

## Author
> By ** [Akumu Collins](https://github.com/Akumucollins)
 ** ;

***

## Description
>This application allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application


---

## Live Link
[View Site](https://akumucollins-pitches.herokuapp.com)

***

## Setup/Installation Requirements
To get the code..
Cloning the repository:
  ```bash
 https://github.com/Akumucollins/Wise_Pitches.git
  ```
Move to the folder and install requirements
  ```bash
  cd Wise_Pitches
  pip install -r requirements.txt
  ```
Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
Running the application
  ```bash
  python3.8 manage.py server
  ```
Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser 
```bash
127.0.0.1:5000
```
---

## Dependencies
>* python3.8
>* pip
>* virtualenv

***

# Technologies Used
>* Flask
>* Python.

***

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select login|
| Select login |  **Email**,**Password** |Redirect to Home page|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with all pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Select comment button | **Add Comment** | Form that you input your comment|
| Select comment button | **View Comment** | Redirect to all comments|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|

---

## Support and Contact Information
> The application is an open-source product if you  want to improve it or include an event of a bug  contact this
> akumucollins001@gmail.com .

***

## License
The project is [MIT](LICENSE) licensed 