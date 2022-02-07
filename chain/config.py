
ENV_LIVE = True
if ENV_LIVE == False:
    SERVICE_URL = 'http://localhost:3000/'
    API_KEY = 'API_KEY'

if ENV_LIVE == True:
    SERVICE_URL = ''
    API_KEY = ''

