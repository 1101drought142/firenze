import os
import json
from datetime import datetime
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def query_set_to_dict(queryset):
    res = {}
    for q in queryset:
        res[q.external_code] = q
    return res

@method_decorator(csrf_exempt, name='dispatch')
class ImportCatalogView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        current_date = datetime.now().strftime('%Y-%m-%d')
        directory_path = os.path.join(settings.MEDIA_ROOT, 'imported_data', current_date)
        os.makedirs(directory_path, exist_ok=True)

        file_name = f"catalog_{datetime.now().strftime('%H-%M-%S')}.json"
        file_path = os.path.join(directory_path, file_name)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        file_url = f"http://217.12.40.76{settings.MEDIA_URL}imported_data/{current_date}/{file_name}"
        
        data_dict = data

        from catalog.models import Material, Color, Size, Collections, Group, Product, ProductType, ProductTypeShopLeft
        from main.models import Shops
        
        materials = query_set_to_dict(Material.objects.all())
        colors = query_set_to_dict(Color.objects.all())
        sizes = query_set_to_dict(Size.objects.all())
        collections = query_set_to_dict(Collections.objects.all())
        groups = query_set_to_dict(Group.objects.all())
        products = query_set_to_dict(Product.objects.all())
        shops = query_set_to_dict(Shops.objects.all())
        producttypes = query_set_to_dict(ProductType.objects.all())
        producttypeshoplefts = query_set_to_dict(ProductTypeShopLeft.objects.all())

        # Цикл по продуктам
        for element in data_dict["products"]:
            try:
                product = element["strProduct"]

                #Добавление цвета
                if (product["codeColor"] and product["nameColor"]):
                    color_name = product["nameColor"]
                    color_external_code = product["codeColor"]
                elif not(product["nameColor"]) and product["codeColor"]:
                    color_name = product["codeColor"]
                    color_external_code = product["codeColor"]
                else:
                    color_name = "Цвета нет"
                    color_external_code = "no"

                curent_color = None
                if not(colors.get(color_external_code)):
                    new_color = Color()
                    new_color.external_code = color_external_code
                    new_color.name = color_name
                    new_color.color_code = "ffffff"
                    new_color.save()
                    curent_color = new_color
                    colors[color_external_code] = curent_color

                else: 
                    curent_color = colors.get(color_external_code)

                #Добавление материала
                if (product["codeMaterial"] and product["composition"]):
                    material_name = product["composition"]
                    material_external_code = product["codeMaterial"]
                elif not(product["composition"]) and product["codeMaterial"]:
                    material_name = product["codeMaterial"]
                    material_external_code = product["codeMaterial"]
                else:
                    material_name = "Цвета нет"
                    material_external_code = "no"

                curent_material = None
                if not(materials.get(material_external_code)):
                    new_material = Material()
                    new_material.external_code = material_external_code
                    new_material.name = material_name
                    new_material.save()
                    curent_material = new_material
                    materials[material_external_code] = curent_material

                else: 
                    curent_material = materials.get(material_external_code)

                #Добавление модели
                if (product["codeModel"] and product["nameModel"]):
                    model_name = product["nameModel"]
                    model_external_code = product["codeModel"]
                elif not(product["nameModel"]) and product["codeModel"]:
                    model_name = product["codeModel"]
                    model_external_code = product["codeModel"]
                else:
                    model_name = "Цвета нет"
                    model_external_code = "no"

                curent_model = None
                if not(collections.get(model_external_code)):
                    new_model = Collections()
                    new_model.external_code = model_external_code
                    new_model.name = model_name
                    new_model.save()
                    curent_model = new_model
                    collections[model_external_code] = curent_model
                else: 
                    curent_model = collections.get(model_external_code)

                #Добавление группы
                if (product["group"]):
                    group_name = product["group"]
                    group_external_code = product["group"]
                else:
                    group_name = "Группы нет"
                    group_external_code = "no"

                curent_group = None
                if not(groups.get(group_external_code)):
                    new_group = Group()
                    new_group.external_code = group_external_code
                    new_group.name = group_name
                    new_group.save()
                    curent_group = new_group
                    groups[group_external_code] = curent_group
                else: 
                    curent_group = groups.get(group_external_code)


                #Добавление товара 
                curent_product = None
                if not(products.get(product["article"])):
                    new_product = Product()
                    new_product.external_code = product["article"]
                    new_product.name = product["name"]
                    new_product.collection = curent_model
                    new_product.group = curent_group
                    new_product.save()
                    curent_product = new_product
                    products[product["article"]] = curent_product
                else:
                    curent_product = products.get(product["article"])
                    curent_product.name = product["name"]
                    curent_product.collection = curent_model
                    curent_product.group = curent_group
                    curent_product.save()

                # Цикл по размерам
                for item in element["items"]:

                    #Добавляем размер
                    size = item["size"]
                    if (size["sizeINT"] and size["sizeIT"]):
                        external_code = size["sizeINT"]+size["sizeIT"]+size["sizeRU"]
                        size_name = size["sizeINT"]
                    if not(size["sizeINT"] or size["sizeIT"] or size["sizeRU"]):
                        external_code = "NoSize"
                        size_name = "Нет"
                    else:
                        external_code = size["sizeRU"]  
                        size_name = size["sizeRU"]

                    curent_size = None
                    if not(sizes.get(external_code)):
                        new_size = Size()
                        new_size.external_code = external_code
                        new_size.name = size_name
                        new_size.sizeit = size["sizeIT"]
                        new_size.sizeru = size["sizeRU"]
                        new_size.save()
                        sizes[external_code] = new_size
                        current_size = new_size
                    else:
                        current_size = sizes.get(external_code)

                    #Добавляем магазин
                    curent_shop = None
                    shop_name = item["place"]
                    if not(shops.get(shop_name)):
                        new_shop = Shops()
                        new_shop.external_code = shop_name
                        new_shop.name = shop_name
                        new_shop.save()
                        shops[shop_name] = new_shop
                        curent_shop = new_shop
                    else:
                        curent_shop = shops.get(shop_name)


                    #Добавление типа товаров и остатков
                    curent_product_type = None
                    product_type_external_code = f"{curent_product.external_code}{external_code}"
                    if not(producttypes.get(product_type_external_code)):
                        new_producttype =  ProductType()
                        new_producttype.name = curent_product.name
                        new_producttype.external_code = product_type_external_code
                        new_producttype.product = curent_product
                        new_producttype.size = current_size
                        new_producttype.color = curent_color
                        new_producttype.material = curent_material
                        new_producttype.price = 0
                        new_producttype.save()
                        producttypes[product_type_external_code] = new_producttype
                        curent_product_type = new_producttype
                    else:
                        curent_product_type = producttypes.get(product_type_external_code)
                        curent_product_type.name = curent_product.name
                        curent_product_type.external_code = product_type_external_code
                        curent_product_type.product = curent_product
                        curent_product_type.size = current_size
                        curent_product_type.color = curent_color
                        curent_product_type.material = curent_material
                        curent_product_type.price = 0
                        curent_product_type.save()

                    product_type_shop_left_external_code = f"{curent_product_type.external_code}{curent_shop.external_code}"
                    if not(producttypeshoplefts.get(product_type_shop_left_external_code)):
                        new_producttypeshopleft =  ProductTypeShopLeft()
                        new_producttypeshopleft.external_code = product_type_shop_left_external_code
                        new_producttypeshopleft.producttype = curent_product_type
                        new_producttypeshopleft.shop = curent_shop
                        new_producttypeshopleft.left = item["quant"]
                        new_producttypeshopleft.save()
                    else:
                        curent_producttypeshopleft = producttypeshoplefts.get(product_type_shop_left_external_code)
                        curent_producttypeshopleft.external_code = product_type_shop_left_external_code
                        curent_producttypeshopleft.producttype = curent_product_type
                        curent_producttypeshopleft.shop = curent_shop
                        curent_producttypeshopleft.left = item["quant"]
                        curent_producttypeshopleft.save()

            except BaseException  as e:
                print(str(e), type(e))

        return JsonResponse({'message': 'success', 'path': file_path, 'url': file_url}, status=201)

