# -*- coding: utf-8 -*-

import re

from module.plugins.Crypter import Crypter


class FourChanOrg(Crypter):
    # Based on 4chandl by Roland Beermann
    # https://gist.github.com/enkore/3492599
    __name__ = "FourChanOrg"
    __type__ = "crypter"
    __version__ = "0.3"
    __pattern__ = r'http://(?:www\.)?boards\.4chan.org/\w+/res/(\d+)'
    __description__ = """4chan.org folder decrypter plugin"""

    def decrypt(self, pyfile):
        pagehtml = self.load(pyfile.url)

        images = set(re.findall(r'(images\.4chan\.org/[^/]*/src/[^"<]*)', pagehtml))
        urls = []
        for image in images:
            urls.append("http://" + image)

        self.core.files.addLinks(urls, pyfile.package().id)
