import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

def scraping_instagram(username:str):
    url='https://www.instagram.com/{username}/'.format(username=username)

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    req = requests.get(url=url, headers=headers)

    if req.status_code == 200:
        soup = BeautifulSoup(req.text,'html.parser')
        meta_tag=soup.find_all('meta')

        result=[]
        for i in meta_tag:
            try:
                if i.attrs['property'] == 'og:image':
                    result.update({'img':i.attrs['content']})

                if i.attrs['property'] == 'og:title':
                    result.update({'title':i.attrs['content']})

                if i.attrs['property'] == 'og:description':
                    result.update({'descricao':i.attrs['content']})

            except:
                result.append(i.attrs)
                pass

        return result

    return req.status_code

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('401.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perfil/<string:username>',methods=['GET'])
def perfil(username):
    data=scraping_instagram(username=username)
    return render_template('perfil/instagram.html',data=data)

@app.route('/teste',methods=['GET'])
def teste():
    data=scraping_instagram(username='robertogomes.jr')
    return render_template('teste.html',data=data)

if __name__=="__main__":
    app.run()
