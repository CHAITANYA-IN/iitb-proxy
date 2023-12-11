class RequestPrintOutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def print_request(self, request):
        print(f"Method: {request.method}")

        # Print the request path
        print(f"Path: {request.path}")
        print(request.session)

        print(f"User: {request.user}")
        print(f"User: {request.user.is_authenticated}")

        # Print request GET parameters
        # print("GET Parameters:")
        # for key, value in request.GET.items():
        #     print(f"  {key}: {value}")

        # # Print request POST parameters
        # print("POST Parameters:")
        # for key, value in request.POST.items():
        #     print(f"  {key}: {value}")

    def print_response(self, request, response):
        print(f'Response to {request.path}:')
        print(f"Status code: {response.status_code}")
        print(f"Content type: {response['Content-Type']}")
        # print(f"Content: {response.content}")

    def __call__(self, request):
        self.print_request(request)
        response = self.get_response(request)
        self.print_response(request, response)
        return response
