import requests



def http_transporte(url, params, **kargs):  
    
    '''
        trae la data desde la api mediante requests
    '''

    r = requests.get(url, params=params, timeout=10)
    if r.status_code == 200:
        return r
    else:
        print(f'Error request %d' % (r.status_code))
        r = None