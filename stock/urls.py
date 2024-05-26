# ---------- Router ----------
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryView,
    BrandView,
    ProductView,
    FirmView,
    PurchaseView,
    SaleView,
)
router = DefaultRouter()
router.register('categories', CategoryView)
router.register('brands', BrandView)
router.register('products', ProductView)
router.register('firms', FirmView)
router.register('purchases', PurchaseView)
router.register('sales', SaleView)
urlpatterns = router.urls