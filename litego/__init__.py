import urllib


class API:
    """
    Core LiteGo API implementation
    """

    endpoints = {
        'authenticate': '/merchant/authenticate',
        'refresh_auth': '/merchant/me/refresh-auth',
        'me': '/merchant/me',
        'create_charge': '/charges',
        'list_charges': '/charges',
        'get_charge': '/charges/{charge_id}',
        'set_notification': '/merchant/me/notification-url',
        'webhooks': '/merchant/me/notification-responses',
    }

    def __init__(self, *, merchant_id:"Merchant ID", secret_key:"Secret Key",
                 is_sandbox:bool):
        self.merchant_id = merchant_id
        self.secret_key = secret_key
        self.is_sandbox = is_sandbox

        self.auth_token = None
        self.refresh_token = None

    @property
    def (self):
        if self.is_sandbox:
            return 'https://sandbox.litego.io:9000'
        return 'https://api.litego.io:9000'

    def _authenticate(self):
        pass
