from .forms import NumberPhone


def form_middleweare(get_response):
    def middleware(request):

        response = get_response(request)

        return response
    return middleware
    # def middleweare(request):
    #     if request.method == 'GET':
    #         response = get_response(request)
    #         form = NumberPhone()
    #         return (response, {'numform': form})
    #     else:
    #         form = NumberPhone(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             response = get_response(request)
    #             return (response, {'numform': form})
    # return middleweare
