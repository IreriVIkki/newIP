# import the create app function that will be called when tis file is run. the function creates an instance of the main application which up to this point does not exist.
# it also registers all available blueprints to the app that it just created so that they can be instantiates as well since we know that blueprints are dormant until registered with an application
from app import create_app


# import the manager and server classes fron flask script
from flask_script import Manager, Server
# we create an instance of the main app and call it app by calling the create app function that takes a configuration a=setting as an argument and creates the main application
app = create_app('development')


# import the manager class from flask script that initializes the flask script extension in our application. from flaskmanager, server class is also imported and this helps us to run our server for the application
manager = Manager(app)
manager.add_command('server', Server)

# check if this file is being called and call the run method on our manager
if __name__ == '__main__':
    manager.run()
