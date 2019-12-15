from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/hello')
def hello():
	ime = "Nenad"
	dani_u_nedelji = ["Ponedeljak","Utorak","Sreda","Cetvrtak","Petak","Subota","Nedelja"]
	mesec = ["januar","februar","mart","april","maj","jun","jul","avgust","septembar","oktobar","novembar","decembar"]
	return render_template("hello.html",ime_na_stranici = ime,dani = dani_u_nedelji,meseci = mesec)

@app.route('/raspored')
def studenti():
	f = open("src/RAFraspored.csv","r")
	redovi = f.readlines()
	test = 5
	svi_predavaci = [red.split(',')[2] for red in redovi]
	sve_ucionice = [red.split(',')[6] for red in redovi]

	jedinstveni_predavaci = []
	jedinstvene_ucionice = []

	for predavac in svi_predavaci:
		if predavac not in jedinstveni_predavaci:
			jedinstveni_predavaci.append(predavac)
	svi_predavaci = jedinstveni_predavaci.sort()
	

	for ucionica in sve_ucionice:
		if ucionica not in jedinstvene_ucionice:
			jedinstvene_ucionice.append(ucionica)
	sve_ucionice = jedinstvene_ucionice.sort()
	
	return render_template("raspored.html",redovi = redovi,test = test,svi_predavaci = jedinstveni_predavaci, sve_ucionice = jedinstvene_ucionice)

if __name__ == '__main__':
	app.run()

