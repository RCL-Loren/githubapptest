import logging
import json

log = logging.getLogger('percheck.sub')

class GitApp:

    def __init__(self):
        self.private_key =''
        self.github_app_id =''
        self.github_webhook_secret=''
        self.payload_raw=None
        self.payload=None

    def get_request_payload(self, request):
        self.payload_raw=request.get_data()
        self.payload=request.get_json()
        log.info(str(self.payload))

    def verify_webhook_signature(self):
        incoming_sig = request.headers.get('HTTP_X_HUB_SIGNATURE')
        if incoming_sig == None:
            log.error('No Github Webhook Signature')




