from mongoengine import Document, fields
from mongoengine.queryset.base import CASCADE
from .custom_codes import CustomCode
from .payment_gateways import PaymentGateway

# Create your fields here.


class TemplateStyling(Document):
    """
    Contains all configurations for the frontend view of marketplace.
    """

    # TODO: remember to set resolutions for the images below on the fields
    id = fields.SequenceField(primary_key=True)
    favicon = fields.StringField(max_length=500, required=False)
    logo = fields.StringField(max_length=500, required=False)

    wide_logo = fields.StringField(max_length=500, required=False)
    cover_photo = fields.StringField(max_length=500, required=False)
    small_cover_photo = fields.StringField(max_length=500, required=False)
    theme_color = fields.StringField(max_length=200)
    landing_page_settings = fields.DynamicField()
    custom_codes = fields.ReferenceField(
        CustomCode, on_delete=CASCADE, null=True
    )
    footer_background = fields.StringField(max_length=200)
    created_at = fields.DateTimeField(auto_now_add=True)
    updated_at = fields.DateTimeField(auto_now_add=True)


class SocialMediaPage(Document):
    id = fields.SequenceField(primary_key=True)
    facebook_page = fields.URLField()
    twitter_page = fields.URLField()
    instagram_page = fields.URLField()
    github_page = fields.URLField()
    linkedin_page = fields.URLField()
    tiktok_page = fields.URLField()
    created_at = fields.DateTimeField(auto_now_add=True)
    updated_at = fields.DateTimeField(auto_now_add=True)


class Configuration(Document):
    """
    Transaction FLow, related to marketplace plans
    TODO: remember to create default configuration fixure for new marketplaces
    should be run for every new marketplace accounts.
    """

    id = fields.SequenceField(primary_key=True)
    slogan = fields.StringField(max_length=200)
    description = fields.StringField(max_length=500)
    language = fields.StringField(max_length=200, default="en")
    # TODO: remember to create a new file and add all countries and make this field a choice field
    country = fields.StringField(max_length=200)
    currency = fields.StringField(max_length=200)
    templatestyle = fields.ReferenceField(
        TemplateStyling, reverse_delete_rule=CASCADE, default="1")
    malliva_terms_consent = fields.BooleanField(default=False)
    transaction_agreement_in_use = fields.BooleanField(default=False)
    notify_admins_about_new_members = fields.BooleanField(default=False)
    notify_admins_about_new_transactions = fields.BooleanField(default=False)
    require_verification_to_post_listings = fields.BooleanField(default=False)
    private_marketplace = fields.BooleanField(default=True)
    automatic_newsletters = fields.BooleanField(default=False)
    invite_only_marketplace = fields.BooleanField(default=False)
    send_emails_from = fields.EmailField(max_length=200)
    preapprove_listing = fields.BooleanField(default=False)
    show_date_in_listing_view = fields.BooleanField(default=False)
    # TODO: decide which field to use for transaction flow settings later
    transaction_flow = fields.StringField(max_length=200)
    active_payment_processor = fields.ReferenceField(
        PaymentGateway, reverse_delete_rule=CASCADE, default="1")
    show_location = fields.BooleanField(default=False)
    created_at = fields.DateTimeField(auto_now_add=True)
    updated_at = fields.DateTimeField(auto_now_add=True)
