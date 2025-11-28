import unittest
from app import app, classify_weather, load_model
import numpy as np

class TestUnit(unittest.TestCase):
	def setUp(self):
		app.testing = True
		self.client = app.test_client()

	def test_post_missing_field(self):
		form_data = {
			'temperature': '270.277',
			'pressure': '1006',
			'humidity': '84',
			# 'wind_speed' is missing
			'wind_deg': '274',
			'rain_1h': '0',
			'rain_3h': '0',
			'snow': '0',
			'clouds': '9'
		}
		response = self.client.post('/', data=form_data)
		self.assertEqual(response.status_code, 400)

	def test_model_can_be_loaded(self):
		model = load_model()
		self.assertIsNotNone(model, "The model has not loaded correctly")

	def test_clear_classification_output(self):
		test_input = np.array([269.686,1002,78,0,23,0,0,0,0]).reshape(1,-1)
		class_result, _ = classify_weather(test_input)
		return class_result

	def test_rainy_classification_output(self):
		test_input = np.array([279.626,998,99,1,314,0.3,0,0,88]).reshape(1,-1)
		class_result, _ = classify_weather(test_input)
		return class_result

	def test_cloudy_classification_output(self):
		test_input = np.array([291.15,1028,61,1,260,0,0,0,75]).reshape(1,-1)
		class_result, _ = classify_weather(test_input)
		return class_result

if __name__ == '__main__':
	unittest.main()

