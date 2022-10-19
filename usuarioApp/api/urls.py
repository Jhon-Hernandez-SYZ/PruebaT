from rest_framework.routers import DefaultRouter
from usuarioApp.api.views import PersonasMVS

router = DefaultRouter()
router.register(r'persona', PersonasMVS, basename='persona-admin')


urlpatterns = [


  
]
urlpatterns += router.urls