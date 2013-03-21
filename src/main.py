import urllib2
import base64
import struct


class message1:
    def getMessage(self, domain, host):
        #bytes 0-3   NTLM  = self.protocol
        #bytes 4-7   SSP\0 = self.protocol
        #bytes 8-11  1000 = type as integer
        #bytes 12-15 3,B2, 0,0  = flags as integer
        #bytes 16-19 domainlength, domainlength = domainlength as SHORT (2bytes) x2
        #bytes 20-23 domainoffsett, 0,0 
        #bytes 24-27 hostlength, hostlength
        #bytes 28-31 hostoffset, 0,0
        #bytes 32+ hoststring, domainstring
        domainlength =struct.pack('<H', len(domain))
        domainNameBufferOffset  =struct.pack('<I', 32 + len(host)) #32 because of number of bytes + length of host string
        hostlength = struct.pack('<H', len(host))
        ProductMajorVersion = struct.pack('<B', 5)
        ProductMinorVersion = struct.pack('<B', 1)
        hostOffset = struct.pack('<I', 32)

        msg1 = self.protocol + struct.pack('<I',self.type) +  \
            struct.pack('<I', self.flags) + \
            domainlength  + domainlength + domainNameBufferOffset + \
            hostlength + hostlength + hostOffset + host + domain
        print 'msg1', msg1
        
        return base64.encodestring(msg1)


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
    msg1  = message1()
    print msg1.getMessage('domain', 'host')
    #makeWebRequest('https://sharepoint.sonomapartners.com',
    #    'sonomapartners\ameyers', '\')
