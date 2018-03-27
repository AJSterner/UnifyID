import urllib2
from urllib import urlencode
from ctypes import c_int64


def random_ints(num=1, min_val=-1e9, max_val=1e9):
        """
        get random integers from random.org

        arguments
        ---------        
        num (int): number of integers to get
        min_val (int): min int value
        max_val (int): max int value
        timeout (int): timeout in seconds (should be long as random.org may ban)
        
        """
        num = int(num)
        min_val = int(min_val)
        max_val = int(max_val)

        assert 1 <= num, "num must be positive"
        assert min_val < max_val, "min must be less than max"
        
        rand_ints = []

        while num > 0:
                to_get = min(num, 1E4)
                rand_ints.extend(random_ints_helper(to_get, min_val, max_val))
                num -= to_get
        
        return rand_ints


def random_ints_helper(num=1, min_val=-1e9, max_val=1e9):
        """
        get random integers from random.org (not to be called directly)

        arguments
        ---------        
        num (int): number of integers to get
        min_val (int): min int value
        max_val (int): max int value
        timeout (int): timeout in seconds (should be long as random.org may ban)
        
        """
        num = int(num)
        min_val = int(min_val)
        max_val = int(max_val)

        assert 1 <= num <= 1E4, "num invalid (if too great use many_random_ints)"
        assert min_val < max_val, "min must be less than max"
        

        req = urllib2.Request(random_request_url(num, min_val, max_val))
        
        try:
                response = urllib2.urlopen(req).read()
        except urllib2.HTTPError as e:
                print('Request could\'t be filled by the server')
                print('Error code: ' + e.code)
        except urllib2.URLError as e:
                print('Connection error')
                print('Reason: ' + e.reason)
        
        return [int_from_hexstr(line) for line in response.splitlines()]


        
def random_request_url(num, min_val, max_val):
        """ return GET random request URL (see https://www.random.org/clients/http/) """
        assert isinstance(num, int) and isinstance(min_val, int) and isinstance(max_val, int)

        req_data = dict(num=num,
                min=min_val,
                max=max_val,
                col=1,
                base=16,
                format='plain',
                rnd='new')
        
        return "https://www.random.org/integers/?" + urlencode(req_data)
        

        
        
def int_from_hexstr(hexstr):
        """
        returns a python integer from a string that represents a twos complement integer in hex
        """
        uint = int(hexstr, base=16) # python assumes positive int from string
        return c_int64(uint).value
