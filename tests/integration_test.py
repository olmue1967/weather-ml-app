import unittest
from app import app


class TestModelAppIntegration(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.client = app.test_client()

	def test_model_app_integration(self):

		form_data = {
			'temperature': '275.15',   # Kelvin
			'pressure': '1013',        # hPa
			'humidity': '85',          # %
			'wind_speed': '3.6',       # m/s
			'wind_deg': '180',         # degrees
			'rain_1h': '0',            # mm
			'rain_3h': '0',            # mm
			'snow': '0',               # mm
			'clouds': '20'             # %
		}

		response = self.client.post('/', data=form_data)

		self.assertNotIn(b"The weather is:</strong> </p>", response.data)

		self.assertNotIn(b"Prediction time:</strong> </p>", response.data)

		html_text = response.data.decode('utf-8').lower()
		valid_classes = [
			'clear', 'cloudy', 'drizzly', 'foggy', 'hazey',
			'misty', 'rainy', 'smokey', 'thunderstorm'
		]
		found = any(weather in html_text for weather in valid_classes)

		self.assertTrue(found, "Invalid weather class")

if __name__ == '__main__':
	unittest.main()
