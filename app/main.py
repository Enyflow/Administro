from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
#import matplotlib.pyplot as plt
#import numpy as np
import psycopg2
import psycopg2.extras



url = "host='localhost' dbname='impresa' user='postgres' password='Giulia06'"

app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("select code from login where username = %s", (username,))
    r = []
    for t in cursor:
        i = {
            "passwordc":t[0],
            }
        r.append(i)
    connection.commit()
    cursor.close()
    connection.close()

    #return menu() if (p == r[0]["passwordc"]) else paginaweb
    if password == r[0]["passwordc"]:
        return render_template("menu.html")
    else:
        return render_template("paginaweb.html")
      
    
    

def leggi():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM presentazione ")

    impresaa = []
    for row in cursor:
        impresa = {
            "nome": row[0],
            "descrizione": row[1],
            "via": row[2]
            }
        impresaa.append(impresa)
       
    connection.commit()
    cursor.close()
    connection.close()
    print(impresaa)
    return impresaa

def leggiclienti():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM clienti ")

    B = []
    for row in cursor:
        impresa = {
            "cliente": row[0],
            "nome": row[1],
            "cognome": row[2],
            "cf": row[3],
            "citta": row[4],
            "via": row[5],
            "cap": row[6],
            "nazione": row[7],
            "tel": row[8],
            "mail": row[9],
            "piva": row[10],
            "iban": row[11],
            }
        B.append(impresa)
       
    connection.commit()
    cursor.close()
    connection.close()
    print(B)
    return B

def ordini():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM commerciale order by id_ordine")

    a = []
    for row in cursor:
        impresa = {
            "id_ordine": row[0],
            "n_articolo": row[1],
            "data_ordine": row[2],
            "quantita": row[3],
            "prezzo": row[4],
            "sconto": row[5],
            "citta": row[6],
            "via": row[7],
            "cap": row[8],
            "cliente": row[9],
            "stato_ordine":row[10],
            "fattura":row[11],
            "guadagno":row[12],
            "numero":row[13],
            "pagamento":row[14]
            
            
            }
        a.append(impresa)
       
    connection.commit()
    cursor.close()
    connection.close()
    
    return a

def leggintroiti():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM commerciale ")

    r = []
    for row in cursor:
        impresa = {
            "id_ordine": row[0],
            "n_articolo": row[1],
            "quantita":row[3],
            "prezzo":row[4],
            "sconto":row[5],
            "guadagno": row[12]
            }
        r.append(impresa)
       
    connection.commit()
    cursor.close()
    connection.close()
    print(r)
    return r

def leggiprodotti():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM prodotti ")

    C = []
    for row in cursor:
        impresa = {
            "n_articolo": row[0],
            "nome": row[1],
            "descrizione": row[2],
            "prezzo": row[3],
            "scontomax": row[4],
            "disponibilita": row[5]
            }
        C.append(impresa)
       
    connection.commit()
    cursor.close()
    connection.close()
    print(C)
    return C


def leggicpp():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM cpp ")

    c = []
    for row in cursor:
        impresa = {
            "n": row[0],
            "valore": row[1]
            }
        c.append(impresa)
       
    connection.commit()
    cursor.close()
    connection.close()
    print(c)
    return c


def leggicpp2():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("SELECT valore  FROM cpp where n = 'Acquisti' ")

    
    c = []
    for row in cursor:
        acquisti = {
            "acquisti": row[0]
            }
        c.append(acquisti)

        
    connection.commit()
    cursor.close()
    connection.close()
    return c

def leggicpp3():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("SELECT valore FROM cpp where n = 'Ricavi' ")

    e = []
    for t in cursor:
        ricavi = {
            "ricavi": t[0]
            }
        e.append(ricavi)

        
    connection.commit()
    cursor.close()
    connection.close()
    return e


def leggiimp():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM imposta ")

    imp = []
    for row in cursor:
        impo = {
            "impostap": row[0]
            }
        imp.append(impo)
       
    connection.commit()
    cursor.close()
    connection.close()
    print(imp)
    return imp


def leggiordinidaricevere():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("select * from commerciale where pagamento = 'Pagamento non eseguito'")

    t = []
    for row in cursor:
        ordini = {
            "id_ordine": row[0],
            "n_articolo": row[1],
            "data_ordine": row[2],
            "quantita": row[3],
            "cliente": row[9],
            "stato_ordine":row[10],
            "guadagno":row[12],
            "pagamento":row[14]
            }
        t.append(ordini)
       
    connection.commit()
    cursor.close()
    connection.close()
    
    return t

def leggiclientidaricevere():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("select * from clienti inner join commerciale on clienti.cliente = commerciale.cliente where pagamento ='Pagamento non eseguito'")

    q = []
    for row in cursor:
        clienti = {
            "nome": row[1],
            "cognome": row[2],
            "citta": row[4],
            "via": row[5],
            "cap": row[6],
            "nazione": row[7],
            "tel": row[8],
            "mail": row[9],
            "piva": row[10],
            "iban": row[11],
            }
        q.append(clienti)
       
    connection.commit()
    cursor.close()
    connection.close()
    
    return q


def totint():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("select sum(guadagno) from commerciale ")

    u = []
    for row in cursor:
        impo = {
            "totint": row[0]
            }
        u.append(impo)
       
    connection.commit()
    cursor.close()
    connection.close()
    
    return u

def totintric():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("select sum(guadagno) from commerciale where pagamento = 'Pagamento eseguito' ")

    t = []
    for row in cursor:
        impo = {
            "totintric": row[0]
            }
        t.append(impo)
    valore= + t[0]["totintric"]
    x="Ricavi"
    cursor.execute("DELETE FROM cpp WHERE n = %s", (x,))
    cursor.execute("INSERT INTO cpp (n,valore) \
        VALUES (%s, %s)", (x,valore))
    connection.commit()
    cursor.close()
    connection.close()

    return t

def totintdaric():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("select sum(guadagno) from commerciale where pagamento = 'Pagamento non eseguito' ")

    w = []
    for row in cursor:
        impo = {
            "totintdaric": row[0]
            }
        w.append(impo)
       
    connection.commit()
    cursor.close()
    connection.close()

    return w

def totintcoa():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("select sum(guadagno) from commerciale where pagamento = 'Pagamento in contanti (Inserisci in cassa)' or pagamento= 'Pagamento in assegno (Inserisci in cassa)' ")

    p = []
    for row in cursor:
        impo = {
            "totintcoa": row[0]
            }
        p.append(impo)
       
    connection.commit()
    cursor.close()
    connection.close()

    return p


def scrivi_pers(Nome,Cognome,Anni,Mestiere,Tariffa,oremensili):
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    r = 0
    cursor.execute("INSERT INTO personale (Nome,Cognome,Anni,Mestiere,Tariffa,oremensili,guadagno) \
        VALUES ( %s, %s, %s, %s, %s, %s, %s)", (Nome,Cognome,Anni,Mestiere,Tariffa,oremensili,r))

    connection.commit()
    cursor.close()
    connection.close()

def scrivi_vendita(n_articolo,data_ordine,quantita,prezzo,sconto,citta,via,cap,cliente,guadagno,numero,percentuale,stato_ordine,pagamento):
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO commerciale (n_articolo,data_ordine,quantita,prezzo,sconto,citta,via,cap,cliente,guadagno,numero,stato_ordine,pagamento) \
        VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (n_articolo,data_ordine,quantita,prezzo,sconto,citta,via,cap,cliente,guadagno,numero,stato_ordine,pagamento))

    cursor.execute("update prodotti set disponibilita = (disponibilita - (%s)) where prodotti.n_articolo = %s", (quantita,n_articolo))

    cursor.execute("update personale set guadagno = t1.guadagno from (select guadagno + (%s * %s) as guadagno from personale)as t1 where numero = %s",(int(guadagno),float(percentuale),numero))
     
    
    connection.commit()
    cursor.close()
    connection.close()
    
def scrivi_acquisto(n_articolo,nome,tipo,data_acquisto,descrizione,azienda,prezzo,quantita,stato_ordine,stato_pagamento):
    connection = psycopg2.connect(url)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    
    cursor.execute("insert into acquisti (n_articolo,nome,tipo,data_acquisto,descrizione,azienda,prezzo,quantita,stato_ordine,stato_pagamento) \
        VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(n_articolo,nome,tipo,data_acquisto,descrizione,azienda,prezzo,quantita,stato_ordine,stato_pagamento))
    if tipo == "Prodotto (merce da vendere)":
        cursor.execute("update prodotti set disponibilita = (disponibilita + (%s)) where prodotti.n_articolo = %s", (quantita,n_articolo))
        
    
    connection.commit()
    
    cursor.close()
    
    connection.close()
    
def scrivi_cliente(nome,cognome,cf,citta,via,cap,nazione,tel,mail,piva,iban):
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO clienti (nome,cognome,cf,citta,via,cap,nazione,tel,mail,piva,iban) \
        VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome,cognome,cf,citta,via,cap,nazione,tel,mail,piva,iban))

    connection.commit()
    cursor.close()
    connection.close()

def scrivi_prodotto(n_articolo,nome,descrizione,prezzo,scontomax,disponibilita):
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO prodotti (n_articolo,nome,descrizione,prezzo,scontomax,disponibilita) \
        VALUES ( %s, %s, %s, %s, %s, %s)", (n_articolo,nome,descrizione,prezzo,scontomax,disponibilita))

    connection.commit()
    cursor.close()
    connection.close()
    
@app.route('/aggiungi_personale')
def aggiungi_personale():
    return render_template('aggiungi_personale.html')

@app.route('/aggiungi_cliente')
def aggiungi_cliente():
    return render_template('aggiungi_cliente.html')

@app.route('/aggiungi_prodotto')
def aggiungi_prodotto():
    return render_template('aggiungi_prodotto.html')

@app.route('/aggiungi_acquisto')
def aggiungi_acquisto():
    return render_template('aggiungi_acquisto.html')

@app.route('/vendita')
def vendita():
    return render_template('vendita.html')

@app.route('/statistiche')
def statistiche():
    return render_template('statistiche.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/clienti')
def clienti():
    l = leggiclienti()
    return render_template('clienti.html',e = l)

@app.route('/prodotti')
def prodotti():
    l = leggiprodotti()
    return render_template('prodotti.html',e = l)

@app.route('/introiti')
def introiti():
    l = leggintroiti()
    r = totint()
    y = totintric()
    p = totintdaric()
    x = totintcoa()
    return render_template('introiti.html',e = l, u = r,t = y, w = p,a =x)

@app.route('/ordinidaricevere')
def ordinidaricevere():
    l = leggiordinidaricevere()
    y = leggiclientidaricevere()
    return render_template('ordinidaricevere.html',t = l,r = y)

@app.route('/comm')
def comm():
    l = ordini()
    return render_template('comm.html',e = l)

@app.route('/cpp')
def cpp():
    l = leggicpp()
    return render_template('cpp.html',e = l)



@app.route('/Stat_prodotti')
def stat_prodotti():
    #y = leggipr2()
    #l = leggipr1()
    return render_template('Stat_prodotti.html') #e=l , y=y)



def scrivi_cpp(n,valore):
    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO cpp (n,valore) \
        VALUES (%s, %s)", (n,valore))

    connection.commit()
    cursor.close()
    connection.close()
    
@app.route('/salva_cpp', methods=['POST'])
def salva_cpp():
    n = request.form['n']
    valore = request.form['valore']
    print('n:', n)
    print('valore:', valore)
    
    scrivi_cpp(n, valore)
    
    return cpp()

@app.route('/imp')
def imp():
    l = leggiimp()
    return render_template('imp.html',e = l)


@app.route('/salva_dipendente', methods=['POST'])
def salva_dipendente():
    Nome = request.form['nome']
    Cognome = request.form['cognome']
    Anni = request.form['anni']
    Mestiere = request.form['mestiere']
    Tariffa = request.form['tariffa']
    oremensili = request.form['oremensili']
    print('Nome:', Nome)
    print('Cognome:', Cognome)
    print('Anni:', Anni)
    print('Mestiere:', Mestiere)
    print('Tariffa:', Tariffa)
    print('Ore Mensili:', oremensili)
    scrivi_pers(Nome,Cognome,Anni,Mestiere,Tariffa,oremensili)
    return personale()

@app.route('/salva_cliente', methods=['POST'])
def salva_cliente():
    nome = request.form["nome"]
    cognome = request.form["cognome"]
    cf = request.form["cf"]
    citta = request.form["citta"]
    via = request.form["via"]
    cap = request.form["cap"]
    nazione = request.form["nazione"]
    tel = request.form["tel"]
    mail = request.form["mail"]
    piva = request.form["piva"]
    iban = request.form["iban"]
    scrivi_cliente(nome,cognome,cf,citta,via,cap,nazione,tel,mail,piva,iban)
    return clienti()


@app.route('/salva_prodotto', methods=['POST'])
def salva_prodotto():
    n_articolo = request.form["n_articolo"]
    nome = request.form["nome"]
    descrizione = request.form["descrizione"]
    prezzo = request.form["prezzo"]
    scontomax = request.form["scontomax"]
    disponibilita = request.form["disponibilita"]
    scrivi_prodotto(n_articolo,nome,descrizione,prezzo,scontomax,disponibilita)
    return prodotti()

@app.route('/salva_vendita', methods=['POST'])
def salva_vendita():
    n_articolo = request.form["n_articolo"]
    data_ordine = request.form["data_ordine"]
    quantita = request.form["quantita"]
    prezzo = request.form["prezzo"]
    sconto = request.form["sconto"]
    citta = request.form["citta"]
    via = request.form["via"]
    cap = request.form["cap"]
    cliente = request.form["cliente"]
    numero = request.form["numero"]
    percentuale = request.form["percentuale"]
    stato_ordine = request.form["stato_ordine"]
    pagamento = request.form["pagamento"]
    guadagno = (int(prezzo) - int(sconto))*int(quantita)
    scrivi_vendita(n_articolo,data_ordine,quantita,prezzo,sconto,citta,via,cap,cliente,guadagno,numero,percentuale,stato_ordine,pagamento)
    return comm()


                   
@app.route('/')
@app.route('/paginaweb')
def paginaweb():
    lista = leggi()
    return render_template('paginawebb.html', impresa = lista)


@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/personale')
def personale():
    r = leggi_personale()
    return render_template('personale.html', personale = r)

@app.route('/acquisti')
def acquisti():
    r = leggi_acquisti()
    return render_template('acquisti.html', e = r)


def leggi_personale():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PERSONALE order by Numero")
    personale = []
    for t in cursor:
        persona = {
            "Numero": t[0],
            "Nome": t[1],
            "Cognome": t[2],
            "Anni": t[3],
            "Mestiere": t[4],
            "Tariffa": t[5],
            "oremensili":t[6],
            "cf": t[7],
            "titolostudio": t[8],
            "data_titolostudio": t[9],
            "autoaziendale": t[10],
            "modelloauto": t[11],
            "targa": t[12],
            "percentuale":t[13]
            }
        personale.append(persona)
    print(personale)
    connection.commit()
    cursor.close()
    connection.close()
    return personale

def leggi_acquisti():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM acquisti order by id_acquisto")
    e = []
    for t in cursor:
        persona = {
            "id_acquisto": t[0],
            "n_articolo": t[1],
            "nome": t[2],
            "tipo": t[3],
            "data_acquisto": t[4],
            "descrizione": t[5],
            "azienda":t[6],
            "prezzo": t[7],
            "quantita": t[8],
            "stato_ordine": t[9],
            "stato_pagamento": t[10]
            }
        e.append(persona)

    connection.commit()
    cursor.close()
    connection.close()
    return e


@app.route('/busta_paga')
def personale2():
    r = leggi_personale2()
    return render_template('busta_paga.html', personale2 = r)


def leggi_personale2():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT nome,cognome,(sum((tariffa * oremensili)+ guadagno)) FROM PERSONALE group by nome,cognome, numero order by Numero")
    personale2 = []
    for t in cursor:
        stpinps = (t[2]*13)-(t[2]*0.0919)
        irpef = 0
        if stpinps < 15000 :
            irpef = round((stpinps*0.23),2)
        if stpinps >= 15000 and stpinps < 28000:
            irpef = 3450 + (stpinps - 15000)*0.27
        if stpinps >= 28000 and stpinps < 55000:
            irpef = 6960 + (stpinps - 28000)*0.38
        if stpinps >= 55000 and stpinps < 75000:
            irpef = 17220 + (stpinps - 55000)*0.41
        if stpinps >= 75000:
            irpef = 25420 + (stpinps-75000)*0.43
        persona = {
            "Nome": t[0],
            "Cognome": t[1],
            "Stip":t[2]*13,
            "Stipendio": round(((t[2]*13)-(t[2]*0.0919)-irpef)/13,2),
            "INPS":round(t[2]*0.0919,2) ,
            "IRPEF": round(irpef,2)
            }
        personale2.append(persona)

    
    connection.commit()
    cursor.close()
    connection.close()

    return personale2

def leggitot():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("select(sum((tariffa * oremensili)+ guadagno)) from personale ")
    t = []
    for e in cursor:
        ts = { "Retribuzione": e[0]*13
               }
        t.append(ts)
    valore = -t[0]["Retribuzione"]
    d = 'Retribuzione annuale lorda'
    cursor.execute("DELETE FROM cpp WHERE n = %s", (d,))
    cursor.execute("INSERT INTO cpp (n,valore) \
        VALUES (%s, %s)", (d,valore))
    connection.commit()
    cursor.close()
    connection.close()
    
    return t

def leggitotacq():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("select sum(prezzo*quantita) from acquisti")
    e = []
    for y in cursor:
        te = { "Acquisti": y[0]}
        e.append(te)
    valore = -e[0]["Acquisti"]
    t = 'Acquisti'
    cursor.execute("DELETE FROM cpp WHERE n = %s", (t,))
    cursor.execute("INSERT INTO cpp (n,valore) \
        VALUES (%s, %s)", (t,valore))
    connection.commit()
    cursor.close()
    connection.close()
    
    return e



@app.route('/tot_stipendi')
def tot_stipendi():
    s = leggitot()
    return render_template("tot_stipendi.html", p = s)

@app.route('/tot_acquisti')
def tot_acquisti():
    s = leggitotacq()
    return render_template("tot_acquisti.html", e = s)

@app.route('/dettaglip',methods=['POST'])
def dettaglip():
    Numero = request.form['Numero']
    s = dettagli_personale(Numero, True)
    return render_template("dettaglip.html", personale = s)

def dettagli_personale(Numero, valori_testo):
    connection = psycopg2.connect(url)  
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM personale WHERE Numero = %s", (Numero,))
    
    r = cursor.fetchone()
    
    
    persona = {
        "Numero": r["numero"],
        "Nome": r["nome"],
        "Cognome": r["cognome"],
        "Anni": r["anni"],
        "Mestiere": r["mestiere"],
        "Tariffa": r["tariffa"],
        "oremensili": r["oremensili"],
        }
    
    
    connection.commit()
    cursor.close()
    connection.close()

    return persona

def dettagli_cliente(cliente, valori_testo):
    connection = psycopg2.connect(url)  
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM clienti WHERE cliente = %s", (cliente,))
    
    t = cursor.fetchone()
    
    
    r = {
        "cliente": t["cliente"],
        "nome": t["nome"],
        "cognome": t["cognome"],
        "cf": t["cf"],
        "citta": t["citta"],
        "via": t["via"],
        "cap": t["cap"],
        "nazione": t["nazione"],
        "tel": t["tel"],
        "mail": t["mail"],
        "piva": t["piva"],
        "iban": t["iban"]
        }
    
    
    connection.commit()
    cursor.close()
    connection.close()

    return r

def dettagli_ordine(id_ordine, valori_testo):
    connection = psycopg2.connect(url)  
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM commerciale WHERE id_ordine = %s", (id_ordine,))
    
    t = cursor.fetchone()
    
    
    o = {
         "id_ordine": t["id_ordine"],
            "n_articolo": t["n_articolo"],
            "data_ordine": t["data_ordine"],
            "quantita": t["quantita"],
            "prezzo": t["prezzo"],
            "sconto": t["sconto"],
            "citta": t["citta"],
            "via": t["via"],
            "cap": t["cap"],
            "cliente": t["cliente"],
            "stato_ordine":t["stato_ordine"],
            "fattura":t["fattura"],
            "guadagno":t["guadagno"],
            "numero":t["numero"],
            "pagamento":t["pagamento"]
            
        }
    
    
    connection.commit()
    cursor.close()
    connection.close()

    return o

def dettagli_prodotto(n_articolo, valori_testo):
    connection = psycopg2.connect(url)  
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM prodotti WHERE n_articolo = %s", (n_articolo,))
    
    t = cursor.fetchone()
    
    
    y = {
        "n_articolo": t["n_articolo"],
        "nome": t["nome"],
        "descrizione": t["descrizione"],
        "prezzo": t["prezzo"],
        "scontomax": t["scontomax"],
        "disponibilita": t["disponibilita"]
        }
    
    
    connection.commit()
    cursor.close()
    connection.close()

    return y

@app.route('/dettaglic',methods=['POST'])
def dettaglic():
    cliente = request.form['cliente']
    s = dettagli_cliente(cliente, True)
    return render_template("dettaglic.html", r = s)

@app.route('/dettaglipr',methods=['POST'])
def dettaglipr():
    n_articolo = request.form['n_articolo']
    s = dettagli_prodotto(n_articolo, True)
    return render_template("dettaglipr.html", r = s)

@app.route('/modifica_personale', methods=['POST'])
def modifica_personale():
    Numero = request.form['Numero']
    s = dettagli_personale(Numero, False)
    return render_template("modifica_personale.html", personale = s)
    
@app.route('/modifica_cliente', methods=['POST'])
def modifica_cliente():
    cliente = request.form['cliente']
    s = dettagli_cliente(cliente, False)
    return render_template("modifica_cliente.html", r = s)

@app.route('/modifica_prodotto', methods=['POST'])
def modifica_prodotto():
    n_articolo = request.form['n_articolo']
    s = dettagli_prodotto(n_articolo, False)
    return render_template("modifica_prodotto.html", r = s)


@app.route('/modifica_ordine', methods=['POST'])
def modifica_ordine():
    id_ordine = request.form['id_ordine']
    s = dettagli_ordine(id_ordine, False)
    return render_template("modifica_ordine.html", r = s)


@app.route('/salva_modifichep', methods=['POST'])
def salva_modifichep():
    Numero = request.form['Numero']

    salvap(Numero)
    
    return personale()

@app.route('/salva_modifichec', methods=['POST'])
def salva_modifichec():
    cliente = request.form['cliente']

    salvac(cliente)
    
    return clienti()

@app.route('/salva_acquisto', methods=['POST'])
def salva_acquisto():
    
    n_articolo = request.form["n_articolo"]
    nome = request.form["nome"]
    tipo = request.form["tipo"]
    data_acquisto = request.form["data_acquisto"]
    descrizione = request.form["descrizione"]
    azienda = request.form["azienda"]
    prezzo = request.form["prezzo"]
    quantita = request.form["quantita"]
    stato_ordine = request.form["stato_ordine"]
    stato_pagamento = request.form["stato_pagamento"]
    scrivi_acquisto(n_articolo,nome,tipo,data_acquisto,descrizione,azienda,prezzo,quantita,stato_ordine,stato_pagamento)
    
    return acquisti()

@app.route('/salva_modificheo', methods=['POST'])
def salva_modificheo():
    id_ordine = request.form['id_ordine']

    salvao(id_ordine)
    
    return comm()

@app.route('/salva_modifichepr', methods=['POST'])
def salva_modifichepr():
    n_articolo = request.form['n_articolo']

    salvapr(n_articolo)
    
    return prodotti()


@app.route('/salva_imposta', methods=['POST'])
def salva_imposta():
    impostap = request.form['impostap']

    salvaimp(impostap)
    
    return imp()

def salvap(Numero):
    connection = psycopg2.connect(url)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    Nome = request.form["Nome"]
    Cognome = request.form["Cognome"]
    Anni = request.form["Anni"]
    Mestiere = request.form["Mestiere"]
    Tariffa = request.form["Tariffa"]
    oremensili = request.form["oremensili"]

    cursor.execute("UPDATE personale SET Nome = %s,\
        Cognome = %s, Anni = %s , Mestiere = %s, Tariffa = %s, oremensili = %s WHERE Numero = %s", (Nome,Cognome,Anni,Mestiere,Tariffa,oremensili,Numero))
    
    connection.commit()
    
    cursor.close()
    
    connection.close()

def salvao(id_ordine):
    connection = psycopg2.connect(url)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    n_articolo = request.form["n_articolo"]
    data_ordine = request.form["data_ordine"]
    quantita = request.form["quantita"]
    prezzo = request.form["prezzo"]
    sconto = request.form["sconto"]
    citta = request.form["citta"]
    via = request.form["via"]
    cap = request.form["cap"]
    cliente = request.form["cliente"]
    numero = request.form["numero"]
    stato_ordine = request.form["stato_ordine"]
    pagamento = request.form["pagamento"]

    cursor.execute("UPDATE commerciale SET n_articolo = %s,\
        data_ordine = %s, quantita = %s , prezzo = %s, sconto = %s, citta = %s,via = %s, cap = %s , cliente = %s, numero = %s, stato_ordine = %s, pagamento = %s WHERE id_ordine = %s", (n_articolo,data_ordine,quantita,prezzo,sconto,citta,via,cap,cliente,numero,stato_ordine,pagamento,id_ordine))
    
    connection.commit()
    
    cursor.close()
    
    connection.close()



def salvapr(n_articolo):
    connection = psycopg2.connect(url)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    n_articolo = request.form["n_articolo"]
    nome = request.form["nome"]
    descrizione = request.form["descrizione"]
    prezzo = request.form["prezzo"]
    scontomax = request.form["scontomax"]
    disponibilita = request.form["disponibilita"]

    cursor.execute("UPDATE prodotti SET nome = %s,\
        descrizione = %s, prezzo = %s , scontomax = %s, disponibilita = %s WHERE n_articolo = %s", (nome,descrizione,prezzo,scontomax,disponibilita,n_articolo))
    
    connection.commit()
    
    cursor.close()
    
    connection.close()
    

def salvac(cliente):
    connection = psycopg2.connect(url)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    nome = request.form["nome"]
    cognome = request.form["cognome"]
    cf = request.form["cf"]
    citta = request.form["citta"]
    via = request.form["via"]
    cap = request.form["cap"]
    nazione = request.form["nazione"]
    tel = request.form["tel"]
    mail = request.form["mail"]
    piva = request.form["piva"]
    iban = request.form["iban"]

    cursor.execute("UPDATE clienti SET nome = %s,\
        cognome = %s, cf = %s , citta = %s, via = %s, cap = %s, nazione = %s , tel = %s , mail = %s , piva = %s , iban = %s WHERE cliente = %s", (nome,cognome,cf,citta,via,cap,nazione,tel,mail,piva,iban,cliente))
    
    connection.commit()
    
    cursor.close()
    
    connection.close()

    
def salvaimp(impostap):
    connection = psycopg2.connect(url)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    impostap = request.form["impostap"]

    cursor.execute("UPDATE imposta SET impostap = %s",(impostap,))
    
    connection.commit()
    
    cursor.close()
    
    connection.close()

@app.route('/elimina_personale', methods=['POST'])
def elimina_personale():
    Numero = request.form['Numero']
    
    s = dettagli_personale(Numero, False)
    
    return render_template("elimina_personale.html", personale = s)

@app.route('/elimina_cliente', methods=['POST'])
def elimina_cliente():
    cliente = request.form['cliente']
    
    s = dettagli_cliente(cliente, False)
    
    return render_template("elimina_cliente.html", r = s)

@app.route('/elimina_prodotto', methods=['POST'])
def elimina_prodotto():
    n_articolo = request.form['n_articolo']
    
    s = dettagli_prodotto(n_articolo, False)
    
    return render_template("elimina_prodotto.html", r = s)

@app.route('/elimina_personalep', methods=['POST'])
def elimina_personalep():
    Numero = request.form['Numero']
    
    elimina_definitivop(Numero)
    
    return personale()

@app.route('/elimina_clientec', methods=['POST'])
def elimina_clientec():
    cliente = request.form['cliente']
    
    elimina_definitivoc(cliente)
    
    return clienti()

@app.route('/elimina_prodottop', methods=['POST'])
def elimina_prodottop():
    n_articolo = request.form['n_articolo']
    
    elimina_definitivopr(n_articolo)
    
    return prodotti()

def elimina_definitivop(Numero):
    connection = psycopg2.connect(url)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute("DELETE FROM Personale WHERE Numero = %s", (Numero,))
    connection.commit()

    cursor.close()

    connection.close()

def elimina_definitivopr(n_articolo):
    connection = psycopg2.connect(url)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute("DELETE FROM prodotti WHERE n_articolo = %s", (n_articolo,))
    connection.commit()

    cursor.close()

    connection.close()
    
def elimina_definitivoc(cliente):
    connection = psycopg2.connect(url)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute("DELETE FROM clienti WHERE cliente = %s", (cliente,))
    connection.commit()

    cursor.close()

    connection.close()

@app.route('/elimina_cpp', methods=['POST'])
def elimina_cpp():
    n = request.form['n']
    
    elimina_definitivocpp(n)
    
    return cpp()


def elimina_definitivocpp(n):
    connection = psycopg2.connect(url)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    
    cursor.execute("DELETE FROM cpp WHERE n = %s", (n,))
    
    connection.commit()

    cursor.close()

    connection.close()


def c():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(valore) AS margine_lordo from cpp where n in ('CDV','Ricavi')")
    z = []
    for e in cursor:
        
        ts = { "margine_lordo": e[0]}
        z.append(ts)
    
    connection.commit()
    cursor.close()
    connection.close()
    print(z)
    return z
    

@app.route('/cob')
def cob():
    s = c()
    r = c1()
    t = c2()
    u = c3()
    v = c4()
    z = c5()
    print(z)
    return render_template("cob.html", p = s, p1 = r, p2 = t, p3 = u, p4 = v, p5 = z)



def c1():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(valore) AS roc from cpp where n in ('CDV','Ricavi','Stipendi','Ammortamento', 'Affitto stabilimento', 'Quota fondo svalutazione crediti')")
    z = []
    for e in cursor:
    
        ts = { "roc": e[0]}
        z.append(ts)
    
    connection.commit()
    cursor.close()
    connection.close()
    print(z)
    return z

def c2():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(valore) AS roc from cpp where n in ('CDV','Ricavi','Stipendi','Ammortamento', 'Affitto stabilimento', 'Quota fondo svalutazione crediti','Gestione Accessoria')")
    z = []
    for e in cursor:
        print(e)
        ts = { "rog": e[0]}
        z.append(ts)
    
    connection.commit()
    cursor.close()
    connection.close()
    print(z)
    return z

def c3():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(valore) AS roc from cpp where n in ('CDV','Ricavi','Stipendi','Ammortamento', 'Affitto stabilimento', 'Quota fondo svalutazione crediti','Gestione Accessoria', 'Interesse Passivo')")
    z = []
    for e in cursor:
        print(e)
        ts = { "rordcomp": e[0]}
        z.append(ts)
    
    connection.commit()
    cursor.close()
    connection.close()
    print(z)
    return z

def c4():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(valore) AS roc from cpp where n in ('CDV','Ricavi','Stipendi','Ammortamento', 'Affitto stabilimento', 'Quota fondo svalutazione crediti','Gestione Accessoria', 'Interesse Passivo', 'Eventi straordinari')")
    z = []
    for e in cursor:
        z.append(e[0])
    
    connection.commit()
    cursor.close()
    connection.close()
    print(z)
    return z

def c5():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT impostap FROM imposta")
    z=[]
    e= []
    for c in cursor:
        z.append(c[0])
    l = c4()
    r = int((1-(z[0]/100)) * int(l[0]))
    e.append(r)
    
    connection.commit()
    cursor.close()
    connection.close()
    return e

def collegamento():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT impostap FROM imposta")


    
    connection.commit()
    cursor.close()
    connection.close()
    
@app.route('/eliminat_comm', methods=['POST'])
def eliminat_comm():


    return render_template("eliminat_comm.html")

@app.route('/eliminat_commc', methods=['POST'])
def eliminat_commc():
    
    eliminat_comm1()
    
    return comm()

    
def eliminat_comm1():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM commerciale")
    cursor.execute("update personale set guadagno = 0 ")
    connection.commit()
    cursor.close()
    connection.close()

    
if __name__ == '__main__':

    app.run(debug=True) #debug=True
