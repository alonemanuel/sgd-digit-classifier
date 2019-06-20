import inspect
import ntpath
import os
import time

import matplotlib.pyplot as plt

IMDIR = os.path.join('..', '..','images')

class Garcon2:
	first_gc = None

	def __init__(self):
		self.start_time = time.time()
		self.fig = None
		self.iterable_len = None
		self.iter_count = 0
		self.iter_step = 1
		self.iter_stage = 0
		if not Garcon2.first_gc:
			Garcon2.first_gc = self

	def show_time(self):
		elapsed_time = time.time() - self.start_time
		self.log('Execution took {0:.2f} seconds.'.format(elapsed_time))

	def iter(self, iterable=None):
		if iterable is not None:
			self.iter_step = (int)(0.1 * len(iterable))
			self.iterable_len = len(iterable)
			self.log(f'Starting to iterate {len(iterable)} times')
		else:
			if self.iter_count == self.iter_step:
				self.iter_count = 0
				self.iter_stage += 1
				self.log(f'\tDone {self.iter_stage*10}%')
			self.iter_count += 1

	def init_subplt(self, title):
		plt.subplot()
		plt.title(title)

	def __del__(self):
		if Garcon2.first_gc is self:
			self.show_time()

def init_plt(title=''):
	fig = plt.figure()
	if not title:
		curr_frame = inspect.currentframe()
		call_frame = inspect.getouterframes(curr_frame, 2)
		title = call_frame[1][3]
	plt.title(title)

def save_plt(fn=''):
	if not fn:
		curr_frame = inspect.currentframe()
		call_frame = inspect.getouterframes(curr_frame, 2)
		fn = call_frame[1][3]
	plt.tight_layout()
	plt.savefig(os.path.join(IMDIR, fn))

def log(*args):
	print('Log:', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()

def enter_func():
	curr_frame = inspect.currentframe()
	call_frame = inspect.getouterframes(curr_frame, 2)
	file_name = ntpath.basename(call_frame[1][1])
	function_name = call_frame[1][3]
	log(f'In {function_name} (in {file_name})')

def log_var(**kwargs):
	for name, val in kwargs.items():
		log(f'{name} is {val}')

def log_shape(**kwargs):
	for name, val in kwargs.items():
		dim_str = 'length' if isinstance(val, list) else 'shape'
		dim = len(val) if isinstance(val, list) else val.shape
		log(f'{name}\'s {dim_str} is', dim)
