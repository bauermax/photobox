#IMPORTS
############################################################
import requests
############################################################


class Upload:

    def __init__(self,token):
        self.token = token

    def tryConnexion(self,url):
        r = requests.get(url, timeout = 15)
        return r.status_code == 200

    def process(self,filepath,url):

        #UPLOAD TO THE SERVER WITH POST METHOD
        photo = open(filepath, "rb")

        #POST DATAS
        file = {'file': photo }
        values = {'token': self.token}

        #SENDING REQUEST
        r = requests.post(url, files=file,data=values, timeout = 150)

        #CLOSING PHOTO
        photo.close()

        #IF THE UPLOAD IS A SUCCESS, RETURN TRUE
        return r.status_code == 200
