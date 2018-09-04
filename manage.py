# import the create app function that will be called when tis file is run. the function creates an instance of the main application which up to this point does not exist.
# it also registers all available blueprints to the app that it just created so that they can be instantiates as well since we know that blueprints are dormant until registered with an application
from app import create_app

# we create an instance of the main app and call it app by calling the create app function that takes a configuration a=setting as an argument and creates the main application

app = create_app('development')
