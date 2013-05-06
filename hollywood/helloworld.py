import cgi
import datetime
import urllib
import urllib2
import webapp2
import jinja2
import json
import os
import re
from google.appengine.ext import db
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Films(db.Model):
	film_id = db.StringProperty()
	film_name = db.StringProperty()
	film_producer = db.StringProperty()
	youtube_views = db.IntegerProperty()
	youtube_likes=db.IntegerProperty()
	youtube_dislikes=db.IntegerProperty()
	release_year = db.StringProperty()
	year = db.IntegerProperty()
	film_rating = db.FloatProperty()
	film_genre = db.StringProperty()
	budget = db.IntegerProperty()
	gross = db.IntegerProperty()
	rt_critics = db.FloatProperty()
	rt_audience = db.FloatProperty()
	
class Producer(db.Model):
	producer_name = db.StringProperty()
	
class MainPage(webapp2.RequestHandler):

    def get(self):
		page_select = "main"
		template_values = {
		            'page_title': page_select
		        }
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render(template_values))
		
class Columbia(webapp2.RequestHandler):

    def get(self):
		page_select = "Columbia"
		template_values = {
		            'page_title': page_select
		        }
		template = JINJA_ENVIRONMENT.get_template('columbia.html')
		self.response.write(template.render(template_values))
		
class ParaMount(webapp2.RequestHandler):

    def get(self):
		page_select = "Para mount"
		template_values = {
		            'page_title': page_select,
		        }
		
		template = JINJA_ENVIRONMENT.get_template('paramount.html')
		self.response.write(template.render(template_values))
class Universal(webapp2.RequestHandler):

    def get(self):
		page_select = "Universal"
		template_values = {
		            'page_title': page_select,
		        }

		template = JINJA_ENVIRONMENT.get_template('Universal.html')
		self.response.write(template.render(template_values))
class Disney(webapp2.RequestHandler):

    def get(self):
		page_select = "Disney"
		template_values = {
		            'page_title': page_select,
		        }

		template = JINJA_ENVIRONMENT.get_template('Disney.html')
		self.response.write(template.render(template_values))
		
class Warner(webapp2.RequestHandler):

    def get(self):
		page_select = "Warner"
		template_values = {
		            'page_title': page_select,
		        }

		template = JINJA_ENVIRONMENT.get_template('Warner.html')
		self.response.write(template.render(template_values))
		
		
class MGM(webapp2.RequestHandler):

    def get(self):
		page_select = "MGM"
		template_values = {
		            'page_title': page_select,
		        }

		template = JINJA_ENVIRONMENT.get_template('MGM.html')
		self.response.write(template.render(template_values))
		
class LoadData(webapp2.RequestHandler):

    def get(self):
			# input data
			source = urllib2.urlopen('http://bia660datasource.appspot.com/txt/crawl_final.txt')
			film_file = source.readlines()
			for line in film_file:
				if line.split('[')[6][1:-6][0:1] == 'p':
					if len(line.split('[')[4].split('(')[0]) >4:
						film_template = Films(key_name = str(line.split('[')[1][:-2]),film_id = str(line.split('[')[1][:-2]),film_name=str(line.split('[')[2][2:-3]),
											release_year = str(line.split('[')[4].split('(')[0]),
											film_rating = float(line.split('[')[3][:-2]),
											year = int(line.split('[')[4].split('(')[0][-4:]),
											film_genre = line.split('[')[5][:-2],
											budget = int(line.split('[')[6][1:-6][6:].replace(",",''))	)
					else:
						film_template = Films(key_name = str(line.split('[')[1][:-2]),film_id = str(line.split('[')[1][:-2]),film_name=str(line.split('[')[2][2:-3]),
											film_rating = float(line.split('[')[3][:-2]),
											film_genre = line.split('[')[5][:-2],
											budget = int(line.split('[')[6][1:-6][6:].replace(",",''))	)						
				else:
					if line.split('[')[6][1:-6][0:1] == 'R' or line.split('[')[6][1:-6][0:1] == 'K' or line.split('[')[6][1:-6][0:1] == 'A' or line.split('[')[6][1:-6][0:1] == 'N'or line.split('[')[6][1:-6][0:1] == 'O'or line.split('[')[6][1:-6][0:1] == 'E'or line.split('[')[6][1:-6][0:1] == 'e':
						film_template = Films(key_name = str(line.split('[')[1][:-2]),film_id = str(line.split('[')[1][:-2]),film_name=str(line.split('[')[2][2:-3]),
											release_year = str(line.split('[')[4].split('(')[0]),film_rating = float(line.split('[')[3][:-2]),film_genre = line.split('[')[5][:-2],
											budget = int(0)	)
					else:
						film_template = Films(key_name = str(line.split('[')[1][:-2]),film_id = str(line.split('[')[1][:-2]),film_name=str(line.split('[')[2][2:-3]),
											release_year = str(line.split('[')[4].split('(')[0]),film_rating = float(line.split('[')[3][:-2]),film_genre = line.split('[')[5][:-2],
											budget = int(line.split('[')[6][1:-6].replace(",",''))	)
				film_template.put()	
			# add youtube data
			source2 = urllib2.urlopen('http://bia660datasource.appspot.com/txt/views.txt')
			view_file = source2.readlines()
			for line in view_file:
				key = db.Key.from_path('Films', str(line.split('(')[0].split()[0]))
				afilm = db.get(key)
				if afilm:
					afilm.youtube_views = int(line.split('(')[1][0:-2])
					afilm.youtube_likes = int(line.split('(')[2][0:-2])
					afilm.youtube_dislikes = int(line.split('(')[3][0:-2])
					afilm.put()
			# add producers
			source2 = urllib2.urlopen('http://bia660datasource.appspot.com/txt/ids.txt')
			view_file = source2.readlines()
			for line in view_file:
				key = db.Key.from_path('Films', str(line.split()[1]))
				afilm = db.get(key)
				if afilm:
					afilm.film_producer = str(line.split()[2])
					afilm.year=int(line.split()[3])
					afilm.put()
			#rotton_tomato	
			source2 = urllib2.urlopen('http://bia660datasource.appspot.com/txt/rt.txt')
			view_file = source2.readlines()
			for line in view_file:
				key = db.Key.from_path('Films', str(line.split('{')[0][:-1]) )
				afilm = db.get(key)
				if afilm:
					afilm.rt_critics = float(line.split('{')[1].split(',')[0].split(':')[1][1:])
					afilm.rt_audience = float(line.split('{')[1].split(',')[1].split(':')[1].split()[0][:-1])
					afilm.put()
			source2 = urllib2.urlopen('http://bia660datasource.appspot.com/txt/gross.txt')
			view_file = source2.readlines()
			for line in view_file:
				key = db.Key.from_path('Films', str(line.split('[')[1][:-3]) )
				afilm = db.get(key)
				if afilm:
					if line.split('[')[2].split()[0][1:-1].replace(",",'')== '':
						afilm.gross = 0
					else:
						afilm.gross = int(line.split('[')[2].split()[0][1:-1].replace(",",''))
					afilm.put()
			return self.redirect('/')
			

class Clear(webapp2.RequestHandler):
	def get(self):
		q = Producer.all()
		db.delete(q)
		q2 = Films.all()
		db.delete(q2)
		return self.redirect('/')



def do_viz(company,whole_genres):
	q = Films.all()	
	q.filter('film_producer =', company)
	temp_dict={ k:0 for k in whole_genres}
	for i in q:
		for each in whole_genres:
			if (i.film_genre.find(each)!=-1):
				temp_dict[each] +=1
	genres=[v for k,v in temp_dict.items()]
	genres_name1 = [k for k,v in temp_dict.items()]
	# genres.sort(reverse = True)  
	
	temp_dict={ k:0 for k in whole_genres}
	temp_dict2={k:0 for k in whole_genres}
	temp_dict3={k:0 for k in whole_genres}
	temp_dict4={k:0 for k in whole_genres}
	temp_dict5={k:0 for k in whole_genres}
	temp_dict6={k:0 for k in whole_genres}
	temp_dict7={k:0 for k in whole_genres}
	temp_dict8={k:0 for k in whole_genres}
	temp_dict9={k:0 for k in whole_genres}
	q = Films.all()	
	q.filter('film_producer =', company)			
	for i in q:
		for each in whole_genres:
			if (i.film_genre.find(each)!=-1):
				if i.rt_critics:
					temp_dict4[each] +=1
					temp_dict5[each]+=float(i.rt_critics)
					temp_dict6[each]+=float(i.rt_audience)
				if i.gross:
					temp_dict[each] +=1
					temp_dict2[each]+=int(i.gross)
				# if i.youtube_likes > 0:
				# 	temp_dict7[each] +=1
				# 	temp_dict8[each] += float(i.youtube_likes/(i.youtube_likes+i.youtube_dislikes))					
	sumup=0		
	for each in whole_genres:
		sumup += temp_dict[each]
	for each in whole_genres:
		temp_dict3[each] = (float(temp_dict[each]*temp_dict2[each]/sumup))/1000000
		temp_dict2[each] = float(temp_dict2[each]/1000000)
	# for each in whole_genres:
	# 	temp_dict9[each] = float(temp_dict8[each]/temp_dict7[each])	
	best_genre=[]	
	genre=[{"letter":k,"frequency":v} for k,v in temp_dict3.items()]
	genre.sort(key=lambda tup: tup['frequency'],reverse=True)
	best_genre.append(genre[0])
	best_genre.append(genre[1])
	best_genre.append(genre[2])
	best_genre.sort(key=lambda tup: tup['frequency'],reverse=True)
			
	genres2=[v for k,v in temp_dict3.items()]
	genres_name2=[k for k,v in temp_dict3.items()]
		
	genres3=[v for k,v in temp_dict9.items()]
	genres_name3=[k for k,v in temp_dict9.items()]

	sumup=0		
	for each in whole_genres:
		sumup += temp_dict4[each]	
	for each in whole_genres:
		# if temp_dict4[each]	!=0:
		temp_dict5[each] = float(temp_dict5[each]*temp_dict4[each])/sumup/15/1.4
		temp_dict6[each] = float(temp_dict6[each]*temp_dict4[each])/sumup/15/1.4
	
	rating_critics=[v for k,v in temp_dict5.items()]
	genres_name4=[k for k,v in temp_dict5.items()]
	rating_audience=[v for k,v in temp_dict6.items()]
	genres_name5=[k for k,v in temp_dict6.items()]
	
	Months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
	for agenre in range(0,len(best_genre)):
		temp_dict={ k:0 for k in Months}
		temp_dict2={k:0 for k in Months}
		temp_dict3={k:0 for k in Months}			
		q = Films.all()	
		q.filter('film_producer =', company)			
		for i in q:	
			if (i.film_genre.find(best_genre[agenre]['letter'])!=-1):
				for each in Months:
					if (i.release_year.find(each)!=-1):
						if i.gross:
							temp_dict[each] +=1
							temp_dict2[each]+=i.gross
		sumup=0		
		for each in Months:
			sumup += temp_dict[each]
		for each in Months:
			temp_dict3[each] = (float(temp_dict[each]*temp_dict2[each]/sumup))
		if agenre ==0:													
			m_gross1 = [v for k,v in temp_dict3.items()]
		if agenre ==1:
			m_gross2 = [v for k,v in temp_dict3.items()]
		if agenre ==2:
			m_gross3 = [v for k,v in temp_dict3.items()]
	top_gross=[]
	top_gross_value=[]
	q = Films.all()	
	q.filter('film_producer =', company)
	q.order("-gross")
	results = q.fetch(10)
	for p in results:
		top_gross.append(p.film_name)
		top_gross_value.append(p.gross/1000000)
	top_rating=[]
	top_rating_score=[]
	q = Films.all()	
	q.filter('film_producer =', company)
	q.order("-rt_audience")
	results = q.fetch(10)
	for p in results:
		top_rating.append(p.film_name)
		top_rating_score.append(p.rt_audience)	
	top_views=[]
	top_views_time=[]
	q = Films.all()	
	q.filter('film_producer =', company)
	q.order("-youtube_views")
	results = q.fetch(10)
	for p in results:
		top_views.append(p.film_name)
		top_views_time.append(p.youtube_views/1000000)								
	obj = {"genre_count":genres,"genres_name1":genres_name1,
			"genre_count2":genres2,"genres_name2":genres_name2,
			"genre_count3":genres3,"genres_name3":genres_name3,
			"ratings":rating_critics,"ratings2":rating_audience,"genres_name4":genres_name4,"genres_name5":genres_name5,
			"months":Months,"month_gross1":m_gross1,"month_gross2":m_gross2,"month_gross3":m_gross3,"g1":best_genre[0]['letter'],"g2":best_genre[1]['letter'],"g3":best_genre[2]['letter'],
			"top_gross":top_gross,"top_gross_value":top_gross_value,
			"top_rating":top_rating,"top_rating_score":top_rating_score,
			"top_views":top_views,"top_views_time":top_views_time}
	return obj

		
class Viz(webapp2.RequestHandler):
	def post(self):
		viz = self.request.get('viz')
		whole_genres = ["Comedy","Drama","Romance","Biography","Fantasy","Thriller","History","Crime","Action","Adventure","Western","Music","Family","Sport","Animation","Horror"]		
		if viz == "paramount":
			obj=do_viz('paramount_pic',whole_genres)
			return self.response.out.write(json.dumps(obj))
		if viz == "columbia":
			obj=do_viz('columbia',whole_genres)
			return self.response.out.write(json.dumps(obj))
		if viz == "Disney":
			obj=do_viz('walt_Disney',whole_genres)
			return self.response.out.write(json.dumps(obj))
		if viz == "MGM":
			obj=do_viz('MGM',whole_genres)
			return self.response.out.write(json.dumps(obj))
		if viz == "Universal":
			obj=do_viz('universal',whole_genres)
			return self.response.out.write(json.dumps(obj))
		if viz == "Warner":
			obj=do_viz('Warner_Bros',whole_genres)
			return self.response.out.write(json.dumps(obj))
		if viz == "Main":
			obj={}
			return self.response.out.write(json.dumps(obj))
			
			
class Refresh(webapp2.RequestHandler):
	def post(self):
		company = self.request.get('company')
		year = self.request.get('year')
		genre = self.request.get('genre')
		q = Films.all()	
		q.filter('film_producer =', company)
		q.filter('year =', int(year))
		Months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
		temp_dict={ k:0 for k in Months}
		temp_dict2={k:0 for k in Months}
		temp_dict3={k:0 for k in Months}
		temp_dict4={k:0 for k in Months}		
		for i in q:
			for each in Months:
				if (i.film_genre.find(genre)!=-1):
					if (i.release_year.find(each)!=-1):
						if i.gross:
							temp_dict[each] +=1
							temp_dict2[each]+=i.gross
		sumup=0		
		for each in Months:
			sumup += temp_dict[each]
		for each in Months:
			temp_dict3[each] = (float(float(temp_dict[each]*temp_dict2[each])/(sumup)))												
		m_gross1 = [v for k,v in temp_dict3.items()]
		obj = {"months":Months,"month_gross1":m_gross1,"g1":genre}
		return self.response.out.write(json.dumps(obj))
	
	
app = webapp2.WSGIApplication([('/', MainPage),
								('/Columbia',Columbia),
								('/Para_mount',ParaMount),
								('/Disney',Disney),
								('/Warner',Warner),
								('/MGM',MGM),
								('/Universal',Universal),
								('/loaddata',LoadData),
								('/cleardata',Clear),
								('/do_viz',Viz),
								('/refresh',Refresh)],
                              debug=True)