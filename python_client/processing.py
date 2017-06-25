############################################################
from PIL import Image
import os
import yaml
import hashlib
#IMPORTS FOR UPLOAD
from upload import *
############################################################

#OPEN CONF YAML
fileconf = open('config.yaml', 'r')
conf = yaml.load(fileconf)

#GENERATE TOKEN
raw_token = conf["config"]["token_passphrase"]
token = hashlib.md5(raw_token.encode('utf-8')).hexdigest()

#GENERATE URL
base_url = conf["path"]["server_url"]
url = base_url

#SETUP PROCESSED IMAGES FOLDER
processed_images_folder = conf["path"]["processed_images_folder"]

#SETUP LOGO PATH
limage = Image.open(conf["path"]["logo_path"])

#GET LIST OF NON UPLOADED IMAGES
to_upload = os.listdir(processed_images_folder)


############################################################
#DEBUG FUNCTION
def debug(txt):
    if conf["config"]["enable_debug"]:
        print(txt)


#FUNCTION TO ADD A LOGO TO AN IMAGE
def addLogo(imgname):

    mimage = Image.open(imgname)

    finalName = processed_images_folder + imgname.split('/')[1]
    debug(finalName)

    #RESIZE LOGO
    wsize = int(min(mimage.size[0], mimage.size[1]) * 0.25)
    wpercent = (wsize / float(limage.size[0]))
    hsize = int((float(limage.size[1]) * float(wpercent)))

    simage = limage.resize((wsize, hsize))
    mbox = mimage.getbbox()
    sbox = simage.getbbox()

    #RIGHT BOTTOM CORNER
    box = (20, mbox[3] - sbox[3] - 20)
    mimage.paste(simage, box,mask=simage)
    mimage.save(finalName)
    os.remove(imgname)

    return finalName


#RESUME UPLOADS
def resume_uploads():
    #CREATE INSTANCE OF UPLOAD
    upload = Upload(token)
    #IF SERVER IS REACHABLE
    if upload.tryConnexion:
        for img in to_upload:
            fname = processed_images_folder+img
            if upload.process(fname,url):
                os.remove(fname)
                debug('UPLOAD SUCCESS')
            else:
                debug('UPLOAD FAILURE')


#ASYNC FUNCTION CALLED FROM MAIN PROGRAM AS THREAD
def asyncTask(toUpload):

    #ADD LOGO IF 'step_add_logo' IS TRUE
    if conf['config']['step_add_logo']:
        fname = addLogo(toUpload)
    else:
        fname = toUpload

    #CREATE INSTANCE OF UPLOAD
    upload = Upload(token)
    #IF SERVER IS REACHABLE
    if upload.tryConnexion:
        #UPLOAD THE FILE
        if upload.process(fname,url):
            os.remove(fname)
            debug('UPLOAD SUCCESS')
        else:
            debug('UPLOAD FAILURE')

    else:
        debug('UNABLE TO CONNECT TO SERVER')

    exit()
