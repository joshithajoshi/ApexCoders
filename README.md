# ApexCoders

## Project : Portal For The Course

### Collaborators : 210050033 , 210050134 , 210050162

We have developed a website using Django, Python and HTML which functions as a Learning Management System.
Key features of it include:
1. User Login, Logout and Signup, Update profile
2. Course Management
3. Creating and deleting assignments
4. Making Submissions and Grading Submissions and submission validation
5. Seperate User-Interface for teachers and students

Explanation of the feature is as follows:

#### User Login, Logout, Updating Profile and registration:
When we start the server using the local host, the first page one encounters is the login page. Here one can login in using the credentials or signup.
One will never be able to bypass loginpage by directly entering the url. If tried so, they will be redirected to a page saying "oops!wrong location"

![loginpage](https://user-images.githubusercontent.com/111419098/204011351-0caa759a-e330-44bb-a12c-07cdaba0d4c0.jpg)

![registrationpage](https://user-images.githubusercontent.com/111419098/204011407-33a835dc-3407-4487-bd24-bd0fa64567f8.jpg)

![profileupdate](https://user-images.githubusercontent.com/111419098/204012726-c037577c-df3d-491e-86ff-6a980182f9ae.jpg)


The role of the user is differentiated while doing signup where the user would be able to choose whether he/she is enrolling as a teacher or a student. While login, the user enters only the username and password. The backend part searches for the user, checks if the user is a teacher or not and redirects the user to their respected homepage.\
The user will be able to update their profile i.e, they will be able to change the password once they finished login to the homepage.

While updating the profile, It is strongly advised **not to change** the role of the user

One can logout of the website by clicking the logout button in the homepages once they login and then it will be redirected again to the loginpage



#### HomePages:

Once the user is able to login, the teachers and students are redirected to their repected hompages

##### Teacher HomePage

Teacher Homepage includes the fields:
1. Update profile
2. Logout
3. Create Course
4. Existing Courses

A teacher can create a course, delete a course and view the existing courses by clicking on them.
While creating a course, the teacher should add atleast one student to the course and keeping that in mind, entering the remaining fields will successfully create a course and the teacher would be redirected to the teacherhomepage.
On clicking the Existing coursepage, the teacher will be redirected to the Coursepage for the teacher.
![teacherhome](https://user-images.githubusercontent.com/111419098/204011456-4345966c-34ed-4807-bc36-a8ceef3c47c9.jpg)

![createcourse](https://user-images.githubusercontent.com/111419098/204011963-a7b95249-8c8a-4ac1-a7ca-581f5464ee6a.jpg)

##### Student HomePage

Student Homepage includes features like:
1. Update profile
2. Logout
3. Register for a course
4. View a coursepage

A student will not be able to create a course and will only be able to register for a course. 
A student on clicking the link for registering for a course will then be redirected to a page where he/she is required to enter the course code to join the course. Once the course code is entered, then the student will be enrolled in that course and will then be redirected to the student homepage.
On clicking the Courses in which he is already enrolled, he will be redirected to the coursepage for student.
![studenthome](https://user-images.githubusercontent.com/111419098/204011479-7290e840-cf5d-4523-8a00-7a3956dc55e8.jpg)
![courseregistration](https://user-images.githubusercontent.com/111419098/204011788-9aec3516-0ad0-43d0-ac93-039206a531eb.jpg)


#### Coursepages:

Student Coursepage displays all the assignments present which are related to this particular course
On clicking on any assignment, redirects to the assignmentpage for students
![studentcoursepage](https://user-images.githubusercontent.com/111419098/204011610-cd2c4b98-a60c-4172-9667-ac4a6c4c3586.jpg)

Teacher Coursepage displays all the assignments created by the teachers and a link to create an assignment.
Onclicking the assignments displayed on the coursepage, then redirects to the assignment page for the teachers
Onclicking the create assignment link he will then be redirected to the assignment creating page where the teacher is required to give a name to the assignment and file he is uploading and then upload a file which is relevant to the assignment like a file which have the question statement in it. Then On clicking submit, a new assignment will be created and then redirected to the coursepage back.
Teacher Coursepage also allows only teachers to delete an assigment by clicking on the "delete assignment" link which resides just beside the link to the assignment page
![teachercourse](https://user-images.githubusercontent.com/111419098/204011624-04237b84-c832-4bd6-8a38-2c78ee09060f.jpg)

#### Assignment pages:

Student assignmentpage will provide the link to download the problem statement or whichever file the teacher uploaded regarding the assignment and provide a link to make a submission for the assignment where he is required to upload a file and give the uploaded file a name.
The grades and the feedback will be displayed on the page below the submission link. The default values of the grade and feedback will be displayed if the assignment is not yet graded.
Student can only submit ".zip, .tgz, .tar.gz" types of files

![studentassignment](https://user-images.githubusercontent.com/111419098/204012244-3ba1211a-97d2-45d5-8642-1a457a52afa4.jpg)
![createsubmission](https://user-images.githubusercontent.com/111419098/204012326-ea5c4712-5429-4a6d-bbb7-9ac20cbce411.jpg)
![validation](https://user-images.githubusercontent.com/111419098/204023660-37801ea6-bf67-4130-af03-0d43b168b6f9.jpg)

Teacher assignmentpage will also have a link to download the problem statement.
Below the link is where the links to all the submissions made for this assignment shows up.On clicking the submission links, then redirects to the submission page where the teacher can grade the submission.
![teacherassign](https://user-images.githubusercontent.com/111419098/204012276-26bbfd18-7e70-46cd-b7cb-0aaf526b0c9f.jpg)

#### Submission Page:

Only teacher will have this kind of page.
Once the teacher is redirected to this page, he will be able to download the submission made by the student and he need to evaluate it by himself.
The "grade" link in the bottom allows the teacher to grade and provide the feedback for that particular submission.

![teachersubmission](https://user-images.githubusercontent.com/111419098/204012385-814fffe1-7b1f-47f5-b785-6baf8120df6c.jpg)
![grade](https://user-images.githubusercontent.com/111419098/204012401-b2861544-dfb4-4936-a5d5-34b6013bb9fb.jpg)


### Running the code:
Our Django project name is trail2 and the app name is trailer

1. So we need to traverse along the directory till the current directory and directory of manage.py are same.
2. Then we need to run: "python3 manage.py runserver"
3. Then copy the localhost address displayed in the terminal and paste it in the browser and then click search
4. Done! Explore the website

### Contributions:
#### 210050033:
1. Login and Registration
2. Stylising 

#### 210050134:
1. Courses and Assignments
2. Sphinx Documentation

#### 210060162:
1. Models, Forms
2. Student submission, grading
3. Readme.md









