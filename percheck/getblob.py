from flask import Blueprint, request, abort
from app_auth import GitApp
import logging
import requests


log = logging.getLogger('percheck.sub')

bp = Blueprint('getblob', __name__, url_prefix='/')

gitapp = GitApp()

@bp.route('/getblob')
def getblob():
    log.info('Entering Get Blob')

    blob_content = gitapp.get_commit_file_blob(user='zoomies', repo='githubapptest', file_sha='7756ef79677d848c2615550ef0c217abb0b29c6c')

    blob_content = blob_content.replace("\r\n", "<br />")
    blob_content = blob_content.replace("\n", "<br />")


    return blob_content

