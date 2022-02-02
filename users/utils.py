from PIL import Image

def checkImgAndSave(ImageToSave = None, typeImg = None, idUser = None, output_size = None):

	if (ImageToSave == None or typeImg == None or idUser == None or output_size == None):
		return False

	typeImg = str(typeImg).replace("_img", "")
	img = Image.open(ImageToSave)
	img = img.resize(output_size)
	img.save('media/profile_pics/'+str(idUser)+'/'+typeImg+'.png')
	return True
	