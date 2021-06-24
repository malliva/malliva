from django.db import models
from paymentGateways.models import PaymentGateway
from customCodes.models import CustomCode
from translations.models import Translatable

# Create your models here.


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/domain/template_images/<filename>
    return "{0}/{1}/{2}".format(
        get_request_variable("malliva_domain"),
        "template_images",
        filename,
    )


class TemplateStyling(models.Model):
    """
    Contains all configurations for the frontend view of marketplace.
    """

    # TODO: remember to set resolutions for the images below on the fields
    id = models.BigAutoField(primary_key=True)
    favicon = models.ImageField(upload_to=image_directory_path, blank=True)
    logo = models.ImageField(upload_to=image_directory_path, blank=True)
    wide_logo = models.ImageField(upload_to=image_directory_path, blank=True)
    cover_photo = models.ImageField(upload_to=image_directory_path, blank=True)
    small_cover_photo = models.ImageField(
        upload_to=image_directory_path, blank=True, help_text="cover photo for mobile"
    )
    theme_color = models.CharField(max_length=200)
    # TODO: remember to change django to 3.2 in requirements and change this JSON field
    landing_page_settings = models.CharField(max_length=200)
    custom_codes = models.OneToOneField(
        CustomCode, on_delete=models.SET_NULL, null=True
    )
    footer_background = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class SocialMediaPage(models.Model):
    id = models.BigAutoField(primary_key=True)
    facebook_page = models.URLField()
    twitter_page = models.URLField()
    instagram_page = models.URLField()
    github_page = models.URLField()
    linkedin_page = models.URLField()
    tiktok_page = models.URLField()


class Configuration(Translatable):
    """
    Transaction FLow, related to marketplace plans
    TODO: remember to create default configuration fixure for new marketplaces
    should be run for every new marketplace accounts.
    """

    id = models.BigAutoField(primary_key=True)
    slogan = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    language = models.CharField(max_length=200, default="en")
    # TODO: remember to create a new file and add all countries and make this field a choice field
    country = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    templatestyle = models.OneToOneField(
        TemplateStyling, on_delete=models.SET_DEFAULT, default="1", null=True
    )
    malliva_terms_consent = models.BooleanField(
        default=False,
        help_text="track clients agreement of Malliva's latest terms of service",
    )
    transaction_agreement_in_use = models.BooleanField(default=False)
    notify_admins_about_new_members = models.BooleanField(default=False)
    notify_admins_about_new_transactions = models.BooleanField(default=False)
    require_verification_to_post_listings = models.BooleanField(default=False)
    private_marketplace = models.BooleanField(default=True)
    automatic_newsletters = models.BooleanField(default=False)
    invite_only_marketplace = models.BooleanField(default=False)
    send_emails_from = models.EmailField(max_length=200)
    preapprove_listing = models.BooleanField(
        default=False, help_text="listings are public by default in the marketplace"
    )
    show_date_in_listing_view = models.BooleanField(default=False)
    # TODO: decide which field to use for transaction flow settings later
    transaction_flow = models.CharField(max_length=200)
    active_payment_processor = models.ForeignKey(
        PaymentGateway, on_delete=models.SET_DEFAULT, default="1"
    )
    show_location = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class TranslatableMeta:
        fields = ["slogan", "description"]
