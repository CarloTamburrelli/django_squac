'''
	called during request
		process_request(request)
		process_view(request)

	called during response:
		process_exception...
		processs_template_response
		process_response
'''


class DemoMiddleware:

	def __init__(self, get_response):
		self.get_response = get_response
		self.context_responce = {
			"msg": {"something" : "happened" }
		}

	def __call__(self, request):

		#print("Hello World!")

		response = self.get_response(request)
		return response 
	'''
	def process_template_response(self, request, response):
		response.contex_data["new_data"] = self.context_responce
		return response 
	
	def process_view(self, request, view_func, view_args, view_kwargs):
		print(f'view name: {view_func.__name__}')
		pass
	'''
