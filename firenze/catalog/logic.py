from catalog.models import ProductTypePhotos

class FormatedProduct():
    def __init__(
        self,
        id,
        name,
        photo_url,
        colors,
        materials,
        sizes, 
        description,
        collection,
        price, 
        in_fav
    ):
        self.id = id
        self.name = name
        self.photo_url = photo_url
        self.colors = colors
        self.materials = materials
        self.sizes = sizes
        self.description = description
        self.collection = collection
        self.price = price
        self.in_fav = in_fav
        self.variant_name = None
        self.variant_price = None
        self.variant_id = None
        self.choosen_color = None
        self.choosen_material = None
        self.choosen_size = None
        self.variant_photo_url = None
        self.extra_photos = None

# По каждому продукту нужно 
class GetProductFormatted():

    def add_color(formated_product, variant_id, color):
        if not(formated_product.colors.get(variant_id)) and not(color.color_code in formated_product.colors.values()):
            formated_product.colors[variant_id] = color.color_code

    def add_material(formated_product, variant_id, material):
        if not(formated_product.materials.get(variant_id)) and not(material.name in formated_product.materials.values()):
            formated_product.materials[variant_id] = material.name

    def add_sizes(formated_product, variant_id, size):
        if not(formated_product.sizes.get(variant_id)):
            formated_product.sizes[variant_id] = size.name

    def set_choosen_variant(formated_product, variant):
        __class__.add_color(formated_product, variant.id, variant.color)
        __class__.add_material(formated_product, variant.id, variant.material)
        __class__.add_sizes(formated_product, variant.id, variant.size)

        formated_product.choosen_color = variant.color.color_code
        formated_product.choosen_material = variant.material.name
        formated_product.choosen_size = variant.size.name
        formated_product.variant_price = variant.price
        formated_product.variant_name = variant.name
        formated_product.variant_id = variant.id

        if variant.photo:
            formated_product.variant_photo_url = variant.photo.url
        else:
            formated_product.variant_photo_url = formated_product.photo_url

        formated_product.extra_photos = ProductTypePhotos.objects.filter(producttype = variant.id)

    def get_product_json(product_query, choosen_variant=None, in_favourites=False):
        
        if (product_query.photo):
            product_photo = product_query.photo.url
        else:
            product_photo = "" 

        product = FormatedProduct(
            id = product_query.id,
            name = product_query.name,
            photo_url = product_photo,
            colors = {},
            materials = {},
            sizes = {},
            description = product_query.description,
            collection = product_query.collection.name,
            price = product_query.price,
            in_fav = in_favourites
        )

        # if choosen_variant:
        #     __class__.set_choosen_variant(product, choosen_variant)

        for product_type in product_query.producttype_set.all():
            if not(choosen_variant):
                choosen_variant = product_type
                __class__.set_choosen_variant(product, choosen_variant)
            elif (choosen_variant == product_type):
                __class__.set_choosen_variant(product, choosen_variant)

            __class__.add_color(product, product_type.id, product_type.color)
            __class__.add_material(product, product_type.id, product_type.material)
            __class__.add_sizes(product, product_type.id, product_type.size)
        return product


class Filter():
    def get_filter_context(products):
        result = {
            "sizes": {},
            "price": {
                "max_price": 0,
                "min_price": 100000000000,
            },
            "materials": {},
            "colors": {},
        }
        for product in products:
            for product_variant in product.producttype_set.all():
                if not(result["sizes"].get(product_variant.size.id)):
                    result["sizes"][product_variant.size.id] = product_variant.size.name
                if not(result["materials"].get(product_variant.material.id)):
                    result["materials"][product_variant.material.id] = product_variant.material.name                
                if not(result["colors"].get(product_variant.color.id)):
                    result["colors"][product_variant.color.id] = product_variant.color.color_code
                if result["price"]["max_price"] < product_variant.price:
                    result["price"]["max_price"] = product_variant.price
                if result["price"]["min_price"] > product_variant.price:
                    result["price"]["min_price"] = product_variant.price

        return result