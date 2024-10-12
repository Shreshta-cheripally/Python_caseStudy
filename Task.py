class Product:
    def __init__(self,pid,name,price,category):
        self.pid=pid
        self.name=name
        self.price=price
        self.category=category

class ProductApp:
    def __init__(self):
        self.products={}

    def addProduct(self,pid,name,price,category):
        newProduct=Product(pid,name,price,category)
        self.products[id]=newProduct
        print("Product is added successfully")

    def updateProduct(self,pid,name=None,price=None,category=None):
        if id in self.products:
            if name:
                self.products[id].name=name
            if price:
                self.products[id].price=price
            if category:
                self.products[id].category=category
            print("updated successfully")
        else:
            print("product not found")
    
    def deleteProduct(self,pid):
        if id in self.products:
            del self.products[id]
            print("product deleted sucessfully")
        else:
            print("product not found")
    
    def getProductBypId(self,pid):
        if id in self.products:
            return self.products[id]
        else:
            return "product not found"

    def getAllProduct(self):
        return self.products.values()
    
    def getProductByCategory(self,category):
        return [product for product in self.products.values() if product.category==category]
    
    def getProductsBtwPrices(self,min,max):
        return [product for product in self.products.values() if min<=product.price<=max]

if __name__=="__main__":
        
        # flag=True
        # while(flag):
            obj=ProductApp()
            while(True):
                print("choose any one of the operation")
                print("1.Add Product\n2.Update Product\n3.Delete Product\n4.Get Product by PId\n5.Get all products\n6.Get all products by category\n7.Get product between prices\n8.exit")
                print("--------------------------------")

                choice=input("choice a valid option")

                if choice=="1":
                    id=input("enter product Id:")
                    name=input("enter product name:")
                    price=float(input("enter price:"))
                    category=input("enter category:")
                    obj.addProduct(id,name,price,category)
                elif choice=="2":
                    id=input("enter product Id:")
                    name=input("enter product name:")
                    price=float(input("enter price:"))
                    category=input("enter category:")
                    obj.updateProduct(id,name,category,price)
                elif choice=="3":
                    id=input("enter product Id:")
                    obj.deleteProduct(id)
                elif choice=="4":
                    id=input("enter product Id:")
                    print(obj.getProductBypId(id))
                elif choice=="5":
                    print(obj.getAllProduct())
                elif choice=="6":
                    category=input("enter product category:")
                    print(obj.getProductByCategory(category))
                elif choice=="7":
                    min=float(input("enter min price:"))
                    mac=float(input("enter max price:"))
                    print(obj.getProductsBtwPrices(min,max))
                elif choice=="8":
                    break
                else:
                    print("invalid option")



            # n=int(input())
            # if (n<=8 and n>=1):

            #     if n==1:
            #         pName=input("enter product name:")
            #         pPrice=int(input("enter price:"))
            #         pCategory=input("enter the product category:")
            #         pId=int(input("enter product Id:"))
            #         obj.addProduct(pId,pName,pPrice,pCategory)
            #         # p= Product(pName,pPrice,pCategory,pId)
            #         print("data entered successfully")
            #     if n==2:
            #         id=int(input("enter product ID"))
            #         nn=input("enter new name")
            #         np=input("enter new price")
            #         nc=input("enter new category")
            #         obj.updateProduct(pid=id,name=nn,price=np,category=nc)
            #     if n==3:
            #         pId=int(input("enter the id:"))
            #         obj.deleteProduct(pId)
                
            #     if n==4:
            #         pId=int(input("enter the id:"))
            #         obj.getProductBypId(pId)
            #     if n==5:
            #         obj.getAllProduct()
            #     if n==6:
            #         category=input("enter the category")
            #         obj.getProductByCategory(category)
            #     if n==7:
            #         min=int(input("enter the min range"))
            #         max=int(input("enter the max range"))
            #         obj.getProductsBtwPrices(min,max)
                      
            #     if(n==8):
            #         flag=False
            # else:
            #     print("choose valid number")  



