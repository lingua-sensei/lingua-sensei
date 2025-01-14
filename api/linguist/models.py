from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.fields.files import FieldFile

MAX_AUDIO_FILE_SIZE: int = 4 * 1024 * 1024


def audio_file_size(f: FieldFile):
    if f.size > MAX_AUDIO_FILE_SIZE:
        raise ValidationError("File too large, must not exceed 4 MB")


class Audio(models.Model):
    LANGUAGES = [  # language must be compliant with https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
        ("en", "English"),
        ("es", "Spanish"),
        ("th", "Thai"),
    ]

    text = models.TextField()
    language = models.CharField(
        max_length=2,
        choices=LANGUAGES,
    )
    file = models.FileField(
        upload_to="audios/",
        validators=[FileExtensionValidator(allowed_extensions=["mp3"]), audio_file_size],
    )
    correspondent_text = models.TextField(blank=True, null=True)  # Optional for linked audios
    correspondent_language = models.CharField(
        max_length=2,
        choices=LANGUAGES,
        blank=True,
        null=True,  # Optional for linked audios
    )
    linked_audios = models.ManyToManyField(  # For linked word audios from the main text
        "self", symmetrical=False, related_name="related_to", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID {self.id}: {self.text[:64]}"
