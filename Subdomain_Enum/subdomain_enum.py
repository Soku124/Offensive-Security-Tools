import requests




def make_request(url):

    while True:
        print(url)
        r = requests.get(url=url)
        if r.status_code == 200:
            return True
        else:
            print(url + "\t\t" + "NL")


def write_live_domain(domain):

    with open("subdomains.txt",'a') as f:
        f.write(domain + "\n")
        f.close()
    
def subdomain():
    sd = []
    with open("/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt","r") as f:
        for subdomain in f:
            sd.append(subdomain.strip())
    
    return sd

def run():
    url = ".erbeofficinali.org"

    subdomains = subdomain()
    # print(subdomains)

    for sd in subdomains:
        result = make_request("https://"+sd+url)

        if result:
            print(result)
            write_live_domain(result)
        # print(sd)



run()


        
