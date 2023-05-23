from django. views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):   #aboutページ追加する
    template_name = "about.html"        

