import abc
import base64
import os

from library_api.types import PhotoDestinations

class FileContent(object):
    def __init__(self, name, content, destination) -> None:
        self.name = name
        self.content = content
        self.destination = destination

class UploadFileFactory(object):
    def __init(self):
        pass

    def upload(self, files):

        for file in files:
            uploader = None
            if file.destination == PhotoDestinations.LOCAL_DRIVE.value:
                uploader = UploadToLocalDrive()
            elif file.destination == PhotoDestinations.FTP.value:
                uploader = UploadToFTP()
            elif file.destination == PhotoDestinations.S3.value:
                uploader = UploadToS3()
            
            uploader.upload(file)

class UploadFile(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def upload(self, file: FileContent):
        pass


class UploadToLocalDrive(UploadFile):
    def __init__(self):
        pass

    def upload(self, file: FileContent):
        content = base64.b64decode(file.content)
        with open(os.path.join("public", file.name), "w") as file:
            file.write(content.decode("utf-8"))
        

class UploadToFTP(UploadFile):
    def __init__(self):
        pass

    def upload(self, file: FileContent):

       pass

class UploadToS3(UploadFile):
    def __init__(self):
        pass

    def upload(self, file: FileContent):

       pass