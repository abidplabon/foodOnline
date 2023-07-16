# To import and successfully run CSS and Styling in "Production"
Run Command
$python manage.py collectstatic

#To hide information like DB name password
Create .env file
from decouple import config and then hide in setting.py using DB_NAME = config(.env file variable name of DB)

#Flexible model create
Import AbstractUser, BaseUser
BaseUser = creates user then make it a super user
AbstractUser = All user fields and variables

#Tell Django that I'm overriding your model default
AUTH_USER_MODEL = 'accounts.User'---> "AppName.AuthModelName"

MAKE MODEL + REGISTER IN ADMIN.PY + MIGRATIONS

**** Ready(self) for "Signals" in Apps.py file
