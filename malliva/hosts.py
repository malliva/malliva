from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(r"*", "marketplaceRouter.urls", name="marketplace-resolver"),
)
