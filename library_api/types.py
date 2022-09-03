import enum

class PhotoFormats(enum.Enum):
    PDF = "pdf"
    JSON = "json"
    XML = "xml"

class PhotoDestinations(enum.Enum):
    LOCAL_DRIVE = "local_drive"
    FTP = "ftp"
    S3 = "s3"