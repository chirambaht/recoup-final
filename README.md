# Recoup
Created by: Humphrey Chiramba
## Description
Recoup is an application built for athletes, medical practices and trainers. It allows all of them to come together and link up. Athletes can access a knowledge base with many detailed videos that are approved by health professionals to help them with training or recovery. The end goal is to reduce the number of people going in to hospitals for minor injuries that could be can easily be identified and remedied. More is found in the application's about page. **An online version of this webpage is available at: [www.humphreytest.cf](http://www.humphreytest.cf)** or at **[recoupuct.herokuapp.com/](https://recoupuct.herokuapp.com/)**
## Usage
By simply running `make run`, the Django server will run and then navigate in your browser to [localhost:8000](http://localhost:8000/). For the rest of the details on the application and its capabilities, please go to the about of the application.
It is advised to use the online version of the service because of the need for **secret** and  **api** keys. These link up to an Amazon S3 Bucket.
Feel free to create an account and explore the platform for yourself. It will be well worth it.

## Dependancies
Django 3.0.8
Python 3.6+
Pip3 9.0.1
Bootstrap (needs an internet connection)
Pillow: `pip3 install Pillow`
Crispy Forms:`pip3 install django-crispy-forms`
Django Storages: `pip3 install django-storages`
jsonfield: `pip install jsonfield`
## Technologies in the project
This project incorporates modern technologies such as Amazon S3 Buckets and the Django framework.
## References
Much of the work behind this was inspired by [Corey Schafer](https://coreyms.com/) and his introduction to Django course found [here](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
