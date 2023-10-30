from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 50*1024*1024:
        raise ValidationError("50MB 이상의 파일을 업로드 할 수 없습니다.")
    else:
        return value


def validate_image_size(value):
    filesize = value.size

    if filesize > 20*1024*1024:
        raise ValidationError("20MB 이상의 이미지를 업로드 할 수 없습니다.")
    else:
        return value
