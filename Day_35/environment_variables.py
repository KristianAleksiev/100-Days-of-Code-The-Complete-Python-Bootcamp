### Storing information in environment variables so that they are not stored at the same place as the code base
##auth_token, api_key....
#export OWM_API_KEY=key


#Calling the exported variable
import os
#export OMW_API_KEY=4k6kx6dk61f
api_key = os.environ.get("OMW_API_KEY")

#export AUTH_TOKEN=053315fvcb451 # in terminal
auth_token = os.environ.get("AUTH_TOKEN")
