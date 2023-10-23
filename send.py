from requests_html import HTMLSession
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as BS


ua = UserAgent()
headers = {
  'authority': 'announcements.bybit.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'max-age=0',
  'cookie': 'bm_sz=31685FEBA1FAF389C48D0D00619E6D25~YAAQLrIpFynfhziLAQAAOoT9WxXX7Ed3EusEhDJs1bkrf6eYkMhEyhkBO+45VDa0L1+Ng2FNLlm/YP3OPCjSqBOTQdnW2guU1DYt3KPgsq8tc441A/+4nsworTEGo5Ia0/eJM1gKdUFdWi9O2con8iDxaDHbFye8y7OkPPj1hjF1nb48ZwLgegcp+dtj0pWptlyaLrMIzEViGgxEwQJkUKnu7sS6dMw9MHaZvf+PfXZVQREO7QpHmHlKeR7Rc/J7DlPUrouA5d4Nk3mjdqlBb5w2Ee4oGOtNloyyDXNn8EjQiA==~4601913~4470594; deviceId=c76423b1-349a-3b1e-e963-fb62aa144f0c; _ALGOLIA=anonymous-f05976b5-2c0c-4fc9-8324-f06a626663c0; ak_bmsc=1A920C7D29511DDAD3F283A5E5447A1B~000000000000000000000000000000~YAAQLrIpF3PghziLAQAA/LH9WxWgBp0ICdFn9AxpnI0qgDsNENl4Y+nVDg7ZXXHDQdOQ3rJmGIq1uZzN0rtCsoS0tTNDY96d561KeJHPFb36NP/YMMkZYNWLdiqobMeDzP3OEBy8OgeeP10NqEhdf2vxRoy5JJ4Vi8m6z9FKztZdj+9P5OIVjGJ+aobOO9euUfnbz0BGSkfl1eoMmuNWeyR/NmTpwDFP0lEHqg4j3m99+nyVJvyv4skc7u/rraTK4x/4GVHKi3YnHq9m0OS/GHR7Vn8XFG04PjA+ZqnX4eO+Ofbdhw7OsiJfQwztPjpgZhgFfvj17EbGDVw0+N/l0doJUHORE1TvqfZEqikhFtyEWGnD1fdMXoaMSPrV4eiWqd3jDSORL7t3NbFSOtSoLKWZur3RIlEq8bthSTnMNQvBvVhlBqhO24q5P9ZLreOSqZA+8emxDWRnl6wP0SiTXGJtveMDsEishlmRj3yifBXbm3rCcwlGLn0i+6ZAbFfs; _abck=083900E1CD48A13B0F33C4A83CD3E30D~0~YAAQLrIpF3TghziLAQAAO7L9WwpYCO0O8AoBzmn5duqRxAYjgIRVuhQOYQFXoou5CCNdz+nFJYhNgpLPJ4RbiRBLP441UF6g5auNS8KOn2PzL4mmfDz39ivcg1DfHRPE9AqMH+4XtLDdFWxDrZciyflSjwfq+4SuPnw4d4LMUsC4Uskx0bmqHMVIEhNgkb+Tw6794Q8kAr7jR0yc8z//oGNW/abLoslrgMjE4ZcINFHLFGRhg/zlHlUC2qsnmzrA6p9jNcvkZ0QzbACScAELdsi011AgRe6bdMe+0+BeR1hUgSD4jrykKLfuFCMFAY7UeQpjghDIx5g0KW4goSCUYKE4y7Y5/NwJaMcfKIqiu31NgTV+qlzTDpvSnXNAAzbOsLXsUAw9Iq1RCgjTbGL91K5/nn+plgI=~-1~||-1||~-1; _by_l_g_d=49fa09f0-d76b-f862-8701-22e8fbc635f9; _gcl_au=1.1.939002086.1698055441; _ym_uid=1698055442133322969; _ym_d=1698055442; _ym_isad=1; _ga=GA1.1.812730773.1698055443; sajssdk_2015_cross_new_user=1; _by_l_g_d=49fa09f0-d76b-f862-8701-22e8fbc635f9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%220%22%2C%22first_id%22%3A%2218b5bfdd4da45-08729ede13ce468-26031051-2073600-18b5bfdd4db6c4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiNWJmZGQ0ZGE0NS0wODcyOWVkZTEzY2U0NjgtMjYwMzEwNTEtMjA3MzYwMC0xOGI1YmZkZDRkYjZjNCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjAifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%220%22%7D%2C%22%24device_id%22%3A%2218b5bfdd4da45-08729ede13ce468-26031051-2073600-18b5bfdd4db6c4%22%7D; BYBIT_REG_REF_prod={"lang":"ru","g":"49fa09f0-d76b-f862-8701-22e8fbc635f9","medium":"direct","url":"https://announcements.bybit.com/"}; builderSessionId=62a0472ded6b466c88392ceea6c74f3f; g_state={"i_p":1698065221412,"i_l":1}; bm_sv=88B6CD290718AB120B1A4B21807C5645~YAAQLrIpF1KOiTiLAQAANkwyXBVXwqGN14/I2vs7K1kBYWb6YME1Jq687UXpXJ5eHvshaJil7jXt91S7K5egHtl23AVA9xGPnarpyok2ZyRvjooF8ge8LcBnninA6PYRk2HF45WMct7pcCl+fqg+wfo9f2QAYCcu2IPx7y0F53xpH8LpDnR9ObT3EE51qBBUKBqZXZs2wGZICdd/ILca1Y7rIzRDnGRnXCq8P2HT+Hqduv+JrOyGJ9eQTixMU7Ok~1; _ga_SPS4ND2MGC=GS1.1.1698057953.2.1.1698058888.50.0.0',
  'if-none-match': '"a5e7-DL46Zi89EDDzSN5V7Vk3eVaN/1s"',
  'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
  'Referer': '',
  'content-length': '0',
  'origin': 'https://announcements.bybit.com',
  'referer': 'https://announcements.bybit.com/',
  'x-client-data': 'CIm2yQEIprbJAQisncoBCMbaygEIlaHLAQjgxc0BCKfUzQEI4dXNARibr80BGNPYzQE=',
  'content-type': 'text/plain;charset=UTF-8',
  'Origin': 'https://announcements.bybit.com',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
  'if-modified-since': 'Tue, 09 May 2023 02:28:23 GMT',
  'traceparent': '00-83b5a6d5d0ccd98d6bb0dc84ba9b51b8-480e3f49df8be2f2-01',
  'platform': 'pc',
  'guid': '49fa09f0-d76b-f862-8701-22e8fbc635f9',
  'lang': 'en',
  'usertoken': '',
  'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
  'Accept-Language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
  'Connection': 'keep-alive',
  'Cookie': 'bito=AACJ1U7GxLAAACDA9DSv4A; bitoIsSecure=ok',
  'Sec-Fetch-Dest': 'image',
  'Sec-Fetch-Mode': 'no-cors',
  'Sec-Fetch-Site': 'cross-site'
}
url = "https://announcements.bybit.com/en-US/article/special-offer-looking-for-a-new-crypto-card--bltaa691019e4782034/"


session = HTMLSession()
r = session.get(url, headers=headers)

open('c.html', 'w+', encoding='utf8').write(r.text)