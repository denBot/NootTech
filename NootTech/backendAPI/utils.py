from hurry.filesize import size
import base64
import uuid


def get_upload_key():
    """
    Generates a randomised upload key for a user.
    This key is used for authenticating remote uploads (cURL, ShareX) instead of exposing user password.
    :return: String - randomly generate string of 24 characters
    """
    key = base64.b64encode(uuid.uuid4().bytes).decode("utf-8")
    return key[:24] if len(key) > 24 else key


def get_file_path(instance, filename):
    """
    :param instance: - Used for getting the current instance (file upload) uploader id for filepath creation
    :param filename: - The name of the file to be added to path
    :return: - String: the complete relative file-path (from Media dir) for an uploaded file
    """
    return f'{instance.uploader.id}/{filename}'


def get_thumb_path(instance, filename):
    """
    :param instance: - Used for getting the current instance (file upload) uploader id for filepath thumbnail creation
    :param filename: - The name of the file to be added to thumbnail path (thumbnail generated by easy_thimbnails)
    :return: - String: the complete relative thumbnail file-path (from Media dir) for an uploaded file
    """
    return f'Thumbnails/{instance.uploader.id}/Thumb_{filename}'


def get_filesize_str(filesize):
    """
    :param instance: - not used
    :param filesize: - size of a file in bytes
    :return: - String: filesize converted to KB, MB, GB...
    """
    return size(filesize)