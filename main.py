from PIL import Image, ImageEnhance
import os

imagePath = r'D:/pre_process/images'
resizedPath = r'D:/pre_process/resizedImages'
brightness = r'D:/pre_process/brightness'
augmented = r'D:/pre_process/augmented'

imageCount = len(os.listdir(imagePath))
imageList = os.listdir(imagePath)


def ResizeImage():
    # resize 640x640 and save resizedImages folder in the project
    for imageName in imageList:
        imageName = imagePath + '/' + imageName
        # print(imageName)
        image = Image.open(imageName)
        imageWidth, imageHeight = image.size
        print(image.size)
        resizedImage = Image.new(image.mode, (640, 640))
        resizeWidth, resizeHeight = resizedImage.size

        padLeft = (resizeWidth - imageWidth) // 2
        padTop = (resizeHeight - imageHeight) // 2

        imageName = imageName[21:]
        resizedImage.paste(image, (padLeft, padTop))
        resizedImage.save(f"{resizedPath}/{imageName}")
        resizedImage.save(f"{augmented}/{imageName}")
        print(resizedImage.size)

def ChangeBrightness():
    resizedImageList = os.listdir(resizedPath)
    for resizedImage in resizedImageList:
        imgName = resizedImage
        resizedImagePath = resizedPath + '/' + resizedImage
        # print(resizedImagePath)
        resizedImage = Image.open(resizedImagePath)
        # resizedImage.show()
        enhancer = ImageEnhance.Brightness(resizedImage)

        # >1 => brighten, =1 => original image, <1 => darken image
        factor = 1.15
        resizedImage = enhancer.enhance(factor)
        # imOutput.show()

        resizedImage.save(f"{brightness}/{imgName}")

        imgName = imgName[:len(imgName)-4]
        imgName = imgName+"_b.jpg"
        resizedImage.save(f"{augmented}/{imgName}")

def MergeFiles():
    list_dir = [brightness, resizedPath]

    content_list = {}
    for index, val in enumerate(list_dir):
        path = os.path.join(augmented, val)
        content_list[list_dir[index]] = os.listdir(path)


ResizeImage()
ChangeBrightness()
#MergeFiles()

