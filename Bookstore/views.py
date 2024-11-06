from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

class ProductView(APIView):
    # def get(self,request):
        # # this collects all the field from the model
        # all_products = Products.objects.all()
        # # created a empty list to append the data from the dictionery
        # data = []

        # for product in all_products:
        #     single_product = {
        #         "id":product.id,
        #         "product_name":product.product_name,
        #         "book_series": product.book_series,
        #         "price":product.price
        #     }
        #     # appending all the dictionery data into the empty list
        #     data.append(single_product)

        # return Response(data)
    
    def get(self,request):
        all_products = Products.objects.all()
        serialized_product = Product_Serializers(all_products,many=True).data
        return Response(serialized_product)
    
    # <------post method in manual method ----->
    # def post(self,request):
    #     # creating the structure to store the request data
    #     new_product = Products(product_name=request.data["product_name"],book_series=request.data["book_series"],price = request.data["price"])
    #     # saving the data
    #     new_product.save()

    #     return Response("data saved")

    # <----post method using serializers ----->
    def post(self,request):
        serialized_product = Product_Serializers(data = request.data)
        if serialized_product.is_valid():
            serialized_product.save()
            return Response(serialized_product.data, status=status.HTTP_201_CREATED)
        return Response(serialized_product.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ProductViewById(APIView):
    def get(self,request,id):
        # getting a particular object using id 
        product = Products.objects.get(id=id)

        single_product = {
                "id":product.id,
                "product_name":product.product_name,
                "book_series": product.book_series,
                "price":product.price
            }
        
        return Response(single_product)

    def patch(self,request,id):
        product = Products.objects.filter(id=id)
        product.update(product_name=request.data["product_name"],book_series=request.data["book_series"],price = request.data["price"])
        
        return Response("updated")

    def delete(self,request,id):
        product = Products.objects.get(id=id)
        product.delete()
        return Response("deleted")