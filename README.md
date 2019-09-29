# Creating-templates-in-python-with-jinja-module  

This repository is about creating templates in <strong>python with jinja module, knowing about Bootstrap Modal, a simpleproject demonstarting the use case of creating the objects in Django and rendering them on the web</strong>. I will make a lot more in this reposiotry so that better knowledge can be imparted.  

## Key points with respect to the project simpleproject   

In this Project, I have used mysql as a database instead of sqlite3 which is default used by django. Please follow the instruction given in this tutorial to customize mysql instead of sqlite3 in settings.py (Django). https://justinmi.me/blog/2017/04/28/migrating-sql-databases. I would say this is best tutorial I have searched and hence is adding its link here.IT feel better if you praise something which you found good. Some points to remember while <strong>migrating SQLite Databases to MySQL (Django)</strong> are as below.  
<ol>
  <li> Driver is needed to integrate mysql database with the python code. You must use <strong>MySQL-python</strong> if you are using python2 and 
    <strong>mysqlclient</strong> if you are using python3.</li>
  <li> For installing mysqlclient using pip it is important to install these two additional packages.    
   
    sudo apt-get install libmysqlclient-dev    
    sudo apt-get install python-dev 
    
 </li>
</ol>

## How to run the Project simpleproject
If you go inside the directory simpleproject, you will find the file manage.py. You need to create the superuser to see the all the models and their data in the admin panel so please execute the below command to create the superuser.  
```
python manage.py createsuperuser 
```
Now one need to run the command make migration to get ready the table and then fill the values in the table using the command makemigrations  

```
python manage.py makemigrations  
python manage.py migrate 
```

To finally run the project, please execute the below command  
```
python manage.py runserver 
```  

# keypoints with respect to relationaldatadjango   

![FEATURE_IMAGE](https://user-images.githubusercontent.com/3431730/65816813-0f979780-e21e-11e9-98bc-3558c0b6e732.png)  
<strong>Keypoints</strong>  
<ol>
  <li> I have created two tables and they are related to each other using foreign key</li>
  <li> in views.py search queries are applied to retrieve data from database and show it on the front end.</li>
  </ol>  
  
ALSO remember, I have used mysql at the backend. Please follow this link https://justinmi.me/blog/2017/04/28/migrating-sql-databases for migrating to mysql database with Django.   

# Keypoints with respect to decorators_python  
![Feature_image](https://user-images.githubusercontent.com/3431730/65826825-0c95b900-e2a9-11e9-87f1-59b710a896e6.png)

1.) Decorators are used to call other function inside the decorator function.  
2.) This makes codes small and handy.
  

## References
[Installing mysql client](https://stackoverflow.com/questions/7475223/mysql-config-not-found-when-installing-mysqldb-python-interface)  
[Django 2.0 url() to path() Cheatsheet](https://consideratecode.com/2018/05/02/django-2-0-url-to-path-cheatsheet/)  
[saganshul django tutorial](https://github.com/saganshul/django_tutorials)
      
