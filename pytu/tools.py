from datetime import datetime
from dateutil.parser import parse
import re
import os


class Tools(object):
	date_format = '%d.%m.%Y'
	log_path = None

	def parse_date(date):
		if date and type(date).__name__ == 'str':
			# dd.mm.yyyy
			d = re.search(r'^(\d+)\.\s*(\d+)\.\s?(\d+)$', date)
			if d:
				year = int(d[3])
				month = int(d[2])
				day = int(d[1])

				if (day > 31) or (month > 12):
					raise ValueError()

				return datetime(year, month, day)

			# mm/dd/yyyy
			d = re.search(r'^(\d+)/(\d+)/(\d+)$', date)
			if d:
				year = int(d[3])
				month = int(d[1])
				day = int(d[2])

				if (day > 31) or (month > 12):
					raise ValueError()

				return datetime(year, month, day)

			# yyyy-mm-dd
			d = re.search(r'^(\d+)-(\d+)-(\d+)$', date)
			if d:
				year = int(d[1])
				month = int(d[2])
				day = int(d[3])

				if (day > 31) or (month > 12):
					raise ValueError()

				return datetime(year, month, day)

			return parse(date)

		return date

	def str(value):
		if type(value).__name__ == 'str':
			value = re.sub(r'\.0+$', '', value)

		if type(value).__name__ == 'datetime':
			value = value.strftime(Tools.date_format)

		if type(value).__name__ == 'float':
			value = str(float(value))

		if type(value).__name__ == 'int':
			value = str(value)

		if isinstance(value, Exception):
			value = "{:s}: {:s}".format(
				type(value).__name__,
				str(value),
			)

		if (not value) or (value == 'None'):
			value = ''

		return str(value)

	def now_str():
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	def log(m):
		m = "[{:s}] {:s}".format(Tools.now_str(), m)

		print(m)

		if Tools.log_path:
			Tools.log_to_file(m)

	def log_to_file(m, filepath=None):
		if not filepath:
			now = datetime.now()
			filepath = Tools.log_path\
				.replace('{year}', str(now.year))\
				.replace('{month}', str(now.month))\
				.replace('{day}', str(now.day))\
				.replace('{hour}', str(now.hour))\
				.replace('{minute}', str(now.minute))\
				.replace('{second}', str(now.second))

		log_dir, log_file = os.path.split(filepath)

		if not os.path.isdir(log_dir):
			os.makedirs(log_dir, exist_ok=True)

		with open(filepath, mode='a', encoding='utf8') as file:
			file.write(f"{m}\n")
