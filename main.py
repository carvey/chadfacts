from flask import Flask
from flask_restful import Resource, Api

import json
import random

app = Flask(__name__)
api = Api(app)

class ChadFact(Resource):

	def select_fact(self, data):
		fact = random.choice(list(data.keys()))
		fact_data = data[fact]
		formatted_fact = "Category:\n--%s\n" % fact

		while 'text' not in fact_data:
			old_fact_data = fact_data
			fact = random.choice(list(fact_data.keys()))
			fact_data = old_fact_data[fact]

			formatted_fact += "--%s\n" % fact
			# formatted_fact = formatted_fact.strip()


		formatted_fact += "Fact: %s" % fact_data['text']
		return formatted_fact

	def get(self):
		facts = open('chadfacts.json')
		data = json.load(facts)

		text = self.select_fact(data)

		facts.close()

		return {"text": text}

api.add_resource(ChadFact, '/')

if __name__ == '__main__':
    app.run(debug=True)