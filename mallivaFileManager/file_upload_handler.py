from django.conf import settings
from django.core.files.storage import default_storage
from threadlocals.threadlocals import get_request_variable
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill


class FileUploadHandler:
    """ 
    - Manage all file uploads on Malliva platform
    - Upload to the right directory
    - Validate uploaded file - this will deny the user if a wrong file type was uploaded.
    - Manage duplicate files.
    """

    def __init__(model, file_type):
        # marketplace account the request is comming from.
        self.marketplace_domain = get_request_variable("malliva_domain")
        self.model = model  # the name of the model class
        self.file_type = file_type  # file or just image

    def validate_uploaded_file():
        """
        Check file type of uploaded files 
        """

    def user_directory_path(self, model_id, filename):
        """ 
        file will be uploaded to MEDIA_ROOT/domain/<modeltype>/<model id>/<filename>
        Remember to store images and thumbnails of the image 
        """
        return "{0}/{1}/{2}/{3}".format(
            self.marketplace_domain,
            self.model,
            model_id,
            filename,
        )

    def upload_file(self):
        """ 
        """
        # if image call generate thumbnail else, upload directly.

    def generate_thumbnails(self, ImageSpec):
        """  
        """
        processors = [ResizeToFill(100, 50)]
        format = 'JPEG'
        options = {'quality': 60}

        source_file = open('/path/to/myimage.jpg')
        image_generator = Thumbnail(source=source_file)
        result = image_generator.generate()

        dest = open('/path/to/dest.jpg', 'wb')
        dest.write(result.read())
        dest.close()
        return True  # change to url of thumbnail

    def verify_existing_duplicate(self):
        """ 
        Check of duplicate files or image exists
        """

        if True:
            return False
        return True
