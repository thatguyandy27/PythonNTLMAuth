import urllib2
import base64


class message1:
    def getMessage(self, domain, host):
        domainlength =struct.pack('<H', len(domain))
        domainnamenufferoffset  =struct.pack('<I', len(host))
        hostlenght = struct.pack('<H', len(host))
        ProductMajorVersion = struct.pack('<B', 5)
        ProductMinorVersion = struct.pack('<B', 1)
        ProductBuild = struct.pack('<H', 2600)
        VersionReserved1 = struct.pack('<B', 0)
        VersionReserved2 = struct.pack('<B', 0)
        VersionReserved3 = struct.pack('<B', 0)
        NTLMRevisionCurrent = struct.pack('<B', 15)

        msg1 = self.protocol + struct.pack('<I',self.type) +  \
            struct.pack('<I', self.flags) + \
            domainlength + domainnamenufferoffset


    def __init__(self):
        self.protocol = 'NTLMSSP\0'
        self.type = 0x01
        self.bytezero = 0x000
        self.flags = 0xb203



def authWIthNTLM(url, username, password):
    #requestObj = urllib2.Request(url)
    message1 = 0x4e544c4d53535000
    print message1


def makeWebRequest(url, username, password):
    requestObj = urllib2.Request(url)
    try:
        response = urllib2.urlopen(requestObj)
        print('Code', response.getcode())
        print('Url', response.geturl())
    except IOError, e:
        if e.code != 401:
            print ('Error, sadface')
        else:
            print('reason', e.reason)
            print(e.headers)
            print(e.headers['www-authenticate'])
            if e.headers['www-authenticate'] == 'NTLM':
                authWIthNTLM(url, username, password)


if __name__ == '__main__':
    makeWebRequest('https://sharepoint.sonomapartners.com',
        'sonomapartners\ameyers', '\')
