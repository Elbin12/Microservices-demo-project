import os
import django



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Product.settings')
django.setup()



import grpc
from concurrent import futures


from . import products_pb2
from . import products_pb2_grpc


from .models import Products

class ProductService(products_pb2_grpc.ProductServiceServicer):
    def GetProductPrice(self, request, context):
        product_id = request.product_id
        product = Products.objects.get(id = product_id)
        price = product.price
        return products_pb2.ProductResponse(price=price)
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    products_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    server.add_insecure_port('[::]:8002')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()