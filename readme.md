Distributed Application Development with EC2 Using AWS CodeDeploy
================================================================================

This is a sample web application to accompany my final project for the fall
2014 CSCIE90 class at Harvard Extension School. Resources for the project can
be found at:
  - [Overview](https://docs.google.com/document/d/1fBK0XlMOSPUKj0A_A7F0ltMhFOQsPuRrnjvTVwcsupE/edit?usp=sharing)
  - [Full Report](https://docs.google.com/document/d/1_TWbq4qTdE9hXFvkbkx3vzDC_Y6KTT-3NnX9tM_JckE/edit?usp=sharing)
  - [Overview Video]()
  - [Full Video]()
  - [Presentation]()

Setting Up Development Environment
--------------------------------------------------------------------------------

The simplest way to play with this code is using
[Vagrant](https://www.vagrantup.com/). Use the following commands to execute
the demo locally.

```
vagrant up
vagrant ssh
cd /vagrant
./setup-dev.sh
```

Setting Up Production Environment
--------------------------------------------------------------------------------

This code is designed to be used with AWS CodeDeploy, however you can also
simply copy this code to an Amazon Linux EC2 instance and execute the
following:

```
./setup-prod.sh
```

Running the Web Server
--------------------------------------------------------------------------------

To start the webserver, execute:

```
python app.py
```

After that you should be able to access:
  - http://localhost:8080/ - Will show a simple Python overview page.
  - http://localhost:8080/version - Will read and show the `version.txt` file.

You should be able to edit the `version.txt` and do muptiple deployments of
this code using AWS CodeDeploy. This is discussed in more detail in the full
report (link above).
