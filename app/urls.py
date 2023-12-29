from django.urls import path
from app.calc import eval_expr
from ninja import NinjaAPI


api = NinjaAPI()

@api.get("/calc")
def add(request, expression: str):
    """
    Evaluates a simple mathematical expression
    """
    return {"result": eval_expr(expression)}

urlpatterns = [
    path("api/", api.urls),
]
